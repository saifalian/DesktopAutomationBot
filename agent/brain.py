import time
import logging
import os
from datetime import datetime
from PIL import Image
from omg.vision.screenshot import ScreenShotter
from omg.vision.preprocess import ImagePreprocessor
from omg.llm.client import LLMClient
from omg.llm.prompts import PromptTemplates
from omg.agent.memory import ShortMemory
from omg.actions.mouse import MouseActions, KeyboardActions

class AgentBrain:
    def __init__(self, config=None):
        self.config = config or {}
        self.screenshotter = ScreenShotter()
        self.preprocessor = ImagePreprocessor()
        self.llm_client = LLMClient(
            base_url=self.config.get("base_url", "http://localhost:1234/v1"),
            api_key=self.config.get("api_key", "lm-studio")
        )
        self.memory = ShortMemory(max_steps=self.config.get("max_history", 3))
        self.running = False
        self.paused = False
        self.current_task = ""
        self.system_prompt = None
        self.initial_prompt = None
        self.screen_w, self.screen_h = self.screenshotter.get_screen_size()
        
    def set_task(self, task, system_prompt=None, initial_prompt=None):
        self.current_task = task
        self.system_prompt = system_prompt
        self.initial_prompt = initial_prompt
        self.memory.clear()

    def run_cycle(self):
        """Executes one step of the (See -> Think -> Act) loop."""
        if self.paused:
            return "Paused"

        # 1. See: Capture screen
        img, path = self.screenshotter.capture()
        img_resized = self.preprocessor.resize_for_vision_model(img)
        img_b64 = self.preprocessor.encode_to_base64_string(img_resized)

        # 2. Think: Build payload and ask LLM
        history = self.memory.get_history()
        messages = PromptTemplates.build_payload(
            img_b64, 
            self.current_task, 
            history, 
            system_prompt=self.system_prompt,
            initial_prompt=self.initial_prompt,
            permissions_granted=self.config.get("permissions_granted", True),
            screen_size=(self.screen_w, self.screen_h)
        )

        response = self.llm_client.ask(
            model=self.config.get("model_id", "qwen2-vl-7b-instruct"),
            messages=messages,
            temperature=self.config.get("temperature", 0.2)
        )

        if "error" in response:
            return f"Error: {response['error']}"

        # 3. Act: Execute action
        action_result = self._execute_action(response)
        
        # 4. Remember: Update short memory
        # We store both User and Assistant turns to ensure alternating roles.
        self.memory.add_turn("user", f"Executing Objective: {self.current_task}")
        self.memory.add_turn("assistant", f"Action: {response.get('action')}, Thought: {response.get('thought')}")
        
        return response

    def _execute_action(self, response):
        """Map model coordinates and trigger system events."""
        action = response.get("action", "").lower()
        thought = response.get("thought", "")
        reason = response.get("reason", "")
        
        logging.info(f"THOUGHT: {thought}")
        logging.info(f"ACTION: {action} (Reason: {reason})")

        # Map coordinates
        # Assume model outputs 0-100 (percentage)
        x_pct = response.get("x", 0)
        y_pct = response.get("y", 0)
        
        # Coordinate Denormalization (pct to pixels)
        target_x = int(x_pct * self.screen_w / 100)
        target_y = int(y_pct * self.screen_h / 100)

        if action == "click":
            MouseActions.click(target_x, target_y)
        elif action == "double_click":
            MouseActions.double_click(target_x, target_y)
        elif action == "type":
            text = response.get("text", "")
            KeyboardActions.type_text(text)
        elif action == "scroll":
            MouseActions.scroll(500)
        elif action == "done":
            self.running = False
            return "Task Complete"
        
        return "Step Executed"

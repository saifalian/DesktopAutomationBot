# Desktop Automation Bot

Desktop Automation Bot is a Python desktop assistant for screen-aware automation. It combines a PyQt-style user interface, screenshot capture, OCR/vision preprocessing, an agent memory layer, prompt orchestration, and mouse action execution.

The project is structured as a local desktop automation workbench: users can describe tasks, the agent can reason over visual context, and the UI provides dashboards, task cards, prompt dialogs, overlays, and bot interaction panels.

## Features

- Desktop dashboard and bot UI components
- Screenshot capture and preprocessing pipeline
- OCR/vision module structure
- Mouse action execution helpers
- Agent memory and session tracking
- LLM client and prompt definitions
- Structured runtime logging
- Worker/task-card UI flow

## Tech Stack

- Python
- PyQt/PySide-style UI modules
- Screen capture and image preprocessing
- OCR-ready vision layer
- Local agent orchestration modules

## Project Structure

```text
actions/   # Mouse and desktop action helpers
agent/     # Agent brain and memory/session modules
config/    # Runtime settings
llm/       # LLM client and prompts
ui/        # Dashboard, dialogs, overlays, cards, workers
utils/     # Logging helpers
vision/    # Screenshot and preprocessing modules
main.py    # Application entry point
```

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

## Notes

Automation tools can move the mouse and interact with applications. Test on safe windows first and avoid running experimental tasks on sensitive websites, payment screens, or account settings pages.


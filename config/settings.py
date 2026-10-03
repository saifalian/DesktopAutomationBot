import os

class Settings:
    # LM Studio API Settings
    BASE_URL = "http://localhost:1234/v1"
    MODEL_ID = "qwen2-vl-7b-instruct"  # Default, can be changed in UI
    TEMPERATURE = 0.2
    
    # Agent Settings
    MAX_HISTORY_STEPS = 3  # Default short memory
    ACTION_DELAY = 1.5      # Seconds between actions
    
    # UI Settings
    APP_NAME = "OMG"
    WINDOW_TITLE = "OMG: Autonomous Visual AI Agent"
    
    # Paths
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    LOG_DIR = os.path.join(BASE_DIR, "logs")
    
    @classmethod
    def ensure_dirs(cls):
        if not os.path.exists(cls.LOG_DIR):
            os.makedirs(cls.LOG_DIR)

Settings.ensure_dirs()

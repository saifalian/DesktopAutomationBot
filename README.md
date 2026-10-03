# Desktop Automation Bot

Desktop Automation Bot is a Python desktop app for experimenting with computer automation.

In easy words, this project is made to help a bot look at the screen, understand what is happening, and prepare actions such as mouse movement or clicks. It includes a desktop interface, screenshot tools, OCR/vision modules, memory files, prompt handling, and automation helpers.

This is useful for learning how a local desktop assistant can be built step by step.

## What This App Can Do

- Show a desktop dashboard for the bot.
- Take screenshots of the screen.
- Prepare screenshots for OCR or vision processing.
- Store memory and session information.
- Use prompt files for AI-style task handling.
- Include helper code for mouse actions.
- Keep runtime logs for debugging.
- Show task cards and worker UI screens.

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

## Safety Notes

This project can be used for desktop automation experiments. Test it first on safe windows, such as a blank app or test page.

Do not run experimental automation on banking pages, payment screens, private accounts, or important settings pages.

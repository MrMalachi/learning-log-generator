from pathlib import Path
import sys


def resource_path(relative_path):
    """Get the correct file path for normal Python or PyInstaller."""
    if hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS / relative_path)

    return Path(relative_path)


# config.py file used for 'settings' or 'constants' that will probably not change during runtime.
LOG_TEMPLATE_PATH = Path("src/learning_log_generator/templates/learning_log_template.md")
LOGS_FOLDER = Path("data/logs")
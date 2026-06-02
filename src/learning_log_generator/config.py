from pathlib import Path
import sys


# Package folder:
# /Users/malachibrown/dev/python_work/projects/learning-log-generator/src/learning_log_generator
PACKAGE_DIR = Path(__file__).resolve().parent

# Project root:
# Users/malachibrown/dev/python_work/projects/learning-log-generator
PROJECT_ROOT = PACKAGE_DIR.parent.parent


def resource_path(relative_path):
    """Get the correct file path for normal Python or PyInstaller."""
    if hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS) / relative_path

    return PROJECT_ROOT / relative_path


# Template file location
LOG_TEMPLATE_PATH = resource_path(
    Path("src") / "learning_log_generator" / "templates" / "learning_log_template.md"
)

# Logs folder location
LOGS_FOLDER = PROJECT_ROOT / "data" / "logs"
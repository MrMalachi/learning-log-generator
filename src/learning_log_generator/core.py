from datetime import datetime
import os
from pathlib import Path
import platform
import subprocess

from send2trash import send2trash

from learning_log_generator.config import LOG_TEMPLATE_PATH, LOGS_FOLDER


class LearningLogManager:
    """Manages learning logs."""

    def open_learning_log(self, file_path):
        """Open a file using the user's operating system."""
        path = Path(file_path)

        if not path.exists():
            print("File does not exist.")
            return

        system = platform.system()

        if system == "Darwin":
            subprocess.run(["open", str(path)])
        elif system == "Windows":
            os.startfile(str(path))
        elif system == "Linux":
            subprocess.run(["xdg-open", str(path)])
        else:
            print("Sorry, your operating system is not supported.")

    def create_learning_log(self):
        """Read from .md template, fill in, and then save a new log entry."""
        LOGS_FOLDER.mkdir(parents=True, exist_ok=True)

        today = datetime.now().strftime("%m-%d-%Y")
        new_file_path = LOGS_FOLDER / f"learning_log{today}.md"

        with open(LOG_TEMPLATE_PATH, "r", encoding="utf-8") as template_file:
            template_content = template_file.read()

        filled_content = template_content.replace("{date}", today)

        try:
            with open(new_file_path, "x", encoding="utf-8") as new_file:
                new_file.write(filled_content)
        except FileExistsError:
            print(
                f"\nAction aborted: File {new_file_path.name} already exists! "
                f"Opening the existing file instead..."
            )
            self.open_learning_log(new_file_path)
        else:
            print(f"\nCreated a new learning log: {new_file_path.name}")
            self.open_learning_log(new_file_path)

    def get_saved_learning_logs(self):
        """Build the saved logs list for reusability."""
        saved_logs = list(LOGS_FOLDER.glob("*.md"))

        return saved_logs

    def search_log_by_keyword(self, keyword):
        """Return a list of learning logs matching the keyword."""
        matching_logs = []

        for file in LOGS_FOLDER.glob("*.md"):
            if file.is_file():
                content = file.read_text(encoding="utf-8")

                if keyword.lower() in content.lower():
                    matching_logs.append(file)

        return matching_logs

    def delete_learning_log(self, selected_learning_log):
        """
        Use imported 3rd party module to send file to trash instead of
        permanently deleting it.
        """
        send2trash(selected_learning_log)
        return selected_learning_log


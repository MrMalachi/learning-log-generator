from datetime import datetime
from learning_log_generator.config import LOG_TEMPLATE_PATH, LOGS_FOLDER


class LearningLogGenerator:
    """
    A Python program that generates a structured daily learning log for my
    Python/Backend learning journey.
    """

    def __init__(self):
        """Initialize attributes."""

    def display_main_menu(self):
        """A neatly printed display of the learning log cli menu."""
        print(
            "\n============================================"
            "\n          🪵 Learning Log Generator🪵            "
            "\n============================================"
            "\n1. Create a new learning log"
            "\n2. View saved learning logs"
            "\n3. Search learning log by keyword"
            "\n4. Edit a learning log"
            "\n5. Delete a learning log"
            "\n6. Exit"
        )

    def get_main_menu_choice(self):
        """Prompt user to enter a corresponding integer & return value."""
        while True:
            self.display_main_menu()  # Redisplay menu every time if invalid input.
            try:
                choice = int(input("\nEnter a number (1-6): "))

                if choice < 1 or choice > 6:
                    print("Please enter a valid number...")
                    continue

            except ValueError:
                print("Please enter a number...")
            else:
                return choice

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
            print(f"Action aborted: File {new_file_path.name} already exists! No data was overwritten.")
        else:
            print(f"Created a new learning log: {new_file_path.name}")

    def display_saved_learning_logs(self):
        """A neatly formatted display of all previously saved learning logs."""
        print()
        files = (item for item in LOGS_FOLDER.iterdir())

        for index, file in enumerate(files, start=1):
            print(f"{index}. {file.name}")

    def get_log_keyword(self):
        """Prompt user to enter a keyword to "search" for."""
        keyword = input("\nSearch logs for: ")

        return keyword

    def search_log_by_keyword(self, keyword):
        """Return a list of learning logs matching the keyword."""
        matching_logs = []

        for file in LOGS_FOLDER.glob("*.md"):
            if file.is_file():
                content = file.read_text(encoding="utf-8")

                if keyword.lower() in content.lower():
                    matching_logs.append(file)

        return matching_logs

    def display_matching_logs(self, matching_logs):
        """Output matching logs found as a result of keyword."""
        if not matching_logs:
            print("\nNo matching logs found...")
            return

        print("\nMatching Learning Logs:")

        for index, file in enumerate(matching_logs, start=1):
            print(f"{index}. {file.name}")

    def get_learning_log_choice(self):
        """Prompt user to enter an integer as their log choice & return it."""
        choice = input("\nEnter the corresponding number of the learning log you want to edit: ")

        return choice

    def edit_learning_log(self):
        """"""
        pass

    def run_learning_log_generator(self):
        """The class' internal orchestrator."""
        choice = self.get_main_menu_choice()

        if choice == 1:
            self.create_learning_log()
        elif choice == 2:
            self.display_saved_learning_logs()
        elif choice == 3:
            keyword = self.get_log_keyword()
            matching_logs = self.search_log_by_keyword(keyword)
            self.display_matching_logs(matching_logs)
        elif choice == 4:
            print("\nList of Saved Learning Logs:")
            self.display_saved_learning_logs()
            self.get_learning_log_choice()




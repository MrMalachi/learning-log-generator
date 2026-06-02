from send2trash import send2trash

from learning_log_generator.core import LearningLogManager
from learning_log_generator.config import LOGS_FOLDER


class LearningLogGenerator:
    """
    A Python program that generates a structured daily learning log for my
    Python/Backend learning journey.
    """

    def __init__(self):
        """Initialize attributes."""
        self.manager = LearningLogManager()

    def display_main_menu(self):
        """A neatly printed display of the learning log cli menu."""
        print(
            "\n============================================"
            "\n          🪵 Learning Log Generator🪵            "
            "\n============================================"
            "\n1. Create and open a new learning log"
            "\n2. View / Edit saved learning logs"
            "\n3. Search learning log by keyword"
            "\n4. Delete a learning log"
            "\n5. Exit"
        )

    def get_main_menu_choice(self):
        """Prompt user to enter a corresponding integer & return value."""
        while True:
            self.display_main_menu()  # Redisplay menu every time if invalid input.
            try:
                choice = int(input("\nEnter a number (1-5): "))

                if choice < 1 or choice > 5:
                    print("Please enter a valid number...")
                    continue

            except ValueError:
                print("Please enter a number...")
            else:
                return choice

    def display_learning_logs(self, saved_logs):
        """A neatly formatted display of all previously saved learning logs."""
        if not saved_logs:
            print("No learning logs found.")
            return None
        else:
            print("\n   || Saved Learning Logs ||")

        for index, file in enumerate(saved_logs, start=1):
            print(f"{index}. {file.name}")

    def ask_to_edit_learning_log(self):
        """Return boolean under the conditions the user enters 'y' or 'n'."""
        while True:
            choice = input(
                "\nWould you like to edit a learning log? (y/n): "
            ).strip().lower()

            if choice == "y":
                return True
            elif choice == "n":
                return False
            else:
                print("\nPlease enter 'y' for yes or 'n' for no...")

    def get_learning_log_choice(self, saved_logs):
        """Return an indexed file from a list specified by the user."""

        # Prevent the program from continuing and asking the user to choose a
        # file where there are no files available.
        if not saved_logs:
            print("No learning logs found.")
            return None

        while True:
            try:
                edit_choice = int(input(
                    "\nEnter the corresponding number to the learning log: "
                ))
            except ValueError:
                print("\nPlease enter a number. Try again...")
                continue

            if edit_choice < 1 or edit_choice > len(saved_logs):
                print("\nPlease enter a number within range...")
                continue

            else:
                selected_learning_log = saved_logs[edit_choice - 1]
                return selected_learning_log

    def edit_learning_log(self, selected_learning_log):
        """
        Call method to open specified file by passing parameter as an argument.
        """
        self.open_learning_log(selected_learning_log)

    def get_log_keyword(self):
        """Prompt user to enter a keyword to "search" for."""
        while True:
            try:
                keyword = input("\nSearch logs for: ")

                if keyword == "":
                    print("\nNo keyword was entered! Try again...")
                    continue
            except AttributeError as e:
                print(f"Debugging log - Attribute missing {e}")
            else:
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

    def confirm_delete_learning_log(self, selected_learning_log):
        """
        Deleting is serious! Better safe than sorry in case user changes mind.
        """
        while True:
            confirm_action = input(
                f"\nAre you sure you want to delete "
                f"{selected_learning_log.name}?! (y/n): "
            ).lower().strip()

            # Naturally filters out int, empty inputs, and miscellaneous text.
            if confirm_action == "y":
                return True
            elif confirm_action == "n":
                return False
            else:
                print("\nInvalid input! Please enter 'y' for yes or 'n' for no.")

    def delete_learning_log(self, selected_learning_log):
        """
        Use imported 3rd party module to send file to trash instead of
        permanently deleting it.
        """
        send2trash(selected_learning_log)
        print(f"\nMoved {selected_learning_log.name} to trash.")  # Confirmation

    def run_learning_log_generator(self):
        """The class' internal orchestrator."""
        while True:
            choice = self.get_main_menu_choice()

            if choice == 1:
                self.create_learning_log()
            elif choice == 2:
                saved_logs = self.manager.get_saved_learning_logs()
                self.display_learning_logs(saved_logs)

                if self.ask_to_edit_learning_log():
                    selected_learning_log = self.get_learning_log_choice(saved_logs)

                    if selected_learning_log is not None:
                        self.edit_learning_log(selected_learning_log)
            elif choice == 3:
                keyword = self.get_log_keyword()
                matching_logs = self.search_log_by_keyword(keyword)
                self.display_matching_logs(matching_logs)
            elif choice == 4:
                saved_logs = self.manager.get_saved_learning_logs()
                self.display_learning_logs(saved_logs)

                selected_learning_log = self.get_learning_log_choice(saved_logs)

                if selected_learning_log is not None:
                    if self.confirm_delete_learning_log(selected_learning_log):
                        self.delete_learning_log(selected_learning_log)
                    else:
                        print(
                            f"\nNo problem, {selected_learning_log.name} was "
                            f"NOT deleted."
                        )
                        continue
            elif choice == 5:
                print(
                    "\nThank you for using 🪵 Learning Log Generator🪵. Goodbye!"
                )
                break
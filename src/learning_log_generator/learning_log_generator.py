import subprocess
import platform


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
            "\n3. Search learning logs by keyword"
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
        """"""
        pass

    def run_learning_log_generator(self):
        """The class' internal orchestrator."""
        self.display_main_menu()
        choice = self.get_main_menu_choice()

        if choice == 1:
            self.create_learning_log()



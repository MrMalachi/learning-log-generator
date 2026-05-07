"""
Entry point for 'learning_log_generator' script, acting as the top-level
orchestrator.
"""

from learning_log_generator.learning_log_generator import LearningLogGenerator


def main():
    generator = LearningLogGenerator()
    generator.run_learning_log_generator()


if __name__ == "__main__":
    main()

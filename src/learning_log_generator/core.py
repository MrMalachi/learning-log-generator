from learning_log_generator.config import LOG_TEMPLATE_PATH, LOGS_FOLDER

class LearningLogManager:
    """Manages learning logs."""

    def get_saved_learning_logs(self):
        """Build the saved logs list for reusability."""
        saved_logs = list(LOGS_FOLDER.glob("*.md"))

        return saved_logs


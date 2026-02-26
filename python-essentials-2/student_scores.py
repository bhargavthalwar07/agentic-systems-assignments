class StudentScores:
    """Class to manage student scores and find highest values."""

    def __init__(self, scores: list):
        """Initialize with a list of scores."""
        self.scores = scores

    def highest_last_two(self) -> None:
        """Find and print the highest score among the last two using negative indexing."""
        try:
            if len(self.scores) < 2:
                raise ValueError("Not enough scores")
            
            # Using negative indexing to get last 2 scores
            last_two = self.scores[-2:]
            highest = max(last_two)
            print(f"Highest score among last two is: {highest}")
        except (ValueError, TypeError):
            print("Not enough scores to find highest value")


if __name__ == "__main__":
    # Example with enough scores
    scores = [45, 67, 89, 72]
    student = StudentScores(scores)
    student.highest_last_two()

    # Example with less than 2 scores
    scores2 = [50]
    student2 = StudentScores(scores2)
    student2.highest_last_two()

    # Example with exactly 2 scores
    scores3 = [85, 90]
    student3 = StudentScores(scores3)
    student3.highest_last_two()

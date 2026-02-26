class StudentPerformance:
    """Class to manage student performance and calculate score differences."""

    def __init__(self, scores: list):
        """Initialize with a list of scores."""
        self.scores = scores

    def score_difference(self) -> None:
        """Find and print the difference between the last and first score using indexing."""
        try:
            if len(self.scores) == 0:
                raise ValueError("No scores available")
            
            # Using indexing to get first and last scores
            first_score = self.scores[0]
            last_score = self.scores[-1]
            difference = last_score - first_score
            print(f"Difference between last and first score is: {difference}")
        except (ValueError, TypeError, IndexError):
            print("No scores available to calculate difference")


if __name__ == "__main__":
    # Example with multiple scores
    scores = [55, 65, 75, 85]
    performance = StudentPerformance(scores)
    performance.score_difference()

    # Example with empty list
    scores2 = []
    performance2 = StudentPerformance(scores2)
    performance2.score_difference()

    # Example with single score
    scores3 = [70]
    performance3 = StudentPerformance(scores3)
    performance3.score_difference()

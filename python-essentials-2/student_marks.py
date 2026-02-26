class StudentMarks:
    """Class to manage student marks and calculate averages."""

    def __init__(self, marks: list):
        """Initialize with a list of marks."""
        self.marks = marks

    def last_three_avg(self) -> None:
        """Calculate and print the average of the last three marks using negative indexing."""
        try:
            if len(self.marks) < 3:
                raise ValueError("Not enough marks")
            
            # Using negative indexing to get last 3 marks
            last_three = self.marks[-3:]
            average = sum(last_three) / 3
            print(f"Average of last 3 marks is: {average}")
        except (ValueError, TypeError):
            print("Not enough marks to calculate average")


if __name__ == "__main__":
    # Example with enough marks
    marks = [50, 60, 70, 80, 90]
    student = StudentMarks(marks)
    student.last_three_avg()

    # Example with less than 3 marks
    marks2 = [50, 60]
    student2 = StudentMarks(marks2)
    student2.last_three_avg()

    # Example with exactly 3 marks
    marks3 = [70, 80, 90]
    student3 = StudentMarks(marks3)
    student3.last_three_avg()

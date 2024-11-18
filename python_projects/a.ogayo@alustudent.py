#!/usr/bin/python3
class Assignment:
    def __init__(self, name, type_, score, weight):
        self.name = name
        self.type_ = type_
        self.score = score
        self.weight = weight

    def weighted_score(self):
        """Calculates the weighted score for the assignment."""
        return self.score * (self.weight / 100)


class Student:
    def __init__(self):
        self.assignments = []

    def add_assignment(self, assignment):
        """Adds an assignment to the student’s list of assignments."""
        self.assignments.append(assignment)

    def calculate_totals(self):
        """Calculates the total weighted scores for Formative and Summative assignments."""
        formative_total = 0
        summative_total = 0
        formative_weight = 0
        summative_weight = 0

        for assignment in self.assignments:
            if assignment.type_ == "Formative":
                formative_total += assignment.weighted_score()
                formative_weight += assignment.weight
            elif assignment.type_ == "Summative":
                summative_total += assignment.weighted_score()
                summative_weight += assignment.weight

        # Ensure weights do not exceed limits
        if formative_weight > 60:
            raise ValueError("Formative assignments weight exceeds 60% limit.")
        if summative_weight > 40:
            raise ValueError("Summative assignments weight exceeds 40% limit.")

        return formative_total, summative_total

    def check_progression(self):
        """Determines if the student has passed based on formative and summative scores."""
        formative_total, summative_total = self.calculate_totals()
        formative_pass = formative_total >= 30
        summative_pass = summative_total >= 20

        if formative_pass and summative_pass:
            return "Passed"
        else:
            return "Failed - Retake Required"

    def check_resubmission_eligibility(self):
        """Identifies formative assignments with scores below the passing threshold (50%)."""
        resubmission_list = [
            assignment for assignment in self.assignments
            if assignment.type_ == "Formative" and assignment.score < 50
        ]
        if not resubmission_list:
            return "All formative assignments passed."

        return resubmission_list

    def display_transcript(self, order="ascending"):
        """Displays a transcript sorted by assignment score in ascending or descending order."""
        sorted_assignments = sorted(
            self.assignments, key=lambda x: x.score, reverse=(order == "descending")
        )

        print("Transcript Breakdown ({} Order):".format(order.capitalize()))
        print("Assignment          Type            Score(%)    Weight (%)")
        print("-----------------------------------------------------------")
        for assignment in sorted_assignments:
            print(f"{assignment.name:<18} {assignment.type_:<14} {assignment.score:<10} {assignment.weight:<10}")
        print("-----------------------------------------------------------")

# Sample usage:
student = Student()

# Adding assignments
student.add_assignment(Assignment("Assignment 1", "Formative", 45, 15))
student.add_assignment(Assignment("Assignment 2", "Formative", 90, 10))
student.add_assignment(Assignment("Assignment 3", "Formative", 45, 10))
student.add_assignment(Assignment("Assignment 4", "Formative", 80, 15))
student.add_assignment(Assignment("Assignment 5", "Formative", 48, 10))
student.add_assignment(Assignment("Midterm", "Summative", 34, 20))
student.add_assignment(Assignment("Final Exam", "Summative", 95, 20))

# Calculating progression
progression_status = student.check_progression()
print(f"Course Progression: {progression_status}")

# Checking resubmission eligibility
resubmissions = student.check_resubmission_eligibility()
if isinstance(resubmissions, str):
    print(resubmissions)
else:
    print("Assignments eligible for resubmission:")
    for assignment in resubmissions:
        print(f"{assignment.name} with a score of {assignment.score}%")

# Display transcript in descending order
student.display_transcript("descending")

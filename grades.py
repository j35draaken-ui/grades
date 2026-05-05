class Grades:
    def __init__(self):
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def remove_grade(self, grade):
        if grade in self.grades:
            self.grades.remove(grade)

    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def sort_grades(self):
        return sorted(self.grades)

    def display_grades(self):
        print("Grades:")
        for grade in self.grades:
            print(grade)

if __name__ == "__main__":
    grades = Grades()
    while True:
        print("Options: add, remove, average, sort, display, exit")
        choice = input("Enter your choice: ")
        if choice == "add":
            grade = float(input("Enter grade to add: "))
            grades.add_grade(grade)
        elif choice == "remove":
            grade = float(input("Enter grade to remove: "))
            grades.remove_grade(grade)
        elif choice == "average":
            print(f"Average grade: {grades.calculate_average()}")
        elif choice == "sort":
            sorted_grades = grades.sort_grades()
            print(f"Sorted grades: {sorted_grades}")
        elif choice == "display":
            grades.display_grades()
        elif choice == "exit":
            break
        else:
            print("Invalid option, please try again.")

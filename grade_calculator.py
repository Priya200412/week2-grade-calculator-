# Student Grade Calculator
# Week 2 Project – Control Flow & Data Structures
# Developed by: Kamala Priya

def calculate_grade(avg):
    if avg >= 90:
        return "A", "Excellent performance!"
    elif avg >= 80:
        return "B", "Very good work!"
    elif avg >= 70:
        return "C", "Good, but can improve."
    elif avg >= 60:
        return "D", "Needs improvement."
    else:
        return "F", "Failed. Needs serious effort."

def get_valid_mark(subject):
    while True:
        try:
            mark = float(input(f"Enter {subject} marks (0-100): "))
            if 0 <= mark <= 100:
                return mark
            else:
                print("Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input! Enter a number.")

def main():
    print("=" * 60)
    print("        STUDENT GRADE CALCULATOR")
    print("=" * 60)

    while True:
        try:
            n = int(input("Enter number of students: "))
            if n > 0:
                break
            else:
                print("Number must be greater than zero.")
        except ValueError:
            print("Invalid input! Enter an integer.")

    names = []
    results = []

    for i in range(n):
        print(f"\nStudent {i+1}")
        name = input("Enter student name: ").strip()
        while not name:
            print("Name cannot be empty.")
            name = input("Enter student name: ").strip()

        math = get_valid_mark("Math")
        science = get_valid_mark("Science")
        english = get_valid_mark("English")

        avg = (math + science + english) / 3
        grade, comment = calculate_grade(avg)

        names.append(name)
        results.append({
            "average": avg,
            "grade": grade,
            "comment": comment
        })

    print("\n" + "=" * 60)
    print("RESULTS SUMMARY")
    print("=" * 60)
    print(f"{'Name':<20}{'Average':<10}{'Grade':<8}Comment")
    print("-" * 60)

    for i in range(n):
        print(f"{names[i]:<20}{results[i]['average']:<10.1f}{results[i]['grade']:<8}{results[i]['comment']}")

    averages = [r["average"] for r in results]
    print("\n" + "=" * 60)
    print("CLASS STATISTICS")
    print("=" * 60)
    print("Total Students:", n)
    print("Class Average:", round(sum(averages) / n, 2))
    print("Highest Average:", max(averages))
    print("Lowest Average:", min(averages))

    # Save results
    with open("results_sample.txt", "w") as file:
        for i in range(n):
            file.write(f"{names[i]} - Avg: {results[i]['average']:.2f}, "
                       f"Grade: {results[i]['grade']}, "
                       f"Comment: {results[i]['comment']}\n")

    print("\nResults saved to results_sample.txt")
    print("Thank you for using the Grade Calculator!")

if __name__ == "__main__":
    main()

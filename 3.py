def manage_marks():
    marks = []
    while len(marks) < 5:
        try:
            mark = float(input("Enter marks: "))
            marks.append(mark)
        except ValueError:
            print("Please enter a valid number.")

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    print("\nMarks:", marks)
    print("Average:", average)
    print("Highest Marks:", highest)
    print("Lowest Marks:", lowest)
    marks.sort(reverse=True)
    print("Marks in Descending Order:", marks)


manage_marks()
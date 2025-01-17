import openpyxl

def write_grades_to_excel(file_path, student_grades):
    try:
        # Create a new workbook and select the active sheet
        workbook = openpyxl.Workbook()
        sheet = workbook.active

        # Add headers
        sheet.append(["Name", "Grade"])

        # Write student grades to the sheet
        for name, grade in student_grades.items():
            sheet.append([name, grade])

        # Save the workbook
        workbook.save(file_path)
        print(f"Grades have been written to {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
grades = {
    "Alice": "A",
    "Bob": "B",
    "Charlie": "A",
    "Diana": "C"
}

file_path = "student_grades.xlsx"  # Desired output Excel file path
write_grades_to_excel(file_path, grades)
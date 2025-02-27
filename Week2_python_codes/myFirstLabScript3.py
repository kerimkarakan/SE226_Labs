std_name = input("Name: ")
lab_grade = int(input("Lab: "))
midterm_grade = int(input("Midterm: "))
final_grade = int(input("Final: "))

calculated_lab_grade = lab_grade * 0.25
calculated_midterm_grade = midterm_grade * 0.35
calculated_final_grade = final_grade * 0.40

print(f"Last Score: {calculated_lab_grade + calculated_midterm_grade + calculated_final_grade}")


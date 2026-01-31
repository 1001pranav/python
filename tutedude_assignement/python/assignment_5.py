def task_1_student_dictionary(student_info = {}) -> None:
    student_name = input("Enter the Student Name ")
    student_marks = input(f"Enter the Marks for {student_name} ")

    if not student_marks.isdigit():
        print("Student Marks should be Number")
        raise ValueError("Marks should be a number")
    
    student_marks = int(student_marks)

    student_info[student_name] = student_marks
    
    find_student_name = input("Find Student Name")

    if find_student_name in student_info:
        print(f"Student Name - {find_student_name}")
        print(f'Marks - {student_info[find_student_name]}')
    else: 
        print("student not found")

def task_2_slicing():
    num_data = list(range(1, 11))
    sliced_list = num_data[:4:-1]
    print("Last 5 Numbers ", num_data[5:])
    print("Reversed Numbers ", sliced_list)
if __name__ == '__main__':
    student_info = {}

    task_1_student_dictionary(student_info)





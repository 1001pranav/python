import os

def task_1_read_files() -> None: 
    file_name =os.path.join('assets', 'sample.txt')
    try:
        with open(file_name, 'r') as file:
            content = file.read() 
            print(content)
    except EOFError as E:
        print(E)
    except FileNotFoundError as E:
        print(f"The file {file_name} not found")


def task_2_write_files() -> None:
    file_name = os.path.join('assets', 'output.txt')
    try:
        with open(file_name, 'w') as file:
            input_file = input("Enter text to write into file ")
            file.writelines(input_file)
            file.writelines('\n')
            file.close()

        with open(file_name, 'a') as file:
            input_file = input("Enter text to append into file ")
            file.writelines(input_file)
            file.close()

    except FileNotFoundError as E:
        print(E)
    except PermissionError as E:
        print(E)
    

if __name__ == "__main__":

    task_1_read_files()
    task_2_write_files()

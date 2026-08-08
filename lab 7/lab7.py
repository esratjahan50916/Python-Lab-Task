import os

# Problem 1:

def divide_numbers(a, b):
    try:
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")


divide_numbers(10, 2)
divide_numbers(10, 0)


# Problem 2:

def is_number(text):
    try:
        float(text)
        return True
    except ValueError:
        return False


def add_two_numbers(num1_text, num2_text):
    try:
        if not is_number(num1_text) or not is_number(num2_text):
            raise TypeError("Both inputs must be numerical")
        total = float(num1_text) + float(num2_text)
        print("Sum:", total)
    except TypeError as e:
        print("Error:", e)


# Problem 2

add_two_numbers("10", "20")
add_two_numbers("10", "abc")


# Problem 3:

def access_list_element(lst, index):
    try:
        value = lst[index]
        print("Value at index", index, ":", value)
    except IndexError:
        print("Error: Index", index, "is out of range")
    except TypeError:
        print("Error: Index must be an integer, not", type(index).__name__)


print("Problem 3")
numbers = [10, 20, 30, 40, 50]
access_list_element(numbers, 2)
access_list_element(numbers, 10)
access_list_element(numbers, "a")


# Problem 4:

def write_to_file(filepath, content):
    try:
        with open(filepath, "w") as file:
            file.write(content)
        print("Write mode: file written successfully")
    except Exception as e:
        print("Error while writing file:", e)


def read_from_file(filepath):
    try:
        with open(filepath, "r") as file:
            data = file.read()
        print("Read mode: file content is ->")
        print(data)
    except FileNotFoundError:
        print("Error: File does not exist, cannot read")


def append_to_file(filepath, content):
    try:
        with open(filepath, "a") as file:
            file.write(content)
        print("Append mode: content appended successfully")
    except Exception as e:
        print("Error while appending to file:", e)


def create_new_file(filepath, content):
    try:
        with open(filepath, "x") as file:
            file.write(content)
        print("Create mode: new file created successfully")
    except FileExistsError:
        print("Error: File already exists, cannot create again")



folder_path = "lab7_files"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

file_path = os.path.join(folder_path, "sample.txt")


if os.path.exists(file_path):
    os.remove(file_path)

create_new_file(file_path, "Hello Python\n")
create_new_file(file_path, "Hello Again\n")

write_to_file(file_path, "This line was written using write mode.\n")
append_to_file(file_path, "This line was added using append mode.\n")
read_from_file(file_path)

read_from_file(os.path.join(folder_path, "missing.txt"))

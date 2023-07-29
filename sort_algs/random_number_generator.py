import os
import random

def generate_random_integers(num_integers, min_range, max_range):
    """
    Generate a list of random integers within a specified range.
    """
    integers = [random.randint(min_range, max_range) for _ in range(num_integers)]
    return integers

def write_to_text_file(integers, file_path):
    """
    Write the list of integers to a text file in the specified format.
    Each integer is written on a separate line.
    """
    with open(file_path, 'w') as file:
        for num in integers:
            file.write(str(num) + '\n')

if __name__ == "__main__":
    num_integers = 1000000
    min_range = 1
    max_range = 1000000
    folder_path = "numbers"
    file_name = "1000000.txt"

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = os.path.join(folder_path, file_name)

    random_integers = generate_random_integers(num_integers, min_range, max_range)
    write_to_text_file(random_integers, file_path)
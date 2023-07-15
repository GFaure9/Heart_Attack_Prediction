import yaml


def load_yaml_file(file_path):
    with open(file_path, 'r') as file:
        try:
            data = yaml.safe_load(file)
            return data
        except yaml.YAMLError as e:
            print(f"Error while loading YAML file: {e}")


def find_two_numbers(target):
    n1 = int(target**0.5)  # Start with the square root of the target as the first number
    while n1 >= 1:
        if target % n1 == 0:  # If n1 is a factor of the target
            n2 = target // n1  # Compute the second number
            return n1, n2  # Return the two numbers
        n1 -= 1  # Decrement n1

    return None  # If no two numbers are found, return None
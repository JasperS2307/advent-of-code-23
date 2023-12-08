import os

def read_file(input_file):
    with open(os.path.join(os.path.dirname(__file__), input_file), 'r') as file:
        lines = file.readlines()

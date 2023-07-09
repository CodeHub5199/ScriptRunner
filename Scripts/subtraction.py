input_req = {'text': 2}

import argparse

# Create an argument parser
parser = argparse.ArgumentParser(description='Perform addition of two numbers.')

# Add command-line arguments
parser.add_argument('arg1', type=int, help='First number')
parser.add_argument('arg2', type=int, help='Second number')

# Parse the command-line arguments
args = parser.parse_args()

input1 = args.arg1
input2 = args.arg2

def sub(input1, input2):
    result = input1-input2
    return f'The subtraction of {input1} and {input2} is {result}'

print(sub(input1, input2))



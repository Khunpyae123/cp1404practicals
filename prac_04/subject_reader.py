"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"

def main():
    data = load_data()
    show_data(data)

def load_data():
    data = []
    with open(FILENAME) as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(',')
            parts[2] = int(parts[2])
            data.append(parts)
    return data

def show_data(data):
    for parts in data:
        print(f"{parts[0]} is taught by {parts[1]} and has {parts[2]} students.")

main()

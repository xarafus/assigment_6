fname = input("Enter a file name: ")

try:
    with open(fname, 'r') as fhand:
        for line in fhand:
            print(line.upper().rstrip())
except FileNotFoundError:
    print(f"File not found: {fname}")
except Exception as e:
    print(f"An error occurred: {e}")

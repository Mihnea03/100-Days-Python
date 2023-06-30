import sys
import os

# First argument: The day of the project
# Second argument: The name of the project
# Call the script like this: 'python3 create_new_project.py {first_argument} {second_argument}'

args = sys.argv

folder_name = f"day-{args[1]} {args[2]}" 
os.mkdir(folder_name)

header = f"""# {args[2]}
# Munteanu Mihnea @ Mihnea03

def main():
    return

if __name__ == '__main__':
    main()
"""

with open(folder_name + '/main.py', 'w') as main:
    main.write(header) 

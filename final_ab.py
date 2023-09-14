import datetime

r = "ROLL NO :-"

# Student data (rollno: name) in dictionary (needed)
students = {
    "1": "KSHITIJ DATAR",
    "2": "HASAN DHUKA",
    "3": "RAJAN GUPTA",
    "4": "SAIRAJ JITEKAR",
    "5": "TEJAS KADU",
    "6": "PRIT PAREKH",
    "7": "ANAS PATEL",
    "8": "SIDDESH PATIL",
    "9": "PARAS RANA",
    "10": "AISHWARYA SAWANT",
    "11": "AMAN SINGH",
    "12": "RISHABH SINGH",
    "13": "ANJALI VISHWAKARMA",
    "14": "AADITYA YADAV",
    "15": "KOMAL ZALTE"
}

# Get today's date
current_date = datetime.datetime.now().strftime("%d-%m-%Y")

# Create an empty absent list
absent_list = []

# Print the students' list
print("\nSTUDENTS LIST : -")
for rollno, name in students.items():
    print(f"{rollno}: {name}")

# Input absent roll numbers
num_absent = int(input("Enter the number of absent students: "))
for i in range(num_absent):
    rollno = input(f"Enter the roll number of absent student {i + 1}: ")
    if rollno in students:
        absent_list.append((rollno, students[rollno]))
    else:
        print(f"Roll number {rollno} not found in the student list.")

def remove_space(text):
     return text.replace(" )", ")")

# Sort the absent_list by roll number in ascending order
absent_list.sort(key=lambda x: int(x[0]))

# Print output
print("DATE:", current_date)
print("S.Y DS")
print("ABSENT LIST : -")
j = 1
for rollno, name in absent_list:
    print(remove_space(f"{j}) {name}"),",", r,f"{rollno}")
    j = j + 1
print(f"\nTOTAL ABSENT NO :- {len(absent_list)}")

non = int(input("TO AVOID CLOSURE"))
print(non)
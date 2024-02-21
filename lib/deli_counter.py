# lib/deli_counter.py

katz_deli = []

def line(deli_queue):
    if not deli_queue:
        print("The line is currently empty.")
    else:
        line_status = "The line is currently:"
        for i, person in enumerate(deli_queue, start=1):
            line_status += f" {i}. {person}"
        print(line_status)

def take_a_number(deli_queue, name):
    deli_queue.append(name)
    print(f"Welcome, {name}. You are number {len(deli_queue)} in line.")

def now_serving(deli_queue):
    if deli_queue:
        next_person = deli_queue.pop(0)
        print(f"Currently serving {next_person}.")  # Updated message
    else:
        print("There is nobody waiting to be served!")

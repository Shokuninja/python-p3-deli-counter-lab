katz_deli = []

def line():
    if len(katz_deli) == 0:
        return 'The line is currently empty.'
    else:
        people_list = [str(katz_deli.index(person) + 1) + f". {person}" for person in katz_deli]

        people_string = " ".join(people_list) 
        return f'The line is currently: {people_string}'

def take_a_number(init_name_string):
    global katz_deli
    name_string = init_name_string.title()
    katz_deli.append(name_string)
    print(f"{name_string}, you're in position {(katz_deli.index(name_string)) + 1}.")

def now_serving(next_customer):
    global katz_deli
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"{next_customer.title()}, you're up next.")
        katz_deli.pop(0)

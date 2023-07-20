def format_name(f_name, l_name):
    first_name = f_name.title()
    last_name = l_name.title()
    return f"{first_name} {last_name}"

name = input("What is your first name? ")
surname = input("what is your last name? ")
print(format_name(name, surname))

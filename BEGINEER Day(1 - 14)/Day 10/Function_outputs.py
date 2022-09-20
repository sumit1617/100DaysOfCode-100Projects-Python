# Function wih outputs

def format_name(f_name, l_name):
    """Takes a first and last name and format it to return the title case version of the name""" 
    # the triple double inverted comma can also be used for multiline comments
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"Your full name is {formatted_f_name} {formatted_l_name}"

print(format_name(f_name = input("Type your first name.\n"),
            l_name = input("Type your last name.\n")))
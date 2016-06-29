"""
    Brandon Herford
    5/6/2016

    This program takes a list of last names and joins them with a first name
    that is entered by a user. The completed names are then output.
"""

# Function 'name_gen' (name generator) is defined.
def name_gen(first_name, last_names):
    """Take every last name from the list and add the user's first name to it."""
    # Set a new variable for the list of last names.
    new_last_name = last_names[:]

    # For every index in the list; something will be done.
    for i in range(len(new_last_name)):

        # Combine the user's first name, along with a space to each last name
        # in the list.
        new_last_name[i] = first_name + " " + new_last_name[i]

    # Send the newly combined list back to the main() function,
    # which is then assigned to the 'new_name' variable.
    return new_last_name

# Main funciton is defined.
def main():

    # Get the first name from the user.
    first_name = input("What is your first name? ")

    # This is a list of last names that isassigned to 'list_names'.
    list_names = ["Bumbledrum", "Thibblepom", "Pineapple", "Mountain", ]

    # Call a function with two parameters to return a value for 'new_name'.
    new_name = name_gen(first_name, list_names)

    # Print the returned value from the name_gen() function.
    print(new_name)

# Call the main funciton.
main()



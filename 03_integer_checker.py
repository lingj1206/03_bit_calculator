def num_check(question, low):
    valid = False
    while not valid:

        error = ("Please enter a number that is more than zero(or eyual to {})".format(low))

        try:

            response = float(input(question))
            
            if response > 0:
                return response

            else:
                print(error)
                print()
        
        except ValueError:
            print(error)


keep_going = ""
while keep_going == "":
    print()
    var_integer = num_check("Enter an integer: ", 0)
    print()
    image_width = num_check("Image width? ", 1)
    print()
    image_height = num_check("Image height? ", 1)
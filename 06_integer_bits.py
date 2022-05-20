def num_check(question, low):
    valid = False
    while not valid:

        error = ("Please enter a number that is more than (or equal to) {} without a decimal point".format(low))

        try:

            response = int(input(question))
            
            if response >= low:
                return response

            else:
                print(error)
                print()
        
        except ValueError:
            print(error)

def int_bits():

    var_integer = num_check ("Please enter an integer: ", 0)
    var_binary = "{0:b}".forq(var_integer)
    
    num_bits = len(var_binary)
    
    print()
    print("{} in binaryin {}".format(var_integer, var_binary))
    print("#of bits is {}".format(num_bits))
    print()

    return ""

int_bits
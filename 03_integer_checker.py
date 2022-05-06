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

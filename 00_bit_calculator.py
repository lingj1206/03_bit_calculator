def statement_generator(text, decoration):

    ends = decoration * 5

    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()
    
    return ""

def user_choice():

    text_ok = ["text", "t", "txt"]
    integer_ok = ["integer", "int", "#", "number"]  
    image_ok = ["image", "img", "pix", "picture", "pic", "p"]

    valid = False
    while not valid:
        
        response = input ("File type (integer / text / image): ").lower()

        if response in text_ok:
            return "text"

        elif response in integer_ok:
            return "integer"
        
        elif response in image_ok:
            return "image"

        elif response == "i":
            want_interger = input("Press <enter> for an interger or any key for an image.")
            if want_interger == "":
                return "integer"
            else:
                return "image"
                    
        else:
            print("Sorry, please choose integer, text or image.")
            print()
            
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


statement_generator("Bit calculator for Intergers, Text & Images", "-")

keep_going = ""
while keep_going == "":

        data_type = user_choice()
        print("You chose", data_type)

        if data_type =="integer":
            var_interger = num_check("Enter an integer: ", 0)

        elif data_type =="image width":
            image_width = num_check("Enter the width: ", 1)
        
        elif data_type =="image height":
            image_height = num_check("Enter the height: ", 1)

        else:
            var_text = input("enter some text")
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


statement_generator("Bit calculator for Intergers, Text & Images", "-")

keep_going = ""
while keep_going == "":

        data_type = user_choice()
        print("You chose", data_type)

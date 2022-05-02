def user_choice():

    text_ok = ["text", "t", "txt"]
    interger_ok = ["interger", "int", "#", "number"]  
    image_ok = ["image", "img", "pix", "picture", "pic"]

    valid = False
    while not valid:

        response = input ("File type (interger / text / image): ").lower()

        if response in text_ok:
            return "text"

        elif response in interger_ok:
            return "text"
        
        elif response in image_ok:
            return "interger"

        elif response == "i":
            want_interger = input("Press <enter> for an interger or any key for an image")
            if want_interger == "":
                return "interger"
            else:
                return "image"
                
        else:
            print("please choose a valid file type")
            print()

data_type = user_choice()
print("you chose", data_type)
print()
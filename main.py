from form import Myfunction

list = []


def menu_call():
    while True:

        try:

            print("""
        ##################################################
        You have to choose the Number so you can get the options 
        To get the Mean --> 1
        To get the Median --> 2
        To get the Modo --> 3
        To get the Skewness --> 4
        To get the  Enter new lista value --> 5
        To get the Data Type --> 6
        To get the Add more element to list --> 7
        To get the Exit --> 8
        ################################################
        """)
            nux = int(input("Put Your Number Here: "))
            x = Myfunction(list)
            match nux:
                case 1:
                    print("###################################")
                    print("The mean Value is : ", x.get_mean())

                case 2:
                    print("###################################")
                    print("The median Value is : ", x.get_median())

                case 3:
                    print("###################################")
                    print("The Mode is :", x.get_mode())

                case 4:
                    print("###################################")
                    print("The Skewness value is :", x.get_skewness())

                case 5:
                    print("###################################")
                    x.set_new_Number()
                case 6:
                    print("###################################")
                    x.data_type()

                case 7:
                    print("###################################")
                    x.add_number()

                case 8:
                    break

        except Exception:
            print("""
            NOTE: You have enter wrong value.
            Make sure you did put any value the right number
            from 1 to 8. DO NOT ADD CHARACTERS.
            """)


while True:

    print("""
    ##################################################
    You have to enter only 1 number at time
    You will have the option to continue or not
    ex: you can enter 55 after 5.
    Note: you are not allowed to use comma here of different characters 
    
    Enter 1 to add value into the list.
    Enter 2 to end the programming
    Enter 3 to have access to the programming functions
    ##########################################################
    """)

    try:
        m = int(input("Enter 1, 2 or 3: "))  # m variable will only receive the yes or no
        if m == 1:

            list.append(int(input("Enter your value here: ")))  # here we add the user value to the list
            print("#########################################")
            print("The number of elements are:", len(list))
            print("The Numbers are: ", list)


        # this statament will check if we have more than 2 elements in the list
        elif m == 2:
            break

        elif m == 3:

            if len(list) <= 2:
                print("You have to put more number")
                continue
            menu_call()
            break

        else:
            print("#########################################")
            print("You have enter wrong value")


    except Exception:
        print("#########################################")
        print("You have enter wrong value")


class Myfunction:
    # Initialize an instance of the class with a list of numbers
    def __init__(self, num_lista):
        self.num_lista = num_lista


    # Define a method named "get_median" to calculate the median of the list of numbers
    def get_median(self):
        n = len(self.num_lista)
        self.num_lista.sort() # Sort the list in ascending order
        # If the length of the list is even, take the average of the two middle numbers as the median
        if n % 2 == 0:
            median1 = self.num_lista[n // 2]
            median2 = self.num_lista[n // 2 - 1]
            median = (median1 + median2) / 2


            # If the length of the list is odd, take the middle number as the median
        else:
            median =self.num_lista[n // 2]

        return median


    # Define a method named "get_mean" to calculate the mean of the list of numbers

    def get_mean(self):
        # Find sum of the numbers
        num_sum = sum(self.num_lista)
        # divide the sum with length of the list
        mean = num_sum / len(self.num_lista)

        return round(mean, 2)



    # Define a method named "get_mode" to calculate the mode of the list of numbers
    def get_mode(self):
        # Create an empty dictionary to store the frequency of each self.num_lista
        frequency_dict = {}

        # Loop through each self.num_lista in the list and count its frequency
        for number in self.num_lista:
            if number in frequency_dict:
                frequency_dict[number] += 1
            else:
                frequency_dict[number] = 1

        # Check if all frequencies are equal to 1
        if all(freq == 1 for freq in frequency_dict.values()):
            print("There is no mode in the list.")
            return []

        # Find the self.num_lista(s) with the highest frequency
        mode = []  # Initialize an empty list to store the mode(s)
        max_frequency = 0  # Initialize the maximum frequency to 0

        # Loop through the dictionary to find the number(s) with the highest frequency
        for number, frequency in frequency_dict.items():
            if frequency > max_frequency:
                mode = [number]
                max_frequency = frequency
            elif frequency == max_frequency:
                mode.append(number)

        # Return the mode(s) as a list
        return mode



    # Define a method named "get_skewness" to calculate the skewness of the list of numbers
    def get_skewness(self):

        try:

            # calculate mean and standard deviation

            stdev = (sum((x - self.get_mean()) ** 2 for x in self.num_lista) / len(self.num_lista)) ** 0.5 # Calculate the standard deviation

            # calculate skewness

            skewness = (3*(self.get_mean() - self.get_median())/ stdev) # Calculate the skewness using the formula

            # print the result
            return round(skewness, 4)

        except Exception:

            print("The Number of number is small for skewness calculation, add more.")


    # Define a method named "set_new_Number" to allow the user to enter a new list of numbers
    def set_new_Number(self):
        # Ask the user to enter three numbers separated by commas
        while True:
            try:
                old_list = self.num_lista
                new_number = input("Enter three numbers separated by commas: ")
                # Split the input by commas and store in m
                m = new_number.split(",")
                # If the user entered less than three numbers, ask them to try again
                if len(m) <= 2:
                    print("You must enter exactly three or more numbers")
                    continue
                    # Convert each number from string to integer and store in num_lista
                for i in range(len(m)):
                    m[i] = int(m[i])
                    self.num_lista = m
                    # Print the list of numbers that was entered and exit the loop
                print("This was the old list:", old_list)
                print("This is the new list: ", m)
                break
            except ValueError:
                # If the user entered something other than integers, ask them to try again
                print("Invalid input. Please enter three integers separated by commas.")



    def add_number(self):
        # Ask the user to enter numbers separated by commas
        while True:

            try:
                m = input("Enter numbers separated by commas: ")
                # Split the input by commas and convert each number from string to integer
                d = list(map(int, m.split(",")))
                # Add the new numbers to num_lista and print the updated list
                self.num_lista.extend(d)
                print("This are new number added: ",self.num_lista)
                break
            except Exception:
                # If the user entered something other than integers, ask them to try again
                print("You have enter wrong value")






    def data_type(self):
        # Check the data type of num_lista and print a message indicating it is a list of numbers
        d = type(self.num_lista)
        if d is list:
            print("This is the List of numbers")





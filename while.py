# set the intial total value to zero - we will increase the running sum by the number entered by a user
total = 0 
while True:
    # request user to input non zero integer
    number = int(input("Enter a non-zero integer to get a running sum [press -1 to stop]: "))
    # check if number is not zero - ask user to enter a non-zero integer
    if(number == 0):
        print("Wrong number. Number must not be equals to zero.") 
    # exit loop if user enters -1
    elif(number == -1):
        break
    
    # sum up all the numbers entered (exclude 0 and -1 in the calcultation) 
    total = total + number


    
print(f"Total: {total}")

    
names = [] # initialize an empty list to store the names in the file
birthdate = [] # initialize an empty list to store the birth dates in the file
filename = "DOB.txt"
try:        
    with open(filename, "r+") as file: # open file 
        for line in file: # iterate through each line 
            lines = line.split(sep=",", maxsplit= 2) # split each line into 2 ;  separated by a comma and store it in a list
            names.append(lines[0].strip()) # adds each word at the first index to the list of name
            birthdate.append(lines[1].strip()) # add each word at the second index to the list of birthdate
            
    # print names
    print("*****NAME*****")
    for name in names:
        print(name)
            
    print("\n")
    print("*****DATE OF BIRTH*****")
    for date in birthdate:
        print(date)
except FileNotFoundError:
    print(f"The file '{filename}' does not exist")
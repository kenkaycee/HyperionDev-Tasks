# output arrow pattern
# outer loop counts from 1 to 5
for i in range(6): # loop from 1 to 5
    print("*" * i) # print number of stars corresponding to the value of i
    if(i == 5): # check if the value of i is equals to 5
        
        for j in range(4, 0, -1): # inner loop counts from 4 to 1
            print("*" * j ) # print number of stars corresponding to the value of j
# request a user to enter a sentence 
str_manip = input("Enter a sentence: ")

# string manipulations

# Calculate and display the length of of str_manip 

# solution 
# first remove the white spaces in the sentence
str_manip_transformed = str_manip.replace(" ", "")
# get the length of the transformed sentence 

str_manip_length = len(str_manip_transformed)

# display the length 
print(f"Number of characters: {str_manip_length}")

""" Find the last letter in str_manip sentence. Replace every occurrence
of this letter in str_manip with ‘@’. """  

str_manip_last_letter = str_manip[-1] # get the last letter of the sentence 

# replace the last letter with "@"
str_manip_replace_last_character = str_manip.replace(str_manip_last_letter, "@")
# display 
print(str_manip_replace_last_character)

#Print the last three characters in str_manip backwards.
# first reverse the sentence
str_manip_reversed = str_manip[::-1]
# then print the first three letters of the reversed sentence 
print(str_manip_reversed[:3])

"""Create a five-letter word that is made up of the first three characters
and the last two characters in str_manip"""
# first - get the first three letters 
str_manip_first_three_letters = str_manip[0:3]
# get the last two characters 
str_manip_last_two_letters = str_manip[-2:]
# join the two variables 
str_manip_joined = str_manip_first_three_letters + str_manip_last_two_letters
# display result
print(str_manip_joined)
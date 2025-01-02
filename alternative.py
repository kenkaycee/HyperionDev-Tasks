"""Task 1a: Write a program that reads in a string and makes each alternate
character into an uppercase character and each other alternate character
a lowercase character.
E.g.: The string “Hello World” would become “HeLlO WoRlD"""

# solution

# function that reads a string and makes each alternative character into upper case letter and lower case letter

def upperToLowerAlternateCharacter(sentence):
      
    # loop through the characters in the sentence 
    for char in range(len(sentence)):
        if(char == 0): # make the first letter upper case 
            print(sentence[char].upper(), end="") # end = "" print all character on one line
        else:
            if(char % 2 == 0): # upper case the characters at even index
                print(sentence[char].upper(), end="")
            else:
                print(sentence[char].lower(), end="")    # lower case the characters at odd index

# test function 
upperToLowerAlternateCharacter("I love programming in python and java")     
            
            
"""Task1b: Now, try starting with the same string but making each alternative word
lowercase and uppercase.
E.g.: The string “I am learning to code” would become “i AM learning TO
code”.
"""

# solution
# function that reads a string and makes alternative word lowercase and uppercase
def upperToLowerAlternateWord(sentence):
    # split the sentence into list of words that makes up the sentence
    split_sentence = sentence.split()
    for word in range(len(split_sentence)):
        if(word == 0):
            print(split_sentence[word].lower(), end=" ")
        else:
            if(word % 2 == 0):
                print(split_sentence[word].lower(), end=" ")
            else:
                print(split_sentence[word].upper(), end=" ")

# test function 
upperToLowerAlternateWord("I am learning to code")

        

import random 
import string 

# Generating random characters
def genchar():
    chars = random.sample(string.ascii_letters, 3)
    r1:str=""
    for character in chars: r1 += character
    return r1

def coding(s):
#  If the word contains at least 3 characters , remove the first letter & append it at the end
#  now append three random characters at the starting & at the end .
# else : Simply reverse the String
    words = s.split(" ")
    code_word : str =""
    for word in words : 
       if len(word)>=3 :
          word = genchar()+word[1:] + word[0]+genchar()
          code_word += word + " "
       else : 
          char:str = ""
          rev = list()
          for character in word:rev.append(character)
          rev.reverse()
          for index in range(len(rev)):char += rev[index]
          code_word += char + " "
    print(code_word.capitalize())

def decoding(s):
# If the word contains less than 3 characters reverse it  
# else : Remove 3 characters from start & end .  Now remove the last letter & append it to end the beginning .
    words = s.split(" ")
    decoded_word : str =""
    for word in words:
        char:str = ""
        rev = list()
        if len(word)>=3 :
            for character in word:rev.append(character)
            for i in range(0,3):
                rev.pop(0)
                rev.pop(-1)
            for index in range(len(rev)):char += rev[index]
            char = char[len(char)-1]+char[0:len(char)-1]
        else :
          for character in word:rev.append(character)
          rev.reverse()
          for index in range(len(rev)):char += rev[index]
        decoded_word += char + " "
    print(decoded_word.capitalize())

# Taking Input
operations = ("Coding","Decoding")
print("These are the possible operations")
for operation in operations: print(operation,sep=" ")
op = input("Chosse your operation : ")
if op.lower()=="coding": 
 # Coding
    sent = input("Enter the statement you want to \" ENCODE \" : ")
    coding(sent.lower())
 
elif op.lower() == "decoding": 
 # Decoding
    code = input("Enter the code you want to \" DECODE \" : ")
    decoding(code.lower())
else : raise Exception("Please put valid input or check your spelling")
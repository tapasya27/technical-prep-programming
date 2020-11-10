#Replacing spaces with "%20" in a string without replace


#approach 1 - using replace
def replace_space(string):
    string = string.rstrip()
    string = string.replace(" ","%20")
    print(string)


#replace_space("Mr. John Smith      ")

#approach 2, using a deque

from collections import deque
def replace_string(string):
    temp = deque()
    string = string.rstrip()
    for i in string:
        if i == " ":
            temp.append("%20")
        else:
            temp.append(i)

    final_word = ""
    for element in temp:
        final_word+=element

    print(final_word)


#replace_string("Mr. John Smith      ")


#approach 3 - this using a basic queue

def replace_string(string):

    temp=[]
    string = string.rstrip()
    for i in string:
        if i != " ":
            temp.append(i)
        else:
            temp.append("%20")

    final_word = ""
    count=0
    while count<len(temp):
            final_word+=temp[count]
            count+=1

    print(final_word)

#replace_string("Mr. John Smith      ")


#approach 4 - modifying the string itself
def modify_string(string):
    string = string.rstrip()
    temp = []
    for i in string:
        if i == " ":
            temp.append("%20")
        else:
            temp.append(i)

    string = ""
    for element in temp:
        string+=element

    print(string)

modify_string("Mr. John Smith      ")
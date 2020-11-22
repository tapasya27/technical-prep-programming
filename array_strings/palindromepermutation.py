from collections import Counter

def count_even(counter_dict, string):
    #check even odd:
    #if even, continue, if odd remove
    if len(string) % 2 != 0: #odd number
        for key,value in counter_dict.items():
            if value == 1:
                del counter_dict[key]
                break

    Track = False
    for i in counter_dict:
        if counter_dict[i] == 2:
            Track = True
        else:
            Track = False

    return Track


def perm_pal(string):
    string = string.lower().replace(" ", "")   #making my string lower
    char_Track = Counter(string) #making my counter
    if count_even(char_Track, string) == True:
        if len(string)%2 != 0:
            count = 0
            for i in char_Track:
                if char_Track[i] == 1:
                    count+= 1
            if count>1:
                return False
            else:
                return True
        else:
            return True
    else:
        return False

print(perm_pal("Tact Coao"))
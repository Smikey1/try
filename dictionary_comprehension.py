'''
doc string
'''


def my_func(a,b):
    ''' This is a function takes two value And return their max value '''
    return max(a,b)


print(my_func(2,3))

'''
# dictionary comprehension
syntax1: {append_item for loop}
syntax2: {key:(do if-condition else do) for loop}
'''

def square_func(num):
    new_dict={}
    for element in range(0,num+1):
        square = element**2
        if square %2 ==0:
            new_dict[square]="even num"
        else:
            new_dict[square]="odd num"
    return new_dict

print(square_func(5))

print({f"k{k}-->":k**2 for k in range(0,5+1)})
print({k**2:("even num" if k**2%2==0 else "odd num") for k in range(0,5+1)})

def count_char(name):
    char_empty_dict={}
    for char in name:
        char_empty_dict[char]=name.lower().count(char)
    return char_empty_dict

full_name = input("please enter your full name:")
print(count_char(full_name))

print({char: full_name.lower().count(char.lower()) for char in full_name.lower()})
print({f"char->{char}": full_name.lower().count(char.lower()) for char in full_name.lower()})
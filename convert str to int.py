def str_to_int(str,index=0):
    if index == len(str):
        return 0
    #Convert current character to its integer equivalent
    digit = int(str[index])
    remaining_value=str_to_int(str,index+1)
    result=(digit *(10**(len(str)-index-1)))+remaining_value
    return result
x=input("Enter  the string:  ")
print(type(x))
print("The string convert to integer is: ")
output=str_to_int(x)
print(output) 
print(type(output))
print(type(x))
    

    

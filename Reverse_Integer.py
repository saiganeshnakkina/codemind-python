def reverse_number(num):
    
    num_str = str(abs(num))
    
    
    reversed_str = num_str[::-1]
    
    reversed_num = int(reversed_str)
    
    
    if num < 0:
        reversed_num *= -1
    
    return reversed_num


number1 = int(input())
reversed_number1 = reverse_number(number1)
print(reversed_number1) 


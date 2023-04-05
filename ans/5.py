# 5.

def print_max():
    numbers = list()

    for i in range(0, 5):
        num = input()
        numbers.append(int(num))
    
    print(max(numbers))
    
print_max()

print('It computes the square of each number')

value = []
sqr_value = []


def sqr_num(values, sqr_values):
    while(True):
        num = eval(input('Enter the number\n:-'))
        values.append(num)
        num = num **2
        sqr_values.append(num)
        choice = input("Want to enter another number")
        if choice == 'n' or choice == 'N':
            break
        else:
            continue
    return values, sqr_values


sqr_num(value, sqr_value)

print(value)
print(sqr_value)

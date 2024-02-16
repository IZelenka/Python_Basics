import calc


def main() -> None:
    sum = calc.add_numbers(2, 2)
    print(sum)

def number_print() -> None:
    hodn_1 = str(calc.MY_VECTOR [4])
    hodn_2 = str(calc.MY_VECTOR [2])

    print (hodn_1 + ", " + hodn_2) 
    print (calc.MY_VECTOR [4] + calc.MY_VECTOR [2])

# main()

# number_print()

for i in range (0, 10, 1):
    if i+1<5:
        print(i, end = ", ")
    elif i+1<10:
        print(i, end = "- ")
    else:
        print(i)

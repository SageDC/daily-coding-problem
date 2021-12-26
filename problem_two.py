# Question asked by Uber (Hard)

def main():
    # arguments
    numList1 = [1, 2, 3, 4, 5]
    numList2 = [3, 2, 1]

    position = 0
    product = 1
    for i in range(len(numList1)):
        # base cases
        if len(numList1) == 0 or len(numList1) == 1:
            return numList1
        elif position != i and i != len(numList1):
            product = product * numList1[i]
        elif i == len(numList1) - 1:
            position = position + 1
        numList1[position] = product
    return numList1

if __name__ == '__main__':
    print(main())
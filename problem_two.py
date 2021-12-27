# Question asked by Uber (Hard)

def main():
    # argument
    numList = [1, 2, 3, 4, 5]
    resList = [None]*len(numList)

    # base case
    if len(numList) == 0 or len(numList) == 1:
        return numList

    product = 1
    for i in range(len(numList)):
        for j in range(len(numList)):
            if(i != j):
                product = product * numList[j]
        resList[i] = product
        product = 1

    return resList


if __name__ == '__main__':
    print(main())
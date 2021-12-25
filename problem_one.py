def main():
    # arguments
    numList = [10, 15, 3, 7]
    sum_k = 17

    placekeeper = 0
    for i in range(len(numList)):
        if numList[placekeeper] + numList[i] == sum_k and placekeeper != i:
            return True

    return False

if __name__ == '__main__':
    print(main())
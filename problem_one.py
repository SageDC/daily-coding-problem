def main():
    # arguments
    numList = [0]
    sum_k = 17

    placekeeper = 0
    for i in range(len(numList)):
        if numList[placekeeper] + numList[i] == sum_k and placekeeper != i:
            return True
        elif i == 3:
            placekeeper = placekeeper + 1
    return False

if __name__ == '__main__':
    print(main())
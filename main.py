def bubbleSort(array):
    # Write your code here.
    swaps = True

    while swaps == True:
        swaps = False
        for ptr in range(len(array)-1):
            next = ptr + 1
            if array[ptr] > array[next]:
                swaps = True
                # swap elements ptr and next
                temp = array[ptr]
                array[ptr] = array[next]
                array[next] = temp
    return array
    pass

if __name__ == '__main__':

    print(bubbleSort([3,2,1]))
    print(bubbleSort([8,5,2,7]))
    print(bubbleSort([20]))

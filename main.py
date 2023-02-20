# O(n^2) time \ O(1) space

def bubbleSort(array):
    # Write your code here.
    swaps = True

    while swaps == True:
        swaps = False
        for ptr in range(len(array)-1):
            if array[ptr] > array[ptr + 1]:
                swaps = True
                # swap elements ptr and ptr + 1
                swap(ptr, ptr + 1, array)

    return array
    pass

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
    
    # this is a simpler way in Python of performing these statements:
    #            temp = array[ptr]
    #            array[ptr] = array[ptr + 1]
    #            array[ptr + 1] = temp
    # No 'return array' statement seems to be needed for this function

if __name__ == '__main__':

    print(bubbleSort([3,2,1]))
    print(bubbleSort([8,5,2,7]))
    print(bubbleSort([20]))

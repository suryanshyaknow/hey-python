# Given an array of N integers, sort the elements in the ascending order based on the number of times
# they occur in the array. If two elements occur equal number of time, place the numerically smaller 
# value ahead of the other.

from collections import defaultdict


# NOTE: The main difference between "defaultdict" and "dict" is that when you try to access or modify a key
# that's not present in the dictionary, a default value is automatically given to that key .

def sortByFreq(arr):
    # counts = {}
    # for i in arr:
    #     if i in counts:
    #         counts[i] += 1
    #     else:
    #         counts[i] = 1
    counts = defaultdict(lambda: 0)
    for i in arr:
        counts[i] += 1

    # Sorting the array 'arr' where key
    # is the function based on which
    # the array is sorted.
    arr.sort(key=lambda x:(counts[x], x))
    # While sorting we want to give
    # first priority to Frequency
    # then to the value of item.

    return arr


if __name__ == "__main__":
    # Inputs:
    arr_1 = [2, 5, 2, 8, 5, 6, 8, 8]
    arr_2 = [2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8]

    # Outputs:  
    print(sortByFreq(arr=arr_1))
    print(sortByFreq(arr=arr_2))


    


# Given an array, print out all the available Pythaogorean Triplets from it.


def print_pythagorean_triplets(arr) -> None:
    """Prints out all the Pythogorean Triplets from the given array."""
    try:
        len_arr = len(arr)
        triplets = 0
        for i in range(len_arr):
            for j in range(i+1, len_arr):
                for k in range(j+1, len_arr):
                    a = arr[i]**2
                    b = arr[j]**2
                    c = arr[k]**2
                    if a==b+c or b==a+c or c==a+b:
                        print(arr[i], arr[j], arr[k])
                        triplets += 1
        if triplets == 0:
            print("No luck with triplets!")
        ...
    except Exception as e:
        raise e


if __name__ == "__main__":
    arr_1 = [3,1,4,6,5]
    print(f"Printing Pythogorean Triplets for the array {arr_1}..")
    print_pythagorean_triplets([3,1,4,6,5])
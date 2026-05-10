
# INSERTION SORT ALGORITHM
# SORTING IN MONOTONICALLY DECREASING ORDER


# Function to perform insertion sort in descending order
def insertion_sort_desc(arr):

    # Traverse through the array starting from index 1
    for i in range(1, len(arr)):

        # Store the current element to be compared
        key = arr[i]

        # Initialize previous index
        j = i - 1

        # Move elements that are smaller than key
        # one position ahead to make space for key
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the key element into its correct position
        arr[j + 1] = key

    # Return the sorted array
    return arr


# MAIN PROGRAM


# Create an example array of numbers
numbers = [12, 5, 8, 19, 1, 25, 7]

# Display the original unsorted array
print("Original Array:")
print(numbers)

# Call the insertion sort function
sorted_numbers = insertion_sort_desc(numbers)

# Display the sorted array in decreasing order
print("Sorted Array in Decreasing Order:")
print(sorted_numbers)
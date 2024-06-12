def search_element(my_list, target_element):
    # Iterate through the list using an index
    for index, element in enumerate(my_list):
        # Check if the current element matches the target element
        if element == target_element:
            return index
    # If the element is not found, return -1
    return -1

my_list = [1, 3, 5, 7, 9]
target_element = 10
result = search_element(my_list, target_element)

print(f"The element {target_element} is found at index {result}.")

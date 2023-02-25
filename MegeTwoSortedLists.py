#two merge two sorted lists, we must understand what sorted lists are. 
# In Python, a sorted list is a list where the elements are arranged in ascending or descending order. The built-in sorted() function in Python can be used to sort a list in ascending order, and the sort() method can be used to sort a list in-place.

# sorted lists

original_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
sorted_list = sorted(original_list)
print(sorted_list)

#alternatively using the sort method to sort a list in-place
original_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
original_list.sort()
print(original_list)
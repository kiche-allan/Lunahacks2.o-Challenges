#two merge two sorted lists, we must understand what sorted lists are. 
# In Python, a sorted list is a list where the elements are arranged in ascending or descending order. The built-in sorted() function in Python can be used to sort a list in ascending order, and the sort() method can be used to sort a list in-place.

# sorted lists

original_list1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
sorted_list = sorted(original_list1)
print(sorted_list)

#alternatively using the sort method to sort a list in-place
original_list2 = [5, 2, 3, 1, 4, 7, 2, 6, 5, 3, 5, 8, 9, 7, 9]
original_list2.sort()
print(original_list2)

#we can merge two sorted lists i  python by using a simple algorithm that compares these two lists and adds the smaller element to the result list. Then it moves the pointer of the list with the smaller element to the next elementand continues tee process until one of the lists is completely empty. Finally it appends the remaining elements of the non-empty list to the new list

def merge_sorted_lists(original_list1, original_list2):
    merged_list = []
    i, j =0, 0
    while i < len(original_list1) and j < len(original_list2):
        if original_list1[i] < original_list2[j]:
            merged_list.append(original_list1[i])
            i += 1
            
        else:
            merged_list.append(original_list2[j])
            j += 1
            
    merged_list += original_list1[i:] + original_list2[j:]
    return merged_list
print(merge_sorted_lists(original_list1, original_list2))

# After the while loop has completed, we have finished comparing all the elements in the input lists. However, we may have some remaining elements in one of the lists that we haven't yet added to the merged_list. To add these remaining elements, we concatenate the slices originallist1[i:] and originallist2[j:] to the merged_list. These slices contain all the remaining elements in originallist1 and originallist2, respectively.
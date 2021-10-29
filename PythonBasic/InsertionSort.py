"""
Sadia Islam (16CSE007)
Problem 8: Write a program for any one of popular sorting (Selection, Insertion, counting sorting,
merge sort etc excluding bubble sorting).
"""

#Program for Insertion Sort

def insertion_sort(nums):
    # Start on the second element
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        #keep a reference of the index of the previous element
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert #insert items


# Verify it works
random_list_of_nums = [2,4,9, 1, 14, 25, 6,1]
insertion_sort(random_list_of_nums)
print(random_list_of_nums)
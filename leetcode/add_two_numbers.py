""""
Add two numbers
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of ttheir nodes containsa sing digit;
And the two numbers and return the sum as linked list
"""

def add_two_numbers(l1:list[int], l2:list[int]) -> list[int]:
    l1.reverse()
    l2.reverse()
    n1 = int(''.join( map(str, l1) ))
    n2 = int(''.join( map(str, l2) ))
    sum_list =  [int(n) for n in str( n1 + n2 )]
    sum_list.reverse()
    return sum_list


# l1 = [2, 4, 3]
# l2 = [5, 6, 4]
# l1 = [9, 9, 9, 9, 9, 9, 9]
# l2 = [9, 9, 9, 9]

# output = add_two_numbers(l1, l2)
# print(output)

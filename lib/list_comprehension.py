#!/usr/bin/env python3

def return_evens(num_list):
    
    evens = [num for num in num_list if num % 2 == 0]
    return evens

input_list1 = [1, 2, 3, 4, 5, 6]
result1 = return_evens(input_list1)
print("Even numbers in", input_list1, ":", result1)

input_list2 = [1, 3, 5, 7, 9]
result2 = return_evens(input_list2)
print("Even numbers in", input_list2, ":", result2)

input_list3 = []
result3 = return_evens(input_list3)
print("Even numbers in", input_list3, ":", result3)

input_list4 = [2, 4, 6, 8, 10]
result4 = return_evens(input_list4)
print("Even numbers in", input_list4, ":", result4)


def make_exclamation(sentence_list):
    return [sentence + '!' for sentence in sentence_list]

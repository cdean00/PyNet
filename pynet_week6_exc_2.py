"""
2. Write a function that converts a list to a dictionary where the index of the list is used as the key to the new dictionary (the function should return the new dictionary).
"""

def convert_list_dictionary(a_list):
    a_dict = {}
    
    for item in a_list:
        a_dict[item] = ""

    return a_dict

a_list = [1, 2, 3]
a_dict= convert_list_dictionary(a_list)
print a_dict
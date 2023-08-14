# people = ["Sameer", "Sahil", "Siddhart", "Sajal", "KHUSHI"]
# print((n[0]== "S" for n in people))
# ()
# import sys
# list_size = sys.getsizeof([x*10 for x in range(1,1001)])
# generator_size = sys.getsizeof((x*10 for x in range(1,1001)))

# print(f"{list_size} bytes")
# print(f"{generator_size} bytes")

def is_all_strings(lst):
    return all([type(l) == str for l in lst ])
    


print(is_all_strings(['a','b','c']))
def count_instance(string, letter):
    return string.lower().count(letter.lower())

# print(count_instance("hello world", "a"))
# print(count_instance("Julius Robert Oppenheimer was an American theoretical physicist and director of the Manhattan Project's Los Alamos Laboratory during World War II. He is often called the father of the atomic bomb", "c"))


# multiple_instance("string","a","c")
def multiple_letter_instance(string):
    # string.lower()
    return {letter : string.count(letter) for letter in string}

nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,34,76,8,23,34,45,56,67,78,12,23,34,45,56,67,768,23,4,5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,34,45,56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]

def count_seven(*args):
    return args.count(7)

result1 = count_seven(1,4,7)
print(result1)

result2 = count_seven(*nums)
print(result2)



# print(multiple_letter_instance("hellow worldsssssssss"))
# x = multiple_letter_instance("In 1942, Oppenheimer was recruited to work on the Manhattan Project, and in 1943 he was appointed director of the project's Los Alamos Laboratory in New Mexico, tasked with developing the first nuclear weapons. His leadership and scientific expertise were instrumental in the project's success. On July 16, 1945, he was present at the first test of the atomic bomb, Trinity. In August 1945, the weapons were used against Japan in the bombings of Hiroshima and Nagasaki, the only use to date of nuclear weapons in an armed conflict.")

# print(x)


# print(sorted(x))
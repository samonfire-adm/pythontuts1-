def combine_words(str1, **kwargs):
    if "prefix" in kwargs:
        return kwargs["prefix"] + str1
    elif "suffix" in kwargs:
        return str1 + kwargs["suffix"]
    return str1

print(combine_words("work", prefix ="home"))
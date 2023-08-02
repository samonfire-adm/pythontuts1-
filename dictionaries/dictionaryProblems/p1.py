list1 = ["Ind", "Usa", "Uae", "CA"]
list2 = ["india", "united states of america", "united states of arab", "California" ]

x = {list1[i]:list2[i] for i in range(0,len(list1))}
print(x)
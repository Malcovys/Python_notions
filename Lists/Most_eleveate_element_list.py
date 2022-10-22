#List variable itialisation and affectation
list_number = [4,8,5,3,9,8,55,35,10]

#loop variable and plate switch
i = 0

#Variable will stock...
most_elevate_value = 0

#loop who analyse number 
while len(list_number)>i:

    #Cheking if 'most_elevate' in most elevate has 'list_number'
    if most_elevate_value<list_number[i]:
        #if is true, 'list_number[]' value is assigned in 'most_elevate'
        most_elevate_value = list_number[i]
    i = i+1

#Not comment
print(most_elevate_value)


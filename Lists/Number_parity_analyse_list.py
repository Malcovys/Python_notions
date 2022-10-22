#List variable initialised and affected
number_list=[1,2,3,4,5,6,7,8,9,10]

#List who will stock pair numeber in 'number_list'
pair_number_list=[]

#List who will stock odd number in 'number_list'
odd_number_list=[]

#This variable will make fonctional the loop
i=0

#This is the loop !
while len(number_list)>i:

    #Calculate number in the list by %2
    modulo = number_list[i]%2

    #if modulo 2 of one number is 0, this number is pair
    if modulo==0:
        #add pair number of 'number_list' in 'pair_number_list'
        pair_number_list.append(number_list[i])

    #else, you know
    else:
        #add odd number of 'number_list' in 'odd_number_list'
        odd_number_list.append(number_list[i])

    #incremantation of i variable to avoid infinite loop
    i=i+1


#print values
print('Pair numbers in this list are:'+str(pair_number_list))
print('Odd number in this list are:'+str(odd_number_list))

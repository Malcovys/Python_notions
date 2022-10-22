# The list
month = ['January','February','March','April','May','Jun','Julie']

#loop variable comparate
i = 0

#use plate propriety for print list element whith loop
while len(month) > i:

    #def and initialisation of list_print
    #He will take list element one of one in fonction of variable i
    list_print = month[i]

    #'end' use when we whould place caratère over same line
    print(list_print+' ', end='')

    #i incrementation 
    i = i+1
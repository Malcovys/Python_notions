string_list=['hello','what','impermeable','cooker']
word_sixe_character_plus=[]
word_inf_sixe_character=[]
i=0

while len(string_list)>i:
    if len(string_list[i])>=6:
        word_sixe_character_plus.append(string_list[i])
    else:
        word_inf_sixe_character.append(string_list[i])
    i=i+1

print('List of word whith sixe charater plus are:', end='')
print(word_sixe_character_plus)
print('List of word with chataers inferieur thur sixe are:', end='')
print(word_inf_sixe_character)


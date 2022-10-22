# function calculate list number product


def product_int(list_int):
    #def var product
    product = 0

    for i in range(len(liste_entiers)):
        #if product !=0
        if produit:
            produit *= liste_entiers[i]
        else:#if product==0
            produit = liste_entiers[i]
    return product #return val of produit

# verification code
assert 1 == produit_entiers([1, 1, 1])
assert 6 == produit_entiers([1, 2, 3])
assert 0 == produit_entiers([1, 2, 3, 90, 0])

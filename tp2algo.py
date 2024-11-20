#la fonction tamiser(question 1)
def tamiser(T, ipere, ifin):
    
    continuer = True
    ech = False

    while continuer:
        continuer = False
        ifils = 2 * ipere  


        if ifils < ifin and T[ifils + 1] > T[ifils]:
            ifils += 1

        if ifils <= ifin and T[ipere] < T[ifils]:
            T[ipere], T[ifils] = T[ifils], T[ipere]
            ech = True
            continuer = True
            ipere = ifils 
    return ech

def construire_tas(T):

    n = len(T) - 1  
  
    for i in range(n // 2, 0, -1):
        tamiser(T, i, n)
arbre = [10, 22, 5, 18, 20, 25, 40, 30, 35, 12]  
print("Arbre initial :", arbre[1:])
construire_tas(arbre)
print("TAS max :", arbre[1:])



# tri par tas (question 2)
def entasser(tab, i, n):
    """
    Fonction pour réorganiser le tas à partir de l'index i.
    """
    gauche = 2 * i + 1  
    droite = 2 * i + 2  
    plus_grand = i
    
    if gauche < n and tab[gauche] > tab[plus_grand]:
        plus_grand = gauche
    if droite < n and tab[droite] > tab[plus_grand]:
        plus_grand = droite
    if plus_grand != i:
        tab[i], tab[plus_grand] = tab[plus_grand], tab[i]  
        entasser(tab, plus_grand, n)  

def tri_par_tas(tab):
    n = len(tab)
    for i in range(n // 2 - 1, -1, -1):
        entasser(tab, i, n)
    for i in range(n - 1, 0, -1):
        entasser(tab, 0, i)

    return tab
tab = [10, 22, 5, 18, 20, 25, 40, 30, 35, 12] 
print("Tableau avant tri:", tab)
tab_trie = tri_par_tas(tab)
print("Tableau après tri:", tab_trie)

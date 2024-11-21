# tri par tas 
def entasser(tab, i, n):

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

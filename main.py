"""
Realise par : GIANNUZZI Anais
Fichier : main.c
Resume : algorithme de Johnson pour l'ordonnancement minimal
Date de creation : le 18/04/20
Date de derniere modification : le 20/04/20
"""

L1 = [];
L2 = [];

# Saisie des données
list_machine1 = [[4, 8, 6, 6, 5, 7], [1, 2, 3, 4, 5, 6]];
list_machine2 = [[3, 6, 6, 6, 8, 4], [1, 2, 3, 4, 5, 6]];

W = list_machine1[0] + list_machine2[0];

list_final_tache = [1, 2, 3, 4, 5, 6];
list_final_ordre = [];

while W != []:
    minimum = min(W);
    if (minimum in list_machine1[0]) :
        index = list_machine1[0].index(minimum);
        L1.append(list_machine1[1][index]);
        # on supprime la tache
        del list_machine1[0][index];
        del list_machine2[0][index];
        del list_machine1[1][index];
        del list_machine2[1][index];
        W = list_machine1[0] + list_machine2[0];
    else :
        index = list_machine2[0].index(minimum);
        L2.insert(0, list_machine2[1][index]);
        # on supprime la tache
        del list_machine1[0][index];
        del list_machine2[0][index];
        del list_machine1[1][index];
        del list_machine2[1][index];
        W = list_machine1[0] + list_machine2[0];

# concatenation
list_final_ordre = L1 + L2;

# affichage
print ("tâche : ",list_final_tache);
print ("ordre : ",list_final_ordre);
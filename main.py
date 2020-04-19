"""
Realise par : GIANNUZZI Anais
Fichier : main.c
Resume : algorithme simple de Johnson, ne gère pas les doublons
Date de creation : le 18/04/20
Date de derniere modification : le 19/04/20

Inspiré de : http://www.unit.eu/cours/EnsROtice/module_avance_thg_voo6/co/johnson.html?fbclid=IwAR1WtxnCjKfx0pvMbqT1PVPlEFpbWpQ_-MHZwBo89Ym9NoNivtP67RzV3TI
"""

L1 = [];
L2 = [];

# Saisie des données
list_machine1 = [21, 19, 18, 20];
list_machine2 = [60, 30, 3, 10];

list_machine1_copy = list(list_machine1);
list_machine2_copy = list(list_machine2);

W = list_machine1 + list_machine2;

list_final_tache = [1, 2, 3];
list_final_ordre = [];

while len(list_machine1) != 0:
    minimum = min(W);
    if (minimum in list_machine1) :
        index = list_machine1.index(minimum);
        index_copy = list_machine1_copy.index(minimum);
        L1.append(index_copy+1);
        # on supprime la tache
        del list_machine1[index];
        del list_machine2[index];
        W = list_machine1 + list_machine2;
    else :
        index = list_machine2.index(minimum);
        index_copy = list_machine2_copy.index(minimum);
        L2.insert(0, list_machine2_copy.index(minimum)+1);
        # on supprime la tache
        del list_machine1[index];
        del list_machine2[index];
        W = list_machine1 + list_machine2;

# concatenation
print(L2);
print(L1);
list_final_ordre = L1 + L2;

# affichage
print ("tâche : ",list_final_tache);
print ("ordre : ",list_final_ordre);



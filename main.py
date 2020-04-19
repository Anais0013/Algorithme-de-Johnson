#########################################################
#Realise par : GIANNUZZI Anais
#Fichier : main.c
#Resume : application de l'algorithme de Johnson
#Date de creation : le 18/04/20
#Date de derniere modification : le 18/04/20
#########################################################

list_debut =[][];
list_fin =[][];

list_machine1 =[487, 870, 20][1, 2, 3];
list_machine2 =[456, 700, 200][1, 2, 3];

list_de_travail =[][];

list_final =[][];

list_de_travail = list_machine1 + list_machine2;

print (list_de_travail);

while len(list_de_travail) != 0:
    a = min (list_de_travail);
    if (a in list_machine1):
        list_de_travail.remove (a);
        list_debut.append (a);
    else:
        list_de_travail.remove (a);
        list_fin.append (a);
    print (list_de_travail);
    
#inverse la liste debut
list_fin.reverse();

#concatenation
list_final = list_debut + list_fin;
print (list_final);
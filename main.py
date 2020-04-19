#########################################################
#Realise par : GIANNUZZI Anais
#Fichier : main.c
#Resume : application de l'algorithme de Johnson
#Date de creation : le 18/04/20
#Date de derniere modification : le 19/04/20
#########################################################
        
L1 =[];
L2 =[];

W =[[80, 40, 60, 50, 60, 50, 80], [60, 30, 60, 80, 60, 50, 50]];

list_final_tache =[1, 2, 3, 4, 5, 6, 7];
list_final_ordre =[];

while len(W) != 0:
    minimum = min(W);
    if (minimum in [80, 40, 60, 50, 60, 50, 80]):
        L1.append(minimum);
        print(L1);
        del W[[W.index(minimum)][W.index(minimum)]];
    else:
        L2.insert(0, W.index(minimum)+1);
        print(L2);
        del W[[W.index(minimum)][W.index(minimum)]];

# concatenation
list_final_ordre = L1 + L2;

# affichage
print ("tâche : ",list_final_tache);
print ("ordre : ",list_final_ordre);



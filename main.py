#########################################################
#Realise par : GIANNUZZI Anais
#Fichier : main.c
#Resume : application de l'algorithme de Johnson
#Date de creation : le 18/04/20
#Date de derniere modification : le 19/04/20
#########################################################
        
L1 =[];
L2 =[];

list_machine1 =[80, 40, 60, 50, 60, 50, 80];
list_machine2 = [60, 30, 60, 80, 60, 50, 50];

list_final_tache =[1, 2, 3, 4, 5, 6, 7];
list_final_ordre =[];

i = 0;
while i <= len(list_machine1):
    minimum_machine1 = min(list_machine1);
    minimum_machine2 = min(list_machine2);
    if (minimum_machine1 > minimum_machine2):
        L1.append(list_machine1.index(minimum_machine1)+1);
        print(L1);
    else:
        L2.append(list_machine2.index(minimum_machine2)+1);
        print(L2);
    del list_machine1[list_machine1.index(minimum_machine1)];
    del list_machine2[list_machine2.index(minimum_machine2)];
    i = i+1;
    
# inverse la liste debut
L1.reverse();

# concatenation
list_final_ordre = L1 + L2;

# affichage
print ("tâche : ",list_final_tache);
print ("ordre : ",list_final_ordre);



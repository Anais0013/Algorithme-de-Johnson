#########################################################
#Realise par : GIANNUZZI Anais
#Fichier : main.c
#Resume : application de l'algorithme de Johnson
#Date de creation : le 18/04/20
#Date de derniere modification : le 19/04/20
#########################################################

list_debut =[];
list_fin =[];

list_machine1 =[50, 150, 80, 200, 30];
list_machine2 = [60, 50, 150, 70, 200];
list_machine1_copy =list(list_machine1);
list_machine2_copy =list(list_machine2);

list_de_travail =[];

list_final_tache =[1,2,3];
list_final_ordre =[];

list_de_travail = list_machine1 + list_machine2;

print (list_de_travail);

while list_de_travail != []:
    a = min (list_de_travail);
    if (a in list_machine1):
        print("debg 1");
        print(a);
        b = list_machine1.index(a);
        print(b);
        c = list_machine1_copy.index(a);
        print(c);
        list_debut.append (c+1);
        print(list_debut);
        list_de_travail.remove (a);
        del list_machine2[b];
        del list_machine1[b];
        print(list_machine1);
        print(list_machine2);
        list_de_travail = list_machine1 + list_machine2;
        print(list_de_travail);
    else:
        print("debg 2");
        print(a);
        b = list_machine2.index(a);
        c = list_machine2_copy.index(a);
        print(b);
        list_fin.append (c+1);
        print(list_fin);
        list_de_travail.remove (a);
        del list_machine1[b];
        del list_machine2[b];
        print(list_machine1);
        print(list_machine2);
        list_de_travail = list_machine1 + list_machine2;
        print(list_de_travail);
    
#inverse la liste debut
list_fin.reverse();

#concatenation
print(list_debut);
print("ok");
print(list_fin);
list_final_ordre = list_debut + list_fin;
print ("tâche : ",list_final_tache);
print ("ordre : ",list_final_ordre);
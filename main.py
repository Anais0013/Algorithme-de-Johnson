#########################################################
#Realise par : GIANNUZZI Anais
#Fichier : main.c
#Resume : application de l'algorithme de Johnson
#Date de creation : le 18/04/20
#Date de derniere modification : le 19/04/20
#########################################################

def getIndexPositions(listOfElements, element):
    ''' Returns the indexes of all occurrences of give element in
    the list- listOfElements '''
    indexPosList = []
    for i in range(len(listOfElements)): 
        if listOfElements[i] == element:
            indexPosList.append(i)
    return indexPosList
        
list_debut =[];
list_fin =[];

list_machine1 =[80, 40, 60, 50, 60, 50, 80];
list_machine2 = [60, 30, 60, 80, 60, 50, 50];
list_machine1_copy =list(list_machine1);
list_machine2_copy =list(list_machine2);
list_memory1 = [];
list_memory2 = [];

list_de_travail =[];

list_final_tache =[1,2,3];
list_final_ordre =[];

list_de_travail = list_machine1 + list_machine2;

print (list_de_travail);

while list_de_travail != []:
    minimum = min (list_de_travail);
    if (minimum in list_machine1):
        print("debug 1");
        print("min");
        print(minimum);
        index_minimum_list_machine1 = list_machine1.index(minimum);
        print(index_minimum_list_machine1);
        # gere le probleme de doublon
        print("verif",minimum in list_memory);
        print(list_memory);
        print(minimum);
        if (minimum in list_memory):
            print("ok1");
            # compte occurence dans memoire
            combien_de_fois_min = list_memory.count(minimum);
            print(combien_de_fois_min);
            # compte occurence dans list_machine1
            combien_de_fois_min_list_machine1_copy = list_machine1.count(minimum);
            # liste les index du minimum
            list_occurence_du_min = getIndexPositions(list_machine1_copy, minimum);
            print(list_occurence_du_min);
            # on prend le combien de fois min+1 
            index_courant = list_occurence_du_min[combien_de_fois_min];
            #
            c = list_machine1_copy[index_courant];
            list_debut.append (c);
            print(list_debut);
            del list_machine2[index_minimum_list_machine1];
            del list_machine1[index_minimum_list_machine1];
            print(list_machine1);
            print(list_machine2);
            list_de_travail = list_machine1 + list_machine2;
            print(list_de_travail);
        else :
            c = list_machine1_copy.index(minimum);
            print(c);
            list_debut.append (c+1);
            print(list_debut);
            del list_machine2[index_minimum_list_machine1];
            del list_machine1[index_minimum_list_machine1];
            print(list_machine1);
            print(list_machine2);
            list_de_travail = list_machine1 + list_machine2;
            print(list_de_travail);
    else:
        print("debug 2");
        print("min");
        print(minimum);
        index_minimum_list_machine2 = list_machine2.index(minimum);
        print("index min");
        print(index_minimum_list_machine2);
        # gere le probleme de doublon
        if (minimum in list_memory):
            print("ok2");
            # compte occurence dans memoire
            combien_de_fois_min = list_memory.count(minimum);
            print(combien_de_fois_min);
            # compte occurence dans list_machine1
            combien_de_fois_min_list_machine2_copy = list_machine2.count(minimum);
            # liste les index du minimum
            list_occurence_du_min = getIndexPositions(list_machine2_copy, minimum);
            print(list_occurence_du_min);
            # on prend le combien de fois min+1 
            index_courant = list_occurence_du_min[combien_de_fois_min];
            c = list_machine2_copy[index_courant];
            list_fin.append (c);
            print(list_fin);
            del list_machine1[index_minimum_list_machine1];
            del list_machine2[index_minimum_list_machine1];
            print(list_machine1);
            print(list_machine2);
            list_de_travail = list_machine1 + list_machine2;
            print(list_de_travail);
        else :
            recup_index_reel = list_machine2_copy.index(minimum);
            print(index_minimum_list_machine2);
            # si l'indice minimum est 0 récupère la première valeur
            list_fin.append (recup_index_reel+1);
            print(list_fin);
            # efface les tache traite
            del list_machine1[index_minimum_list_machine2];
            del list_machine2[index_minimum_list_machine2];
            # nouvelle liste de travail
            list_de_travail = list_machine1 + list_machine2;
            print(list_de_travail);
    # stock en memoire l'element traite
    list_memory1.append(minimum);
    list_memory2.append(minimum);
    
# inverse la liste debut
list_fin.reverse();

# concatenation
list_final_ordre = list_debut + list_fin;

# affichage
print ("tâche : ",list_final_tache);
print ("ordre : ",list_final_ordre);



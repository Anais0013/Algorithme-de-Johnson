#########################################################
#Realise par : GIANNUZZI Anais
#Fichier : main.c
#Resume : application de l'algorithme de Johnson
#Date de creation : le 18/04/20
#Date de derniere modification : le 19/04/20
#########################################################

def get_indexes(my_list, s):
    # liste les index d'une occurence
    start = 0
    while True:
        try:
            index = my_list.index(s, start)
            start = index+1
            yield index
        except ValueError:
            break
        
list_debut =[];
list_fin =[];

list_machine1 =[80, 40, 60, 50, 60, 50, 80];
list_machine2 = [60, 30, 60, 80, 60, 50, 50];
list_machine1_copy =list(list_machine1);
list_machine2_copy =list(list_machine2);
list_memory = [];

list_de_travail =[];

list_final_tache =[1,2,3];
list_final_ordre =[];

list_de_travail = list_machine1 + list_machine2;

print (list_de_travail);

while list_de_travail != []:
    minimum = min (list_de_travail);
    # garde en memoire les elements traites
    list_memory.append(minimum);
    if (minimum in list_machine1):
        print("debug 1");
        print("min");
        print(minimum);
        index_minimum_list_machine1 = list_machine1.index(minimum);
        print(index_minimum_list_machine1);
        # gere le probleme de doublon
        if (minimum in list_memory == True):
            print("ok1");
            # compte occurence
            combien_de_fois_min = list_memory.count(minimum);
            # liste les index du minimum
            list_occurence_du_min = get_indexes(list_machine1, minimum);
            # on prend le n ième index
            list_occurence_du_min.index(combien_de_fois_min);
            #
            c = list_occurence_du_min.index(combien_de_fois_min);
            print(c);
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
        if (minimum in list_memory == True):
            print("ok2");
            # compte occurence
            combien_de_fois_min = list_memory.count(minimum);
            # liste les index du minimum
            list_occurence_du_min = get_indexes(list_machine2, minimum);
            # on prend le n ième index
            list_occurence_du_min.index(combien_de_fois_min);
            #
            c = list_occurence_du_min.index(combien_de_fois_min);
            print(c);
        else :
            c = list_machine2_copy.index(minimum);
            print(index_minimum_list_machine2);
            list_fin.append (c+1);
            print(list_fin);
            del list_machine1[index_minimum_list_machine2];
            del list_machine2[index_minimum_list_machine2];
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
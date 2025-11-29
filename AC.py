import time
import sys
import os

# Changer le répertoire courant vers celui où se trouve le script. 
# Cela évite les erreurs "file not found" lorsque vous lisez ou écrivez des fichiers.
os.chdir(os.path.dirname(__file__))

#############################################################################################################################
# QUESTION 1 – Lecture du fichier
# Écrire une fonction Python permettant de lire les valeurs entières du fichier valeurs_aleatoires.txt
# La lecture doit se faire à l’aide d’une liste, en convertissant chaque ligne en entier.
#############################################################################################################################

def read_file(file_name):
    # Ouvre le fichier en mode lecture 'r'
    file = open(file_name, 'r')
    values = []   # Liste qui va contenir les entiers du fichier
    for line in file:
        # Convertir chaque ligne en entier et l'ajouter à la liste
        values.append(int(line.strip()))
    file.close()  # Fermer le fichier après lecture
    return values    

#############################################################################################################################
# QUESTION 2 – Comptage des occurrences (Complexité O(n²))
def nombre_occurrences(values_list):
    n = len(values_list)  # CORRECTION: Définir n ici
    iterations = 0
    start_time = time.time()
    occurrences = dict()
    remaining_time = 0

    for i in range(n):
        iterations += 1
        count = 0
        for j in range(n):
            iterations += 1
            if values_list[j] == values_list[i]:
                count += 1
        occurrences[values_list[i]] = count  # CORRECTION: Déplacé en dehors de la boucle interne
        
        elapsed_percentage = (i + 1) * 100 / n
        remaining_percentage = 100 - elapsed_percentage 
        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_percentage > 0:
            remaining_time = remaining_percentage * elapsed_time / elapsed_percentage 
        
        sys.stdout.write(f"\rProgress: {elapsed_percentage:.2f}%, Elapsed Time: {elapsed_time:.2f}s, RemainingTime: {remaining_time:.2f}s")
        sys.stdout.flush()  

    end_time = time.time()
    print(f"\nDuree totale du comptage : {end_time - start_time:.5f} secondes")
    print(f"Nombre total d'iterations : {iterations}")
    return occurrences
#
# QUESTION 3 – Analyse algorithmique
# - Indiquer le nombre exact d’itérations
# - Déterminer la complexité temporelle en notation O.
# - Intégrer un chronomètre pour mesurer la durée d’exécution
#############################################################################################################################

def nombre_occurrences(values_list):
    iterations = 0
    start_time = time.time()
    occurrences = dict()
    remaining_time = 0

    for i in range(n):
        iterations += 1
        count = 0
        for j in range(n):
            iterations += 1
            if values_list[j] == values_list[i]:
                count += 1
            occurrences[values_list[i]] = count
        
        #               100% --> n
        # elapsed_percentage --> i+1 => elapsed_percentage  = (i + 1) * 100 / n  
        elapsed_percentage   = (i + 1) * 100 / n
        remaining_percentage = 100 - elapsed_percentage 

        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_percentage  > 0:
            #    elapsed_time --> elapsed_percentage 
            #  remaining_time --> remaining_percentage => remaining_time = remaining_percentage * elapsed_time / elapsed_percentage 
            remaining_time = remaining_percentage * elapsed_time / elapsed_percentage 
        
        # Affiche la progression sur une seule ligne en écrasant l'affichage précédent.
        # \r ramène le curseur au début de la ligne, sys.stdout.write écrit le texte sans retour à la ligne,
        # et le formatage affiche le pourcentage, le temps écoulé et le temps restant estimé.
        sys.stdout.write(f"\rProgress: {elapsed_percentage :.2f}%, Elapsed Time: {elapsed_time:.2f}s, RemainingTime: {remaining_time:.2f}s")

        # Force l'affichage immédiat du texte (sinon Python peut attendre avant d'afficher).
        sys.stdout.flush()  

    end_time = time.time()
    print(f"\n⏱ Durée totale du comptage : {end_time - start_time:.5f} secondes")
    print(f"Nombre total d’itérations : {iterations}")
    return occurrences
# fin nombre_occurrences

#############################################################################################################################
# QUESTION 4 – Amélioration du calcul des occurrences (Complexité O(n))
# Écrire une fonction nombre_occurrences_ameliore(values_list)
# Objectif : réduire la complexité de O(n²) → O(n)
#############################################################################################################################

# def nombre_occurrences_ameliore(values_list):
def nombre_occurrences_ameliore(values_list):
    iterations = 0
    start_time = time.time()
    occurrences = dict()
    
    print(f"\nDebut du comptage optimise sur {len(values_list)} elements...")

    for i, value in enumerate(values_list):
        iterations += 1
        if value in occurrences:
            occurrences[value] += 1
        else:
            occurrences[value] = 1

    end_time = time.time()
    
    print(f"\nCOMPTAGE OPTIMISE - ANALYSE O(n)")
    print(f"• Itérations : {iterations}")
    print(f"• Temps : {end_time - start_time:.6f}s")
    print(f"• Complexité : O(n) confirmée")
    
    return occurrences


#############################################################################################################################
# QUESTION 5 – Tri par sélection (Selection Sort)
# Écrire une fonction selection_sort() qui :
# - trie les éléments en ordre croissant
# - indique le nombre exact d’itérations
# - affiche la complexité 
# - intègre un chronomètre
#############################################################################################################################

def selection_sort(values_list):
    n = len(values_list)
    iterations = 0

    # Chronomètre
    start_time = time.time()

    # Copie pour éviter de modifier la liste d'origine
    tab = values_list.copy()

    # Tri par sélection
    for i in range(n - 1):
        iterations += 1
        min_index = i
        
        for j in range(i + 1, n):
            iterations += 1
            if tab[j] < tab[min_index]:
                min_index = j
        
        # Échange
        tab[i], tab[min_index] = tab[min_index], tab[i]

    # Fin du chrono
    end_time = time.time()

    # Affichage des informations
    print("\n--- Selection Sort ---")
    print(f" Temps d'exécution : {end_time - start_time:.5f} secondes")
    print(f" Nombre total d’itérations : {iterations}")
    print(" Complexité : O(n²)")

    return tab



#############################################################################################################################
# QUESTION 6 – Tri par fusion (Merge Sort)
# Écrire une fonction merge_sort(tab) qui :
# - trie les éléments en ordre croissant
# - compte le nombre d’itérations
# - affiche la complexité : O(n log n)
# - intègre un chronomètre
#############################################################################################################################

merge_iterations = 0  # variable globale pour compter les itérations

def merge_sort(values_list):
    global merge_iterations
    merge_iterations = 0
    start_time = time.time()

    # Fonction interne pour fusionner deux listes triées
    def merge(left, right):
        global merge_iterations
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            merge_iterations += 1
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        # Ajouter les éléments restants
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    # Fonction récursive de tri par fusion
    def merge_sort_rec(lst):
        if len(lst) <= 1:
            return lst
        mid = len(lst) // 2
        left = merge_sort_rec(lst[:mid])
        right = merge_sort_rec(lst[mid:])
        return merge(left, right)

    sorted_tab = merge_sort_rec(values_list)

    end_time = time.time()
    print("\n--- Merge Sort ---")
    print(f" Temps d'exécution : {end_time - start_time:.5f} secondes")
    print(f" Nombre total d’itérations : {merge_iterations}")
    print(" Complexité : O(n log n)")

    return sorted_tab



#############################################################################################################################
# QUESTION 7 – Sauvegarde du tableau trié
# Écrire une fonction write_to_file(tab) qui enregistre les valeurs triées dans 
# un fichier nommé valeurs_aleatoires_tries.txt
#############################################################################################################################

# def write_to_file():
def write_to_file(tab, filename='valeurs_aleatoires_tries.txt'):
    try:
        start_time = time.time()
        
        print(f"\nSauvegarde dans le fichier '{filename}'...")
        
        with open(filename, 'w') as file:
            for value in tab:
                file.write(f"{value}\n")
        
        end_time = time.time()
        
        print("Sauvegarde reussie!")
        print(f"Fichier '{filename}' cree avec {len(tab)} valeurs.")
        print(f"Temps de sauvegarde : {end_time - start_time:.4f} secondes")
        
        return True
        
    except Exception as e:
        print(f"ERREUR lors de la sauvegarde: {e}")
        return False

#############################################################################################################################
# Début du script principal
#############################################################################################################################

# 1. Lecture du fichier
valeurs_aleatoires_list = read_file('valeurs_aleatoires.txt')
list_length = len(valeurs_aleatoires_list)
n = len(valeurs_aleatoires_list) # n est utilisé dans nombre_occurrences

print('Valeurs lues :', valeurs_aleatoires_list[:10], '...')
print('Longueur de la liste (n) :', n)

# 2. & 3. Comptage des occurrences (O(n²))
#occurrences_on2 = nombre_occurrences(valeurs_aleatoires_list)
#print("Occurrences (O(n²)) :", occurrences_on2)

# 4. Comptage des occurrences amélioré (O(n))
occurrences_on = nombre_occurrences_ameliore(valeurs_aleatoires_list)
print("Occurrences (O(n)) :", occurrences_on)

# 5. Tri par sélection (Selection Sort)
ma_liste = [20, 50, 10, 40, 70, 30]
sorted_selection = selection_sort(ma_liste)
print(sorted_selection)

# 6. Tri par fusion (Merge Sort)
ma_liste = [20, 50, 10, 40, 70, 30]
sorted_merge = merge_sort(ma_liste)
print(sorted_merge)

# 7. Sauvegarde du tableau trié
write_to_file(sorted_merge)







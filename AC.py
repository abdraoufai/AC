import time
import sys
import os

# Changer le répertoire courant vers celui où se trouve le script. 
os.chdir(os.path.dirname(__file__))

#############################################################################################################################
# QUESTION 1 – Lecture du fichier
#############################################################################################################################

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            values = []
            for line in file:
                values.append(int(line.strip()))
        return values
    except FileNotFoundError:
        print(f"ERREUR: Le fichier '{file_name}' est introuvable.")
        print("Creation d'un fichier d'exemple...")
        create_sample_file()
        return read_file(file_name)

def create_sample_file():
    """Crée un fichier d'exemple avec des valeurs aléatoires"""
    import random
    with open('valeurs_aleatoires.txt', 'w') as f:
        for _ in range(100):
            f.write(f"{random.randint(1, 50)}\n")
    print("Fichier 'valeurs_aleatoires.txt' cree avec 100 valeurs aleatoires.")

#############################################################################################################################
# QUESTION 2 & 3 – Comptage des occurrences (Complexité O(n²))
#############################################################################################################################

def nombre_occurrences(values_list):
    n = len(values_list)
    iterations = 0
    start_time = time.time()
    occurrences = dict()

    for i in range(n):
        iterations += 1
        count = 0
        for j in range(n):
            iterations += 1
            if values_list[j] == values_list[i]:
                count += 1
        occurrences[values_list[i]] = count  # Correction: en dehors de la boucle interne
        
        # Barre de progression
        elapsed_percentage = (i + 1) * 100 / n
        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_percentage > 0:
            remaining_time = (100 - elapsed_percentage) * elapsed_time / elapsed_percentage
        else:
            remaining_time = 0
        
        sys.stdout.write(f"\rProgress: {elapsed_percentage:.2f}%, Elapsed: {elapsed_time:.2f}s, Remaining: {remaining_time:.2f}s")
        sys.stdout.flush()

    end_time = time.time()
    print(f"\nDuree totale : {end_time - start_time:.5f} secondes")
    print(f"Nombre d'iterations : {iterations}")
    print(f"Complexite : O(n²)")
    return occurrences

#############################################################################################################################
# QUESTION 4 – Amélioration du calcul des occurrences (Complexité O(n))
#############################################################################################################################

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
        
        # Barre de progression
        if len(values_list) > 100 and (i + 1) % (len(values_list) // 20) == 0:
            elapsed_percentage = (i + 1) * 100 / len(values_list)
            current_time = time.time()
            elapsed_time = current_time - start_time
            
            if elapsed_percentage > 0:
                remaining_time = (100 - elapsed_percentage) * elapsed_time / elapsed_percentage
            else:
                remaining_time = 0
            
            sys.stdout.write(f"\rProgression: {elapsed_percentage:.1f}% | Temps: {elapsed_time:.2f}s | Restant: {remaining_time:.2f}s")
            sys.stdout.flush()

    end_time = time.time()
    execution_time = end_time - start_time
    
    print(f"\rComptage optimise termine! {' '*50}")
    
    print("\n" + "="*60)
    print("COMPTAGE OCCURRENCES OPTIMISE - RESULTATS")
    print("="*60)
    print(f"Nombre d'elements analyses : {len(values_list)}")
    print(f"Valeurs uniques trouvees  : {len(occurrences)}")
    print(f"Temps d'execution         : {execution_time:.6f} secondes")
    print(f"Nombre total d'iterations : {iterations}")
    print(f"Complexite algorithmique  : O(n)")
    
    # Statistiques sur les occurrences
    if occurrences:
        max_value = max(occurrences, key=occurrences.get)
        min_value = min(occurrences, key=occurrences.get)
        avg_occurrences = sum(occurrences.values()) / len(occurrences)
        
        print(f"\nSTATISTIQUES DES OCCURRENCES:")
        print(f"  * Valeur la plus frequente : {max_value} (apparait {occurrences[max_value]} fois)")
        print(f"  * Valeur la moins frequente: {min_value} (apparait {occurrences[min_value]} fois)")
        print(f"  * Occurrences moyennes     : {avg_occurrences:.2f}")
    
    # Aperçu des résultats
    print(f"\nApercu des occurrences (5 premieres):")
    preview_items = list(occurrences.items())[:5]
    for value, count in preview_items:
        print(f"  {value}: {count} occurrence(s)")
    
    return occurrences

#############################################################################################################################
# QUESTION 5 – Tri par sélection (Selection Sort)
#############################################################################################################################

def selection_sort(values_list):
    n = len(values_list)
    iterations = 0
    start_time = time.time()

    tab = values_list.copy()

    for i in range(n - 1):
        iterations += 1
        min_index = i
        
        for j in range(i + 1, n):
            iterations += 1
            if tab[j] < tab[min_index]:
                min_index = j
        
        tab[i], tab[min_index] = tab[min_index], tab[i]

    end_time = time.time()

    print("\n--- Selection Sort ---")
    print(f" Temps d'execution : {end_time - start_time:.5f} secondes")
    print(f" Nombre total d'iterations : {iterations}")
    print(" Complexite : O(n²)")

    return tab

#############################################################################################################################
# QUESTION 6 – Tri par fusion (Merge Sort)
#############################################################################################################################

def merge_sort(values_list):
    iterations = [0]  # Utiliser une liste pour compter les iterations
    
    def merge(left, right):
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            iterations[0] += 1
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        while i < len(left):
            iterations[0] += 1
            result.append(left[i])
            i += 1
            
        while j < len(right):
            iterations[0] += 1
            result.append(right[j])
            j += 1
            
        return result

    def merge_sort_rec(lst):
        if len(lst) <= 1:
            return lst
            
        mid = len(lst) // 2
        left = merge_sort_rec(lst[:mid])
        right = merge_sort_rec(lst[mid:])
        
        return merge(left, right)

    start_time = time.time()
    sorted_list = merge_sort_rec(values_list)
    end_time = time.time()
    
    print("\n--- Merge Sort ---")
    print(f" Temps d'execution : {end_time - start_time:.5f} secondes")
    print(f" Nombre total d'iterations : {iterations[0]}")
    print(" Complexite : O(n log n)")

    return sorted_list

#############################################################################################################################
# QUESTION 7 – Sauvegarde du tableau trié
#############################################################################################################################

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
        
        return True
        
    except Exception as e:
        print(f"ERREUR lors de la sauvegarde: {e}")
        return False

#############################################################################################################################
# Début du script principal
#############################################################################################################################

# 1. Lecture du fichier
print("=" * 60)
print("QUESTION 1 - LECTURE DU FICHIER")
print("=" * 60)
valeurs_aleatoires_list = read_file('valeurs_aleatoires.txt')
n = len(valeurs_aleatoires_list)

print('Valeurs lues :', valeurs_aleatoires_list[:10], '...')
print('Longueur de la liste (n) :', n)

# 2. & 3. Comptage des occurrences (O(n²))
print("\n" + "=" * 60)
print("QUESTIONS 2 & 3 - COMPTAGE OCCURRENCES (O(n²))")
print("=" * 60)
# Utiliser un échantillon réduit
sample_size = min(100, n)
occurrences_on2 = nombre_occurrences(valeurs_aleatoires_list[:sample_size])
print("Occurrences (O(n²)) :", dict(list(occurrences_on2.items())[:5]))

# 4. Comptage des occurrences amélioré (O(n))
print("\n" + "=" * 60)
print("QUESTION 4 - COMPTAGE OCCURRENCES AMELIORE (O(n))")
print("=" * 60)
occurrences_on = nombre_occurrences_ameliore(valeurs_aleatoires_list[:1000])  # Limiter à 1000 éléments
print("Occurrences (O(n)) :", dict(list(occurrences_on.items())[:5]))

# 5. Tri par sélection (Selection Sort)
print("\n" + "=" * 60)
print("QUESTION 5 - TRI PAR SELECTION")
print("=" * 60)
ma_liste = [20, 50, 10, 40, 70, 30]
sorted_selection = selection_sort(ma_liste)
print("Liste triee :", sorted_selection)

# 6. Tri par fusion (Merge Sort)
print("\n" + "=" * 60)
print("QUESTION 6 - TRI PAR FUSION")
print("=" * 60)
ma_liste = [20, 50, 10, 40, 70, 30]
sorted_merge = merge_sort(ma_liste)
print("Liste triee :", sorted_merge)

# 7. Sauvegarde du tableau trié
print("\n" + "=" * 60)
print("QUESTION 7 - SAUVEGARDE DU TABLEAU TRIE")
print("=" * 60)
write_to_file(sorted_merge)

print("\n" + "=" * 70)
print("PROGRAMME TERMINE AVEC SUCCES!")
print("=" * 70)

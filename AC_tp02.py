import itertools
import time
import math

# =========================
# Cities
# =========================
cities = [
    "Alger", "Batna", "Oran", "Setif", "Constantine",
    "Tlemcen", "Ouargla", "Annaba", "Bechar", "Tizi-Ouzou"
]

# =========================
# Distance Matrix (Km)
# =========================
D = [
    [0, 430, 415, 260, 320, 520, 770, 600, 970, 110],
    [430, 0, 798, 100, 120, 620, 420, 300, 950, 350],
    [415, 798, 0, 430, 500, 180, 850, 780, 720, 380],
    [260, 100, 430, 0, 115, 500, 620, 310, 800, 250],
    [320, 120, 500, 115, 0, 550, 610, 160, 950, 340],
    [520, 620, 180, 500, 550, 0, 1000, 720, 450, 540],
    [770, 420, 850, 620, 610, 1000, 0, 720, 770, 640],
    [600, 300, 780, 310, 160, 720, 720, 0, 1150, 360],
    [970, 950, 720, 800, 950, 450, 770, 1150, 0, 1160],
    [110, 350, 380, 250, 340, 540, 640, 360, 1160, 0]
]

# =========================
# Distance of a route
# =========================
def calculate_distance(route, distances):
    total = 0
    for i in range(len(route) - 1):
        total += distances[route[i]][route[i + 1]]
    return total

# =========================
# Brute Force TSP
# =========================
def brute_force_tsp(distances):
    n = len(distances)
    best_distance = math.inf
    best_route = None

    start_time = time.time()
    permutations = list(itertools.permutations(range(1, n)))
    total_permutations = len(permutations)

    for perm in permutations:
        route = [0] + list(perm) + [0]
        dist = calculate_distance(route, distances)

        if dist < best_distance:
            best_distance = dist
            best_route = route

    end_time = time.time()

    return best_route, best_distance, total_permutations, end_time - start_time

# =========================
# Nearest Neighbor TSP
# =========================
def nearest_neighbor_tsp(distances, start=0):
    n = len(distances)
    visited = [start]
    current = start
    total_distance = 0

    while len(visited) < n:
        nearest_city = None
        min_distance = math.inf

        for city in range(n):
            if city not in visited and distances[current][city] < min_distance:
                min_distance = distances[current][city]
                nearest_city = city

        visited.append(nearest_city)
        total_distance += min_distance
        current = nearest_city

    total_distance += distances[current][start]
    visited.append(start)

    return visited, total_distance

# =========================
# MAIN
# =========================
if __name__ == "__main__":

    print("===== BRUTE FORCE TSP =====")
    bf_route, bf_distance, bf_count, bf_time = brute_force_tsp(D)
    print("Route:")
    print(" -> ".join(cities[i] for i in bf_route))
    print("Total distance:", bf_distance, "km")
    print("Permutations:", bf_count)
    print("Execution time:", round(bf_time, 3), "seconds")

    print("\n===== NEAREST NEIGHBOR TSP =====")
    nn_route, nn_distance = nearest_neighbor_tsp(D)
    print("Route:")
    print(" -> ".join(cities[i] for i in nn_route))
    print("Total distance:", nn_distance, "km")

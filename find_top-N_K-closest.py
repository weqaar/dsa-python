import heapq
import math


def k_closest_points(points, k):
    # Calculate the distance of each point from the origin
    distances = [(math.sqrt(x**2 + y**2 + z**2), (x, y, z)) for x, y, z in points]

    # Use a heap to get the k smallest distances
    closest_points = heapq.nsmallest(k, distances, key=lambda x: x[0])

    # Extract the points from the heap
    return [point for _, point in closest_points]


# Example usage:
points = [(-1, -1, -1), (1, 0, 0), (0, -1, 0), (0, 2, 1)]
k = 2
print(k_closest_points(points, k))  # Output: [(1, 0, 0), (0, -1, 0)]

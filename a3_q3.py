def find_frequency(vector, X):
    if not vector:
        return 0  

    frequency = vector.count(X)
    return frequency


vector = [2, 4, 6, 2, 8, 2, 9, 2]
X = 2
frequency_of_X = find_frequency(vector, X)

print(f"The frequency of {X} in the vector is: {frequency_of_X}")

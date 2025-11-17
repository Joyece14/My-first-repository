vector1 = list(map(int, input("Enter elements of vector 1 separated by space: ").split()))
vector2 = list(map(int, input("Enter elements of vector 2 separated by space: ").split()))

<<<<<<< HEAD
=======
def multiply(pair):
    a, b = pair
    return a * b

vector1 = list(map(int, input("elements of vector 1 separated by space: ").split()))
vector2 = list(map(int, input("elements of vector 2 separated by space: ").split()))
>>>>>>> parallel

if len(vector1) != len(vector2):
    print("Vectors must have the same length")
else:

    dot_product = sum(a * b for a, b in zip(vector1, vector2))
    print("Dot Product:", dot_product)
print("Bug Removed.");



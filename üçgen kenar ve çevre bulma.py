from itertools import combinations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_triangles_and_perimeters(start, end):
    # Verilen aralıktaki asal sayıları bul
    primes = [num for num in range(start, end + 1) if is_prime(num)]

    # Üçlü kombinasyonları kontrol et
    triangles = []
    for a, b, c in combinations(primes, 3):
        if a + b > c and a + c > b and b + c > a:  # Üçgen eşitsizliği
            perimeter = a + b + c
            triangles.append((a, b, c, perimeter))

    return triangles

def print_triangles(triangles):
    for triangle in triangles:
        a, b, c, perimeter = triangle
        print(f"Kenarlar: {a}, {b}, {c} - Çevre: {perimeter}")

# Kullanıcıdan giriş al
start = int(input("Başlangıç sayısını girin: "))
end = int(input("Bitiş sayısını girin: "))

triangles = find_triangles_and_perimeters(start, end)

if triangles:
    print("Oluşabilecek üçgenler ve çevreleri:")
    print_triangles(triangles)
else:
    print("Verilen aralıktaki asal sayılarla üçgen oluşturulamaz.")

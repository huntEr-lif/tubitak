def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes(a, b):
    return [x for x in range(a, b + 1) if is_prime(x)]

def find_triangle_triples(primes):
    triples = []
    length = len(primes)
    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                if primes[i] + primes[j] > primes[k]:  # Triangle inequality
                    triples.append((primes[i], primes[j], primes[k]))
    return triples

def triangle_perimeters(triples):
    perimeters = [sum(triple) for triple in triples]
    perimeters.sort(reverse=True)
    return perimeters

def decrypt_message(encrypted_binary, perimeters):
    encrypted_values = [int(x, 2) for x in encrypted_binary.split()]
    decrypted_chars = []
    for i, val in enumerate(encrypted_values):
        decrypted_value = val - perimeters[i % len(perimeters)]
        decrypted_chars.append(chr(decrypted_value))
    return ''.join(decrypted_chars)

def main():
    a = int(input("Lütfen alt sınırı girin: "))
    b = int(input("Lütfen üst sınırı girin: "))
    encrypted_binary = input("Deşifre edilecek ikilik sistemi girin: ")

    primes = find_primes(a, b)
    triples = find_triangle_triples(primes)
    perimeters = triangle_perimeters(triples)
    
    decrypted_message = decrypt_message(encrypted_binary, perimeters)
    print(f"Deşifre edilmiş metin: {decrypted_message}")

    # Kullanıcıdan herhangi bir girdi beklemek için:
    input("Program tamamlandı. Kapanmak için Enter tuşuna basın...")

if __name__ == "__main__":
    main()

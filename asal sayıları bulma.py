def is_prime(num):
    """Bir sayının asal olup olmadığını kontrol eden fonksiyon."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between(start, end):
    """Verilen iki sayı arasındaki asal sayıları bulan fonksiyon."""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Kullanıcıdan başlangıç ve bitiş aralığını alma
start = int(input("Başlangıç sayısını girin: "))
end = int(input("Bitiş sayısını girin: "))

# Asal sayıları bulma ve yazdırma
primes = find_primes_between(start, end)
print(f"{start} ile {end} arasındaki asal sayılar: {primes}")


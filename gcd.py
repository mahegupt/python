#Find the gcd(greatest common divider) of 2 numbers.
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

a=48 
b=12
print(f"gcd of ({a}, {b}) = {gcd(48, 12)}")
a=28
b=18
print(f"gcd of ({a}, {b}) = {gcd(28, 18)}")

# Finding the Most Significant Set Bit (MSB) of a number n.
'''
MSB = The highest-order bit that is set (1) in the binary representation of a number.
Example:
n = 18 → (10010)_2 → MSB at position 4 (value 16)
n = 40 → (101000)_2 → MSB at position 5 (value 32)
'''


def msb_pos(n: int) -> int:
    pos = -1
    while n > 0:
        n >>= 1
        pos += 1
    return pos   # position (0-indexed from LSB)


def msb_val(n: int) -> int:
    if n == 0:
        return 0
    n |= (n >> 1)
    n |= (n >> 2)
    n |= (n >> 4)
    n |= (n >> 8)
    n |= (n >> 16)
    # for 64-bit numbers add n >>= 32
    return (n + 1) >> 1


a = 18
print(f"msb index({a})={msb_pos(a)} and value is {msb_val(a)}")
a = 173
print(f"msb index({a})={msb_pos(a)} and value is {msb_val(a)}")

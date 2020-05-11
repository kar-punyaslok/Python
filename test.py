def reverse_Bits(n):
    result = 0
    for i in range(32):
        result <<= 1
        result |= n & 1
        n >>= 1
    return result


print(reverse_Bits(10))

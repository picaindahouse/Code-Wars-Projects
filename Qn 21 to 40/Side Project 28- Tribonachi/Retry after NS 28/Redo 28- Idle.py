def tribonacci(signature, n):
    if n == 0:
        return []
    elif n <= 2:
        return signature[0:n]
    while len(signature) != n:
        signature.append(sum(signature[:-4:-1]))
    return signature
def Xbonacci(signature, n):
    og = len(signature)
    while len(signature) < n:
        signature.append(sum(signature[:-(og + 1):-1]))
    return signature[:n]
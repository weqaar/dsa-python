
def sumFirstN(n) -> int:
    if (n==0):
        return 0
    elif (n==1):
        return 1
    return n + sumFirstN(n-1)

if __name__ == "__main__":
    print(sumFirstN(5))


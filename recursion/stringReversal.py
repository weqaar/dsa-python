# String reveral

def revStringSlicing(strx):
    if len(strx) == 0: # if not strx:
        return strx
    return revStringSlicing(strx[1:]) + strx[0]

def revStringPythonic(strx):
    return strx[::-1]
    
if __name__ == "__main__":
    revStr = "strings good"
    print("Original String:", revStr)
    print("Reversed String Slicing:", revStringSlicing(revStr))
    print("Reversed String Pythonic:", revStringPythonic(revStr))
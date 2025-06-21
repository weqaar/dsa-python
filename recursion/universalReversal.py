# Reflection based Reversal

"""
Any Object type that supports: Slicing and Concatenation
Technique: Slice and Concatenate O(?)
    e.g. lst = [1, 2, 3, 4, 5]
    1. Slice with [1:] -> lst[1:]
    2. Contacatenate to list the 0th in lst -> + lst[0:1]
"""
def revObject(obj) -> list:
    if not obj:
        return obj
    return (revObject(obj[1:]) + obj[0:1])

if __name__ == "__main__":
    revList = [1, 2, 3, 4, 5]
    print("Original List:", revList)
    print("Reversed List:", revObject(revList))
    
    revStr = "Strings are Good"
    print("Original String:", revStr)
    print("Reversed String:", revObject(revStr))
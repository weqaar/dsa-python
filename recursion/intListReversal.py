# List reversal with recursion

def revListAccumulator(lst) -> list:
    accum = []

    for x in lst:
        """
        e.g. lst = [1, 2, 3, 4, 5]

        accum = [1] + [] = [1] -> x = 1
        accum = [2] + [1] = [2, 1] -> x = 2
        accum = [3] + [2, 1] = [3, 2, 1] -> x = 3
        accum = [4] + [3, 2, 1] = [4, 3, 2, 1] -> x = 4
        accum = [5] + [4, 3, 2, 1] = [5, 4, 3, 2, 1] -> x = 5
        """
        accum = [x] + accum
    return accum

"""
Technique 1: Append O(1)
    e.g. lst = [1, 2, 3, 4, 5]
    1. Slice with [1:] -> lst[1:]
    2. Append to list the 0th in lst -> append lst[0]
"""
def revListSlicingTechnique1(lst) -> list:
    if len(lst) == 0:
        return []
    slicedList = revListSlicingTechnique1(lst[1:])
    #print("DEBUG:", slicedList, "->", lst[0])
    slicedList.append(lst[0])
    return slicedList

"""
Technique 2: Insert at Index O(n)
    e.g. lst = [1, 2, 3, 4, 5]
    1. Slice with [:-1] -> lst[:-1]
    2. Insert to list at index 0 of lst -> insert 0, lst[-1]
"""
def revListSlicingTechnique2(lst) -> list:
    if len(lst) == 0:
        return []
    slicedList = revListSlicingTechnique2(lst[:-1])
    slicedList.insert(0, lst[-1])
    return slicedList

"""
Technique 3: Slice and Concatenate O(?)
    e.g. lst = [1, 2, 3, 4, 5]
    1. Slice with [1:] -> lst[1:]
    2. Contacatenate to list the 0th in lst -> + lst[0:1]
"""
def revListSlicingTechnique3(lst) -> list:
    if len(lst) == 0:
        return []
    return (revListSlicingTechnique3(lst[1:]) + lst[0:1])

if __name__ == "__main__":
    revList = [1, 2, 3, 4, 5]
    print("Original List:", revList)
    print("Accumulator:", revListAccumulator(revList))
    print("Slicing Technique 1:", revListSlicingTechnique1(revList))
    print("Slicing Technique 2:", revListSlicingTechnique2(revList))
    print("Slicing Technique 3:", revListSlicingTechnique3(revList))
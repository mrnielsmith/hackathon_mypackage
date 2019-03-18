def bubble_sort(items):
    '''
    Receives an unsorted list of numbers and
    returns array of items, sorted in ascending order.

    Args:
        items (array): list or array-like object containing numerical values,
        unsorted.

    Returns:
        array: returns list of items, sorted in ascending order.
    '''

    out = items.copy() # in place protection on items
    for i in range(len(out)):
        for j in range(len(out)-1-i):
            if out[j] > out[j+1]:
                out[j], out[j+1] = out[j+1], out[j]     # Swap!

    return out
# end bubble_sort

def merge_sort(items):
    '''
    Receives an unsorted list of numbers and
    returns array of items, sorted in ascending order.

    Args:
        items (array): list or array-like object containing numerical values,
        unsorted.

    Returns:
        array: returns list of items, sorted in ascending order.
    '''
    len_i = len(items)
    if len_i == 1:
        return items

    mid_point = int(len_i / 2)
    i1 = merge_sort(items[:mid_point])
    i2 = merge_sort(items[mid_point:])

    return merge(i1, i2)
# end merge_sort


def merge(A, B):
    '''
    Receives two lists, sorted in ascending order and
    returns a single merged array of items, sorted in ascending order.

    Args:
        items (A) (array): list or array-like object containing
        numerical values, sorted ascending.
        items (B) (array): list or array-like object containing
        numerical values, sorted ascending.

    Returns:
        array: returns list of items, sorted in ascending order.
    '''
    new_list = []
    while len(A) > 0 and len(B) > 0:
        if A[0] < B[0]:
            new_list.append(A[0])
            A.pop(0)
        else:
            new_list.append(B[0])
            B.pop(0)

    if len(A) == 0:
        new_list = new_list + B
    if len(B) == 0:
        new_list = new_list + A

    return new_list
# end merge

def quick_sort(items, index=-1):
    '''
    Receives an unsorted list of numbers and
    returns a list of items, sorted in ascending order.

    Args:
        items (array): list or array-like object containing numerical values,
        unsorted.
        index (default = -1): index position of pivot point.

    Returns:
        array: returns list of items, sorted in ascending order.
    '''
    len_i = len(items)

    if len_i <= 1:
        return items

    pivot = items[index]
    small = []
    large = []
    dup = []
    for i in items:
        if i < pivot:
            small.append(i)
        elif i > pivot:
            large.append(i)
        elif i == pivot:
            dup.append(i)

    small = quick_sort(small)
    large = quick_sort(large)

    return small + dup + large
# end quick_sort

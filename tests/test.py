from mypackage import recursion
from mypackage import sorting

def test_sum_array():
    """
    make sure sum_array works correctly
    """

    assert recursion.sum_array([8, 3, 2, 7, 4]) == 24, 'incorrect'
    assert recursion.sum_array([10, 1, 12, 9, 2]) == 34, 'incorrect'
    assert recursion.sum_array([1, 2, -3, 4, 5]) == 9, 'incorrect'
# end test_sum_array

def test_fibonacci():
    """
    make sure fibonacci works correctly
    """

    assert recursion.fibonacci(0) == 0, 'incorrect'
    assert recursion.fibonacci(1) == 1, 'incorrect'
    assert recursion.fibonacci(5) == 5, 'incorrect'
# end test_fibonacci

def test_factorial():
    """
    make sure factorial works correctly
    """

    assert recursion.factorial(0) == 1, 'incorrect'
    assert recursion.factorial(1) == 1, 'incorrect'
    assert recursion.factorial(5) == 120, 'incorrect'
# end test_factorial

def test_reverse():
    """
    make sure reverse works correctly
    """

    assert recursion.reverse('abc') == 'cba', 'incorrect'
    assert recursion.reverse('one two') == 'owt eno', 'incorrect'
    assert recursion.reverse('123') == '321', 'incorrect'
# end test_reverse

def test_bubble_sort():
    """
    make sure bubble_sort works correctly
    """

    assert sorting.bubble_sort([3,2,1]) == [1,2,3], 'incorrect'
    assert sorting.bubble_sort([5,7,9,1]) == [1,5,7,9], 'incorrect'
    assert sorting.bubble_sort([-1,-5,4,0,-7]) == [-7,-5,-1,0,4], 'incorrect'
# end test_bubble_sort

def test_merge_sort():
    """
    make sure merge_sort works correctly
    """

    assert sorting.merge_sort([3,2,1]) == [1,2,3], 'incorrect'
    assert sorting.merge_sort([5,7,9,1]) == [1,5,7,9], 'incorrect'
    assert sorting.merge_sort([-1,-5,4,0,-7]) == [-7,-5,-1,0,4], 'incorrect'
# end test_merge_sort

def test_quick_sort():
    """
    make sure quick_sort works correctly
    """

    assert sorting.quick_sort([3,2,1]) == [1,2,3], 'incorrect'
    assert sorting.quick_sort([5,7,9,1]) == [1,5,7,9], 'incorrect'
    assert sorting.quick_sort([-1,-5,4,0,-7]) == [-7,-5,-1,0,4], 'incorrect'
# end test_quick_sort

test_sum_array()
test_fibonacci()
test_factorial()
test_reverse()
test_bubble_sort()
test_merge_sort()
test_quick_sort()

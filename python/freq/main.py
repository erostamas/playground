from collections import Counter
nums = [1, 1, 1, 1, 1, 2, 2, 3]


def most_frequent(l: list, k: int) -> list:
    """
    Calculate the most frequent elements in a list
    
    Args:
        l: List of elements
        k: Number of most frequent elements to return

    Returns:
        List of k most frequent elements
    """
    counts = Counter(l)
    return counts.most_common(k)

def test_most_frequent():
    assert most_frequent(nums, 1) == [(1, 5)]
    assert most_frequent(nums, 2) == [(1, 5), (2, 2)]
    assert most_frequent(nums, 3) == [(1, 5), (2, 2), (3, 1)]
    
def most_frequent_empty_list():
    assert most_frequent([], 1) == []

def most_frequent_k_is_zero():
    assert most_frequent(nums, 0) == []
    
def most_frequent_k_is_negative():
    assert most_frequent(nums, -1) == []
    
def most_frequent_k_is_greater_than_list():
    assert most_frequent(nums, 10) == [(1, 5), (2, 2), (3, 1)]
    
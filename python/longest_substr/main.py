def length_of_longest_substring(s: str) -> int:
    """
    Returns the length of the longest substring without repeating characters.
    """
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        print(f"right: {right}")
        print(f"left: {left}")
        print(s[right])
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        print(F"seen: {seen}")
        max_len = max(max_len, right - left + 1)

    return max_len

print(length_of_longest_substring("abcabcbb"))

def valid_palindrome(s: str) -> bool:
    """
    Return True if s can become a palindrome after deleting at most one character.
    """
    def is_pal_range(i: int, j: int) -> bool:
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    i, j = 0, len(s) - 1
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            # try skipping either character
            return is_pal_range(i + 1, j) or is_pal_range(i, j - 1)
    return True


if __name__ == "__main__":
    # quick checks
    assert valid_palindrome("abca") is True  # remove 'b' or 'c'
    assert valid_palindrome("abc") is False
    assert valid_palindrome("a") is True
    assert valid_palindrome("") is True
    print("All tests passed.")
def palindrome(word):
    if word == word[::1]:
        return True
    else:
        False


result = palindrome("dad")

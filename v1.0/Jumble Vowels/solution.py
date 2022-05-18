def reverseTheVowels(n, sentence):
    if n <= 1:
        return sentence
    vowels = set(["a", "e", "i", "o", "u"])
    newStr = list(sentence)
    i, j = 0, n - 1
    while i < j:
        if sentence[i] in vowels and sentence[j] in vowels:
            newStr[i], newStr[j] = newStr[j], newStr[i]
            i, j = i + 1, j - 1
        elif sentence[i] in vowels:
            j -= 1
        elif sentence[j] in vowels:
            i += 1
        else:
            i, j = i + 1, j - 1

    return "".join(newStr)

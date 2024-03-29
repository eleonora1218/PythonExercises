def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    map = {}
    for letter in phrase.lower():
        if letter in 'aeiou': 
            map[letter] = map.get(letter, 0) + 1
    return map

    # phrase = phrase.lower()
    # counter = {}

    # for ltr in phrase:
    #     if ltr in VOWELS:
    #         counter[ltr] = counter.get(ltr, 0) + 1

    # return counter

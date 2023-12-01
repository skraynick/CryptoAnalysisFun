def get_frequencies(cryptotext):
    frequencyDict = dict()
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']

    # Finds the count in the string.
    for xa in alphabet:
        #  frequencyDict.update({xa, cryptotext.count(xa)})
        frequencyDict[xa] = cryptotext.count(xa)
    print("Found frequencies:  ")
    print(frequencyDict)
    return frequencyDict

#Write a brute forcer. Go through every letter and print it!
# todo print top letter. convert to percentage and compare. 
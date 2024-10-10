
def anagram_detection_first(word1, word2):
    list_word2 = list(word2)

    pos_1 = 0
    still_ok = True
    while pos_1 < len(word1) and still_ok:
        pos_2 = 0
        found = False
        while pos_2 < len(word2) and not found:
            if word1[pos_1] == list_word2[pos_2]:
                found = True
            else:
                pos_2 += 1

        if found:
            pos_1 += 1
        else:
            still_ok = False
    return still_ok



# used sort to alphabetically sort the words and then compare to each other
# depends on sort time complexity O(n^2) or O(nlogn)
def anagram_detection_second(word1, word2):
    list_word1 = list(word1)
    list_word2 = list(word2)

    list_word1.sort()
    list_word2.sort()

    pos = 0
    matches = True

    while pos < len(list_word1) and matches:
        if list_word1[pos] == list_word2[pos]:
            pos = pos + 1
        else:
            matches = False
    return matches



# O(n) time complexity, but requires more space
def anagram_detection_third(word1, word2):
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(word1)):
        pos = ord(word1[i]) - ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(word2)):
        pos = ord(word2[i]) - ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    still_ok = True
    while j < 26 and still_ok:
        if c1[j] == c2[j]:
            j += 1
        else:
            still_ok = False

    return still_ok



print(anagram_detection_first("earth", "heart"))
print(anagram_detection_second("earth", "heart"))
print(anagram_detection_third("earth", "heart"))
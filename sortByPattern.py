def sortByPattern(str, pattern):
    store = ""

    for i in pattern:
        if i in str:
            for char in str:
                if char == i:
                    store += char

    return store

print(sortByPattern("abaabbcdc", "abcd"))
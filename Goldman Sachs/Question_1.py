
def sol(words:list, n):
    arr = []
    for word in words:
        check = True
        for i in range(len(arr)):
            if all(word.count(char) == arr[i][0].count(char) for char in word):
                arr[i].append(word)
                print(arr[i][1])
                check=False
                break
        if check:
            arr.append([word])

    for i in range(len(arr)):
        print(' '.join(arr[i]))
    return arr

sol(['act','god','cat','dog','tac'],5)
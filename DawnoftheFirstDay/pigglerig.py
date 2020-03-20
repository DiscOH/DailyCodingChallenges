def winnable(arr):
    index = 1
    step = arr[0]
    path = [0]

    if len(arr) < 2:
        return []
    if step + 1 >= len(arr):
        return [0]

    for elem in arr[1:-1]:
        if step == 0:
            return []
        if index == len(arr):
            return []
        if elem > step:
            path.append(index)
            index += 1
            step = elem
            if step - 1 > len(arr[index:-1]):
                return path
        else:
            step -= 1
            index += 1

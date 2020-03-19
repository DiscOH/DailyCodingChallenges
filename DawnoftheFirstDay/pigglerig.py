def winnable(arr):
    index = 0
    step = arr[0]
    path = []
    for elem in arr:
        if step == 0:
            print('poohead')
            return []
        elif index == len(arr):
            print('so close yet so far')
            return []
        else:
            if elem > step:
                path.append(index)
                step += elem
                index += 1
                if step > len(arr):
                    return path
            else:
                step -= 1
                index += 1
        return []


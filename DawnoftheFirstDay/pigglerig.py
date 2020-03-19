def winnable(arr):
    step = arr[0]
    path = []
    for elem in arr:
        if step == 0:
            print('poohead')
            return []
        elif arr.index(elem) == len(arr)-1:
            print('so close yet so far')
            return []
        else:
            if elem > step:
                path.append(elem)
                step += elem
                if step > len(arr):
                    return path
            else:
                step -= 1

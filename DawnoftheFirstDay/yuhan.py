def to_win(lst):
    if len(lst) == 1:
        return []
    if len(lst) == 2:
        if lst[0] > 1:
            return [0]
        else:
            return []
    else:
        if lst[0] == 0:
            return []
        if lst[0] > len(lst):
            return [0]
        else:
            result = []
            for i in range(1, lst[0]+1):
                winnable = to_win(lst[i:])
                if winnable != []:
                    result = [0] + [x+i for x in winnable]
                    break
            return result


if __name__ == '__main__':
    print(to_win([6,1,1]))
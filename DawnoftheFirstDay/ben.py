from time import sleep


def jump(path: list) -> list:
    if len(path) < 2:
        return []
    velocity = 0
    route = []
    for i, v in enumerate(path[:-1]):
        if v > velocity:
            velocity = v
            route.append(i)
        if velocity == 0:
            return []
        velocity -= 1
    # remove last index if added by mistake
    if velocity >=1:
        return route
    else:
        return []
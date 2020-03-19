#!/usr/bin/python3

path = []


def toEnd(arr, start, end):
  
  if start > end:
    print("WINNER WINNER CHICKEN DINNER")
    return path

  if arr[start] == 0:
    print("You're Stuck LOSER")
    return []

  if start == end:
    print("LOSER")
    return []

  path.append(start)
  return toEnd(arr, start + arr[start], end)


# Added __main__ pattern to avoid accidental code execution on import
if __name__ == '__main__':
  arr = [int(i) for i in input().split()]
  print("Index Traversed = ",(toEnd(arr, 0, len(arr)-1)))

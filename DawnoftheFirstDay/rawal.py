#!/usr/bin/python3


def toEnd(arr, start, end):
  
  if start > end:
    # print("WINNER WINNER CHICKEN DINNER")
    return path

  if arr[start] == 0:
    # print("You're Stuck LOSER")
    return []

  if start == end:
    # print("LOSER")
    return []

  path.append(start)
  return toEnd(arr, start + arr[start], end)

def getList(arr):
  global path
  path  = []
  # arr = [int(i) for i in input().split()]
  # print("Index Traversed = ",(toEnd(arr, 0, len(arr)-1)))
  return toEnd(arr, 0, len(arr)-1)

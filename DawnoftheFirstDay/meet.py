def winner(arr):
    start = 1
    path= []
    jump = arr[1]


    for i in len(range(arr)):
        if len(arr)==1:
            return "u loose"
        elif start == len(arr) ## last point
            return "u loose"
        elif if i> jump:
            path.append(start)
            jump=i
            start+=1
            if jump>len(arr-1):
                return path
        else:
            start+=1


x = winner([1,2,3,4])
print(x)


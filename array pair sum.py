def pair_sum(arr,k):
    if len(arr)<2:
        return
    #sets for tracking
    seen =set()
    output=set()
    #for every no. in array
    for num in arr:
        #set target difference
        target=k-num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num,target),max(num,target))) 
    return len(output)
print(pair_sum([1,2,4,4,3],8)) 
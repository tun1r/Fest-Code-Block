


def snail(snail_map):
    array=[]
    n=len(snail_map)
    for i in snail_map[0]:
        array.append(i)
    for i in range(1,n):
        array.append(snail_map[i][-1])
    '''print(snail_map[n-1][1])
    print(snail_map[n-1][0])'''
    for i in range(1,-1,-1):
        array.append(snail_map[n-1][i])
    for i in range(0,2):
        array.append(snail_map[n-2][i])
    print(array)       
snail([[1,2,3],
       [8,9,4],
       [7,6,5]])
        
    
    
    
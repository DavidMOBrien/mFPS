'''
Author: DavidMOBrien
Date: 9 - 30 - 19
'''

if __name__ == '__main__':
    '''using 'A' as our example input'''
    A = [[1,2,3],[4,5,6],[7,8,9]]

    '''starting at the bottom row, we don't have any calculations to do because
through the logic of our solution (in the readme.txt), the lowest sum that we
can have at the bottom row is the bottom row's original value.'''
    results = []
    results.append(A.pop())

    '''Run our calculations, removing the list we calculated at the end, then
    stop once there are no more lists to look at ( in other words, we've done
    everything that we want to ).'''
    while A != []:
        current = A.pop()
        '''make a newList to store the values we find'''
        newList = []

        '''for each item in a row, look at the row above it (in this case it
        will be 'results[-1]' and look at both the value directly above the value
        and the above value's neighbors. If the value is at the end of the list
        it will only have two values to look at, otherwise it will have 3. Then
        we simply take the lowest of the 3 and add it to the newList'''
        for i in range(len(current)):
            if i == 0:
                newList.append(min(current[i] + results[-1][0],
                                    current[i] + results[-1][1]))
            elif i == len(current)-1:
                newList.append(min(current[i] + results[-1][-1],
                                    current[i] + results[-1][-2]))
                
            else:
                newList.append(min(current[i] + results[-1][i-1],
                                    current[i] + results[-1][i],
                                    current[i] + results[-1][i+1]))
        results.append(newList)

    '''output the lowest value in the last-generated row in results to find
our minimum falling path sum'''
    print(min(results[-1]))

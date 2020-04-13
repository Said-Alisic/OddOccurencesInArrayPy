# find odd number which only occurs once in an array
def solution(A):   

    # if array only holds a single number, return that one  
    if len(A) == 1:
         return A[0]

    # sort array to more easily loop over it
    A = sorted(A)

    # check every 2nd element to see if it is the 
    # same as next one or if it is the last then return last one
    for i in range(0 , len(A) , 2):
         if i + 1 == len(A):
             return A[i]
         if A[i] != A[i + 1]:
             return A[i]
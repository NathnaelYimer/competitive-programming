
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr=[i for i in range(1,n+1)]
        def res(index,k):
            if len(arr)==1:
                return
            index=(index + k) % len(arr)
            arr.pop(index)
            res(index,k)
        res(0,k-1)
        return arr[0]

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        list2 =[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                list2.append('FizzBuzz')
            elif i%3==0:
                list2.append('Fizz')
            elif i%5==0:
                list2.append('Buzz')
           
            else:
                list2.append(str(i))
        return list2

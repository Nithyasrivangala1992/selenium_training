class Numbers:
    def even_odd(self,start, end):
        for num in range(40, 60):
            if num%2==0:
               print(f"{num} is even")
            else:
               print(f"{num} is odd")

num = Numbers()
num.even_odd(40, 60)

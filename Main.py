prime = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]



for x in prime:
    if x > 1:
       for i in range(2, x):
           if (x % i) == 0:
               break
       else:
           print(x)




sum = 0
come = True

while come ==True:
     s=int(input("input a number"))

     if  s == 0: 
         print("Loop terminated")
         print("Total of all sum is ", sum)
         break
     else:
          print("Loop Continue")
          su+=s
          print("current total is ",  sum )
          continue
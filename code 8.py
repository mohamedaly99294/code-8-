q=200 #total coins 
x=0   #player 1
y=0   #player 2 
print ("total : " ,q)
while True:
          x=int(input('player 1 select your num. '))
          while( x<0 or x==0 or (q-x)<0 or (x>(2*y) and (y!=0 or x==q)) ):
            x=int(input())
          q=q-x
          print ("rimender : " ,q)
          if q==0: # the rimender is equale 0 
             print ('the winer is player 1')
             break
             y=int(input('player 2 select your num. '))
          while y<0 or y==0 or (q-y)<0 or y>(2*x):
             y=int(input())
          q=q-y
          print ("rimender : " ,q)
          if q==0: # the rimender is equale 0
             print ('the winer is player 2')
             break

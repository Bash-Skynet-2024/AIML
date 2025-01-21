import random

x1 = 5
x2 = 10

w1 = 1
w2 = 1
b1 = 1
b2 = 1

yt = 10

#Init Step
ya = w1*x1 + b1 + w2*x2 + b2
e = yt - ya

#Back Propagation Condition
etol = 0.01
count = 1
while(abs(e) > etol) :
  #Weight Update
  if(e > 0) :
    w1 = w1 + random.random()
    b1 = b1 + random.random()/10
    w2 = w2 + random.random()
    b2 = b2 + random.random()/10
  else :
    w1 = w1 - random.random()
    b1 = b1 - random.random()/10
    w2 = w2 - random.random()
    b2 = b2 - random.random()/10

  #Feed Forward
  ya = w1*x1 + b1 + w2*x2 + b2
  e = yt - ya
  print('W1=%f, b1=%f, W2:%f, b2:%f, ya=%f, e=%f\n'%(w1,b1,w2,b2,ya,e))
  count = count + 1

print('Iter = %d' % count)

from matplotlib.pyplot import *
import numpy as np

y=[8,0,2,2,4]
x = np.empty(len(y))
x.fill(4)

y1=[13,164,10,125,22]
x1 = np.empty(len(y1))
x1.fill(8)

y2=[1937,263,2528,2287,82]
x2 = np.empty(len(y2))
x2.fill(12)


y3=[4397,6155,4982,35766,22541]
x3 = np.empty(len(y3))
x3.fill(16)

y4=[1154731,300455,86312,20417,965289]
x4 = np.empty(len(y4))
x4.fill(20)

# Averages
x5=[4,8,12,16,20]
y5=[3.2,66.8,1419.4,14768.2,505440.8]

scatter(x,y,color = 'yellow')
scatter(x1,y1,color = 'green')
scatter(x2,y2,color = 'black')
scatter(x3,y3)
scatter(x4,y4,color = 'grey',label="something")

plot(x5,y5,color = 'red')
xlabel("number of iterations")
ylabel("frequency")
labels = ['Averages ','4 bits' ,'8 bits', '12 bits' , '16 bits ', '20 bits' ]
legend(labels, loc="best")
show()


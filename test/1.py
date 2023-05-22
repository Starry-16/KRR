# X=[36.5,54.3,80.1,109.8,143.2]
# X=[1015,11258,2348,3538]
# Xd=[0,0,0,0,0]
# for i in range(len(X)):
#     Xd[i]=(1/(len(X)-(i+1)+1))*sum(X[i:])

# Xd2=[0,0,0,0,0]
# for i in range(len(X)):
#     Xd2[i]=(1/(len(X)-(i+1)+1))*sum(Xd[i:])
# print(Xd)
# print(Xd2)

X0=[3.5,4.7,6.3,8.2,10]
X1=[3.2,5.1,7,8.6,10.4]
# X0=[0.91,0.97,0.90,0.93,0.91,0.93,0.95]
# X1=[0.60,0.68,0.61,0.62,0.63,0.64,0.65]
# X1=[0.82,0.86,0.90,0.89,0.88,0.87,0.86]
x1=[]
for i in range(len(X0)):
    x1.append(round(X0[i]-X0[0],2))
print("x1",x1,type(x1))
x2=[]
for i in range(len(X1)):
    x2.append(round(X1[i]-X1[0],2))
print("x2",x2)

sumx1=sum(x1[1:-1])
sumx2=sum(x2[1:-1])
sum111=(sumx1-sumx2)+0.5*(x1[len(x1)-1]-x2[len(x2)-1])
sum111=abs(sum111)
print("s0-s1",sum111)
final=1/(1+sum111)
print("灰色相似关联度",final)

sumX1=sum(X0[1:-1])
sumX2=sum(X1[1:-1])
sum222=(sumX1-sumX2)+0.5*(X0[len(X0)-1]-X1[len(X1)-1])
sum222=abs(sum222)
print("S0-S1",sum222)
final2=1/(1+sum222)
print("灰色接近关联度",final2)
import numpy as np

ab = [3,76]
data = [[2,81],[4,93],[6,91],[8,97]]
x = [i[0] for i in data]
y = [i[1] for i in data]

print(x)

def predict(x):
    return ab[0]*x + ab[1]

def rmse(p,y):
    return np.sqrt(((p-y)**2).mean())

def rmse_val(p_rst,y):
    return rmse(np.array(p_rst),np.array(y))

p_rst = []
for i in range (len(x)) :
    p_rst.append(predict(x[i]))
    print("hour:%.f,y:%.1f,pre_y:%.1f" %(x[i],y[i],p_rst[i]))
    
rst = rmse_val(p_rst,y)

print(rst)

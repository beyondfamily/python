import numpy as np
import matplotlib.pyplot as plt

#预设参数
L = 13
nb = 6
N = 25000
mu = 0.02


#读取数据
filename = '7_ss_all3.txt'
source = np.genfromtxt(filename,delimiter=',')
source = np.mat(source)
source[source==0] = -1
filename = '7_rr_all3.txt'
source_f2 = np.genfromtxt(filename,delimiter=',')
source_f2 = np.mat(source_f2)
ber_num = np.mat(np.zeros((1,32)))

ii = 31    # 数据集为32*250000，此处取第32行
source0 = source[:,ii]
source1 = source0[N+1:-nb+1]
data_cnt = len(source1)
source_f = source_f2[:,ii]

cnt = len(source_f)
out = np.mat(np.zeros((cnt-nb+1,1)))
for i in range(0,nb+1):
    out[i] = source_f[i]

B = np.mat(np.zeros((nb,1)))
B1 = np.mat(np.zeros((nb,N)))
fe = np.mat(np.zeros((cnt,1)))
z = np.mat(np.zeros((cnt,1)))
e = np.mat(np.zeros((N,1)))
for i in range(nb,cnt-nb-1):
    #U = source_f[i-nw:i+nw+1]
    U = out[i-nb:i]
    z[i] = B.T*U
    out[i] = np.sign(z[i])
    if i < N:
        e[i] = source0[i] - z[i]
        B = B + np.mat((mu * 2 * e[i] * U.T).T)  #更新前馈系数
        B1[:,i] = B
out2 = out[N+1:]
erro = np.where(out2 != source1) #返回输出和原信号不同的位置
ber_num[0,ii] = len(erro[0])/data_cnt #错误率

print('B = ',B.T)
print(erro[0])
print('错误个数 = ',len(erro[0]))
print('错误率 = ',ber_num[0,ii])
plt.figure(1)
plt.title('loss')
plt.plot(np.linspace(0, len(e), N), e)
plt.show()
plt.figure(2)
plt.title('Feedforward Equalizer')
plt.plot(B1.T)
plt.show()
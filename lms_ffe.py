import numpy as np
import matplotlib.pyplot as plt

#预设参数
L = 13
nw = 6
N = 25000
mu = 0.02
loops = 0

#读取数据
filename = '7_ss_all3.txt'
source = np.genfromtxt(filename,delimiter=',')
source = np.mat(source)
source[source==0] = -1
filename = '7_rr_all3.txt'
source_f2 = np.genfromtxt(filename,delimiter=',')
source_f2 = np.mat(source_f2)
ber_num = np.mat(np.zeros((1,32)))

ii = 31   # 数据集为32*250000，此处取第32行
source0 = source[:,ii]
source1 = source0[N+1:-nw+1]
data_cnt = len(source1)
source_f = source_f2[:,ii]

cnt = len(source_f)
out = np.mat(np.zeros((cnt-nw+1,1)))

W = np.mat(np.zeros((L,1)))
W1 = np.mat(np.zeros((L,N)))
fe = np.mat(np.zeros((cnt,1)))
z = np.mat(np.zeros((cnt,1)))
e = np.mat(np.zeros((N,1)))
for i in range(nw,cnt-nw):
    U = source_f[i-nw:i+nw+1]
    z[i] = W.T*U
    out[i] = np.sign(z[i])
    if i < N:
        e[i] = source0[i] - z[i]
        W = W + np.mat((mu * 2 * e[i] * U.T).T)  #更新前馈系数
        W1[:,i] = W
out2 = out[N+1:]
erro = np.where(out2 != source1) #返回输出和原信号不同的位置
ber_num[0,ii] = len(erro[0])/data_cnt #错误率

print('W = ',W.T)
print(erro[0])
print('错误个数 = ',len(erro[0]))
print('错误率 = ',ber_num[0,ii])
plt.figure(1)
plt.title('loss')
plt.plot(np.linspace(0, len(e), N), e)
plt.show()
plt.figure(2)
plt.title('Feedforward Equalizer')
plt.plot(W1.T)
plt.show()

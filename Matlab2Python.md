# 有关matlab转python的一些经验总结（Pycharm）

## 共同点

变量设置：
python和matlab相同，无需变量声明，对变量赋值后即视为创建变量

## python与matlab的比较

Python + ‘numpy’ + ‘scipy’ + ‘matplotlib’ ≈ Matlab

在python中，使用numpy，scipy，matplotlib这三个库基本可以实现matlab所需要的所有功能

## 一些区别

#### 1 数组编号

Python 数组编号从0开始，matlab数组序号从1开始

![python](https://images.gitee.com/uploads/images/2021/0506/214623_9b75fdab_9056218.png "屏幕截图.png")

![matlab](https://images.gitee.com/uploads/images/2021/0506/214641_fa49dc12_9056218.png "屏幕截图.png")

#### 2 区间

Python 服从左闭右开原则，matlab则是左闭右闭
（比如0：5，在python中显示为0，1，2，3，4，在matlab中显示为0，1，2，3，4，5）

#### 3 矩阵：

Python 用numpy.mat创建矩阵，矩阵的形式与list相似，用[]表示矩阵外。
![python](https://images.gitee.com/uploads/images/2021/0506/214906_5308647f_9056218.png "屏幕截图.png")

Matlab矩阵与数组一致，用（）表示矩阵外
![matlab](https://images.gitee.com/uploads/images/2021/0506/214926_19c3d0d2_9056218.png "屏幕截图.png")

#### 4 find函数

Matlab 中的find（）函数对应python的 numpy.where函数，同样表示（）中表达式成立时在矩阵中的位置。python也有find函数，不过表达的和matlab中不是一个意思


#### 5 数组对数组赋值

Python 中一个数组对另外一个数组赋值会使得原数组跟着被赋值的数组一起变化 为了避免这样的变化，可用 List(a) = list(b) 或者用 copy库中的deepcopy函数

#### 6 调试

同样在python和matlab中都是非常强大的工具。在遇到pyhton结果与matlab不符合的时候，可以利用调试功能步进模块查看变量，比较python和matlab的变量差异，从而找到程序错误的位置

![python](https://images.gitee.com/uploads/images/2021/0506/215751_4716a548_9056218.png "屏幕截图.png")

![python](https://images.gitee.com/uploads/images/2021/0506/215809_46d1076a_9056218.png "屏幕截图.png")

![python](https://images.gitee.com/uploads/images/2021/0506/215818_436a89e3_9056218.png "屏幕截图.png")

![matlab](https://images.gitee.com/uploads/images/2021/0506/215827_b043ebf9_9056218.png "屏幕截图.png")

![matlab](https://images.gitee.com/uploads/images/2021/0506/215835_e5ed6964_9056218.png "屏幕截图.png")
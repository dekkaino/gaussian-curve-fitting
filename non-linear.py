##フィッティングに使う
from scipy.optimize import curve_fit
import numpy as np

## 図示のために使う
import seaborn as sns
import matplotlib.pyplot as plt

## フィッティングしたい関数式
def gauss_fit(x, amplitude, mean, stdev):
    gaussian =  amplitude * np.exp( -((x - mean)/(np.sqrt(2)*stdev))**2)
    return gaussian

#csvからデータを読み込む
def getWaves():
    from tkinter import filedialog
    filename = filedialog.askopenfilename()
    #2列のデータを読み込んで、xとyの1次元配列に分ける
    xy_array = np.loadtxt(filename, delimiter=',')
    x_array, y_array = xy_array[:,0], xy_array[:,1]

    return x_array, y_array

#主の処理
def main():
    array_x, array_y = getWaves()

    param, cov = curve_fit(gauss_fit, array_x, array_y)
    #paramはamplitude, mean, stdev
    print(param)
    #回帰パラメータの保存
    np.savetxt('param.txt', param)


    #回帰曲線を作る
    list_y = []
    for num in array_x:
        list_y.append( gauss_fit(num, param[0],param[1],param[2]))
        
    ##図示
    sns.pointplot(x=array_x, y=array_y, join=False)
    sns.pointplot(x=array_x, y=np.array(list_y), markers="")
    plt.show()

main()
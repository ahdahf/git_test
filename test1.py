dist_log=[56,22,8,91,44,15,77]
dist_log.append(-5)  #手动加入异常数据
k=a=b=c=d=e=q=0  #分别为除数,危险数据数,近距离数据数,安全数据数,有效数据总和,异常数据数,平均值
for i in  dist_log:  #遍历list
        print(f"当前检测距离{i}cm")
        print(type(i))
        if i<0:
            e+=1
        elif i<=10:
            a+=1
            k+=1
            d+=i
            print("危险预警,紧急避让")
        elif i <= 30:
            b += 1
            k += 1
            d += i
            print("近距离,谨慎行驶")
        else:
            c+=1
            k+=1
            d+=i
            print("安全距离,正常行驶")
if k>0:  #若k为0,直接计算将出错
    q=d/k
    print("平均距离为%.2fcm"%(q))
else:
    q=0
    print("数据出错")
print("=====设备日志数据分析报告=====")
print(f"危险数据次数:{a}次")
print(f"近距离数据次数:{b}次")
print(f"安全数据次数:{c}次")
print(f"有效数据总次数:{a+b+c}次")
print(f"本次检测平均距离:{q:.2f}")
print(f"异常数据条数:{e}条")
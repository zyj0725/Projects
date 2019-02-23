'''
    测试pycharm上传代码
    输出斐波那契数列前n项
'''
a,b,n = 0,1,0
num = int(input('请输入一个正整数:'))
print(a,end=' ')
while True:
    a += b
    a,b = b,a
    n += 1
    if n == num:
        break
    print(a,end=' ')
print()



#函数声明
def fun(a,b):
    a,b=b,a
    print('函数内交换数值后:a=%d,\tb=%d\n' %(a,b))

a=10
b=15
print('调用函数前的数值:a=%d,\tb=%d\n'%(a,b))

print('\n-------------------------------------')
    
#调用函数
fun(a,b)
print('\n-------------------------------------')
print('调用函数后的数值:a=%d,\tb=%d\n'%(a,b))
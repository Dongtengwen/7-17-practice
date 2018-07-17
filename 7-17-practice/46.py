def dollarToRMB(dollar):
    RMB=dollar*6.28
    return RMB
d=float(input('请输入美元数目'))
print('人民币数目为：%f'%dollarToRMB(d))

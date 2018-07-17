salary=int(input('请输入收入金额：'))
if salary>3500 and salary<3500+1500:
    tax=(salary-3500)*0.03
elif salary>3500+1500 and salary<3500+4500:
    tax=1500*0.03+(salary-3500-1500)*0.1
elif salary>3500+4500 and salary<3500+9000:
    tax=1500*0.03+3000*0.1+(salary-3500-4500)*0.2
elif salary>3500+9000 and salary<3500+35000:
    tax=1500*0.03+3000*0.1+4500*0.2+(salary-3500-9000)*0.25
elif salary>3500+35000 and salary<3500+55000:
    tax=1500*0.3+3000*0.1+4500*0.2+0.25*26000+0.3*(salary-3500-35000)
elif salary>3500+55000 and salary<3500+80000:
    tax=1500*0.3+3000*0.1+4500*0.2+0.25*26000+0.3*20000+0.35*(salary-3500-55000)
elif salary>3500+80000:
    tax=1500*0.3+3000*0.1+4500*0.2+0.25*26000+0.3*20000+0.35*25000+0.45*(salary-3500-80000)
getMoney=salary-tax
print('需缴纳个人所得税%d元，实际收入%d元'%(tax,getMoney))

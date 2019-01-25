# 1. 提示用户输入苹果的单价
price = float(input("请输入苹果的单价："))
# 2.提示用户输入苹果的重量
weigh = float(input("请输入苹果的重量："))
# 3. 计算金额
money = price * weigh
print("请支付：" + str(money) + "元")
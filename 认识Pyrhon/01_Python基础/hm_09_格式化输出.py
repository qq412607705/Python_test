# 1.定义字符串变量name，输出 我的名字叫小明，请多多关照！
name = "大明"
print("我的名字叫%s，请多多关照！" %name)

# 2.定义整数变量student_no,输出我的学号是00001
student_no = 2
print("我的学号是%06d" % student_no)

# 3.定义小数price、weight、money，
# 输出苹果单价8.50元/斤，购买了7.50斤，需要支付63.75元
price = 8.5
weight = 7.5
money = price * weight
print("苹果单价%.2f元/斤，购买了%.2f斤，需要支付%.2f元" % (price,weight,money))

# 4.定义一个小数scale，输出数据比例是10.00%
scale = 0.25
print("数据比例是%.2f%%" % (scale * 100))


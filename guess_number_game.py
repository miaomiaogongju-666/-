import random
sentences=["嘻嘻，猜错了哟","僵尸吃掉了你的脑子","又错了，你真的有在认真猜吗？","小傻瓜又猜错了","宝贝你是一只笨笨猪咪","恭喜你又没猜对，哈哈:p""啊嘞勒，你的运气很差喔"
           "特此颁发猜数最慢奖，恭喜获奖""我猜你在用二分法，可惜你还是猜错了""不要气馁，我给你准备了很多‘温馨鼓励’哦""哈哈哈哈又错了"]
secret=random.randint(1,100)
print("请在1到100以内猜出正确的整数")
while True:
    guess=int(input("猜猜我是谁"))
    if guess not in range(1,100):
        print("你这家伙，给我输入100以内的整数啊喂！我是不会给别人卡bug的机会的！")
    if guess>secret:
        sentence=random.choice(sentences)
        print("大了",sentence )
    elif guess<secret:
        sentence = random.choice(sentences)
        print("小了",sentence)
    elif guess==secret:
        print("哇塞你终于猜对了鼓掌鼓掌。")
        break

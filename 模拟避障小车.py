import random
import time
print("------------模拟避障小车启动----------")
obstacle=random.choice([True,False])
print("小车前进")

if not obstacle:
    print("小车状态：正常前进")
else:
    print("前方检测到障碍")
    print("执行：后退")
    time.sleep(1)
    print("执行：左转")
    time.sleep(0.8)
    print("执行：恢复前进\n")
    time.sleep(1)
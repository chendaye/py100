"""
跑马灯
"""

import os
import time

content = 'chendaye666@gmail.com'
while True:
    os.system('cls')  # 清屏
    print(content)
    time.sleep(1)
    content = content[1:] + content[0]
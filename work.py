import json

# 读取receiver.json文件
with open('receiver.json', 'r') as f:
    data = json.load(f)

# 遍历礼物类
for category in data['礼物类']:
    # TODO: 在这里实现你的礼物挑选逻辑
    pass

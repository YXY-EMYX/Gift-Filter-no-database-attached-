
import jieba.posseg as pseg

# 读取本地txt文本
with open('爱好.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# 分词并统计词频
word_generator = pseg.cut(content)
word_dict = {}
for word, flag in word_generator:
    if flag == 'n':  # 筛选名词
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1

# 将字典转换为列表形式
word_list = list(word_dict.keys())

print(word_list)
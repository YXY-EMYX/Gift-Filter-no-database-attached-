import tkinter as tk
from Recipient import Recipient

class ReceiverForm:
    def __init__(self, master):
        self.master = master
        self.master.title("礼物入库")
        self.master.geometry("800x950")
        # 创建礼物名称输入框
        name_frame = tk.Frame(master)
        name_frame.pack(side=tk.TOP, padx=10, pady=10)
        tk.Label(name_frame, text="礼物名称：").pack(side=tk.LEFT)
        self.name_entry = tk.Entry(name_frame)
        self.name_entry.pack(side=tk.LEFT)

        # 创建性别选项框
        gender_frame = tk.Frame(master)
        gender_frame.pack(side=tk.TOP, padx=10, pady=10)
        tk.Label(gender_frame, text="性别：").pack(side=tk.LEFT)
        self.gender_var = tk.StringVar(value="不限")
        tk.Radiobutton(gender_frame, text="男", variable=self.gender_var, value="男").pack(side=tk.LEFT)
        tk.Radiobutton(gender_frame, text="女", variable=self.gender_var, value="女").pack(side=tk.LEFT)
        tk.Radiobutton(gender_frame, text="不限", variable=self.gender_var, value="不限").pack(side=tk.LEFT)

        # 创建年龄选项框
        age_frame = tk.Frame(master)
        age_frame.pack(side=tk.TOP, padx=10, pady=10)
        tk.Label(age_frame, text="年龄：").pack(side=tk.LEFT)
        self.age_var = tk.StringVar(value="不限")
        ages = ["不限","幼年", "少年", "青年", "壮年", "中年", "老年"]
        for i in range(len(ages)):
            tk.Radiobutton(age_frame, text=ages[i], variable=self.age_var, value=ages[i]).pack(side=tk.LEFT)

        # 创建爱好选项框
        hobby_frame = tk.Frame(master)
        hobby_frame.pack(side=tk.TOP, padx=10, pady=10)

        tk.Label(hobby_frame, text="礼物符合的爱好：").grid(row=0, column=0, sticky="w")

        self.hobby_vars = []
        hobbies = ['健身', '足球', '篮球', '排球', '乒乓球', '羽毛球', '网球', '滑板', '跑步', '自行车', '跆拳道', '柔道',
                    '剑', '音乐', '唱歌', '乐器', '美食', '摄影', '画画', '书法', '剪纸', '编织',
                    '陶艺', '雕刻', '电影', '戏剧', '舞蹈', '歌剧', '美术', '徒步旅行', '背包','电子游戏', '棋牌',
                    '桌游', '科技', '编程', '算法', '人工智能', '机器人', '虚拟现实', '手工', '绣花', '刺绣', '纸艺',
                    '木工', '金工', '邮票', '硬币', '纪念币', '文物', '艺术品', '玉器', '瓷器', '书画', '卡', '宠物', '养猫',
                    '养鱼', '养鸟', '动物', '植类', '种花', '种草', '盆栽', '绿化', '园艺', '社交', '聚会', '聚餐',
                    '课程', '语言', '潜水', '户外活动', '钓鱼', '探险', '艺术类', '阅读写作', '剧本创作',
                    '棋类', '牌类', '玩具', '影视', '品酒', '咖啡', '茶艺', '餐饮', '交友', '公益','文化','科技', '创客', '购物',
                    '服饰', '鞋', '收藏品', '车友', '动漫', '手工艺', '游乐场', '演唱会', '话剧', '博物馆', '动物园', '水族馆', '马戏', '杂技', '魔术',
                    '名胜古迹', '野餐', '瑜伽', '爬山', '赛车', '赛艇', '冰球', '保龄球', '马术', '射箭', '划艇', '皮划艇', '骑马', '极限运动',
                    '艺术', '绘画', '雕塑', '建筑', '服装','室内摆件','动画', '电视','蜜月游', '手游', '小说',
                    '历史', '传记', '心理学', '哲学', '散文', '诗歌', '日记', '新闻稿', '剧本','家常菜',
                    '西餐', '中餐', '饮品', '装饰', '手艺', '插花', '字画', '桥牌', '麻将',"长笛", "古典吉他", "电吉他", "钢琴",
                    "萨克斯管", "三角铁", "小提琴", "鼓", "双簧管", "手风琴", "大提琴", "萧", "尤克里里"]

        # Define the number of columns and rows for the grid
        num_columns = 8
        num_rows = len(hobbies) // num_columns + (1 if len(hobbies) % num_columns != 0 else 0)

        # Create the grid of checkboxes
        for i, hobby in enumerate(hobbies):
            var = tk.BooleanVar(value=False)
            tk.Checkbutton(hobby_frame, text=hobby, variable=var).grid(row=i // num_columns + 1, column=i % num_columns,
                                                                       sticky="w")
            self.hobby_vars.append((hobby, var))

        # 创建是否为实物选项框
        is_physical_frame = tk.Frame(master)
        is_physical_frame.pack(side=tk.TOP, padx=10, pady=10)
        tk.Label(is_physical_frame, text="是否为实物：").pack(side=tk.LEFT)
        self.is_physical_var = tk.StringVar(value="否")
        is_physical = ["是", "否"]
        for i in range(len(is_physical)):
            tk.Radiobutton(is_physical_frame, text=is_physical[i], variable=self.is_physical_var, value=is_physical[i] ).pack(side=tk.LEFT)

        # 创建实物体积选项框
        size_frame = tk.Frame(master)
        size_frame.pack(side=tk.TOP, padx=10, pady=10)
        tk.Label(size_frame, text="实物体积：").pack(side=tk.LEFT)
        self.size_var = tk.StringVar(value="无")
        sizes = ["大", "中", "小","无"]
        for i in range(len(sizes)):
            tk.Radiobutton(size_frame, text=sizes[i], variable=self.size_var, value=sizes[i]).pack(side=tk.LEFT)

        # 创建价格选项框
        prices_frame = tk.Frame(master)
        prices_frame.pack(side=tk.TOP, padx=10, pady=10)
        tk.Label(prices_frame, text="价格区间：").grid(row=0, column=0, sticky="w")

        self.prices_vars = []
        price = ['0-50', '50-100', '100-500', '500-1000', '1000-2000', '1000以上']

        # Create the grid of checkboxes
        for i, prices in enumerate(price):
            var = tk.BooleanVar(value=False)
            tk.Checkbutton(prices_frame, text=prices, variable=var).grid(row=i // num_columns + 1, column=i % num_columns,
                                                                       sticky="w")
            self.prices_vars.append((prices, var))

        # 创建保存按钮
        save_button = tk.Button(master, text="保存", command=self.save)
        save_button.pack(side=tk.TOP, padx=10, pady=10)


    # 将表单信息保存到文件
    def save(self):
        name = self.name_entry.get()
        gender = self.gender_var.get()
        age = self.age_var.get()
        hobbies = [hobby for hobby, var in self.hobby_vars if var.get()]
        is_physical = self.is_physical_var.get()
        size = self.size_var.get()
        prices = [price for price ,var in self.prices_vars if var.get()]
        receiver = {"name":name,"gender": gender, "age": age, "hobbies": hobbies,"is_physical":is_physical,"size":size,"prices":prices}
        with open("gift.txt", "a") as f:
            for key, value in receiver.items():
                f.write(key + ": " + str(value) + "\n")
        self.master.destroy()

# 创建主窗口和表单实例
root = tk.Tk()
form = ReceiverForm(root)
root.mainloop()

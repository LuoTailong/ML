# coding:utf-8
import math
# 定义基于用户的协同过滤算法类
class UserBasedCF:
    # 初始化对象
    def __init__(self, train_file, test_file):
        # 训练数据
        self.train_file = train_file
        # 测试数据
        self.test_file = test_file
        # 读取数据
        self.readData()

    # 数据读取函数
    def readData(self):
        # 读取文件，生成用户-物品的评分表和测试集
        # 用户-物品的评分表
        # 训练集
        self.train = dict()
        # 打开文件，按行读取训练数据
        for line in open(self.train_file):
            # 获得用户、物品、评分数据，丢弃时间戳数据
            user, item, score, _ = line.strip().split("\t")
            # 用户-物品评分矩阵
            self.train.setdefault(user, {})
            # 分数赋值
            self.train[user][item] = int(score)
            # print(self.train[user][item])

        # 测试集
        self.test = dict()
        # 打开文件，按行读取训练数据
        for line in open(self.test_file):
            # 获得用户、物品、评分数据，丢弃时间戳数据
            user, item, score, _ = line.strip().split("\t")
            # 用户-物品评分矩阵
            self.test.setdefault(user, {})
            # 分数赋值
            self.test[user][item] = int(score)

    # 用户间相似度
    def UserSimilarity(self):
        # 建立物品-用户的倒排表
        # 数据格式：key:物品 value:用户1，用户2
        self.item_users = dict()

        # 遍历训练集中用户-物品数据
        for user, items in self.train.items():
            # 遍历用户对应的物品数据
            for i in items.keys():
                # 倒排表还没有该物品
                if i not in self.item_users:
                    # 倒排表中该物品项赋值为set()集合
                    self.item_users[i] = set()
                # 倒排表中该物品项添加该用户
                self.item_users[i].add(user)

        # 计算用户-用户相关性矩阵
        C = dict()  # 用户-用户共现矩阵
        N = dict()  # 用户产生行为的物品个数

        # 遍历物品-用户的倒排表，取得物品-用户数据
        for i, users in self.item_users.items():
            # 遍历物品i下的用户
            for u in users:
                # 初始化用户产生行为的物品个数0
                N.setdefault(u, 0)
                # 遍历到该用户加1
                N[u] += 1

                # 用户-用户共现矩阵初始化
                C.setdefault(u, {})
                # 遍历该物品下所有的用户
                for v in users:
                    # 若该项为当前用户，跳过
                    if u == v:
                        continue
                    # 遍历到其他不同用户则加1
                    # 初始化为0
                    C[u].setdefault(v, 0)
                    # 加1
                    C[u][v] += 1

        # 计算用户-用户相似度，余弦相似度
        self.W = dict()  # 相似度矩阵
        # 遍历用户-用户共现矩阵的所有项，
        # 每行用户、该行下的其他用户
        for u, related_users in C.items():
            # 存放用户间相似度
            self.W.setdefault(u, {})
            # 遍历其他每一个用户及对应的同现矩阵的值，即分子部分
            for v, cuv in related_users.items():
                # 余弦相似度
                self.W[u][v] = cuv / math.sqrt(N[u] * N[v])
                # 返回用户相似度
        return self.W

        # 给用户user推荐，前K个相关用户喜欢的，

    # 用户user未产生过行为的物品
    # 默认3个用户，推荐10个物品
    def Recommend(self, user, K=3, N=10):
        # 用户user对物品的偏好值
        rank = dict()
        # 用户user产生过行为的物品项item
        action_item = self.train[user].keys()

        # 对用户user按相似度从大到小进行排列
        # 取与用户user相似度最大的K个用户
        for v, wuv in sorted(self.W[user].items(), key=lambda x: x[1], reverse=True)[0:K]:
            # 遍历前K个与user最相关的用户
            # 遍历每件物品、用户对该物品的偏好值
            for i, rvi in self.train[v].items():
                # 若用户user对物品i已有评价，则跳过
                if i in action_item:
                    continue
                # 计算用户user对物品i的偏好值
                # 初始化该值为0
                rank.setdefault(i, 0)
                # 通过与其相似用户对物品i的偏好值相乘并相加
                rank[i] += wuv * rvi
                # 按评分值大小，为用户user推荐结果的取前N个物品
        return dict(sorted(rank.items(), key=lambda x: x[1], reverse=True)[0:N])


if __name__ == '__main__':
    #将训练集和测试集指定为u.data
    cf = UserBasedCF('u.data', 'u.data')
    cf.UserSimilarity()
    print(cf.Recommend('3'))
# {'313': 7.702489204665911, '286': 7.193871110379812, '315': 6.675060438409236, '316': 6.675060438409236, '750': 6.172183941417205, '895': 6.156249766438661, '289': 5.65337326944663, '269': 5.140304194770122, '301': 5.134562597476054, '292': 4.627235120093614}












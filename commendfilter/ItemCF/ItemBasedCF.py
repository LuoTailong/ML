# coding:utf-8
import math


# 定义基于物品的协同过滤算法类
class ItemBasedCF:
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
        # 读取文件，并生成用户-物品的评分表和测试集
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


    # 物品间相似度
    def ItemSimilarity(self):
        # 建立物品-物品的共现矩阵
        C = dict()  # 物品-物品的共现矩阵
        N = dict()  # 物品被多少个不同用户购买

        # 遍历训练数据，获得用户对有过行为的物品
        for user, items in self.train.items():
            # 遍历该用户每件物品项
            for i in items.keys():
                # 该物品被用户购买计数加1
                N.setdefault(i, 0)
                N[i] += 1
                # 物品-物品的共现矩阵数据加1
                C.setdefault(i, {})
                # 遍历该用户每件物品项
                for j in items.keys():
                    # 若该项为当前物品，跳过
                    if i == j: continue
                    # 同一个用户下，其他物品项
                    # 遍历到其他不同物品则加1
                    # 初始化为0
                    C[i].setdefault(j, 0)
                    # 加1
                    C[i][j] += 1

                    # 计算相似度矩阵
                    # 计算物品-物品相似度，余弦相似度
        self.W = dict()
        # 遍历物品-物品共现矩阵的所有项，
        # 每行物品、该行下的其他物品
        for i, related_items in C.items():
            # 存放物品间相似度
            self.W.setdefault(i, {})
            # 遍历其他每一个物品及对应的同现矩阵的值，即分子部分
            for j, cij in related_items.items():
                # 余弦相似度
                self.W[i][j] = cij / (math.sqrt(N[i] * N[j]))
                # 返回物品相似度
        return self.W


    # 给用户user推荐，前K个相关用户喜欢的，
    # 用户user未产生过行为的物品
    # 默认3个用户，推荐10个物品
    def Recommend(self, user, K=3, N=10):
        # 用户user对物品的偏好值
        rank = dict()
        # 用户user产生过行为的物品项item和评分
        action_item = self.train[user]

        # 找用户user产生过行为的物品item，
        # 与物品item按相似度从大到小进行排列
        # 取与物品item相似度最大的K个物品
        for item, score in action_item.items():
            # 遍历与物品item最相似的前K个物品，获得这些物品及相似分数
            for j, wj in sorted(self.W[item].items(), key=lambda x: x[1], reverse=True)[0:K]:
                # 若该物品当前物品，跳过
                if j in action_item.keys():
                    continue
                # 计算用户user对物品i的偏好值
                # 初始化该值为0
                rank.setdefault(j, 0)
                # 通过与其相似物品对物品i的偏好值相乘并相加
                rank[j] += score * wj
                # 按评分值大小，为用户user推荐结果的取前N个物品


        return dict(sorted(rank.items(), key=lambda x: x[1], reverse=True)[0:N])

if __name__ == '__main__':
    cf = ItemBasedCF('u.data', 'u.data')
    cf.ItemSimilarity()
    print(cf.Recommend('3'))


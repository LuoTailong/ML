# coding:utf-8
import math
# 计算物品之间评分差的平均值，输入如下
# 物品-用户评分数据items
# 用户-物品评分数据users
# 存放平均分字典类型数据
def buildAverageDiffs(items, users, averages):
    # 遍历每条物品-用户评分数据
    for itemId in items:
        ##遍历每条其他物品-用户评分数据
        for otherItemId in items:
            # 物品间的评分偏差
            average = 0
            # 两件物品均评过分的用户数
            userRatingPairCount = 0
            # 若为不同的物品项
            if itemId != otherItemId:
                # 遍历每条用户-物品评分数据
                for userId in users:
                    # 每条数据为用户对物品的评分
                    userRatings = users[userId]
                    # 当前物品项在用户的评分数据中，且用户也对其他物品有评分
                    if itemId in userRatings and otherItemId in userRatings:
                        # 两件物品均评过分的用户数加1
                        userRatingPairCount += 1
                        # 评分偏差为每项当前物品评分-其他物品评分求和
                        average += (userRatings[otherItemId] - userRatings[itemId])
                        # 物品间的评分偏差等于评分偏差和/两件物品均评过分的用户数
                averages[(itemId ,otherItemId)] = average / userRatingPairCount


# 推荐评分，输入如下
# 用户-物品评分数据users
# 物品-用户评分数据items
# 物品间的评分偏差
# 推荐用户targetUserId
# 推荐物品targetItemId
def suggestedRating(users, items, averages, targetUserId, targetItemId):
    # 预测评分分母
    runningRatingCount = 0
    # 预测评分分子
    weightedRatingTotal = 0.0

    # 遍历需要推荐的用户targetUserId对有过评分的物品
    for i in users[targetUserId]:
        # 保存当前物品与要推荐物品targetItemId，共同评分用户数
        ratingCount = usersWhoRatedBoth(users, i, targetItemId)
        # 分子
        weightedRatingTotal += (users[targetUserId][i] - averages[(targetItemId, i)])* ratingCount
    # 分母
    runningRatingCount += ratingCount
    # 返回预测评分
    return weightedRatingTotal / runningRatingCount


# 物品itemId1与itemId2共同有多少用户评分
def usersWhoRatedBoth(users, itemId1, itemId2):
    count = 0
    # 用户-物品评分数据users
    for userId in users:
        # 用户对物品itemId1与itemId2都有过评分则计数值加1
        if itemId1 in users[userId] and itemId2 in users[userId]:
            # 加1
            count += 1
            # 返回itemId1与itemId2共同评分用户数
    return count

if __name__ == '__main__':
    items = {'A': {1 :5, 2 :3},
             'B': {1 :3, 2 :4, 3 :2},
             'C': {1 :2, 3 :5}}

    users = {1: {'A' :5, 'B' :3, 'C' :2},
             2: {'A' :3, 'B' :4},
             3: {'B' :2, 'C' :5}}

    # 物品间评分偏差初始化
    averages = {}
# 计算物品之间评分差的平均值
buildAverageDiffs(items, users, averages)

# 输出：总共的物品项、用户数
print({'ItemCount': len(items), 'UserCount': len(users)} )
print("Guess that user A will rate item 3= " +
      str(suggestedRating(users ,items, averages, 3, 'A')))






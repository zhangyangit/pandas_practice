# -*- coding: utf-8 -*-
__author__ = 'Morgan'

'''
python Pandas Practice| 01-数据生成之道
'''
## 导入数据
import numpy as np
import pandas as pd
import os
## 读取原始文件

def read_csv(path):
    # 定义返回值
    fd = None
    # 参数检测
    if os.path.exists(path) != True:
        return fd
    fpath = path
    # 出错处理
    try:
        fd = pd.read_csv(fpath)
        print('Success open path :' + fpath)
        print(fd.head(2))
    except IOError:
        print('Failure open path :'+fpath)
    finally:
        print('open path : ' + fpath)
    return fd

# def merge_data():

# path = "../data/ml-latest-small/ratings_1.csv"
# fd = read_csv(path)
# print(fd.head(10))
# (1) 读取两个用户评分数据文件
ratings_1 = pd.read_csv("../data/ml-latest-small/ratings_1.csv")
print(ratings_1.head(2))
ratings_2 = pd.read_csv("../data/ml-latest-small/ratings_2.csv")
print(ratings_2.head(2))
# (2) 读取电影文件
movies = pd.read_csv("../data/ml-latest-small/movies.csv")
print(movies.head(2))
# (3) 读取电影链接文件
links = pd.read_csv("../data/ml-latest-small/links.csv")
print(links.head(2))

## 合并数据
# (1) 合并用户评分数据(拼接)
# 由于原始数据集本身不存在重复的用户评分数据，因此用户数据直接合并即可
print(len(ratings_1))
print(len(ratings_2))
ratings_info = ratings_1.append(ratings_2, ignore_index=True)
print(ratings_info.shape)
print(ratings_info.tail(5))
# (2) 合并电影信息 (关联)
# movie and link 的交叉点集中在 movieid
print(len(movies.movieId.unique()))
print(len(links.movieId.unique()))
print(len(np.intersect1d(movies.movieId.unique(), links.movieId.unique())))
movies_info = movies.merge(links, how='inner', on='movieId')
print(movies_info.shape)
print(movies_info.head())
# (3) 合并用户和电影信息 (关联)
# 用户与电影信息之间的关联在 movieId
print(len(ratings_info.movieId.unique()))
print(len(movies_info.movieId.unique()))
print(len(np.intersect1d(ratings_info.movieId.unique(), movies_info.movieId.unique())))
data = ratings_info.merge(movies_info, how='left', on='movieId')
print(data.shape)
print(data.head())

## 保存数据
data.to_csv("../data/ml-latest-small/data.csv")
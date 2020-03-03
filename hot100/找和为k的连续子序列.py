# -*- coding: utf-8 -*-
'''
leetcode 56
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
'''
def subarr(nums,k):
    sumarrj=0
    count=0
    dicsumarr={0:1}
    for j in nums:
        sumarrj+=j
        if sumarrj-k in dicsumarr:
            count+=dicsumarr[sumarrj-k]
        if sumarrj not in dicsumarr:
            dicsumarr[sumarrj]=1
        else:
            dicsumarr[sumarrj]+=1            
    return count
'''
解法2
#if else 可以浓缩为:
def subarr(nums,k):
    sumarrj=0
    count=0
    dicsumarr={0:1}
    for j in nums:
        sumarrj+=j
        count+=dicsumarr.get(sumarrj-k,0)
        dicsumarr[sumarrj]=dicsumarr.get(sumarrj,0)+1  
    return count
'''

nums=[1,1,1]
k=2
res=subarr(nums,k)
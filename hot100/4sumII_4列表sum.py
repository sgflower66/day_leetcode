# -*- coding: utf-8 -*-

#leetcode 454

'''
给定四个包含整数的数组列表 A , B , C , D ,
计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。

时间复杂度：O(n2)+O(n2)=O(n2)
空间复杂度：O(n2)
'''

def FourSum2(A,B,C,D):
    hashAB={}
    res=0
    for a in A:
        for b in B:
            ab=a+b
            if ab in hashAB:
                hashAB[ab]+=1
            else:
                hashAB[ab]=1
    for c in C:
        for d in D:
            cd=c+d
            if -cd in hashAB:
                res+=hashAB[-cd]
    return res
'''
利用库函数法2
'''
import collections
def FourSum22(A,B,C,D):
    hashAB=collections.Counter(a+b for a in A for b in B)
    res=sum(hashAB.get(-c-d,0) for c in C for d in D)
    return res

A,B,C,D=[1,2],[-2,-1],[-1,2],[0,2]               
res=FourSum2(A,B,C,D)
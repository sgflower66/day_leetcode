'''
two sum

#使用哈希表
#O(n),O(n)

nums=[2,9,3,7]
target=11

dict.get(key) key存在返回val,不存在返回None

hashmap={}
for index,num in enumerate(nums):
    if hashmap.get(target-num) is not None:
        return [hashmap.get(target-num),index]
    hashmap[num]=index


'''

'''
three sum
时间O(n2),空间O(1)
nums=[2,9,3,7]
target=0


nums=[-1,0,1,2,-1,-4]
nums=[0,0,0]
n=len(nums)
if n<3 or not nums:
    return []
res=[]
nums=sorted(nums)
for i in range(n-2):#range(n)
    L=i+1
    R=n-1
    if nums[n-1]<0:
        return res
    if nums[i]>0:
        return res
    if i>0 and nums[i]==nums[i-1]:#在while之外11#nums() 去重
        continue

    while L<R:

对于这种边界情况少的会较低效率
#        #min
#        if nums[i]+nums[L]+nums[L+1]>0:
#            break
#        elif nums[i]+nums[L]+nums[L+1]==0:
#            res.append([nums[i],nums[L],nums[L+1]])
#            break
#        
#        #max
#        if nums[i]+nums[R]+nums[R-1]<0:
#            break
#        elif nums[i]+nums[R]+nums[R-1]==0:
#            res.append([nums[i],nums[R],nums[R-1]])
#            break  

            
        if nums[i]+nums[L]+nums[R]==0:#nums()
            res.append([nums[i],nums[L],nums[R]])
            while (L<R and nums[L+1]==nums[L] ):#nums(),L<R防止后面再进行加减1越界,L<R必须放在前面
                L=L+1
            while (L<R and nums[R-1]==nums[R]) :#nums()
                R=R-1

            L=L+1# forget可能越界但是没有Nums[L],所以无所谓
            R=R-1# forget
        elif nums[i]+nums[L]+nums[R]>0:
            R=R-1
        else:
            L=L+1
return res

'''
'''
three sum
找三个数的和最接近目标数，唯一解
时间O(n2),空间O(1)
总时间复杂度：O(nlogn) + O(n^2) = O(n^2)
def threeSumClosest( nums,target) :
    n=len(nums)
    if n<3 or not nums:
        return []
    #res=[]
    nums.sort()
    res=nums[0]+nums[1]+nums[n-1]
    for i in range(n-2):
        L=i+1
        R=n-1

        if i>0 and nums[i]==nums[i-1]:
            continue
    #    val=abs(nums[i]+nums[L]+nums[R]-target)

        while L<R:  
            #优化边界，即时止损
            if nums[i]+nums[L]+nums[L+1]>target:
                if (nums[i]+nums[L]+nums[L+1]-target) <abs(res-target):
                    res=nums[i]+nums[L]+nums[L+1]                    
                break
            elif nums[i]+nums[L]+nums[L+1]==target:
                return target
                 
            if nums[i]+nums[R]+nums[R-1]<target:
                if (target-(nums[i]+nums[R]+nums[R-1]))<abs(res-target):
                    res=nums[i]+nums[R]+nums[R-1]
                break
            elif nums[i]+nums[R]+nums[R-1]==target:
                return target
             #优化边界，即时止损

            if abs(nums[i]+nums[L]+nums[R]-target )<abs(res-target):#放在while里面防止越界
                res=nums[i]+nums[L]+nums[R]
            if nums[i]+nums[L]+nums[R]<target:
#                    if (target-(nums[i]+nums[L]+nums[R]) )<abs(target-res):
#                        res=nums[i]+nums[L]+nums[R]
                L=L+1
                while L<R and nums[L]==nums[L-1]:#去重非解的重复值：+1之后和不变，没有用，所以继续+1
                    L=L+1                
            elif nums[i]+nums[L]+nums[R]==target:
#                    res=target
                return target
            else:
#                    if (nums[i]+nums[L]+nums[R]-target )<abs(target-res):
#                        res=nums[i]+nums[L]+nums[R]
                R=R-1
                while L<R and nums[R]==nums[R+1]:
                    R=R-1                
    return res

nums=[1,1,1,0]
target=100
resu=threeSumClosest(nums,target)    

'''   
        
    
    
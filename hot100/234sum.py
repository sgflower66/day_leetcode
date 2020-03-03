
#leetcode 1,15,16,18
'''

two sum

#使用哈希表
#O(n),O(n)
'''

def twoSum(nums, target):
    hashmap={}
    for index,num in enumerate(nums):
        if hashmap.get(target-num) is not None:
            return [hashmap.get(target-num),index]
        hashmap[num]=index

nums=[2,9,3,7]
target=11
#dict.get(key) key存在返回val,不存在返回None
res=twoSum(nums, target)

'''
three sum
时间O(n2),空间O(1)
'''

def threeSum(nums):
    n=len(nums)
    if n<3 or not nums:
        return []
    res=[]
    nums=sorted(nums)
    for i in range(n-2):#range(n)
        L=i+1
        R=n-1
       
        if i>0 and nums[i]==nums[i-1]:#在while之外11#nums() 去重
            continue
 #仅仅针对leetcode本题解得情况，边界情况少，所以替代了一下边界判断 begin      
        if nums[n-1]<0:
            return res
        if nums[i]>0:
            return res
 #仅仅针对leetcode本题解得情况，边界情况少，所以替代了一下边界判断 end 
 
        while L<R:

#        对于这种对于这种多解的，边界情况少的会较低效率
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

nums=[2,9,3,7]
target=0

nums=[-1,0,1,2,-1,-4]
nums=[0,0,0]
res=threeSum(nums) 

'''
three sum closet
找三个数的和最接近目标数，唯一解
时间O(n2),空间O(1)
总时间复杂度：O(nlogn) + O(n^2) = O(n^2)
'''
def threeSumClosest( nums,target) :
    n=len(nums)
    if n<3 or not nums:
        return []
    nums.sort()
    res=nums[0]+nums[1]+nums[n-1]
    for i in range(n-2):
        L=i+1
        R=n-1

        if i>0 and nums[i]==nums[i-1]:
            continue

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
                L=L+1
                while L<R and nums[L]==nums[L-1]:#去重非解的重复值：+1之后和不变，没有用，所以继续+1
                    L=L+1                
            elif nums[i]+nums[L]+nums[R]==target:
                return target
            else:

                R=R-1
                while L<R and nums[R]==nums[R+1]:
                    R=R-1                
    return res

nums=[1,1,1,0]
target=100
res=threeSumClosest(nums,target)    
  
'''
4 sum = target,非重复解
O(n^3),O(1)
'''
def FourSum(nums,target):
    n=len(nums)
    if len(nums)<4 or not nums:
        return []
    res=[]
    nums.sort()
    for i in range(n-3):
 #仅仅针对leetcode本题解得情况，边界情况少，所以替代了一下边界判断 begin      
        #min 中断
        if nums[i]+3*nums[i+1]>target:#不能等于，比如【0,0,0,0】
            break
        #max 继续
        if nums[i]+3*nums[-1]<target:
            #while i<n-4 and nums[i]==nums[i+1]:i=i+1#加速-------加不加无所谓，因为太针对性了
            continue
 #仅仅针对leetcode本题解得情况，边界情况少，所以替代了一下边界判断 end   
        if i>0 and nums[i]==nums[i-1]:#去重
            continue
      
        for j in range(i+1,n-2):
            L=j+1
            R=n-1  
 #仅仅针对leetcode本题解得情况，边界情况少，所以替代了一下边界判断 begin      
            #min 中断
            #if nums[i]+nums[j]+nums[L]+nums[L+1]==target:
                #res.append([nums[i],nums[j],nums[L],nums[L+1]])#绝对不能乱加，可能造成重复
                 #break
            if nums[i]+nums[j]+nums[L]+nums[L+1]>target:
                break
            #max 继续
            #if nums[i]+nums[j]+nums[R]+nums[R-1]==target:
                #res.append([nums[i],nums[j],nums[R],nums[R-1]])#绝对不能乱加，可能造成重复
                #continue
            if nums[i]+nums[j]+nums[R]+nums[R-1]<target:
                continue
 #仅仅针对leetcode本题解得情况，边界情况少，所以替代了一下边界判断 end              
            if j-i>1 and nums[j]==nums[j-1]:#去重,但是ij可以重复
                continue
           
            while L<R:
                #对于这种多解的，边界情况少的会较低效率-------------
#                #min
#                if nums[i]+nums[j]+nums[L]+nums[L+1]==target:
#                    res.append([nums[i],nums[j],nums[L],nums[L+1]])
#                    break
#                elif nums[i]+nums[j]+nums[L]+nums[L+1]>target:
#                    break
#                #max
#                if nums[i]+nums[j]+nums[R]+nums[R-1]==target:
#                    res.append([nums[i],nums[j],nums[R],nums[R-1]])
#                    break
#                elif nums[i]+nums[j]+nums[R]+nums[R-1]<target:
#                    break
                #对于这种边界情况少的会较低效率-------------                    
                if nums[i]+nums[j]+nums[L]+nums[R]==target:
                    res.append([nums[i],nums[j],nums[L],nums[R]])
                    while (L<R and nums[L+1]==nums[L]):
                        L=L+1
                    while (L<R and nums[R-1]==nums[R]):
                        R=R-1
                    L=L+1
                    R=R-1
                elif nums[i]+nums[j]+nums[L]+nums[R]<target:
                    L=L+1
                else:
                    R=R-1
    return res

     
nums=[-3,-3,-3,-3,0,1,1,2,3]
target=100     
res=FourSum(nums,target)                        
    
    
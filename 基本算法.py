
'''顺序查找 O(n)'''
def ord_search(lst,value):
    for i in range(len(lst)):
        if lst[i]==value:
            print('list[{0}]=={1}'.format(i,value))
            return i
    else:
        print('no found')


'''二分查找(仅适用于顺序表) O(logn)'''
def bin_search(lst,value):
    low=0
    height=len(lst)-1
    
    while(low<=height):
        middle=int((low+height)/2)
        print(low,middle,height)
        if lst[middle]==value:
            print('list[{0}]=={1}'.format(middle,value))
            return(middle)
        elif lst[middle]>value:
            height=middle-1
        else:
            low=middle+1


'''冒泡 O(n²) 每一次把最大的放后面'''
def Bubble(lst):
    height=len(lst)-1
    while height>0:
        for i in range(0,height):
            if lst[i]>lst[i+1]:
                lst[i],lst[i+1]=lst[i+1],lst[i]
        height-=1
    return(lst)

'''选择排序 O(n²)'''
def choice1(lst):
    for i in range(len(lst)):
        min_=i
        for j in range(i+1,len(lst)):
            if lst[min_]>lst[j]:
                min_=j
        lst[i],lst[min_]=lst[min_],lst[i]
    return(lst)

'''插入排序 O(n²)'''
def Insert(lst):
    for i in range(1,len(lst)):
        judge=lst[i]
        for j in range(i-1,-1,-1):
            if judge<lst[j]:
                lst[j+1]=lst[j]
                lst[j]=judge
            else:break
    return lst

lst1 = [5,1,3,7,8,6,2,0,4,9]
'''快速排序   最好O(nlogn) 最坏O(n²)'''
def quick_sort(lst,left,right):
    if left>=right:
        return
    key=lst[left]
    while left<right:
        while left<right and lst[right]>key:
            right-=1
        lst[left]=lst[right]
        while left<right and lst[left]<=key:
            left+=1
        lst[right]=lst[left]
    lst[right]=key
    quick_sort(lst,0,right-1)
    quick_sort(lst,right+1,-1)









        








lists = [7,5,9,1,8,3,4,2,6]
n = len(lists)          #個數

#選擇排序 找出最大值放最後
def selection_sort(lists,n):
    for j in range(n-1,0,-1):    #j表示還需進行的次數也是最後值的索引，第一次進行時最大值應該放在最後j的位置，第二次第二大值應該放j-1位置
        maxs = lists[0]          #假設最大值是第一個數值
        post = 0                 #post記錄最大值所在的索引
        for i in range(j+1):
            if lists[i]>maxs:       #當發現更大的值時
                maxs = lists[i]     #保留更大的值
                post = i              #並記錄位置
        lists[post],lists[j] = lists[j],lists[post]      #最大值放到最後
    return lists
print(selection_sort(lists,n))
#介紹網站 https://www.itread01.com/content/1548402668.html
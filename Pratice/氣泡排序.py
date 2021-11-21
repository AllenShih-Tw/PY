lists = [7,5,9,1,8,3,4,2,6]
n = len(lists)          #個數
#氣泡排序 從左到右兩個值做比較
def bubble_sort(lists,n):
    for j in range(n,0,-1):     #j剩餘沒得出最大值的個數
        for i in range(j-1):    #從左到右開始比較i為索引
            if lists[i]>lists[i+1]:
                lists[i],lists[i+1]=lists[i+1],lists[i]   #如果前一個數大於後一個數 兩個數位置對調
    return lists
print(lists)
print(bubble_sort(lists,n))

#介紹網站 https://www.itread01.com/content/1548402668.html
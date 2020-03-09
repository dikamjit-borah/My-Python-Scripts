d5 = [2.5,1, 5.5 , 4,0]

def min(dataList):
    dataListNum = []
    dataListStr = []
    for i in dataList:
        if (type(i) == str):
            dataListStr.append(i)
        else:
            dataListNum.append(i)
    dataListStr.sort()
    dataListNum.sort()
    dataList = dataListNum + dataListStr
    print("Sorted List = " + str(dataList))
    return dataList[0]

def max(dataList):
    dataListNum = []
    dataListStr = []
    for i in dataList:
        if (type(i) == str):
            dataListStr.append(i)
        else:
            dataListNum.append(i)
    dataListStr.sort()
    dataListNum.sort()
    dataList = dataListNum + dataListStr
    return dataList[len(dataList)-1]
    
def mean(dataList):
    dataListNum = []
    dataListStr = []
    for i in dataList:
        if (type(i) == str):
            dataListStr.append(i)
        else:
            dataListNum.append(i)
    dataListStr.sort()
    dataListNum.sort()
    s = 0
    for i in dataListNum:
        s +=i
    
    return (s/(len(dataListNum)))


def median (dataList):
    dataListNum = []
    dataListStr = []
    for i in dataList:
        if (type(i) == str):
            dataListStr.append(i)
        else:
            dataListNum.append(i)
    dataListStr.sort()
    dataListNum.sort()
    dataList = dataListNum + dataListStr
    if(len(dataList)%2 == 0):
        return dataList[int(len(dataList)/2)-1], dataList[int(len(dataList)/2)]
    else:
        return dataList[int(len(dataList)/2)]

def getRange(dataList):
    dataListNum = []
    dataListStr = []
    for i in dataList:
        if (type(i) == str):
            dataListStr.append(i)
        else:
            dataListNum.append(i)
    dataListStr.sort()
    dataListNum.sort()
    dataList = dataListNum + dataListStr
    
    return abs(dataListNum[0] - dataListNum[len(dataListNum)-1])

def test1(di):
    if(len(di) == 0):
        print("For " + str(di))
        print("NO ELEMENTS IN LIST")
    elif(type(di)!=list):
        di_new = []
        for i in di:
            di_new.append(ord(i))
        print(di_new)
        test1(di_new)
    else:
        print("For " + str(di))
        print("Minimum = " + str(min(di)))
        print("Maximum = " + str(max(di)))
        print("Mean = " + str(mean(di)))
        print("Median = " + str(median(di)))
        print("getRange = " + str(getRange(di)))
    
  
    
def main(): 
    d1 = [37,32,46,28,37,41,31]
    d2 = [2.5, 5.3, 6.1, 1.34, 3.3, 5, 25, 4.3, 6.0, 0.5]
    d3 = []
    d4 = "abc"
    d5 = [2.5, "abc", 4]
    
    test1(d1)
    test1(d2)
    test1(d3)
    test1(d4)
    test1(d5))
    
  
  
if __name__=="__main__": 
    main() 
    
    
            
            

#함수배열.py 

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y
#list에 함수 주소를 전달 
functionList = [add, sub, mul, div, add, add, sub, mul, add]
#함수호출
print( functionList[0](4,5) )

for func in functionList:
    print( func(5,3))

for i in range(0, len(functionList)):
    print( functionList[i](6,2) )

rList = [add(5,3),add(15,3),add(2,3),add(6,3)]
print(rList)

funcDict = dict()

funcDict["add"]=add 
funcDict["sub"]=sub 
funcDict["mul"]=mul 
funcDict["div"]=div 

fname = input("함수이름 : ")
x = int(input("x = "))
y = int(input("y = "))

print ( funcDict[fname](x, y) )











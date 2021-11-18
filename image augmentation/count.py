import os

#사용전 클래스 확인필수!
classpaths = ['beach','bigcity','bridge','cliff','harbor','lighthouse','mountain','mudflat','waterfall']

countFiles=[]
differ_fromMax=[]


#경로의 파일갯수 읽어들이기
for classpath in classpaths:
    #사용전 경로확인 필수!
    path = '../Train_6컬러+흑백/'+classpath
    
    countFiles.append(len(os.listdir(path)))

print("디렉토리  :  파일갯수  //  오차")
for i in range(len(classpaths)):
    print(classpaths[i], ":",countFiles[i], "개 // ", (max(countFiles)-countFiles[i]))
print("모든 파일 :",sum(countFiles))


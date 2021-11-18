from PIL import Image
import os

#사용 시 클래스 확인필수!
classpaths = ['beach','bigcity','bridge','cliff','harbor','lighthouse','mountain','mudflat','waterfall']

countFiles=[]
#사용 시 경로확인 필수 !
basepath = '../Train_4데이터량일치/'

for classpath in classpaths:
    
    path = basepath+classpath
    
    countFiles.append(len(os.listdir(path)))

#작업 전 파일현황
print("디렉토리  :  파일갯수  //  오차")
for i in range(len(classpaths)):
    print(classpaths[i], ":",countFiles[i], "개 // ", (max(countFiles)-countFiles[i]))

for i in range(len(countFiles)):
    
    path = basepath+classpaths[i]+'/'
    file_names = os.listdir(path)

    for n in range(len(file_names)): #파일이름들 확장자명과 분리
        file_names[n] = os.path.splitext(file_names[n])[0]
    
    differ = max(countFiles)-countFiles[i]        #최대값과 현 디렉토리의 갯수 차이
    
    if(differ == 0):                                                            #가장많은 디렉토리 처리
        print(classpath,"가 최댓값을 가진 디렉토리 입니다.")
        continue
    
    elif(differ > (countFiles[i]*2)):                                           #3배이상 적은 디렉토리 처리
        for a in range(countFiles[i]):
            img = Image.open((path+file_names[a]+'.jpg'))               #이미지 열기
            
            flipImg = img.transpose(Image.FLIP_LEFT_RIGHT)              #좌우반전
            flipImg.save((path+file_names[a]+'FL.jpg'))                 #결과저장
            flipImg = img.transpose(Image.FLIP_TOP_BOTTOM)              #상하반전
            flipImg.save((path+file_names[a]+'FTB.jpg'))                #결과저장 
            
    elif(differ > countFiles[i]):                                               #2배이상 적은 디렉토리 처리
        for b in range(countFiles[i]):
            img = Image.open((path+file_names[b]+'.jpg'))               #이미지 열기
            
            flipImg = img.transpose(Image.FLIP_LEFT_RIGHT)              #좌우반전
            flipImg.save((path+file_names[b]+'FL.jpg'))                 #결과저장
        for c in range(differ-countFiles[i]):
            img = Image.open((path+file_names[c]+'.jpg'))               #이미지 열기

            flipImg = img.transpose(Image.FLIP_TOP_BOTTOM)              #상하반전
            flipImg.save( (path+file_names[c]+'FTB.jpg'))               #결과저장
            
    else:                                                                       #2배이하로 적은 디렉토리 처리
        for d in range(differ):
            img = Image.open((path+file_names[d]+'.jpg'))               #이미지 열기
            
            flipImg = img.transpose(Image.FLIP_LEFT_RIGHT)              #좌우반전
            flipImg.save((path+file_names[d]+'FL.jpg'))                 #결과저장

#작업 후 파일현황
countFiles=[]

for classpath in classpaths:
    
    path = basepath+classpath
    
    countFiles.append(len(os.listdir(path)))

#작업 전 파일현황
print("\n---실행 후\n디렉토리  :  파일갯수  //  오차")
for i in range(len(classpaths)):
    print(classpaths[i], ":",countFiles[i], "개 // ", (max(countFiles)-countFiles[i]))

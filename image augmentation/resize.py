from PIL import Image
import numpy as np

#사용시 클래스 확인필수!
classpaths = ['beach','bigcity','bridge','cliff','harbor','lighthouse','mountain','mudflat','waterfall']

#변수
size_x = []
size_y = []

for classpath in classpaths:  #평균사이즈 계산

    #전체 파일 확인
    imagenumber=1
    while(True):
        try:
            #사용시 경로확인 필수!
            path = '../Train_3사이즈일치/'+classpath+'/'+str(imagenumber)+'.jpg'
            img = Image.open(path)
        
            size_x.append(img.size[0])
            size_y.append(img.size[1])
        except FileNotFoundError:
            break
        imagenumber+=1
    
set_x = int(np.mean(size_x))
set_y = int(np.mean(size_y))
    
print("set_x :",set_x,", set_y :", set_y)

#에러갯수 계산함수
def Checkerror(label_x, label_y):
    errors_x = 0
    errors_y = 0

    for i in range(len(label_x)):
        if(label_x[i] != set_x):
            errors_x+=1
        if(label_y[i] != set_y):
            errors_y+=1
            
    return print("Xerrors :",errors_x,", Yerrors :", errors_y)

#전체 파일크기 변경
for classpath in classpaths:
    imagenumber=1
    while(True):
        try :
            path = '../Train_3사이즈일치/'+classpath+'/'+str(imagenumber)+'.jpg'
            img = Image.open(path)
            
            img_resize = img.resize((set_x, set_y))
            img_resize.save(path)
        except FileNotFoundError :
            break
        imagenumber+=1

Checkerror(size_x, size_y)

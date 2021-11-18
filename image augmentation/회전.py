from PIL import Image
 
classpaths = ['0백사장', '1자갈해변', '2해안절벽', '3갯벌', '4다도해', '5등대', '6부두', '7마리나항',
             '8해안도로', '9해안둘레길', '10방파제', '11대교']
path = '../Train_4데이터량일치/bigcity/'
imagenumber=1
while(True):
    try:
        #이미지 반전 후 저장
        img = Image.open((path+str(imagenumber)+'.jpg'))    #이미지 열기
            
        flipImg = img.transpose(Image.FLIP_LEFT_RIGHT)        #좌우반전
        flipImg.save( (path+str(imagenumber)+'FL.jpg'))       #결과저장
        
        flipImg = img.transpose(Image.FLIP_TOP_BOTTOM)      #상하반전
        flipImg.save( (path+str(imagenumber)+'FTB.jpg'))    #결과저장
    except FileNotFoundError:
        break
    imagenumber+=1

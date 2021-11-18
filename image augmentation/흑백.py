from PIL import Image
import os
 
classpaths = ['beach','bigcity','bridge','cliff','harbor','lighthouse','mountain','mudflat','waterfall']


for classpath in classpaths:
    
    #사용시 경로확인 필수!
    target_path = '../Train_4데이터량일치/'+classpath+'/'                        #흑백으로 바꿀 디렉토리
    save_path = '../Train_5모두흑백/'+classpath+'/'                             #흑백으로 저장할 디렉토리
    
    file_names = os.listdir(target_path)                    #디렉토리 내 파일이름들 검색
    
    for file_name in file_names:
        
        img = Image.open(target_path+file_name)      #이미지 열기
        imggray = img.convert('L')
        imggray.save(save_path+'B'+file_name)        #흑백이미지 저장
        

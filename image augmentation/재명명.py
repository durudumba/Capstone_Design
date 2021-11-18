import os

"""
#사용전 클래스 확인필수!
classpaths = ['0백사장', '1자갈해변', '2해안절벽', '3갯벌', '4다도해', '5등대', '6항구', '7방파제', '8대교']

for classpath in classpaths:
    
    #사용시 경로확인 필수!
    path = '../학습데이터_6정제2/'+classpath
    file_names = os.listdir(path)
    
    imagenumber=1
    
    for name in file_names:
        
        src = os.path.join(path, name)
        dst = str(imagenumber) + '.jpg'
        dst = os.path.join(path, dst)
        os.rename(src, dst)
        imagenumber += 1
"""
#단편
path = '../Train_4데이터량일치/_garbage'
file_names = os.listdir(path)

imagenumber = 1
for name in file_names:
        
    src = os.path.join(path, name)
    dst = str(imagenumber) + '.jpg'
    dst = os.path.join(path, dst)
    os.rename(src, dst)
    imagenumber += 1
        

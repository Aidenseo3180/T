import os
import subprocess

def check_dir(self, value):
    #이 chdir()에는 이제 우리가 browse한 주소를 넣을거임
    #os.chdir(r'C:\Users\minwo\Pictures\A\ffmpeg-20200312-675bb1f-win64-static\bin')
    
    o_path = os.getcwd()    #현재 directory 얻어옴
    try:
        os.chdir(value) #들어온 디렉토리로 바꿈
    except OSError:     #만약 value가 아무것도 안들어오면(그냥 browse안하고 check만 누르면) OSError가 나옴. 이걸 잡음
        os.chdir(o_path)    #그래서 original 디렉토리로 다시 바꿈
        return          #그리고 리턴 함 (false를 리턴, status가 빨간색으로 됨)

    file_list = ['ffmpeg.exe','ffplay.exe','ffprobe.exe']
    exist_list = [] #여기에 true, false 가 들어감
    for f in file_list:
        exist_list.append(os.path.exists(f))
    if all(exist_list):  #만약 모든 exist_list의 element들이 true면
        return 'True'
    else:
        os.chdir(o_path)    #아니면 다시 원래 directory로 돌아옴
        return 'False'

import os
import subprocess

def check_dir(self, value):
    #이 chdir()에는 이제 우리가 browse한 주소를 넣을거임
    #os.chdir(r'C:\Users\minwo\Pictures\A\ffmpeg-20200312-675bb1f-win64-static\bin')
    #path = os.getcwd()

    os.chdir(value)

    file_list = ['ffmpeg.exe','ffplay.exe','ffprobe.exe']
    exist_list = [] #여기에 true, false 가 들어감
    for f in file_list:
        exist_list.append(os.path.exists(f))
    if all(exist_list):  #만약 모든 exist_list의 element들이 true면
        os.chdir(r'C:\Users\minwo\Documents\Code\twitch_ffpng_downloader')
        return 'True'
    else:
        return 'False'

import os
import subprocess

def check_dir(self, value):

    o_path = os.getcwd()
    try:
        os.chdir(value)     
    except OSError:         
        os.chdir(o_path)    
        return

    file_list = ['ffmpeg.exe','ffplay.exe','ffprobe.exe']
    exist_list = []
    for f in file_list:
        exist_list.append(os.path.exists(f))
    if all(exist_list):
        return 'True'
    else:
        os.chdir(o_path)
        return 'False'

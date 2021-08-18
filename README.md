# vid-downloader
About 
-------
This is a PyQt5 program that allows the user to download twitch videos 
In order to use, please read the directions carefully.

*Currently under maintenance and developments, but still can be used without having difficulties*  
**This is made for a practice purpose. I will not take responsibility of the consequences from misusing my codes**

How to Use
-------------
1. Download ffmpeg from the store, and save to the directory
2. Go to Twitch, find the video that you want to download, press left-click and **copy image link**
3. Run the exe, paste the image link and browse the ffmpeg from the computer
4. Press Confirm and Download

*I didn't add option to change the name of the video, so please double check if the chosen directory doesn't contain "1111.mp4" (this is the default name of the video), and make sure to change the name of the video file once you download.*

Founded Errors
------------
* Error with multi-threading
  * When downloading, the progress bar doesn't work
  * sub process - communicate blocks other threadings from running. So the progress bar cannot be ran at the same time.
* Byte Error
  * stdout cannot be shown in the download progress textbox due to the byte error

IF
-----
* If it's not working, copy&paste the converted link and modify it. Then, paste that link to the cmd that is connected to ffmpeg.exe directory


Links
---
* How to Download Ffmpeg : [ffmpeg](https://www.wikihow.com/Install-FFmpeg-on-Windows)

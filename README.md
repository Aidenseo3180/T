# twitch-vid-downloader
About 
-------
This is a PyQt5 program that allows the user to download twitch videos.  
The video will be downloaded in 1080p quality.
Tested from Windows OS, haven't tested with Linux OS

In order to use, please read **How to Use**.

*Currently under maintenance and developments, but still can be used without having difficulties.*  

*If the video contains copyright issues (the muted part, shown as red bar), the downloader ignores that part, and continues to download.*    
*Therefore, the user won't get to see those parts.*

**This is made for a practice purpose. I will not take any responsibilities of misusing my codes.**

How to Use
-------------
1. Download ffmpeg from the store, and save to the directory.
2. Go to Twitch, find the video that you want to download, right-click on top of the video, and **copy image link**.
3. Run the exe, paste the image link and browse the ffmpeg from the computer.
4. Press Confirm and Download.

Founded Errors
------------
* Error with multi-threading
  * When downloading, the progress bar doesn't work.
  * sub process - communicate blocks other threadings from running. So the progress bar cannot be ran at the same time.
* Byte Error
  * stdout cannot be shown in the download progress textbox due to the byte error.
* Theme Error
  * Color issue with QLabel (title of program) in the beginning.

IF
-----
* If it's not working, copy&paste the converted link and modify it. Then, paste that link to the cmd that is connected to ffmpeg.exe directory.

Todos
----
- [X] No Video Name Error (No Overlapping)
- [ ] Fix Thread Bug
- [ ] Show Download Progress (output of what's going on inside)
- [X] Add Dark Theme
- [ ] Add browsing function in another tab

Links
---
* How to Download Ffmpeg : [ffmpeg](https://www.wikihow.com/Install-FFmpeg-on-Windows)

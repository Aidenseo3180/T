# twitch-vid-downloader
About 
-------
| Home Page                           | Start Page                          |
| ----------------------------------- | ----------------------------------- |
| ![Capture](https://github.com/Aidenseo3180/blog-web-application/assets/66958352/399f5523-3dee-4ca5-a061-b8f1b0baf1f6) | ![Image](https://github.com/Aidenseo3180/blog-web-application/assets/66958352/cadd10d9-182a-442e-ac67-051dee2b07c8) |

A PyQt5 program that allows the user to download twitch videos for a purpose of testing the viability of ffmpeg.
The video is downloaded in 1080p quality, tested in Windows 10 OS

In order to use, please read **How to Use**.

*No longer in the development, but still can be used without having difficulties as of 2021.*  

*If the video contains copyright issues (the muted part, shown as red bar in twitch), the downloader skips that section and continues to download.*

**Last Checked : 08/31/2021**

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
* Download ends in 1 sec  
  * when the given link is unavailable the download ends within a second (and says Done, instead of 'try again later')

IF
-----
* If it's not working, copy&paste the converted link and modify it. Then, paste that link to the cmd that is connected to ffmpeg.exe directory.

Todos
----
- [X] No Video Name Error (No Overlapping)
- [ ] Fix Thread Bug
- [ ] Show Download Progress (output of what's going on inside)
- [X] Add Dark Theme

Links
---
* How to Download Ffmpeg : [ffmpeg](https://www.wikihow.com/Install-FFmpeg-on-Windows)

# CrayTag

Want free software to resize all album covers in your mp3 music library? So did I! I searched for free software to do this in a batch operation and could only find overpriced software. So I made my program to resize all album covers for all music in my music library. No matter how large your music library is this program should handle the job. Best of all I am releasing this software for free! 

![CrayTag Wallpaper](https://user-images.githubusercontent.com/30564402/83311269-f2abcd80-a1cb-11ea-8a6a-f86f4a0e1b36.jpg)

This program was originally made to resize album covers. But it quickly turned into something larger, I added options to renumber mp3 files, resize external album covers, embedded album covers, and it will even alert you if album art (along with other data) is missing so you can correct the issue. There are options in the program to modify all the operations so it will do only what you want it too. There are several and I mean several things this program can do. It automates frivolous tasks and best of all its got a graphical interface so you don't need to run it in a command-line. 

![Capture](https://user-images.githubusercontent.com/30564402/83311341-2981e380-a1cc-11ea-846a-349a850e27ce.PNG)

I am releasing the raw python code so you can look over the code to verify its safety if you so desire. I have also compiled the program to run on Windows, so all you have to do is download the Windows executable file and run it like any other program. If you don't trust me that's fine, just download the source code, look it over to verify its safety, and compile it yourself. Or just run it as a regular Python file. 

## **CrayTag for Windows OS**

I have compiled CrayTag to run on Windows. There are two compiled versions of CrayTag. The first version is a standalone executable file where all files are stored in a single file. The second version is a zipped folder containing the program files and the CrayTag.exe file which can run on Windows also. The difference is that the single CrayTag.exe file takes longer to start up on Windows, while the one in the zipped folder starts up much faster because all files aren't compressed into a single file.

## ***Version One***

This version takes longer to launch, but the benefits are that all files are stored in a single executable file.

[Download the CrayTag.exe](https://github.com/Dalton-Overlin/CrayTag/blob/master/Windows%20Executables/CrayTag.exe)

## Instructions

Download CrayTag.exe and run it on a Windows OS. I have verified this program to run on Windows 8.1, and Windows 10. Presumably, it will work on Windows 7, but I have not verified this.

## ***Version Two***
This version launches quicker, but all program files are extracted so it looks a little messy. You would probably want to create a shortcut to the CrayTag.exe file to make it easier to launch.

[Download the CrayTag.zip](https://github.com/Dalton-Overlin/CrayTag/blob/master/Windows%20Executables/CrayTag.zip)

## Instructions

Download the zipped file, then extract the zipped file. Once you do you can run the program by running the CrayTag.exe file. To make it easier you may want to create a shortcut and place it somewhere on your device that will make it easier for you to launch the program in the future. This way you don't have to sort through all the files to find the CrayTag.exe file each time. I have verified this program to run on Windows 8.1, and Windows 10. Presumably, it will work on Windows 7, but I have not verified this.

## ***Running from Python Script***

 - First, download the Python script.

[Download CrayTag.pyw](https://github.com/Dalton-Overlin/CrayTag/blob/master/CrayTag.pyw)

This program is built using Python 3, so if you want to run the raw code of this program you will need a way of running Python 3 scripts. This program depends on these modules below.

**Required Python Modules**

 - os
 - sys
 - shutil
- threading
- random
- string
- Tkinter
- time
- DateTime
- eyed3
- tinytag
- PIL (also known as pillow)

Most of those modules come pre-installed with Python, but on some systems like Linux, some packages may be missing which you will have to install. Then once those modules are installed on your system you can run the raw Python script.

## *Program Usage Instructions*

**Type or Select Path of Folder to Process (or "Browse" button)**

 - The text box allows you to manually type the path of the folder to be
   processed (meaning the folder holding mp3s for processing). The
   "Browse" button opens a GUI window to select the folder for
   processing. That way you don't have to manually type out the path.

**Notify to Add Missing Album Artist (Checkbox)**

 - When this option is checked, while the program is processing your mp3
   files if it finds an album with no defined artist name it will pop-up
   asking you to add the missing artist name. If you uncheck the box it
   will not notify you to add the missing data.

**Notify to Add Missing Album Cover (Checkbox)**

- When this option is checked, while the program is processing your mp3 files if it finds an album with no defined album cover it will pop-up asking you to add the missing album cover. If you uncheck the box it will not notify you to add the missing cover. 

**Notify to Add Missing Album Name (Checkbox)**

- When this option is checked, while the program is processing your mp3 files if it finds an album with no defined album name it will pop-up asking you to add the missing album name. If you uncheck the box it will not notify you to add the missing album name.

**Resize Album Cover to: (dropdown menu)**

- It allows you to select the size for the album art to be resized to. This will be the size that either embedded or standalone album covers will be resized too. For this operation, you don't need to click the "Save Custom" button as changing the dropdown value immediately sets the value. 

**or Custom: & "Save Custom" button (for custom album art size)**

- This option allows you to set a custom album cover size by either typing a numeric value or by using the toggle option to increase or decrease the value. Once you've set the custom size you must click the "Save Custom" button for the custom album cover size to be set. 

**Renumber mp3 Filenames: (checkbox)** 

- When this box is checked it will carry out the file renumbering process. If the box is not checked it will not renumber the files.

**Renumbering Example Style (Dropdown Menu)**

- This dropdown menu will give you options for different renumbering styles to choose from. 

**Change all Genres to: (dropdown menu)**

- If you leave this option at "Don't Change" then the program will not change the genre of all files being processed. But if you do change the option, then all files that are processed by the program will be changed to the new genre.

**Delete Embedded (dropdown menu)**

- By default this option is set to No, when set to No it will not remove embedded album art. If you set this option to Yes then all embedded album art in your mp3 files will be removed. This is a way of stripping all embedded album art. 

**Resize JPG File (dropdown menu)**

- By default this option is set to No, when set to No it will not resize external album art (external meaning album art stored as separate image files). If you set this option to Yes then all external album art will be resized. 

**Embed Cover (dropdown menu)**

- By default, this option is set to Yes when setting to Yes it will embed album art into mp3 files. If you set this option to No then-new album art will not be embedded into the mp3 files. This option does not strip embedded album covers, it just prevents the setting of new embedded album covers if set to No. 

**Keep Backup (dropdown menu)**

- By default, this option is set to Yes. This option controls whether or not a backup of an embedded album cover will be made before resizing. This is done by extracting embedded album art and storing it as an external image file. Yes means a backup will be made. No means a backup will not be made. 

**Start (button)**

- This button is notably larger than the rest and is located at the bottom right area of the main GUI window. Once you've defined a directory to process and optionally additional settings you simply click the "Start" button and it will start processing the files. 

**Settings (button with fish image)**

- This button opens up a new window that will give you additional options. There is an option to specify custom names for album covers to look for. While the second option in the settings menu will let you define files to be deleted during the scanning process. This means if you define a filename like "folder.jpg" to be deleted the program will delete that file if it comes across it during the scan process of the directory you define. 

**Processing Window**

![Capture-2](https://user-images.githubusercontent.com/30564402/83311440-78c81400-a1cc-11ea-827b-e5ab60a88998.PNG)

- This window will display while the program is processing your files. It will display live feedback of the current albums it is processing. If you want to cancel the processing of files just click the X button at the top right of the window. Once you do it will pop-up asking you if you want to cancel the running processes. 

**Feedback Area**

- There is a small text area at the bottom left of the main program window. This text area will give you feedback whenever you change a setting. After processing file this text area will also hold data about how many files were processed. 

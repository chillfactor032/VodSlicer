# VodSlicer
This is a Windows 64 bit application that extracts subclips of mp4 videos hosted on a remote server. This is very useful when the files are so large they take a long time to download. 

![Vod Slicer Screenshot](https://chillaspect.com/images/vodslicer3.png "VodSlicer GUI Overview")


## Usage

To use VodSlicer, find the URL to the directory listing of the mp4 files you want to explore. If this link requires a username and password specify them in the settings. Once the URL and username and password are set, click "Refresh" icon button to view the directory listing in the VoD explorer. 
This version of VodSlicer also supports searching local directories for mp4 files. Click the "Folder" icon button to select a directory and VodSlicer will display all the mp4 files.

![Vod Slicer Screenshot](https://chillaspect.com/images/vodslicer2.png "Viewing a local directory")


Select the VoD that contains the clip you want. Enter the start time and end time of the part of the VoD you wish to extract. This is also a good time to give the clip a name. With these set, click "Slice" to start the extraction process.

A dialog will open showing the progress. A success or failure message will be displayed on completion. 

## How does it work?

For mp4 video's hosted on servers that support the HTML5 `Range` header, a user can request a section of data (or byte range) from the middle of the video. This is how you can seek around in the video player. This makes it trivial to request a section of data out of the middle of the file.

Remember though that mp4 is a container format, which means that simply pulling data out of the middle of the video will result in a corrupted file. 

![MP4 Container Structure](https://chillaspect.com/images/mp4_structure2.png "MP4 Container Structure")


This tool makes use of the [FFMPEG utility](https://ffmpeg.org/about.html) to take the chunk of data and rebuild the structure of the mp4 file so it will be playable.

## Releases

_The easiest way to get started using VodSlicer is to download the latest release executable and run it. Releases are located at this [link](https://github.com/chillfactor032/VodSlicer/releases)._

## Build From Source

To build this project from source, Windows 64 bit OS and python 3.9+, and is required.

First clone the repository and enter the directory:

```bash
git clone https://github.com/chillfactor032/VodSlicer.git
cd VodSlicer
```

Install all of the dependencies with pip:

```bash
py -m pip install -r requirements.txt
```

Compile VodSlicer.py using [Nuitka](https://nuitka.net/) python compiler. This will create the executable VodSlicer.exe in the `dist` directory. Note that you can issue `py build.py partial` to build the Qt resources file and UI files, but not compile the binary. You can also set `TEST_BUILD = True` to enable the console when the exe runs to better troubleshoot. The console is hidden if `TEST_BUILD = False`.

```bash
py build.py
```

Now execute `dist/VodSlicer.exe` to run the application.

### Donations

VodSlicer is provided free and without warranty. If you feel compelled to donated here are my crypto addresses below.

Coin | Address
--- | ---
BTC | 3C7UT1a2Do3LxFvxZt88S7gsNkRyRKXYCw
ETH | 0xc24Fc5E6C2b3E1e1eaE62f59Fab8cFBC87b1FEfc
LTC | MViPMqjn2kdMwbLAbYtgpgnHfzwwpbzUZQ

### Contact

chill@chillaspect.com
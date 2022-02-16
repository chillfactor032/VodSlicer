# VodSlicer
This is a Windows 64 bit application that extracts subclips of mp4 videos hosted on a remote server. This is very useful when the files are so large they take a long time to download. 

![Vod Slicer Screenshot](https://chillaspect.com/images/vodslicer1.png "Vod Slicer")

## Usage

To use VodSlicer, find the URL to the directory listing of the mp4 files you want to explore. If this link requires a username and password specify them in the settings along with the URL. Once the URL and username and password are set, click "Load VoDs" to view the directory listing in the VoD explorer.

Select the VoD that contains the clip you want. Enter the start time and end time of the part of the VoD you wish to extract. This is also a good time to give the clip a name. With these set, click "Slice" to start the extraction process.

A dialog will open showing the progress. A success or failure message will be displayed on completion. 

## Releases

The easiest way to get started using VodSlicer is to download a release exe and execute it. Releases are located at this [link](https://github.com/chillfactor032/VodSlicer/releases).

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
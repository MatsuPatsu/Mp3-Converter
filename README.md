# YouTube to MP3 Downloader

MP3 Converter is a simple application that lets you download and convert YouTube videos into MP3 audio files. With an easy-to-use GUI, 
you can quickly paste a YouTube URL and download the audio. 
The converted MP3 file is automatically saved in your `Downloads` folder for easy access.

## Requirements

Make sure you have Python 3.x installed on your system.

### Libraries

You can install the required Python libraries using `pip`:

`pip install pywebview yt-dlp`

### FFmpeg Installation

The application requires FFmpeg to extract and convert audio from YouTube videos. Follow the steps below to install FFmpeg on your system:

On macOS (using Homebrew):

`brew install ffmpeg`

On Windows:
Download FFmpeg from the official website: FFmpeg Download and add the bin folder to your system’s PATH.

On Linux (Ubuntu):

`sudo apt update`

`sudo apt install ffmpeg`

## Usage
1. Clone or download this repository.
2. Install the required dependencies as mentioned above.
3. Make sure you have FFmpeg installed and accessible from your command line.
4. Run the Python script:
`python YTCV.py`

## Notes
- Ensure that both yt-dlp and FFmpeg are installed correctly for the download and conversion to work.
- The downloaded MP3 files will be saved automatically in the Downloads folder.

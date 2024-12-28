# Emoji Video Renderer

A Python-based program that converts video files into real-time text-based animations using moon emojis. The application displays the video frame-by-frame in the terminal at 30 frames per second, creating a unique and engaging visual experience.

## Features

- Converts video frames to grayscale and maps pixel brightness to moon emojis:
  🌑 (darkest) → 🌕 (lightest)
- Real-time text-based animation displayed in the terminal.
- Adjustable resolution and frame rate for customization.
- Supports common video formats like `.mp4`, `.avi`, and `.mkv`.

## Requirements

- Python 3.7 or higher
- Libraries:
  - OpenCV
  - NumPy

Install required libraries with:
```bash
pip install opencv-python numpy
```

## Usage
 - Clone this repository or download the script.
 - Place your video file in the same directory as the script.
 - Update the video_path variable in the script to point to your video file.
 - Run the script:

```bash
python app.py
```
## Customization
 - Resolution: Adjust the scale parameter to control the size of the emoji grid. Higher values reduce the grid size, while lower values provide more detail.
 - Frame Rate: Modify the fps parameter to set the playback speed (default is 30 FPS).

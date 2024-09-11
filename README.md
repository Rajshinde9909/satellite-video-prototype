# satellite-video-prototype
SIH
# Flask Video Processing Prototype

This project is a Flask-based web application for video processing, which utilizes several Python libraries to handle requests, process videos, and serve the application.

## Features

- **Flask:** A lightweight WSGI web application framework to serve the application.
- **requests:** Used to make HTTP requests within the application.
- **opencv-python:** Library for computer vision tasks, primarily for video processing.
- **ffmpeg-python:** Python bindings for FFmpeg to handle video conversion, manipulation, and other multimedia tasks.

## Prerequisites

- Python 3.6 or higher
- `pip` (Python package installer)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Rajshinde9909/satellite-video-prototype.git
   cd your-repo
# File structure
```
satellite-video-prototype/
│
├── app.py               # Flask backend
├── fetch_images.py      # Script to fetch satellite images
├── interpolate.py       # Script for frame interpolation
├── generate_video.py    # Script to generate video
├── requirements.txt     # Python dependencies
├── static/              # Static files (CSS, JS)
│   └── video.mp4        # Placeholder for the generated video
└── templates/
    └── index.html       # Frontend HTML file

# satellite-video-prototype
SIH
# To Install Dependencies
Create a requirements.txt file to manage Python dependencies:
Enter the content:

"""Flask
requests
opencv-python
ffmpeg-python
"""
# Install the dependencies using:

Copy code
pip install -r requirements.txt

# Run the Prototype
Run the Flask App:
   python app.py

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

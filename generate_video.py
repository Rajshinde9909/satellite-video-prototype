import cv2
import os

def create_video_from_frames(frame_dir, output_video):
    frame_files = [os.path.join(frame_dir, f) for f in sorted(os.listdir(frame_dir)) if f.endswith('.png')]
    frame = cv2.imread(frame_files[0])
    height, width, layers = frame.shape

    video = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc(*'MP4V'), 1, (width, height))

    for frame_file in frame_files:
        video.write(cv2.imread(frame_file))

    cv2.destroyAllWindows()
    video.release()

# Example usage
create_video_from_frames('frames/', 'static/video.mp4')

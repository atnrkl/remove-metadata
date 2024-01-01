import os
from PIL import Image
from moviepy.editor import VideoFileClip

directory_path = '<folder path>' 

def remove_metadata_from_image(image_path):
    try:
        with Image.open(image_path) as img:
            data = img.tobytes()
            img_without_metadata = Image.frombytes(img.mode, img.size, data)
            img_without_metadata.save(image_path)
            print(f"Metadata removed from image: {image_path}")
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")

def remove_metadata_from_video(video_path):
    try:
        with VideoFileClip(video_path) as video:
            new_video_path = video_path.replace('.mp4', '_nometa.mp4')
            video.write_videofile(new_video_path, codec="libx264", audio_codec="aac")
            print(f"Metadata removed from video: {new_video_path}")
    except Exception as e:
        print(f"Error processing video {video_path}: {e}")

for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    if filename.lower().endswith(('_nometa.mp4')):
       
        print("Skipped a video that ends with _nometa.mp4")
        continue
    elif filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        remove_metadata_from_image(file_path)
    elif filename.lower().endswith(('.mp4', '.avi', '.mov')):
        remove_metadata_from_video(file_path)

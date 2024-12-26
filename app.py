import cv2
import numpy as np
import time
import os

# Define the emoji map based on brightness levels
emoji_map = ['🌑', '🌒', '🌓', '🌔', '🌕']

def pixel_to_emoji(value):
    """Map a grayscale value to a moon emoji."""
    index = int((value / 255) * (len(emoji_map) - 1))
    return emoji_map[index]

def frame_to_emojis(frame, scale=10):
    """
    Convert a grayscale frame to emojis.
    `scale` reduces the resolution for better visual output.
    """
    # Resize the frame to a smaller resolution
    small_frame = cv2.resize(frame, (frame.shape[1] // scale, frame.shape[0] // scale))
    emoji_frame = [[pixel_to_emoji(value) for value in row] for row in small_frame]
    return emoji_frame

def display_emojis(emoji_frame):
    """Print the emoji frame."""
    for row in emoji_frame:
        print("".join(row))

def video_to_emojis(video_path, scale=10):
    """
    Convert video to emoji frames.
    """
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Convert grayscale frame to emojis
        emoji_frame = frame_to_emojis(gray_frame, scale)

        # Display emoji frame
        display_emojis(emoji_frame)
        print("\n" + "=" * 50 + "\n")  # Separate frames

        # Add a small delay to simulate video playback
        cv2.waitKey(100)

    cap.release()

def render_animation(video_path, scale=20, fps=30):
    """
    Convert video frames to an emoji animation and render in the terminal.
    - `scale`: Adjusts the size of the emoji grid.
    - `fps`: Frames per second for the animation.
    """
    cap = cv2.VideoCapture(video_path)

    # Get video dimensions and calculate emoji display resolution
    video_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    video_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    emoji_width = video_width // scale
    emoji_height = video_height // scale
    print(f"Emoji Display Resolution: {emoji_width} x {emoji_height}")

    # Frame duration for the desired fps
    frame_duration = 1 / fps

    while cap.isOpened():
        start_time = time.time()

        ret, frame = cap.read()
        if not ret:
            break  # Exit when video ends

        # Convert frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Convert grayscale frame to emojis
        emoji_frame = frame_to_emojis(gray_frame, scale)

        # Render the emoji frame as animation
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
        for row in emoji_frame:
            print("".join(row))

        # Ensure consistent frame rate
        elapsed_time = time.time() - start_time
        sleep_time = max(0, frame_duration - elapsed_time)
        time.sleep(sleep_time)

    cap.release()
    print("Video playback complete.")

# Input video path
video_path = "2.mp4"  # Replace with your video file path
render_animation(video_path)
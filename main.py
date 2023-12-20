import cv2
import os
import time

video_capture = cv2.VideoCapture('path to file')


if not video_capture.isOpened():
    print("Error: Couldn't open the video file.")
    exit()

frame_count = 0

output_directory = '' #path to folder where the photos will go to

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

frame_interval = 30

while True:
    # Read a frame from the video
    ret, frame = video_capture.read()

    if not ret:
        break

    if frame_count % frame_interval == 0:

        frame_filename = os.path.join(output_directory, f'frame_{frame_count:04d}.png')
    #print(f'Saving frame as: {frame_filename}')
        cv2.imwrite(frame_filename, frame)

    frame_count += 1

#print(f'Output directory: {output_directory}')

video_capture.release()

#print(f'Frames extracted: {frame_count}')

import cv2
import pyaudio
import wave
import keyboard

# Open the default camera
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera")
    exit()

# Set up audio recording parameters
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()  # Capture frame-by-frame

    if not ret:
        print("Error: Failed to capture frame")
        break

    # Record audio
    audio_frame = stream.read(1024)
    # Add logic to process audio_frame and combine with video frame

    # Write the frame to the output video file
    out.write(frame)

    # Check for the 'q' keypress to exit the loop and stop recording
    if keyboard.is_pressed(' '):
        break

# Release resources
cap.release()
out.release()
stream.stop_stream()
stream.close()
audio.terminate()

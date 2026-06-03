

from deepface import DeepFace

import cv2
import time
import serial

CAMERA_INDEX = 0
WARMUP_SECONDS = 2.0
SNAPSHOT_PATH = "instant_photo.jpg"

cap = cv2.VideoCapture(CAMERA_INDEX)
if not cap.isOpened():
    raise RuntimeError(f"Could not open camera {CAMERA_INDEX}. Try CAMERA_INDEX=1 or close other apps using the webcam.")

time.sleep(WARMUP_SECONDS)

ret, frame = cap.read()
cap.release()

if not ret or frame is None:
    raise RuntimeError("Failed to read a frame from the camera.")

cv2.imwrite(SNAPSHOT_PATH, frame)
print(f"Snapshot saved: {SNAPSHOT_PATH}")

actions = ["emotion"]
demography = DeepFace.analyze(
    frame,
    actions,
    silent=True,
    detector_backend="opencv",
)

dominant = demography[0].get("dominant_emotion")
emotion_scores = demography[0].get("emotion", {})

print("Dominant emotion:", dominant)
if emotion_scores:
    print("Scores (% confidence):")
    for name, score in sorted(emotion_scores.items(), key=lambda x: -x[1]):
        print(f"  {name}: {score:.2f}")

PORT = "COM3"
BAUD = 9600

ser = serial.Serial(PORT, baudrate=BAUD, timeout=1)
time.sleep(2)  # wait for Arduino reset after USB connect

# Your sketch: '1' = D2 on, '2' = D3, '3' = D4, '4' = D5, '0' = all off
if dominant == "happy":
    ser.write(b"1")
    time.sleep(1)
elif dominant == "sad":
    ser.write(b"2")
    time.sleep(1)
elif dominant == "angry":
    ser.write(b"3")
    time.sleep(1)
elif dominant == "surprise":
    ser.write(b"4")
    time.sleep(1)
elif dominant == "fear":
    ser.write(b"5")
    time.sleep(1)
elif dominant == "neutral":
    ser.write(b"6")
    time.sleep(1)
time.sleep(5)
ser.write(b"0")

print(f"Sent '{ser.bytesize}' -> LED command for detected emotion '{dominant}'")
time.sleep(1)

print("Sent '0' -> all LEDs off")

ser.close()
print("Port closed.")
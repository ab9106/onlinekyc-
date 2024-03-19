import cv2
import time
from PIL import ImageGrab  # For taking a screenshot

# Load pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to draw rectangle around detected faces
def draw_face_rectangles(frame, faces):
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Function to display a message
def display_message(message):
    print(message)

# Open video capture device (webcam)
cap = cv2.VideoCapture(0)

# Print message to keep face straight
display_message("Please keep your face straight.")

# Capture face screenshot after 30 seconds
time.sleep(30)
ret, frame = cap.read()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
if len(faces) > 0:
    draw_face_rectangles(frame, faces)
cv2.imwrite("face_screenshot.png", frame)

# Save the current time
start_time = time.time()

# Display a message to keep the ID card near the screen
display_message("Please keep your ID card near the screen.")

# Capture ID card screenshot after another 30 seconds
time.sleep(30)
ret, frame = cap.read()
cv2.imwrite("id_card_screenshot.png", frame)

# Close the program after 1 minute
if time.time() - start_time > 60:
    cap.release()
    cv2.destroyAllWindows()

# Print thank you message
print("Thank you for using our verification system!")
import os
from imutils.video import VideoStream
from imutils.video import FPS
import face_recognition
import imutils
import pickle
import time
import cv2
import requests

# Directory path containing the images
image_directory = r"F:\4-2\Accuracy\Tester"
cascade = "haarcascade_frontalface_default.xml"

# Load the known faces and embeddings along with OpenCV's Haar
# cascade for face detection
encodingsP = "encodings_3.pickle"
data = pickle.loads(open(encodingsP, "rb").read())
detector = cv2.CascadeClassifier(cascade)

# Set the tolerance level (adjust as needed)
tolerance = 0.5

# Loop through each image in the directory
total_image=0
total_unknown=0
for filename in os.listdir(image_directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Load the image
        image_path = os.path.join(image_directory, filename)
        frame = cv2.imread(image_path)
        frame = imutils.resize(frame, width=500)

        # Convert the input frame from (1) BGR to grayscale (for face
        # detection) and (2) from BGR to RGB (for face recognition)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect faces in the grayscale frame
        rects = detector.detectMultiScale(gray, scaleFactor=1.1,
                                          minNeighbors=5, minSize=(30, 30),
                                          flags=cv2.CASCADE_SCALE_IMAGE)

        # OpenCV returns bounding box coordinates in (x, y, w, h) order
        # but we need them in (top, right, bottom, left) order
        boxes = [(y, x + w, y + h, x) for (x, y, w, h) in rects]

        # Compute the facial embeddings for each face bounding box
        encodings = face_recognition.face_encodings(rgb, boxes)
        names = []

        # Loop over the facial embeddings
        
        for encoding in encodings:
            # Attempt to match each face in the input image to our known
            # encodings
            matches = face_recognition.compare_faces(data["encodings"],
                                                     encoding, tolerance=tolerance)
            name = "Unknown"

            # Check to see if we have found a match
            total_image=total_image+1
            
            if True in matches:
                # Find the indexes of all matched faces then initialize a
                # dictionary to count the total number of times each face
                # was matched
                matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                counts = {}

                # Loop over the matched indexes and maintain a count for
                # each recognized face
                for i in matchedIdxs:
                    name = data["names"][i]
                    counts[name] = counts.get(name, 0) + 1

                # Determine the recognized face with the largest number
                # of votes
                name = max(counts, key=counts.get)

                # If someone in your dataset is identified, print the original
                # and detected names
                index_of_underscore = filename.find('_')
                if name != filename[:index_of_underscore]:
                    total_unknown=total_unknown+1

                print(f"Original image: {filename}, Detected face: {name}")
            else:
                total_unknown=total_unknown+1
                print(f"Original image: {filename}, Detected face: {name}")

            # Update the list of names
            names.append(name)
accuracy=1- total_unknown/total_image
print(accuracy)
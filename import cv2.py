import cv2
import numpy as np
import mysql.connector

# Connect to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="SHpatel@9893",
  database="face_recognizer"
)

# Create a cursor object
mycursor = mydb.cursor()

# Load the classifier and the trained model
face_cascade = cv2.CascadeClassifier('C:\\Users\\HP\\Desktop\\minner 1\\haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainningData.xml')

# Initialize the camera
cap = cv2.VideoCapture(0)

while True:
    # Capture the frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

    # Loop through each detected face
    for (x, y, w, h) in faces:
        # Crop the face region
        face_roi = gray[y:y + h, x:x + w]

        # Recognize the face using the trained model
        id_, confidence = recognizer.predict(face_roi)

        # If the confidence is high enough, fetch the name of the employee from the database
        if confidence > 50:
            mycursor.execute("select Shift from employee where employeeid=%s", (id_,))
            result = mycursor.fetchone()

            # Draw a rectangle around the face and display the name and confidence
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, str(result[0]), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, str(round(confidence)), (x + w - 50, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('Face Recognition', frame)

    # If the 'q' key is pressed, break out of the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()

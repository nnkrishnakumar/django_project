from django.shortcuts import render
import cv2
from django.shortcuts import render, redirect
from .models import DetectedFace
import numpy as np
from skimage.metrics import structural_similarity as ssim


def unique_face_detection(request):
    # Load the pre-trained Haarcascades face detection classifier
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Open a video capture object
    cap=cv2.VideoCapture(0)
    # cap = cv2.VideoCapture("/home/krishnakumar/Documents/Project2/test/How We Film Interviews With Two People In Frame.mp4")  # Replace with the path to your video file
    image_matrix_gray = []
    ssi_index_threshold = 0.25

    while True:
        # Read a frame from the video
        ret, frame = cap.read()
        
        # Break the loop if the video has ended
        if not ret:
            break

        # Convert the frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Perform face detection
        faces = face_cascade.detectMultiScale(gray,scaleFactor=1.3, minNeighbors=7, minSize=(30, 30))

        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            face_crop = gray[y:y+h, x:x+w]
            face_crop = cv2.resize(face_crop, (100, 100))
            
            # Initialize a flag to check if a similar face is found
            similar_face_found = False
            
            for i, existing_face in enumerate(image_matrix_gray):
                print(existing_face)
                ssi_index, _ = ssim(face_crop/255, existing_face/255, full=True, data_range=1)
                print("SSI Index:", ssi_index)
                
                if ssi_index > ssi_index_threshold:
                    similar_face_found = True
                    print("The images are similar. SSI Index:", ssi_index)
                    break

            if not similar_face_found:
                print("The images are not very similar.")
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                image_matrix_gray.append(face_crop)
                # Convert the face crop image to binary format
                _, image_encoded = cv2.imencode('.png', face_crop)
                image_binary = image_encoded.tobytes()

                # Save the binary image to the database
                detected_face = DetectedFace(image=image_binary)
                detected_face.save()          

        # Display the frame with detected faces
        cv2.imshow('Face Detection', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close all windows
    cap.release()
    cv2.destroyAllWindows()



def detected_faces(request):
    detected_faces = DetectedFace.objects.all()
    return render(request, 'detected_faces.html', {'detected_faces': detected_faces})

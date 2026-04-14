import cv2
import os

def collect_samples(name):
    # Load the built-in Haar Cascade model for face detection
    face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Initialize Webcam
    cap = cv2.VideoCapture(0)
    count = 0

    print(f"[SYSTEM]: Starting Face Capture for {name}. Look at the camera and move your head slightly...")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR]: Could not access webcam.")
            break

        # Convert to grayscale (Face detection is faster and more accurate in gray)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect faces in the frame
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            count += 1
            # Crop the face region
            face = gray[y:y+h, x:x+w]
            face = cv2.resize(face, (200, 200))
            
            # Save the file into your specific folder
            file_name_path = f"data/faces/{name}/{count}.jpg"
            cv2.imwrite(file_name_path, face)

            # Draw a rectangle and count on the screen for feedback
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, f"Samples: {count}/100", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow('ORION Face Trainer', frame)

        # Stop if 'Enter' (13) is pressed or we hit 100 samples
        if cv2.waitKey(1) == 13 or count == 100: 
            break

    cap.release()
    cv2.destroyAllWindows()
    print(f"[SYSTEM]: Successfully collected {count} samples for {name}.")

if __name__ == "__main__":
    # Ensure the directory exists before running
    if not os.path.exists("data/faces/akash"):
        os.makedirs("data/faces/akash")
    
    collect_samples("akash")
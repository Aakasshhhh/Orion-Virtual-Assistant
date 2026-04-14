import cv2
import face_recognition
import os
import numpy as np

def authenticate_user():
    # 1. Load your training image to learn your face
    # We use the first image from your dataset as the 'Gold Standard'
    known_image_path = "data/faces/akash/1.jpg"
    
    if not os.path.exists(known_image_path):
        print("[ERROR]: No training data found. Run face_trainer.py first.")
        return False

    known_image = face_recognition.load_image_file(known_image_path)
    # Convert image to a 128-dimension mathematical encoding
    known_encoding = face_recognition.face_encodings(known_image)[0]

    # 2. Start the Webcam for Live Verification
    cap = cv2.VideoCapture(0)
    print("[SYSTEM]: Initializing Face Authentication... Look at the camera.")

    # We will try to recognize you for a maximum of 10 seconds
    for _ in range(30): 
        ret, frame = cap.read()
        if not ret: break

        # Find all faces in the current frame
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for face_encoding in face_encodings:
            # Compare live face with your saved 'akash' encoding
            matches = face_recognition.compare_faces([known_encoding], face_encoding, tolerance=0.6)
            
            if True in matches:
                print("[SUCCESS]: Identity Verified. Welcome Akash.")
                cap.release()
                cv2.destroyAllWindows()
                return True

        cv2.imshow('ORION Security Scan', frame)
        if cv2.waitKey(1) == 13: break

    cap.release()
    cv2.destroyAllWindows()
    print("[FAILED]: Access Denied. Identity not recognized.")
    return False

if __name__ == "__main__":
    authenticate_user()
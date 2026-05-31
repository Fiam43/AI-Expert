import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands

hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

if not cap.isOpened():

    print("Error: Could not access the webcam.")

    exit()

print("Hand tracking Started! Press 'q' to quit.")

def detect_gesture(hand_landmarks):
    
    landmarks = hand_landmarks.landmark

    tip_ids = [4, 8, 12, 16, 20]

    pip_ids = [2, 6, 10, 14, 18]

    extended = 0


    if abs(landmarks[tip_ids[0]].x - landmarks[pip_ids[0]].x) > 0.04:

        extended += 1

    for i in range(1, 5):

        if landmarks[tip_ids[i]].y < landmarks[pip_ids[i]].y:

            extended += 1

    if extended >= 4:

        return "Open"
    
    elif extended <= 1:

        return "Closed Fist"

    else:

        return "Partial"   
    
while True:

    success, frame = cap.read()

    if not success:

        break

    frame = cv2.flip(frame, 1)

    h, w, _ = frame.shape

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(frame_rgb)

    gesture = "No hands detected"


    if results.multi_hand_landmarks and results.multi_handedness:

        for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):

            hand_label = results.multi_handedness[idx].classification[0].label

            gesture = detect_gesture(hand_landmarks)

            

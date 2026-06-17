
import cv2
import mediapipe as mp
import numpy as np
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc

# ---------------------------
# MediaPipe Setup
# ---------------------------
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

draw = mp.solutions.drawing_utils

TH = mp_hands.HandLandmark.THUMB_TIP
IX = mp_hands.HandLandmark.INDEX_FINGER_TIP

# ---------------------------
# Audio Setup (Windows)
# ---------------------------
try:
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_,
        23,
        None
    )
    volctl = interface.QueryInterface(IAudioEndpointVolume)

    minv, maxv, _ = volctl.GetVolumeRange()

except Exception as e:
    print("Audio initialization failed:", e)
    exit()

# ---------------------------
# Webcam Setup
# ---------------------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Webcam not accessible.")
    exit()

WIN = "Hand Gesture Control"
cv2.namedWindow(WIN, cv2.WINDOW_NORMAL)

# ---------------------------
# Main Loop
# ---------------------------
while True:

    success, img = cap.read()

    if not success:
        print("Failed to read frame.")
        break

    img = cv2.flip(img, 1)

    h, w, _ = img.shape

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks and results.multi_handedness:

        for i, hand in enumerate(results.multi_hand_landmarks):

            label = results.multi_handedness[i].classification[0].label

            draw.draw_landmarks(
                img,
                hand,
                mp_hands.HAND_CONNECTIONS
            )

            lm = hand.landmark

            thumb = (
                int(lm[TH].x * w),
                int(lm[TH].y * h)
            )

            index = (
                int(lm[IX].x * w),
                int(lm[IX].y * h)
            )

            cv2.circle(img, thumb, 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, index, 10, (255, 0, 0), cv2.FILLED)

            cv2.line(img, thumb, index, (0, 255, 0), 3)

            distance = np.hypot(
                index[0] - thumb[0],
                index[1] - thumb[1]
            )

            distance = np.clip(distance, 30, 300)

            # --------------------------------------------------
            # RIGHT HAND → Volume
            # Because frame is flipped, MediaPipe sees it as Left
            # --------------------------------------------------
            if label == "Left":

                volume = np.interp(
                    distance,
                    [30, 300],
                    [minv, maxv]
                )

                try:
                    volctl.SetMasterVolumeLevel(volume, None)
                except Exception as e:
                    print("Volume error:", e)

                bar = int(
                    np.interp(distance, [30, 300], [400, 150])
                )

                percent = int(
                    np.interp(distance, [30, 300], [0, 100])
                )

                cv2.rectangle(
                    img,
                    (50, 150),
                    (85, 400),
                    (255, 0, 0),
                    2
                )

                cv2.rectangle(
                    img,
                    (50, bar),
                    (85, 400),
                    (255, 0, 0),
                    cv2.FILLED
                )

                cv2.putText(
                    img,
                    f"VOL {percent}%",
                    (20, 450),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (255, 0, 0),
                    2
                )

            # --------------------------------------------------
            # LEFT HAND → Brightness
            # Because frame is flipped, MediaPipe sees it as Right
            # --------------------------------------------------
            elif label == "Right":

                brightness = int(
                    np.interp(distance, [30, 300], [0, 100])
                )

                brightness = max(0, min(100, brightness))

                try:
                    sbc.set_brightness(brightness)
                except Exception as e:
                    print("Brightness error:", e)

                bar = int(
                    np.interp(distance, [30, 300], [400, 150])
                )

                x1 = w - 85
                x2 = w - 50

                cv2.rectangle(
                    img,
                    (x1, 150),
                    (x2, 400),
                    (0, 255, 0),
                    2
                )

                cv2.rectangle(
                    img,
                    (x1, bar),
                    (x2, 400),
                    (0, 255, 0),
                    cv2.FILLED
                )

                cv2.putText(
                    img,
                    f"BRI {brightness}%",
                    (w - 170, 450),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0),
                    2
                )

    cv2.imshow(WIN, img)

    key = cv2.waitKey(1) & 0xFF

    if key == 27 or key == ord("q"):
        break

    try:
        if cv2.getWindowProperty(
            WIN,
            cv2.WND_PROP_VISIBLE
        ) < 1:
            break
    except cv2.error:
        break

# ---------------------------
# Cleanup
# ---------------------------
cap.release()
hands.close()
cv2.destroyAllWindows()


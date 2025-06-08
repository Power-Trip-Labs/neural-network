import cv2
import threading
import os

video_path = 'neural.mp4'  # now correctly named
window_name = 'Neural Network'
running = True

def main_logic():
    global running
    os.system('train')
    os.system('model')
    running = False

logic_thread = threading.Thread(target=main_logic)
logic_thread.start()

cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Failed to open video file.")
    running = False

cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

while running:
    ret, frame = cap.read()
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    cv2.imshow(window_name, frame)
    fps = cap.get(cv2.CAP_PROP_FPS)
    delay = int(1000 / fps * 1)  # 2x slower
    if cv2.waitKey(delay) == 27:
        running = False
        break

    if cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
        running = False
        break

cap.release()
cv2.destroyAllWindows()
logic_thread.join()

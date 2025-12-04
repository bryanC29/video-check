import cv2
import os
import numpy as np

def analyze_color(frames_dir, color_threshold=0.25):
    frames = sorted([f for f in os.listdir(frames_dir) if f.endswith(".jpg")])

    if len(frames) < 2:
        print("[ERROR] Not enough frames for color analysis.")
        return 0, 0

    suspicious = 0
    differences = []

    last_hist = None

    for f in frames:
        path = os.path.join(frames_dir, f)
        frame = cv2.imread(path)

        # Convert to HSV for better color comparison
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        hist = cv2.calcHist([hsv], [0, 1], None, [30, 30], [0, 180, 0, 256])
        hist = cv2.normalize(hist, hist).flatten()

        if last_hist is not None:
            diff = cv2.compareHist(hist, last_hist, cv2.HISTCMP_BHATTACHARYYA)
            differences.append(diff)

            if diff > color_threshold:
                suspicious += 1

        last_hist = hist

    if differences:
        print(f"[COLOR DEBUG] Min diff: {min(differences):.4f}, "
              f"Max diff: {max(differences):.4f}, "
              f"Avg diff: {sum(differences)/len(differences):.4f}")

    return suspicious, len(frames)

import cv2
import os

def detect_changes(frames_dir, threshold=30.0):
    frames = sorted([f for f in os.listdir(frames_dir) if f.endswith(".jpg")])

    if len(frames) < 2:
        print("[ERROR] Not enough frames.")
        return 0, 0

    suspicious_count = 0
    last_frame = None
    diff_values = []

    for f in frames:
        path = os.path.join(frames_dir, f)
        frame = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

        if last_frame is None:
            last_frame = frame
            continue

        diff = cv2.absdiff(frame, last_frame)
        diff_score = diff.mean()
        diff_values.append(diff_score)

        if diff_score > threshold:
            suspicious_count += 1

        last_frame = frame

    if diff_values:
        print(f"[DEBUG] Min diff: {min(diff_values):.2f}, Max diff: {max(diff_values):.2f}, Avg diff: {sum(diff_values)/len(diff_values):.2f}")

    return suspicious_count, len(frames)

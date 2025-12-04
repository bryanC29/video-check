import cv2
import os

def variance_of_laplacian(image):
    # Computes sharpness measure
    return cv2.Laplacian(image, cv2.CV_64F).var()

def analyze_blur(frames_dir, blur_threshold=100.0):
    frames = sorted([f for f in os.listdir(frames_dir) if f.endswith(".jpg")])

    if len(frames) == 0:
        print("[ERROR] No frames found in:", frames_dir)
        return 0, 0

    blur_values = []
    blurred_frames = 0

    for f in frames:
        path = os.path.join(frames_dir, f)
        frame = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

        sharpness = variance_of_laplacian(frame)
        blur_values.append(sharpness)

        if sharpness < blur_threshold:  
            blurred_frames += 1

    # Debug output
    print(f"[BLUR DEBUG] Min sharpness: {min(blur_values):.2f}, "
          f"Max sharpness: {max(blur_values):.2f}, "
          f"Avg sharpness: {sum(blur_values)/len(blur_values):.2f}")

    return blurred_frames, len(frames)

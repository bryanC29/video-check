import cv2
import os
from skimage.metrics import structural_similarity as ssim

def analyze_ssim(frames_dir, ssim_threshold=0.92):
    frames = sorted([f for f in os.listdir(frames_dir) if f.endswith(".jpg")])

    if len(frames) < 2:
        print("[ERROR] Not enough frames for SSIM analysis.")
        return 0, 0

    suspicious = 0
    ssim_values = []
    last_frame = None

    for f in frames:
        path = os.path.join(frames_dir, f)
        frame = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

        if last_frame is not None:
            score, _ = ssim(frame, last_frame, full=True)
            ssim_values.append(score)

            if score < ssim_threshold:
                suspicious += 1

        last_frame = frame

    print(f"[SSIM DEBUG] Min SSIM: {min(ssim_values):.3f}, "
          f"Max SSIM: {max(ssim_values):.3f}, "
          f"Avg SSIM: {sum(ssim_values)/len(ssim_values):.3f}")

    return suspicious, len(frames)

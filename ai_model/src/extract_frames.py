import os
import shutil
import cv2

# Folders for raw videos
RAW_DIRS = {
    "original": os.path.join("data", "raw", "original"),
    "tampered": os.path.join("data", "raw", "tampered"),
}

# Base folder for extracted frames
FRAMES_BASE = os.path.join("data", "frames")


def clean_old_frames():
    """
    Delete previous extracted frames so that old runs
    do not mix with new videos.
    """
    print("\n[CLEAN] Removing previous extracted frames...")
    for label in RAW_DIRS.keys():
        out_dir = os.path.join(FRAMES_BASE, label)
        if os.path.exists(out_dir):
            shutil.rmtree(out_dir)
            print(f"[CLEAN] Deleted folder: {out_dir}")
        os.makedirs(out_dir, exist_ok=True)
        print(f"[CLEAN] Ready folder: {out_dir}")
    print("[CLEAN] Done.\n")


def extract_for_label(label: str):
    raw_dir = RAW_DIRS[label]
    if not os.path.isdir(raw_dir):
        print(f"[WARN] Raw directory not found: {raw_dir}")
        return

    videos = [
        f for f in os.listdir(raw_dir)
        if f.lower().endswith((".mp4", ".avi", ".mov", ".mkv"))
    ]

    print(f"[DEBUG] Checking {raw_dir} | Found files: {videos}")

    if not videos:
        print(f"[INFO] No videos found in {raw_dir}")
        return

    for filename in videos:
        video_path = os.path.join(raw_dir, filename)
        stem, _ = os.path.splitext(filename)

        out_dir = os.path.join(FRAMES_BASE, label, stem)
        os.makedirs(out_dir, exist_ok=True)

        print(f"[INFO] Extracting frames from: {video_path}")
        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            print(f"[ERROR] Could not open video: {video_path}")
            continue

        count = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frame_name = f"frame_{count:03d}.jpg"
            cv2.imwrite(os.path.join(out_dir, frame_name), frame)
            count += 1

        cap.release()
        print(f"[DONE] Saved {count} frames to: {out_dir}")


def main():
    # 1) Always clean previous frames
    clean_old_frames()

    # 2) Extract fresh frames for both classes
    extract_for_label("original")
    extract_for_label("tampered")


if __name__ == "__main__":
    main()

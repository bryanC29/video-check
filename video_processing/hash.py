import sys, subprocess
# subprocess.check_call([sys.executable, "-m", "pip", "install", "gdown", "opencv-python-headless", "numpy"])

import gdown, cv2, numpy as np, hashlib

# ---- 1. Download video from Google Drive ----
# FILE_ID = "YOUR_FILE_ID"  # <-- replace with your video file ID
# url = f"https://drive.google.com/uc?id={FILE_ID}"
url = "https://drive.google.com/uc?id=1v-1IQBj0cgNLpHvIyxlQz5468F-qIS3B"
output = "video.mp4"
gdown.download(url, output, quiet=False)

# ---- 2. SHA256 hash (exact file match) ----
def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1<<20), b""):
            h.update(chunk)
    return h.hexdigest()

# ---- 3. Perceptual hash for frames ----
def frame_phash(frame, hash_size=8):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (hash_size*4, hash_size*4))
    dct = cv2.dct(np.float32(gray))
    dct_lowfreq = dct[:hash_size, :hash_size]
    med = np.median(dct_lowfreq[1:,1:])
    bits = (dct_lowfreq > med).astype(int).flatten()
    return int("".join(str(b) for b in bits), 2)

def video_fingerprint(path, frame_interval=1.0):
    cap = cv2.VideoCapture(path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    hashes = []
    frame_no = 0
    while True:
        ret, frame = cap.read()
        if not ret: break
        if fps > 0 and int(frame_no % int(fps*frame_interval)) == 0:
            hashes.append(frame_phash(frame))
        frame_no += 1
    cap.release()
    return hashes

# ---- 4. Run on your video ----
print("SHA256:", sha256_file(output))
print("Frame Hashes:", video_fingerprint(output))

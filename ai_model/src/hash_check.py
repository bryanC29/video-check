import hashlib
import os

def compute_sha256(file_path, chunk_size=8192):
    """
    Compute SHA-256 hash of a file in binary mode.
    Returns the hex digest string.
    """
    if not os.path.exists(file_path):
        return None

    sha = hashlib.sha256()
    with open(file_path, "rb") as f:
        while True:
            data = f.read(chunk_size)
            if not data:
                break
            sha.update(data)
    return sha.hexdigest()


def print_hash_report():
    """
    Compute and print hash for original and tampered videos.
    Also compare them if both exist.
    """
    orig_path = "data/raw/original/originalV.mp4"
    tamp_path = "data/raw/tampered/tamperedV.mp4"

    print("\n====== HASH VERIFICATION (SHA-256) ======")

    orig_hash = compute_sha256(orig_path)
    tamp_hash = compute_sha256(tamp_path)

    if orig_hash is None:
        print(f"[HASH] Original video not found at: {orig_path}")
    else:
        print(f"[HASH] Original video SHA-256: {orig_hash}")

    if tamp_hash is None:
        print(f"[HASH] Tampered video not found at: {tamp_path}")
    else:
        print(f"[HASH] Tampered video SHA-256: {tamp_hash}")

    # Compare only if both hashes exist
    if orig_hash and tamp_hash:
        if orig_hash == tamp_hash:
            print("[HASH RESULT] Hashes MATCH — files are bitwise identical.")
        else:
            print("[HASH RESULT] Hashes DIFFER — file-level tampering or modification detected.")

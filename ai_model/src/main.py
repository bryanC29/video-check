import os
from detect_changes import detect_changes
from blur_detection import analyze_blur
from color_tampering import analyze_color
from ssim_tampering import analyze_ssim
from hash_check import print_hash_report


def analyze_video(video_name, video_type):
    frames_dir = f"data/frames/{video_type}/{video_name}"
    
    if not os.path.exists(frames_dir):
        print(f"[ERROR] Frames directory not found: {frames_dir}")
        return

    print(f"\n====== ANALYZING VIDEO: {video_name} ({video_type}) ======")

    # MODULE 1 — Motion Tampering
    motion_suspicious, total = detect_changes(frames_dir, threshold=30.0)
    print(f"[MOTION] Suspicious frames: {motion_suspicious}")

    # MODULE 2 — Blur Tampering
    blurred, _ = analyze_blur(frames_dir, blur_threshold=100.0)
    print(f"[BLUR] Blurred frames: {blurred}")

    # MODULE 3 — Color Tampering
    color_suspicious, _ = analyze_color(frames_dir)
    print(f"[COLOR] Color-changed frames: {color_suspicious}")

    # MODULE 4 — SSIM Tampering
    ssim_suspicious, _ = analyze_ssim(frames_dir)
    print(f"[SSIM] SSIM-irregular frames: {ssim_suspicious}")

    # FINAL DECISION RULE
    total_flags = 0
    if blurred > total * 0.30:
        total_flags += 1
    if motion_suspicious > total * 0.25:
        total_flags += 1
    if color_suspicious > total * 0.25:
        total_flags += 1
    if ssim_suspicious > total * 0.25:
        total_flags += 1

    print("\n--- FINAL RESULT ---")
    if total_flags >= 2:
        print("[RESULT] VIDEO IS TAMPERED — MULTIPLE FORENSIC FLAGS\n")
    elif total_flags == 1:
        print("[RESULT] VIDEO MAY BE TAMPERED — SINGLE ANOMALY DETECTED\n")
    else:
        print("[RESULT] VIDEO APPEARS ORIGINAL\n")


if __name__ == "__main__":
    print_hash_report()
    analyze_video("originalV", "original")
    analyze_video("tamperedV", "tampered")

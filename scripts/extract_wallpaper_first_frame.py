#!/usr/bin/env python3
"""
Extract one frame from the wallpaper MP4 for manifest first_frame (0-based index).

Run: python scripts/extract_wallpaper_first_frame.py --frame 7
"""
import argparse
import os
import sys

try:
    import cv2
except ImportError:
    print("Install OpenCV: pip install opencv-python")
    sys.exit(1)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.join(SCRIPT_DIR, "..")


def read_frame_bgr(video_path: str, frame_index: int):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise SystemExit(f"Could not open video: {video_path}")
    frame = None
    for i in range(frame_index + 1):
        ret, frame = cap.read()
        if not ret or frame is None:
            cap.release()
            raise SystemExit(f"Could not read frame index {i}.")
    cap.release()
    return frame


def main():
    default_video = os.path.join(PROJECT_ROOT, "wallpaper", "Ochaco vs Himiko.mp4")
    default_out = os.path.join(PROJECT_ROOT, "wallpaper", "first_frame_ochaco.jpeg")

    p = argparse.ArgumentParser(description="Extract wallpaper first_frame JPEG from MP4.")
    p.add_argument("--video", default=default_video)
    p.add_argument("--frame", type=int, default=0)
    p.add_argument("-o", "--output", default=default_out)
    p.add_argument("--quality", type=int, default=92)
    args = p.parse_args()

    if args.frame < 0:
        raise SystemExit("--frame must be >= 0")

    output = os.path.normpath(args.output)
    os.makedirs(os.path.dirname(output) or ".", exist_ok=True)

    frame = read_frame_bgr(os.path.normpath(args.video), args.frame)
    if not cv2.imwrite(output, frame, [cv2.IMWRITE_JPEG_QUALITY, args.quality]):
        raise SystemExit(f"Failed to write: {output}")
    print(f"Frame {args.frame} -> {output}")


if __name__ == "__main__":
    main()

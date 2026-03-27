#!/usr/bin/env python3
"""
Creates placeholder WAV files using only Python stdlib (no ffmpeg).
Run: python scripts/generate_placeholder_sounds.py

For MP3 browser sounds: install ffmpeg, then run with --full flag, or
download free sounds from freesound.org and place in sound/ and music/.
"""
import os
import wave
import struct
import math

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOUND_DIR = os.path.join(BASE, "sound")
KEYBOARD_DIR = os.path.join(BASE, "keyboard")
MUSIC_DIR = os.path.join(BASE, "music")

def make_tone(duration_ms=50, freq=800, sample_rate=44100, gain=0.5):
    """Generate a short tone as WAV bytes."""
    n_samples = int(sample_rate * duration_ms / 1000)
    data = []
    for i in range(n_samples):
        t = i / sample_rate
        val = int(32767 * gain * (0.5 + 0.5 * math.sin(2 * math.pi * freq * t)))
        data.append(struct.pack("<h", max(-32768, min(32767, val))))
    return b"".join(data)

def write_wav(path, data, sample_rate=44100):
    with wave.open(path, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sample_rate)
        w.writeframes(data)

def main():
    os.makedirs(SOUND_DIR, exist_ok=True)
    os.makedirs(KEYBOARD_DIR, exist_ok=True)
    os.makedirs(MUSIC_DIR, exist_ok=True)

    # Browser sounds - we create WAV; user can convert to MP3 with ffmpeg
    # Or use online converter. Opera GX expects MP3 - create both paths.
    sounds = [
        ("click", 50, 800, 0.15),
        ("hover", 30, 600, 0.1),
        ("important_click", 80, 1000, 0.2),
        ("feature_switch_on", 50, 700, 0.15),
        ("feature_switch_off", 50, 600, 0.15),
        ("switch", 50, 750, 0.15),
        ("level_upgrade", 150, 523, 0.25),
        ("limiter_on", 50, 650, 0.15),
        ("limiter_off", 50, 550, 0.15),
        ("close_tab", 60, 400, 0.15),
        ("new_tab", 50, 600, 0.15),
        ("tab_slash", 40, 500, 0.12),
    ]
    for name, dur, freq, gain in sounds:
        path = os.path.join(SOUND_DIR, f"{name}.wav")
        write_wav(path, make_tone(dur, freq, 44100, gain))
        print(f"Created: {path}")

    # Keyboard
    for i, (name, dur, freq, gain) in enumerate([
        ("backspace", 30, 200, 0.08),
        ("enter", 40, 400, 0.1),
        ("letter_1", 25, 600, 0.06),
        ("letter_2", 25, 650, 0.06),
        ("letter_3", 25, 700, 0.06),
        ("space", 35, 150, 0.05),
    ]):
        path = os.path.join(KEYBOARD_DIR, f"{name}.wav")
        write_wav(path, make_tone(dur, freq, 44100, gain))
        print(f"Created: {path}")

    # Music - 5 second placeholder tracks
    for i in range(1, 5):
        path = os.path.join(MUSIC_DIR, f"track_{i}.wav")
        data = make_tone(5000, 440, 44100, 0.05)
        write_wav(path, data)
        print(f"Created: {path}")

    print("\nNote: Opera GX expects .mp3 for browser_sounds and background_music.")
    print("Convert WAV to MP3 with: ffmpeg -i input.wav -acodec libmp3lame output.mp3")
    print("Or use an online converter. Then update manifest paths if needed.")

if __name__ == "__main__":
    main()

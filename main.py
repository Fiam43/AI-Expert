
import threading
import sys
import time
import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import speech_recognition as sr
from speech_recognition import AudioData

stop_event = threading.Event()


def wait_for_enter():
    input("\n🎤 Press Enter to stop recording...\n")
    stop_event.set()


def spinner():
    chars = "|/-\\"
    i = 0
    while not stop_event.is_set():
        sys.stdout.write(f"\r🔴 Recording... {chars[i % 4]}")
        sys.stdout.flush()
        i += 1
        time.sleep(0.1)
    print("\r✅ Recording complete!          ")


def record_audio(label):
    p = pyaudio.PyAudio()
    stop_event.clear()

    try:
        stream = p.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=16000,
            input=True,
            frames_per_buffer=1024
        )
    except Exception:
        p.terminate()
        raise

    frames = []

    print(f"\n🎤 {label}")
    print("Press Enter to stop...")

    threading.Thread(
        target=wait_for_enter,
        daemon=True
    ).start()

    try:
        while not stop_event.is_set():
            frames.append(
                stream.read(1024, exception_on_overflow=False)
            )
            print(".", end="", flush=True)
    finally:
        stream.stop_stream()
        stream.close()
        width = p.get_sample_size(pyaudio.paInt16)
        p.terminate()

    print("\n✅ Recording stopped.")

    return b"".join(frames), 16000, width


def analyze_audio(data, rate):
    samples = np.frombuffer(data, dtype=np.int16)

    if len(samples) == 0:
        raise ValueError("No audio was recorded.")

    return {
        "duration": len(samples) / rate,
        "avg_volume": np.mean(np.abs(samples.astype(np.int32))),
        "max_volume": np.max(np.abs(samples.astype(np.int32))),
        "samples": samples
    }


def transcribe(data, rate, width):
    recognizer = sr.Recognizer()

    try:
        return recognizer.recognize_google(
            AudioData(data, rate, width)
        )
    except sr.UnknownValueError:
        return "Speech could not be understood."
    except sr.RequestError:
        return "Speech recognition service is unavailable."
    except Exception as e:
        return f"Transcription failed: {e}"


def display_stats(stats, text, label):
    print("\n" + "-" * 40)
    print(f"🎙️ {label}")
    print("-" * 40)
    print(f"Duration: {stats['duration']:.2f} seconds")
    print(f"Average Amplitude: {stats['avg_volume']:.2f}")
    print(f"Maximum Amplitude: {stats['max_volume']:.2f}")
    print(f"Transcription: {text}")


def compare(stats1, stats2):
    print("\n" + "=" * 40)
    print("📊 COMPARISON RESULTS")
    print("=" * 40)

    d1 = stats1["duration"]
    d2 = stats2["duration"]

    if d1 > d2:
        longer = "Recording 1"
        diff = (d1 - d2) / d2 * 100 if d2 > 0 else 0
    elif d2 > d1:
        longer = "Recording 2"
        diff = (d2 - d1) / d1 * 100 if d1 > 0 else 0
    else:
        longer = "Both recordings"
        diff = 0

    if d1 == d2:
        print("⏱️ Both recordings have equal duration.")
    elif min(d1, d2) == 0:
        print(f"⏱️ {longer} is longer; percentage comparison unavailable.")
    else:
        print(f"⏱️ {longer} is longer by {diff:.1f}%")

    v1 = stats1["avg_volume"]
    v2 = stats2["avg_volume"]

    if v1 > v2:
        louder = "Recording 1"
        diff = (v1 - v2) / v2 * 100 if v2 > 0 else 0
    elif v2 > v1:
        louder = "Recording 2"
        diff = (v2 - v1) / v1 * 100 if v1 > 0 else 0
    else:
        louder = "Both recordings"
        diff = 0

    if v1 == v2:
        print("🔊 Both recordings have equal average amplitude.")
    elif min(v1, v2) == 0:
        print(f"🔊 {louder} has greater average amplitude.")
    else:
        print(f"🔊 {louder} has greater average amplitude by {diff:.1f}%")


def plot_both(stats1, stats2, rate):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6))

    t1 = np.arange(len(stats1["samples"])) / rate
    ax1.plot(t1, stats1["samples"], color="blue", linewidth=0.5)
    ax1.set_title(
        f"Recording 1 (Normal) - Duration: "
        f"{stats1['duration']:.2f}s, "
        f"Avg: {stats1['avg_volume']:.0f}"
    )
    ax1.set_ylabel("Amplitude")
    ax1.grid(True, alpha=0.3)

    t2 = np.arange(len(stats2["samples"])) / rate
    ax2.plot(t2, stats2["samples"], color="red", linewidth=0.5)
    ax2.set_title(
        f"Recording 2 (Modified) - Duration: "
        f"{stats2['duration']:.2f}s, "
        f"Avg: {stats2['avg_volume']:.0f}"
    )
    ax2.set_xlabel("Time (seconds)")
    ax2.set_ylabel("Amplitude")
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()


def main():
    print("=" * 40)
    print("🎤 VOICE ANALYSIS LAB")
    print("=" * 40)
    print("Record twice and compare your voice!")

    try:
        audio1, rate, width = record_audio(
            "Recording 1: Speak NORMALLY"
        )
        stats1 = analyze_audio(audio1, rate)
        text1 = transcribe(audio1, rate, width)
        display_stats(stats1, text1, "Recording 1 Results")

        input("\n🎤 Press Enter to begin Recording 2...")

        audio2, rate, width = record_audio(
            "Recording 2: Speak LOUDER or FASTER"
        )
        stats2 = analyze_audio(audio2, rate)
        text2 = transcribe(audio2, rate, width)
        display_stats(stats2, text2, "Recording 2 Results")

        compare(stats1, stats2)
        plot_both(stats1, stats2, rate)

    except KeyboardInterrupt:
        print("\nRecording cancelled.")
    except Exception as e:
        print(f"\nError: {e}")
        print("Check your microphone and installed dependencies.")


if __name__ == "__main__":
    main()

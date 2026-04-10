"""
transcribe_call.py — Call transcription and summarization

Records audio (optional) or processes an existing file, transcribes
with speaker detection, summarizes with LLM, and saves as a structured note.

Usage:
    python Tools/transcribe_call.py recording.mp3
    python Tools/transcribe_call.py recording.mp3 --title "Team meeting"
    python Tools/transcribe_call.py --record
    python Tools/transcribe_call.py --record --title "Call with Sarah"

Supported formats: mp3, wav, m4a, ogg, flac
"""

import argparse
import os
from datetime import date
from pathlib import Path

CALLS_PATH = Path("Calls")


def record_audio(output_path: Path):
    """
    Record from microphone until Ctrl+C.

    What to implement:
    - Use sounddevice + scipy.io.wavfile for simple recording
    - Print "Recording... Press Ctrl+C when done." before starting
    - Save to output_path as WAV

    Dependencies: pip install sounddevice numpy scipy
    Note: requires PortAudio — usually installed automatically with sounddevice
    """

    # --- Implement recording here ---
    # import sounddevice as sd
    # import numpy as np
    # from scipy.io.wavfile import write
    #
    # sample_rate = 44100
    # print("Recording... Press Ctrl+C when done.")
    # frames = []
    # try:
    #     with sd.InputStream(samplerate=sample_rate, channels=1) as stream:
    #         while True:
    #             data, _ = stream.read(1024)
    #             frames.append(data)
    # except KeyboardInterrupt:
    #     audio = np.concatenate(frames)
    #     write(str(output_path), sample_rate, audio)
    #     print(f"\nSaved: {output_path}")

    raise NotImplementedError("Implement record_audio() to enable live recording")


def transcribe(audio_path: Path) -> list[dict]:
    """
    Transcribe audio file with speaker detection.

    Returns a list of segments:
        [{"speaker": "Speaker A", "text": "Hello there", "start": 0.0}, ...]

    Suggested services:
    - AssemblyAI: good speaker diarization, generous free tier
    - Groq Whisper: fast and cheap, limited diarization
    - OpenAI Whisper: solid quality, no diarization in base API

    API key from: os.environ["TRANSCRIPTION_API_KEY"]
    Service URL from: os.environ.get("TRANSCRIPTION_API_URL")

    What to implement:
    1. Upload the file to your transcription service
    2. Poll for completion (can take 1-5 min for long recordings)
    3. Parse the response into the segment format above
    """

    # --- Implement your transcription call here ---
    raise NotImplementedError("Implement transcribe() with your transcription service")


def summarize(segments: list[dict], title: str) -> dict:
    """
    Summarize transcription with LLM.

    Returns a dict with:
        summary (str)       — 3-5 sentence overview
        action_items (list) — extracted tasks as strings
        decisions (list)    — key decisions made

    What to implement:
    - Format segments into a readable transcript string
    - Send to LLM with a prompt asking for summary, actions, decisions
    - Ask for JSON output to keep parsing reliable
    - API key from: os.environ["LLM_API_KEY"]
    """

    # --- Implement your LLM summarization here ---
    raise NotImplementedError("Implement summarize() with your LLM provider")


def save_note(title: str, segments: list[dict], summary: dict) -> Path:
    """Format and save the call note to Calls/."""
    CALLS_PATH.mkdir(exist_ok=True)

    today = date.today().isoformat()
    slug = title.lower().replace(" ", "-")
    note_path = CALLS_PATH / f"{today}-{slug}.md"

    transcript = "\n".join(
        f"**{s['speaker']}:** {s['text']}" for s in segments
    )

    actions = "\n".join(f"- [ ] {a}" for a in summary.get("action_items", []))
    decisions = "\n".join(f"- {d}" for d in summary.get("decisions", []))

    content = f"""# {title}
_{today}_

## Summary
{summary.get("summary", "")}

## Action Items
{actions or "_None identified_"}

## Key Decisions
{decisions or "_None identified_"}

## Transcript
{transcript}
"""

    note_path.write_text(content)
    return note_path


def run(audio_path: str | None, title: str, record: bool):
    if record:
        tmp_path = Path(".tmp") / "recording.wav"
        tmp_path.parent.mkdir(exist_ok=True)
        record_audio(tmp_path)
        audio_path = str(tmp_path)

    if not audio_path:
        raise ValueError("Provide an audio file path or use --record")

    path = Path(audio_path)
    if not path.exists():
        raise FileNotFoundError(f"Audio file not found: {path}")

    if not title:
        title = path.stem.replace("-", " ").replace("_", " ").title()

    print(f"[transcribe] Processing: {path.name}")
    segments = transcribe(path)
    print(f"[transcribe] Got {len(segments)} segments")

    summary = summarize(segments, title)
    note_path = save_note(title, segments, summary)

    print(f"[transcribe] Saved: {note_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("audio", nargs="?", help="Path to audio file")
    parser.add_argument("--title", default="", help="Title for the note")
    parser.add_argument("--record", action="store_true", help="Record from microphone")
    args = parser.parse_args()
    run(args.audio, args.title, args.record)

# Workflow: Call Transcription

## Objective
Record a call via microphone, transcribe it with speaker detection, summarize with LLM, and save as a structured note.

## Inputs Required
- `.env` — transcription API key, LLM API key
- `.env` (optional) — messaging tool webhook for posting results

## Tools Used
- `Tools/transcribe_call.py` — main script (record + transcribe + summarize + save)

## Execution

### Record live (speakerphone)
```bash
python Tools/transcribe_call.py --record
python Tools/transcribe_call.py --record --title "Call with [name]"
```

Terminal shows: `Recording... Press Ctrl+C when done.`

### Existing audio file
```bash
python Tools/transcribe_call.py recording.mp3
python Tools/transcribe_call.py recording.mp3 --title "Team meeting"
```

Supported formats: mp3, wav, m4a, ogg, flac

## Output
- `Calls/YYYY-MM-DD-title.md` containing:
  - Summary (3-5 sentences)
  - Action items as checkboxes
  - Key decisions
  - Full transcript with speaker labels (Speaker A, Speaker B, etc.)
- Optional: notification via messaging tool

## Edge Cases

### Audio quality
- Poor audio or echo may affect speaker detection accuracy
- Keep microphone close to the speaker source

### Long recordings
- Transcription polling timeout is 10 min — sufficient for most calls
- Very long recordings may take longer

### Installation issue (sounddevice)
```bash
pip install sounddevice numpy
```
Requires PortAudio — usually installed automatically with the sounddevice package.

## Learning Log
<!-- Update this section when you discover issues -->

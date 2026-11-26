from memory_meeting_ai.store import add_meeting

def basic_summary(transcript, max_sentences=5):
    """Basic extractive summary: takes the first non-empty sentences.

    This is not an AI/LLM summarizer; integrate an NLP model for that capability.
    """
    parts = [s.strip() for s in transcript.replace("\n", " ").split(".") if s.strip()]
    return ". ".join(parts[:max_sentences]) + ("." if parts else "")

def save_meeting(title, transcript):
    summary = basic_summary(transcript)
    add_meeting(title, transcript, summary)
    return summary

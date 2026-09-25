from pydantic import BaseModel
from typing import List, Optional

class VoiceMemoInput(BaseModel):
    memo_id: str
    audio_transcript: str

class ParsedTaskItem(BaseModel):
    title: str
    due_date: Optional[str]
    priority: str
    tags: List[str]

class VoiceTaskExtraction(BaseModel):
    memo_id: str
    extracted_tasks: List[ParsedTaskItem]
    productivity_summary: str

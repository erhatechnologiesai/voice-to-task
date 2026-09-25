from fastapi import FastAPI
from app.config import settings
from app.models import VoiceMemoInput, VoiceTaskExtraction, ParsedTaskItem
from app.services.memo_extractor import parse_voice_memo

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

@app.post("/parse-memo", response_model=VoiceTaskExtraction)
def parse_memo(memo: VoiceMemoInput):
    tasks_raw, summary = parse_voice_memo(memo.memo_id, memo.audio_transcript)
    tasks = [ParsedTaskItem(**t) for t in tasks_raw]
    return VoiceTaskExtraction(
        memo_id=memo.memo_id,
        extracted_tasks=tasks,
        productivity_summary=summary
    )

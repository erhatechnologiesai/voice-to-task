def parse_voice_memo(memo_id: str, transcript: str):
    tasks = [
        {"title": "Review Q4 AWS infrastructure billing", "due_date": "Tomorrow 5 PM", "priority": "HIGH", "tags": ["FinOps", "Cloud"]},
        {"title": "Schedule 1-on-1 with lead AI researcher", "due_date": "Friday", "priority": "MEDIUM", "tags": ["People", "Leadership"]}
    ]
    summary = f"Voice memo {memo_id} parsed successfully into 2 actionable backlog items."
    return tasks, summary

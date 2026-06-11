"""学習進捗の一元管理（教科書 + クイズ）"""

import json
from datetime import datetime
from pathlib import Path

PROGRESS_FILE = Path.home() / ".command_learn_progress.json"


def _load() -> dict:
    if PROGRESS_FILE.exists():
        try:
            return json.loads(PROGRESS_FILE.read_text())
        except (json.JSONDecodeError, KeyError):
            pass
    return {
        "lessons_started": [],
        "lessons_completed": [],
        "quiz_results": {},   # {question_id: {"attempts": N, "correct": N}}
        "last_updated": None,
    }


def _save(data: dict):
    data["last_updated"] = datetime.now().isoformat()
    PROGRESS_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2))


def mark_lesson_started(lesson_id: str):
    data = _load()
    if lesson_id not in data["lessons_started"]:
        data["lessons_started"].append(lesson_id)
    _save(data)


def mark_lesson_completed(lesson_id: str):
    data = _load()
    for key in ("lessons_started", "lessons_completed"):
        if lesson_id not in data[key]:
            data[key].append(lesson_id)
    _save(data)


def record_quiz_result(question_id: str, correct: bool):
    data = _load()
    if question_id not in data["quiz_results"]:
        data["quiz_results"][question_id] = {"attempts": 0, "correct": 0}
    data["quiz_results"][question_id]["attempts"] += 1
    if correct:
        data["quiz_results"][question_id]["correct"] += 1
    _save(data)


def get_category_stats(lesson_ids: list[str], question_ids: list[str]) -> dict:
    data = _load()
    completed = sum(1 for lid in lesson_ids if lid in data["lessons_completed"])
    started   = sum(1 for lid in lesson_ids if lid in data["lessons_started"])
    attempts  = sum(data["quiz_results"].get(qid, {}).get("attempts", 0) for qid in question_ids)
    correct   = sum(data["quiz_results"].get(qid, {}).get("correct",  0) for qid in question_ids)
    return {
        "lessons_total": len(lesson_ids),
        "lessons_started": started,
        "lessons_completed": completed,
        "quiz_attempts": attempts,
        "quiz_correct": correct,
    }


def reset():
    """全進捗データを削除してリセットする"""
    PROGRESS_FILE.unlink(missing_ok=True)


def get_raw() -> dict:
    return _load()


def get_last_updated() -> str | None:
    data = _load()
    raw = data.get("last_updated")
    if raw:
        try:
            return datetime.fromisoformat(raw).strftime("%Y-%m-%d %H:%M")
        except ValueError:
            pass
    return None

"""教科書レッスンデータ — 言語対応ファサード"""

import lang as _lang


def _get_lessons() -> list[dict]:
    if _lang.LANG == "en":
        from lessons_en import LESSONS
        return LESSONS
    from lessons_ja import LESSONS
    return LESSONS


def get_by_category(category: str) -> list[dict]:
    return [l for l in _get_lessons() if l["category"] == category]


def get_by_id(lesson_id: str) -> dict | None:
    return next((l for l in _get_lessons() if l["id"] == lesson_id), None)


def get_lesson_ids_by_category() -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for lesson in _get_lessons():
        result.setdefault(lesson["category"], []).append(lesson["id"])
    return result

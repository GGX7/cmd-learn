"""問題データベース — 言語対応ファサード"""

from typing import TypedDict
import lang as _lang


class Question(TypedDict):
    id: str
    category: str
    difficulty: int
    type: str
    question: str
    choices: list[str]
    answer: str
    explanation: str


def _get_questions() -> list[Question]:
    if _lang.LANG == "en":
        from questions_en import QUESTIONS
        return QUESTIONS
    from questions_ja import QUESTIONS
    return QUESTIONS


def get_by_category(category: str) -> list[Question]:
    return [q for q in _get_questions() if q["category"] == category]


def get_all() -> list[Question]:
    return list(_get_questions())

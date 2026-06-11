"""クイズエンジン：出題・採点"""

import random

import display as d
import progress
import lang as _lang
from questions import Question

ANSWER_ALIASES: dict[str, str] = {
    "a": "0", "b": "1", "c": "2", "d": "3",
}


def _normalize(answer: str) -> str:
    return " ".join(answer.lower().split())


def _check_fill(user_input: str, correct: str) -> bool:
    user = _normalize(user_input)
    norm = _normalize(correct)
    if user == norm:
        return True
    if norm in ("cd ~", "cd") and user in ("cd ~", "cd"):
        return True
    return False


def run_quiz(questions: list[Question], title: str):
    """問題リストを受け取ってクイズを実行する"""
    random.shuffle(questions)
    total = len(questions)
    correct_count = 0
    cats = _lang.get_categories()

    for i, q in enumerate(questions, 1):
        d.clear_screen()
        cat_name = cats.get(q["category"], q["category"])
        d.print_header(title)
        d.print_question(i, total, q["question"], cat_name, q["difficulty"])

        if q["type"] == "choice":
            d.print_choices(q["choices"])
            while True:
                raw = d.prompt(_lang.t("qe_choice_prompt")).lower()
                idx_str = ANSWER_ALIASES.get(raw, raw)
                if idx_str in ("0", "1", "2", "3"):
                    break
                print(d.c(_lang.t("qe_choice_invalid"), d.Color.RED))

            chosen = q["choices"][int(idx_str)]
            is_correct = (chosen == q["answer"])
        else:
            answer_input = d.prompt(_lang.t("qe_fill_prompt"))
            is_correct = _check_fill(answer_input, q["answer"])

        progress.record_quiz_result(q["id"], is_correct)

        if is_correct:
            correct_count += 1
            d.print_correct(q["explanation"])
        else:
            d.print_wrong(q["answer"], q["explanation"])

        d.press_enter()

    d.clear_screen()
    d.print_header(title + _lang.t("qe_results"))
    d.print_score(correct_count, total)
    d.press_enter()

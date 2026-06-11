#!/usr/bin/env python3
"""コマンドライン学習ツール — メインエントリーポイント"""

import sys

import lang as _lang
import display as d
import quiz_engine as qe
import textbook as tb
import progress
import lessons as les
from questions import get_by_category, get_all


BANNER = r"""
   ___                      ___               _
  / __\  ___   _ __ ___    / _ \ _   _  __ _(_)__
 / /    / _ \ | '_ ` _ \  / / \|| | | |/ _` | |_ \
/ /___ | (_) || | | | | |/ /_\ \ |_| | (_| | |  /
\____/  \___/ |_| |_| |_|\____/ \__,_|\__,_|_|/

   Linux / macOS Command Learning Tool  for Beginners
"""


# ──────────────────────────────────────────────────────────────
# 言語選択 / Language Selection
# ──────────────────────────────────────────────────────────────

def select_language():
    d.clear_screen()
    print(d.c(BANNER, d.Color.CYAN))
    print(d.c(f"  ─── {_lang.t('lang_select_title')} ───", d.Color.BOLD))
    print()
    d.print_menu([
        ("1", _lang.t("lang_ja")),
        ("2", _lang.t("lang_en")),
    ])
    while True:
        choice = d.prompt("1 / 2").strip()
        if choice == "1":
            _lang.set_lang("ja")
            break
        elif choice == "2":
            _lang.set_lang("en")
            break
        else:
            print(d.c("  1 or 2", d.Color.RED))


# ──────────────────────────────────────────────────────────────
# クイズメニュー
# ──────────────────────────────────────────────────────────────

def _ask_difficulty() -> int | None:
    print(d.c(f"  {_lang.t('difficulty_prompt')}", d.Color.BOLD))
    d.print_menu([
        ("1", _lang.t("diff_easy")),
        ("2", _lang.t("diff_med")),
        ("3", _lang.t("diff_hard")),
        ("0", _lang.t("diff_all")),
    ])
    raw = d.prompt(_lang.t("choose")).strip()
    if raw not in ("0", "1", "2", "3"):
        print(d.c(f"  {_lang.t('invalid_input')}", d.Color.RED))
        return None
    return int(raw) if raw != "0" else 0


def _filter_difficulty(qs, diff: int):
    return qs if diff == 0 else [q for q in qs if q["difficulty"] == diff]


def category_quiz():
    cats = _lang.get_categories()
    d.clear_screen()
    d.print_header(_lang.t("quiz_category"))
    keys = list(cats.keys())
    menu = [(str(i + 1), label) for i, (_, label) in enumerate(cats.items())]
    menu.append(("0", _lang.t("menu_back")))
    d.print_menu(menu)

    raw = d.prompt(_lang.t("choose"))
    if raw == "0":
        return
    if not raw.isdigit() or int(raw) < 1 or int(raw) > len(keys):
        print(d.c(f"  {_lang.t('invalid_input')}", d.Color.RED))
        d.press_enter()
        return

    category = keys[int(raw) - 1]
    diff = _ask_difficulty()
    if diff is None:
        d.press_enter()
        return

    qs = _filter_difficulty(get_by_category(category), diff)
    if not qs:
        print(d.c(f"  {_lang.t('quiz_no_diff')}", d.Color.RED))
        d.press_enter()
        return

    qe.run_quiz(qs, cats[category])


def random_quiz():
    d.clear_screen()
    d.print_header(_lang.t("quiz_random"))

    diff = _ask_difficulty()
    if diff is None:
        d.press_enter()
        return

    qs = _filter_difficulty(get_all(), diff)
    if not qs:
        print(d.c(f"  {_lang.t('quiz_no_match')}", d.Color.RED))
        d.press_enter()
        return

    qe.run_quiz(qs, _lang.t("quiz_rand_title"))


def quiz_menu():
    while True:
        d.clear_screen()
        d.print_header(_lang.t("quiz_practice"))
        d.print_menu([
            ("1", _lang.t("quiz_cat_label")),
            ("2", _lang.t("quiz_rand_label")),
            ("0", _lang.t("menu_back")),
        ])
        choice = d.prompt(_lang.t("choose"))
        if choice == "1":
            category_quiz()
        elif choice == "2":
            random_quiz()
        elif choice == "0":
            break
        else:
            print(d.c(f"  {_lang.t('quiz_invalid_menu')}", d.Color.RED))
            d.press_enter()


# ──────────────────────────────────────────────────────────────
# コマンド一覧
# ──────────────────────────────────────────────────────────────

def show_command_list():
    cats = _lang.get_categories()
    d.clear_screen()
    d.print_header(_lang.t("cmd_list_header"))

    seen: set[str] = set()
    for cat_key, cat_label in cats.items():
        print(d.c(f"  {cat_label}", d.Color.BOLD + d.Color.CYAN))
        for q in get_all():
            if q["category"] != cat_key:
                continue
            cmd = q["answer"].split()[0]
            if cmd not in seen:
                seen.add(cmd)
                stars = "★" * q["difficulty"] + "☆" * (3 - q["difficulty"])
                print(f"    {d.c(q['answer'], d.Color.YELLOW):<40} {d.c(stars, d.Color.DIM)}")
        print()

    d.press_enter()


# ──────────────────────────────────────────────────────────────
# 学習進捗
# ──────────────────────────────────────────────────────────────

def _progress_bar(current: int, total: int, width: int = 10) -> str:
    if total == 0:
        return "░" * width
    filled = round(current / total * width)
    return "█" * filled + "░" * (width - filled)


def show_progress():
    cats = _lang.get_categories()
    d.clear_screen()
    d.print_header(_lang.t("progress_header"))

    lesson_ids_by_cat = les.get_lesson_ids_by_category()
    question_ids_by_cat: dict[str, list[str]] = {}
    for q in get_all():
        question_ids_by_cat.setdefault(q["category"], []).append(q["id"])

    total_l_done = total_l_all = 0
    total_q_correct = total_q_attempts = 0

    col1 = d.c(_lang.t("progress_cat_col"), d.Color.BOLD)
    col2 = d.c(_lang.t("progress_tb_col"), d.Color.BOLD + d.Color.CYAN)
    col3 = d.c(_lang.t("progress_qz_col"), d.Color.BOLD + d.Color.YELLOW)
    print(f"{col1:<35} {col2:<20} {col3}")
    print(d.c("  " + "─" * 58, d.Color.DIM))

    for cat_key, cat_label in cats.items():
        l_ids = lesson_ids_by_cat.get(cat_key, [])
        q_ids = question_ids_by_cat.get(cat_key, [])
        stats = progress.get_category_stats(l_ids, q_ids)

        l_bar = _progress_bar(stats["lessons_completed"], stats["lessons_total"])
        l_color = d.Color.GREEN if stats["lessons_completed"] == stats["lessons_total"] and stats["lessons_total"] > 0 else d.Color.YELLOW
        l_str = f"{d.c(l_bar, l_color)} {stats['lessons_completed']}/{stats['lessons_total']}"

        if stats["quiz_attempts"] > 0:
            rate = stats["quiz_correct"] / stats["quiz_attempts"] * 100
            q_bar = _progress_bar(stats["quiz_correct"], stats["quiz_attempts"])
            q_color = d.Color.GREEN if rate >= 80 else d.Color.YELLOW if rate >= 50 else d.Color.RED
            q_str = f"{d.c(q_bar, q_color)} {rate:.0f}% ({stats['quiz_correct']}/{stats['quiz_attempts']})"
        else:
            q_str = d.c(_lang.t("progress_not_taken"), d.Color.DIM)

        print(f"  {cat_label:<22} {l_str:<30} {q_str}")

        total_l_done     += stats["lessons_completed"]
        total_l_all      += stats["lessons_total"]
        total_q_correct  += stats["quiz_correct"]
        total_q_attempts += stats["quiz_attempts"]

    print(d.c("  " + "─" * 58, d.Color.DIM))
    total_l_bar = _progress_bar(total_l_done, total_l_all)
    l_color = d.Color.GREEN if total_l_done == total_l_all and total_l_all > 0 else d.Color.YELLOW
    total_l_str = f"{d.c(total_l_bar, l_color)} {total_l_done}/{total_l_all}"

    if total_q_attempts > 0:
        total_rate = total_q_correct / total_q_attempts * 100
        total_q_bar = _progress_bar(total_q_correct, total_q_attempts)
        q_color = d.Color.GREEN if total_rate >= 80 else d.Color.YELLOW if total_rate >= 50 else d.Color.RED
        total_q_str = f"{d.c(total_q_bar, q_color)} {total_rate:.0f}% ({total_q_correct}/{total_q_attempts})"
    else:
        total_q_str = d.c(_lang.t("progress_not_taken"), d.Color.DIM)

    print(f"  {_lang.t('progress_total'):<22} {total_l_str:<30} {total_q_str}")

    last = progress.get_last_updated()
    if last:
        print()
        print(d.c(f"  {_lang.t('progress_last_updated', ts=last)}", d.Color.DIM))

    print()
    d.print_menu([
        ("r", _lang.t("progress_reset_label")),
        (_lang.t("menu_enter"), _lang.t("menu_back")),
    ])
    choice = d.prompt(_lang.t("choose")).lower()
    if choice == "r":
        _confirm_reset()


def _confirm_reset():
    d.clear_screen()
    d.print_header(_lang.t("progress_reset_header"))
    print(d.c(f"  {_lang.t('progress_reset_warn1')}", d.Color.YELLOW))
    print(d.c(f"  {_lang.t('progress_reset_warn2')}", d.Color.RED + d.Color.BOLD))
    print()
    raw = d.prompt(_lang.t("progress_reset_confirm"))
    if raw.strip().lower() == "yes":
        progress.reset()
        d.clear_screen()
        print()
        print(d.c(_lang.t("progress_reset_done"), d.Color.GREEN + d.Color.BOLD))
        print()
        d.press_enter()
    else:
        print(d.c(_lang.t("progress_cancel"), d.Color.DIM))
        d.press_enter()


# ──────────────────────────────────────────────────────────────
# メインメニュー
# ──────────────────────────────────────────────────────────────

def main():
    select_language()

    while True:
        d.clear_screen()
        print(d.c(BANNER, d.Color.CYAN))
        print(d.c(f"  {_lang.t('menu_title')}", d.Color.BOLD))
        d.print_menu([
            ("1", _lang.t("menu_1")),
            ("2", _lang.t("menu_2")),
            ("3", _lang.t("menu_3")),
            ("4", _lang.t("menu_4")),
            ("q", _lang.t("menu_quit")),
        ])

        choice = d.prompt(_lang.t("choose"))

        if choice == "1":
            tb.run_textbook()
        elif choice == "2":
            quiz_menu()
        elif choice == "3":
            show_command_list()
        elif choice == "4":
            show_progress()
        elif choice.lower() == "q":
            d.clear_screen()
            print(d.c(_lang.t("farewell"), d.Color.GREEN + d.Color.BOLD))
            sys.exit(0)
        else:
            print(d.c(f"  {_lang.t('menu_invalid_range')}", d.Color.RED))
            d.press_enter()


if __name__ == "__main__":
    main()

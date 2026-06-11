#!/usr/bin/env python3
"""コマンドライン学習ツール — メインエントリーポイント"""

import sys

import display as d
import quiz_engine as qe
import textbook as tb
import progress
import lessons as les
from questions import QUESTIONS, CATEGORIES, get_by_category, get_all


BANNER = r"""
   ___                      ___               _
  / __\  ___   _ __ ___    / _ \ _   _  __ _(_)__
 / /    / _ \ | '_ ` _ \  / / \|| | | |/ _` | |_ \
/ /___ | (_) || | | | | |/ /_\ \ |_| | (_| | |  /
\____/  \___/ |_| |_| |_|\____/ \__,_|\__,_|_|/

   Linux / macOS コマンド学習ツール  for Beginners
"""


# ──────────────────────────────────────────────────────────────
# クイズメニュー
# ──────────────────────────────────────────────────────────────

def _ask_difficulty() -> int | None:
    print(d.c("  難易度を選んでください:", d.Color.BOLD))
    d.print_menu([
        ("1", "易  ★☆☆"),
        ("2", "中  ★★☆"),
        ("3", "難  ★★★"),
        ("0", "すべて"),
    ])
    raw = d.prompt("選択").strip()
    if raw not in ("0", "1", "2", "3"):
        print(d.c("  無効な入力です。", d.Color.RED))
        return None
    return int(raw) if raw != "0" else 0


def _filter_difficulty(qs, diff: int):
    return qs if diff == 0 else [q for q in qs if q["difficulty"] == diff]


def category_quiz():
    d.clear_screen()
    d.print_header("📝 カテゴリ別クイズ")
    keys = list(CATEGORIES.keys())
    menu = [(str(i + 1), label) for i, (_, label) in enumerate(CATEGORIES.items())]
    menu.append(("0", "戻る"))
    d.print_menu(menu)

    raw = d.prompt("選択")
    if raw == "0":
        return
    if not raw.isdigit() or int(raw) < 1 or int(raw) > len(keys):
        print(d.c("  無効な入力です。", d.Color.RED))
        d.press_enter()
        return

    category = keys[int(raw) - 1]
    diff = _ask_difficulty()
    if diff is None:
        d.press_enter()
        return

    qs = _filter_difficulty(get_by_category(category), diff)
    if not qs:
        print(d.c("  その難易度の問題はありません。", d.Color.RED))
        d.press_enter()
        return

    qe.run_quiz(qs, CATEGORIES[category])


def random_quiz():
    d.clear_screen()
    d.print_header("🔀 ランダム出題")

    diff = _ask_difficulty()
    if diff is None:
        d.press_enter()
        return

    qs = _filter_difficulty(get_all(), diff)
    if not qs:
        print(d.c("  該当する問題がありません。", d.Color.RED))
        d.press_enter()
        return

    qe.run_quiz(qs, "ランダムクイズ")


def quiz_menu():
    while True:
        d.clear_screen()
        d.print_header("📝 クイズで練習する")
        d.print_menu([
            ("1", "カテゴリ別クイズ"),
            ("2", "ランダム出題（全カテゴリ）"),
            ("0", "戻る"),
        ])
        choice = d.prompt("選択")
        if choice == "1":
            category_quiz()
        elif choice == "2":
            random_quiz()
        elif choice == "0":
            break
        else:
            print(d.c("  1・2・0 のいずれかを入力してください。", d.Color.RED))
            d.press_enter()


# ──────────────────────────────────────────────────────────────
# コマンド一覧
# ──────────────────────────────────────────────────────────────

def show_command_list():
    d.clear_screen()
    d.print_header("📖 コマンド一覧")

    seen: set[str] = set()
    for cat_key, cat_label in CATEGORIES.items():
        print(d.c(f"  {cat_label}", d.Color.BOLD + d.Color.CYAN))
        for q in QUESTIONS:
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
    d.clear_screen()
    d.print_header("📊 学習進捗")

    lesson_ids_by_cat = les.get_lesson_ids_by_category()
    question_ids_by_cat: dict[str, list[str]] = {}
    for q in QUESTIONS:
        question_ids_by_cat.setdefault(q["category"], []).append(q["id"])

    total_l_done = total_l_all = 0
    total_q_correct = total_q_attempts = 0

    # ヘッダー行
    col1 = d.c("  カテゴリ", d.Color.BOLD)
    col2 = d.c("教科書", d.Color.BOLD + d.Color.CYAN)
    col3 = d.c("クイズ正答率", d.Color.BOLD + d.Color.YELLOW)
    print(f"{col1:<35} {col2:<20} {col3}")
    print(d.c("  " + "─" * 58, d.Color.DIM))

    for cat_key, cat_label in CATEGORIES.items():
        l_ids = lesson_ids_by_cat.get(cat_key, [])
        q_ids = question_ids_by_cat.get(cat_key, [])
        stats = progress.get_category_stats(l_ids, q_ids)

        # 教科書バー
        l_bar = _progress_bar(stats["lessons_completed"], stats["lessons_total"])
        l_color = d.Color.GREEN if stats["lessons_completed"] == stats["lessons_total"] and stats["lessons_total"] > 0 else d.Color.YELLOW
        l_str = f"{d.c(l_bar, l_color)} {stats['lessons_completed']}/{stats['lessons_total']}"

        # クイズバー
        if stats["quiz_attempts"] > 0:
            rate = stats["quiz_correct"] / stats["quiz_attempts"] * 100
            q_bar = _progress_bar(stats["quiz_correct"], stats["quiz_attempts"])
            q_color = d.Color.GREEN if rate >= 80 else d.Color.YELLOW if rate >= 50 else d.Color.RED
            q_str = f"{d.c(q_bar, q_color)} {rate:.0f}% ({stats['quiz_correct']}/{stats['quiz_attempts']})"
        else:
            q_str = d.c("未受験", d.Color.DIM)

        print(f"  {cat_label:<22} {l_str:<30} {q_str}")

        total_l_done    += stats["lessons_completed"]
        total_l_all     += stats["lessons_total"]
        total_q_correct += stats["quiz_correct"]
        total_q_attempts += stats["quiz_attempts"]

    # 合計行
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
        total_q_str = d.c("未受験", d.Color.DIM)

    print(f"  {'合計':<22} {total_l_str:<30} {total_q_str}")

    # 最終更新日時
    last = progress.get_last_updated()
    if last:
        print()
        print(d.c(f"  最終更新: {last}", d.Color.DIM))

    print()
    d.print_menu([("r", "進捗をリセットする"), ("Enter", "戻る")])
    choice = d.prompt("選択").lower()
    if choice == "r":
        _confirm_reset()


def _confirm_reset():
    d.clear_screen()
    d.print_header("⚠️  進捗リセット")
    print(d.c("  教科書の完了記録とクイズの回答履歴がすべて削除されます。", d.Color.YELLOW))
    print(d.c("  この操作は元に戻せません。", d.Color.RED + d.Color.BOLD))
    print()
    raw = d.prompt("本当にリセットしますか？ [yes でリセット / その他でキャンセル]")
    if raw.strip().lower() == "yes":
        progress.reset()
        d.clear_screen()
        print()
        print(d.c("  ✓ 進捗をリセットしました。", d.Color.GREEN + d.Color.BOLD))
        print()
        d.press_enter()
    else:
        print(d.c("  キャンセルしました。", d.Color.DIM))
        d.press_enter()


# ──────────────────────────────────────────────────────────────
# メインメニュー
# ──────────────────────────────────────────────────────────────

def main():
    while True:
        d.clear_screen()
        print(d.c(BANNER, d.Color.CYAN))
        print(d.c("  メニュー", d.Color.BOLD))
        d.print_menu([
            ("1", "📚 教科書で学ぶ   — 解説を読んで実際に試す"),
            ("2", "📝 クイズで練習する — カテゴリ別 / ランダム出題"),
            ("3", "📖 コマンド一覧を見る"),
            ("4", "📊 学習進捗を確認する"),
            ("q", "終了"),
        ])

        choice = d.prompt("選択")

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
            print(d.c("\n  お疲れさまでした！また学習しましょう。\n", d.Color.GREEN + d.Color.BOLD))
            sys.exit(0)
        else:
            print(d.c("  1〜4 または q を入力してください。", d.Color.RED))
            d.press_enter()


if __name__ == "__main__":
    main()

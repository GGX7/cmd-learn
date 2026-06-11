"""教科書モード：コマンドの解説 + 実際の実行"""

import shutil
import subprocess
from pathlib import Path

import display as d
import progress
import lessons as les
from questions import CATEGORIES

SANDBOX_DIR = Path("/tmp/cmd_learn_sandbox")


# ──────────────────────────────────────────────────────────────
# サンドボックス
# ──────────────────────────────────────────────────────────────

def _setup_sandbox() -> Path:
    """サンドボックスを初期状態にリセットする"""
    if SANDBOX_DIR.exists():
        shutil.rmtree(SANDBOX_DIR)
    SANDBOX_DIR.mkdir(parents=True)

    (SANDBOX_DIR / "hello.txt").write_text(
        "こんにちは、World!\nこれはサンプルファイルです。\n3行目のテキストです。\n"
    )
    (SANDBOX_DIR / "numbers.txt").write_text("3\n1\n4\n1\n5\n9\n2\n6\n5\n3\n")
    (SANDBOX_DIR / "log.txt").write_text(
        "2024-01-01 INFO: サーバーが起動しました\n"
        "2024-01-01 ERROR: データベース接続エラー\n"
        "2024-01-02 INFO: 再接続しました\n"
        "2024-01-02 ERROR: タイムアウトが発生しました\n"
        "2024-01-03 INFO: バックアップ完了\n"
    )
    (SANDBOX_DIR / "data.csv").write_text(
        "name,age,city\nAlice,30,Tokyo\nBob,25,Osaka\nCarol,35,Kyoto\n"
    )
    (SANDBOX_DIR / ".hidden").write_text("これは隠しファイルです\n")
    docs = SANDBOX_DIR / "docs"
    docs.mkdir()
    (docs / "readme.txt").write_text("プロジェクトのドキュメントです\n")
    src = SANDBOX_DIR / "src"
    src.mkdir()
    (src / "main.py").write_text("print('Hello, World!')\n")
    (src / "utils.py").write_text("def helper():\n    pass\n")
    return SANDBOX_DIR


def _run_command(cmd: str, cwd: Path | None = None, timeout: int = 10) -> str:
    """コマンドを実行して出力を返す"""
    try:
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True,
            cwd=str(cwd) if cwd else None,
            timeout=timeout,
        )
        output = (result.stdout + result.stderr).rstrip()
        return output if output else "(出力なし)"
    except subprocess.TimeoutExpired:
        return "(タイムアウト: 10秒以内に完了しませんでした)"
    except Exception as e:
        return f"(エラー: {e})"


# ──────────────────────────────────────────────────────────────
# レッスン表示
# ──────────────────────────────────────────────────────────────

def _show_overview(lesson: dict):
    """タイトル・説明・構文・オプションを表示する"""
    d.clear_screen()
    d.print_header(f"{lesson['command']}  —  {lesson['title']}")

    print(d.c("  📖 説明", d.Color.BOLD + d.Color.CYAN))
    for line in lesson["description"].strip().splitlines():
        print(f"  {line}")
    print()

    print(d.c("  📋 構文", d.Color.BOLD + d.Color.CYAN))
    for line in lesson["syntax"].strip().splitlines():
        print(f"  {d.c(line, d.Color.YELLOW)}")
    print()

    if lesson.get("options"):
        print(d.c("  ⚙️  主なオプション", d.Color.BOLD + d.Color.CYAN))
        for opt, desc in lesson["options"]:
            opt_str = d.c(opt, d.Color.GREEN)
            # 表示幅を揃えるためにパディング（ANSI エスケープ分を補正）
            pad = max(1, 26 - len(opt))
            print(f"  {opt_str}{' ' * pad}{desc}")
        print()

    d.press_enter()


def _run_example(ex: dict, sandbox: Path, idx: int, total: int) -> bool:
    """1つの例を表示・実行する。False を返すとレッスンを中断。"""
    d.clear_screen()
    print(d.c(f"  例 {idx}/{total}", d.Color.DIM))
    print()
    print(d.c(f"  {ex['desc']}", d.Color.BOLD + d.Color.WHITE))
    print()
    print(f"  {d.c('$', d.Color.GREEN + d.Color.BOLD)} "
          f"{d.c(ex['cmd'], d.Color.YELLOW + d.Color.BOLD)}")
    print()

    if not ex.get("runnable", True):
        if ex.get("simulated_output"):
            print(d.c("  ─── 出力イメージ " + "─" * 25, d.Color.DIM))
            for line in ex["simulated_output"].splitlines():
                print(f"  {d.c(line, d.Color.WHITE)}")
            print(d.c("  " + "─" * 41, d.Color.DIM))
        _show_note(ex)
        d.press_enter()
        return True

    choice = d.prompt("[r] 実行する  [s] スキップ  [q] レッスン終了").lower()
    if choice == "q":
        return False

    if choice == "r":
        cwd = sandbox if ex.get("cwd") == "sandbox" else None
        output = _run_command(ex["cmd"], cwd)
        print()
        print(d.c("  ─── 実行結果 " + "─" * 28, d.Color.DIM))
        for line in output.splitlines():
            print(f"  {d.c(line, d.Color.WHITE)}")
        print(d.c("  " + "─" * 41, d.Color.DIM))

    _show_note(ex)
    print()
    d.press_enter()
    return True


def _show_note(ex: dict):
    if ex.get("note"):
        print()
        print(d.c(f"  💡 {ex['note']}", d.Color.CYAN))


def run_lesson(lesson: dict):
    """1つのレッスンを最初から実行する"""
    progress.mark_lesson_started(lesson["id"])
    _show_overview(lesson)

    sandbox = _setup_sandbox()
    examples = lesson["examples"]
    completed_all = True

    for i, ex in enumerate(examples, 1):
        if not _run_example(ex, sandbox, i, len(examples)):
            completed_all = False
            break

    if completed_all:
        progress.mark_lesson_completed(lesson["id"])
        d.clear_screen()
        print()
        print(d.c("  ✓ レッスン完了！進捗が更新されました。", d.Color.GREEN + d.Color.BOLD))
        print()
        d.press_enter()


# ──────────────────────────────────────────────────────────────
# カテゴリ内のレッスン一覧
# ──────────────────────────────────────────────────────────────

def show_lesson_list(category: str):
    lesson_list = les.get_by_category(category)
    cat_label = CATEGORIES.get(category, category)

    while True:
        d.clear_screen()
        d.print_header(f"{cat_label}  —  レッスン一覧")

        raw_data = progress.get_raw()
        for i, lesson in enumerate(lesson_list, 1):
            lid = lesson["id"]
            if lid in raw_data["lessons_completed"]:
                icon = d.c("✓", d.Color.GREEN + d.Color.BOLD)
            elif lid in raw_data["lessons_started"]:
                icon = d.c("→", d.Color.YELLOW + d.Color.BOLD)
            else:
                icon = d.c("○", d.Color.DIM)
            title_str = f"{lesson['command']} — {lesson['title']}"
            print(f"  {icon} {d.c(str(i), d.Color.YELLOW + d.Color.BOLD)}) {title_str}")

        print()
        print(d.c("  ✓=完了  →=開始済み  ○=未開始", d.Color.DIM))
        print()
        d.print_menu([("0", "戻る")])

        raw = d.prompt("選択")
        if raw == "0":
            break
        if raw.isdigit() and 1 <= int(raw) <= len(lesson_list):
            run_lesson(lesson_list[int(raw) - 1])


# ──────────────────────────────────────────────────────────────
# 教科書トップメニュー
# ──────────────────────────────────────────────────────────────

def run_textbook():
    lesson_ids_by_cat = les.get_lesson_ids_by_category()

    while True:
        d.clear_screen()
        d.print_header("📚 教科書で学ぶ")
        print(d.c("  コマンドの解説を読み、実際に試してみよう！\n", d.Color.DIM))

        raw_data = progress.get_raw()
        keys = list(CATEGORIES.keys())

        for i, (cat_key, cat_label) in enumerate(CATEGORIES.items(), 1):
            ids = lesson_ids_by_cat.get(cat_key, [])
            completed = sum(1 for lid in ids if lid in raw_data["lessons_completed"])
            total = len(ids)
            filled = "█" * completed
            empty  = "░" * (total - completed)
            bar_color = d.Color.GREEN if completed == total and total > 0 else d.Color.YELLOW
            bar = d.c(filled + empty, bar_color)
            count = d.c(f"{completed}/{total}", d.Color.DIM)
            print(f"  {d.c(str(i), d.Color.YELLOW + d.Color.BOLD)})  {cat_label:<22} {bar} {count}")

        print()
        d.print_menu([("0", "戻る")])
        raw = d.prompt("選択")

        if raw == "0":
            break
        if raw.isdigit() and 1 <= int(raw) <= len(keys):
            show_lesson_list(keys[int(raw) - 1])

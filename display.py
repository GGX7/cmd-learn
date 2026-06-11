"""ターミナル表示ユーティリティ（ANSI色付き）"""

# ANSI カラーコード
class Color:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    RED     = "\033[91m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    BLUE    = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN    = "\033[96m"
    WHITE   = "\033[97m"
    DIM     = "\033[2m"


def c(text: str, color: str) -> str:
    return f"{color}{text}{Color.RESET}"


def clear_screen():
    print("\033[2J\033[H", end="")


def print_header(title: str):
    width = 60
    print()
    print(c("=" * width, Color.CYAN))
    print(c(title.center(width), Color.BOLD + Color.CYAN))
    print(c("=" * width, Color.CYAN))
    print()


def print_question(number: int, total: int, question: str, category: str, difficulty: int):
    stars = "★" * difficulty + "☆" * (3 - difficulty)
    print(c(f"  [{category}] {stars}  問題 {number}/{total}", Color.DIM))
    print()
    print(c(f"  {question}", Color.WHITE + Color.BOLD))
    print()


def print_choices(choices: list[str]):
    labels = ["A", "B", "C", "D"]
    for i, choice in enumerate(choices):
        label = c(f"  {labels[i]})", Color.YELLOW + Color.BOLD)
        print(f"{label} {choice}")
    print()


def print_correct(explanation: str):
    print(c("  ✓ 正解！", Color.GREEN + Color.BOLD))
    print(c(f"  {explanation}", Color.DIM))
    print()


def print_wrong(correct: str, explanation: str):
    print(c("  ✗ 不正解", Color.RED + Color.BOLD))
    print(c(f"  正解: {correct}", Color.YELLOW))
    print(c(f"  {explanation}", Color.DIM))
    print()


def print_score(correct: int, total: int):
    rate = correct / total * 100 if total > 0 else 0
    print()
    print(c("─" * 40, Color.CYAN))
    print(c("  結果", Color.BOLD))
    print(c("─" * 40, Color.CYAN))
    print(f"  正解数: {c(str(correct), Color.GREEN + Color.BOLD)} / {total}")
    print(f"  正答率: {c(f'{rate:.0f}%', Color.YELLOW + Color.BOLD)}")
    if rate >= 80:
        print(c("  素晴らしい！", Color.GREEN + Color.BOLD))
    elif rate >= 50:
        print(c("  もう少し！復習してみよう", Color.YELLOW))
    else:
        print(c("  基礎から確認しよう", Color.MAGENTA))
    print()


def prompt(text: str) -> str:
    return input(c(f"  {text} > ", Color.CYAN)).strip()


def press_enter():
    input(c("  Enter キーで続ける...", Color.DIM))


def print_menu(items: list[tuple[str, str]]):
    """(キー, 説明) のリストを表示する"""
    for key, desc in items:
        print(f"  {c(key, Color.YELLOW + Color.BOLD)}  {desc}")
    print()

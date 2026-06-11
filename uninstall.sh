#!/usr/bin/env bash
# cmd-learn アンインストーラー

INSTALL_DIR="$HOME/.cmd-learn"
BIN_DIR="$HOME/.local/bin"

GREEN='\033[0;32m'; YELLOW='\033[0;33m'; BOLD='\033[1m'; RESET='\033[0m'

echo ""
echo -e "${BOLD}  cmd-learn アンインストーラー${RESET}"
echo "  ━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# コマンドとインストールディレクトリを削除
rm -f "$BIN_DIR/cmd-learn"
rm -rf "$INSTALL_DIR"
echo -e "${GREEN}✓${RESET} コマンドとファイルを削除しました"

# 学習進捗データの削除（任意）
if [[ -f "$HOME/.command_learn_progress.json" ]]; then
    printf "${YELLOW}  学習進捗データも削除しますか？ [y/N]${RESET} "
    read -r answer
    if [[ "$answer" =~ ^[Yy]$ ]]; then
        rm -f "$HOME/.command_learn_progress.json"
        echo -e "${GREEN}✓${RESET} 進捗データを削除しました"
    else
        echo "  進捗データは残しました: ~/.command_learn_progress.json"
    fi
fi

echo ""
echo -e "${BOLD}  アンインストール完了${RESET}"
echo ""
echo "  PATH の設定行（# cmd-learn）も"
echo "  ~/.zshrc または ~/.bashrc から手動で削除してください。"
echo ""

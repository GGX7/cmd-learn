#!/usr/bin/env bash
# cmd-learn インストーラー
# 使い方: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/実際のユーザー名/cmd-learn/main/install.sh)"

set -e

REPO_URL="https://github.com/GGX7/cmd-learn.git"
INSTALL_DIR="$HOME/.cmd-learn"
BIN_DIR="$HOME/.local/bin"
SHELL_CONFIG=""

# ── カラー出力 ──────────────────────────────────────────────
RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[0;33m'
CYAN='\033[0;36m'; BOLD='\033[1m'; RESET='\033[0m'

info()    { echo -e "${CYAN}→${RESET} $1"; }
success() { echo -e "${GREEN}✓${RESET} $1"; }
warn()    { echo -e "${YELLOW}!${RESET} $1"; }
abort()   { echo -e "\n${RED}✗ $1${RESET}" >&2; exit 1; }

# ── Python 確認 ─────────────────────────────────────────────
check_python() {
    if ! command -v python3 &>/dev/null; then
        abort "Python 3 が見つかりません。先にインストールしてください。
  macOS:         brew install python3
  Ubuntu/Debian: sudo apt install python3
  Fedora/RHEL:   sudo dnf install python3"
    fi

    local ver major minor
    ver=$(python3 -c 'import sys; print("%d.%d" % sys.version_info[:2])')
    major=${ver%%.*}; minor=${ver##*.}

    if [[ $major -lt 3 || ($major -eq 3 && $minor -lt 9) ]]; then
        abort "Python 3.9 以上が必要です（現在: $ver）"
    fi
    success "Python $ver を確認"
}

# ── ファイル取得 ─────────────────────────────────────────────
download_files() {
    if command -v git &>/dev/null; then
        if [[ -d "$INSTALL_DIR/.git" ]]; then
            info "最新版に更新中..."
            git -C "$INSTALL_DIR" pull --quiet
            success "更新完了"
        else
            info "リポジトリをダウンロード中..."
            git clone --quiet "$REPO_URL" "$INSTALL_DIR"
            success "ダウンロード完了"
        fi
    else
        # git がない場合は zip で取得
        if ! command -v curl &>/dev/null; then
            abort "curl または git が必要です"
        fi
        info "curl でダウンロード中..."
        local zip_url="${REPO_URL%.git}/archive/refs/heads/main.zip"
        local tmp
        tmp=$(mktemp -d)
        curl -fsSL "$zip_url" -o "$tmp/cmd-learn.zip"
        unzip -q "$tmp/cmd-learn.zip" -d "$tmp"
        rm -rf "$INSTALL_DIR"
        mv "$tmp"/cmd-learn-main "$INSTALL_DIR"
        rm -rf "$tmp"
        success "ダウンロード完了"
    fi
}

# ── コマンド配置 ─────────────────────────────────────────────
setup_command() {
    chmod +x "$INSTALL_DIR/cmd-learn"
    mkdir -p "$BIN_DIR"
    ln -sf "$INSTALL_DIR/cmd-learn" "$BIN_DIR/cmd-learn"
    success "コマンドを $BIN_DIR/cmd-learn に配置"
}

# ── PATH 設定 ────────────────────────────────────────────────
setup_path() {
    # すでに PATH に含まれているか確認
    if [[ ":$PATH:" == *":$BIN_DIR:"* ]]; then
        success "PATH はすでに設定済みです"
        return
    fi

    # シェル設定ファイルを検出
    if   [[ -f "$HOME/.zshrc" ]];       then SHELL_CONFIG="$HOME/.zshrc"
    elif [[ -f "$HOME/.bashrc" ]];      then SHELL_CONFIG="$HOME/.bashrc"
    elif [[ -f "$HOME/.bash_profile" ]]; then SHELL_CONFIG="$HOME/.bash_profile"
    else
        warn "シェル設定ファイルが見つかりませんでした。"
        warn "手動で以下を追加してください: export PATH=\"\$PATH:$BIN_DIR\""
        return
    fi

    # 重複追記を防ぐ
    if grep -q "cmd-learn" "$SHELL_CONFIG" 2>/dev/null; then
        success "PATH はすでに $SHELL_CONFIG に記載済みです"
        return
    fi

    printf '\n# cmd-learn\nexport PATH="$PATH:%s"\n' "$BIN_DIR" >> "$SHELL_CONFIG"
    success "PATH を $SHELL_CONFIG に追加"
}

# ── メイン ───────────────────────────────────────────────────
main() {
    echo ""
    echo -e "${BOLD}${CYAN}  cmd-learn インストーラー${RESET}"
    echo "  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""

    check_python
    download_files
    setup_command
    setup_path

    echo ""
    echo -e "${GREEN}${BOLD}  インストール完了！${RESET}"
    echo ""
    if [[ -n "$SHELL_CONFIG" ]]; then
        echo "  ① 設定を反映してください:"
        echo ""
        echo -e "     ${BOLD}source $SHELL_CONFIG${RESET}"
    fi
    echo ""
    echo "  ② 以下のコマンドで起動できます:"
    echo ""
    echo -e "     ${BOLD}cmd-learn${RESET}"
    echo ""
}

main

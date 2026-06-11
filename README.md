# cmd-learn — Linux / macOS コマンド学習ツール

ターミナルで動作する、初心者向けのインタラクティブなコマンド学習ツールです。  
**教科書モード**（解説 + 実際に実行）と **クイズモード**（4択 / コマンド入力）の2つの学習スタイルに対応しています。

---

## 学べるコマンド（全6カテゴリ・124問・40レッスン）

| カテゴリ | 内容 |
|---------|------|
| 📁 ファイル操作 | ls, cd, cp, mv, rm, find, chmod, ln, tar など |
| 📝 テキスト処理 | grep, awk, sed, sort, cut, xargs, tee など |
| ⚙️  プロセス管理 | ps, kill, crontab, lsof, nice, watch など |
| 🌐 ネットワーク | ping, curl, ssh, scp, dig, netstat など |
| 🐚 シェル・環境 | env, export, alias, history, 変数, スクリプト基礎 など |
| 💻 システム情報 | uname, df, du, free, dmesg, sysctl など |

---

## インストール

### 必要なもの
- macOS または Linux
- Python 3.9 以上

### ワンコマンドインストール

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/実際のユーザー名/cmd-learn/main/install.sh)"
```

インストール後、設定を反映して起動します：

```bash
source ~/.zshrc   # または source ~/.bashrc
cmd-learn
```

### 手動インストール（git clone）

```bash
git clone https://github.com/実際のユーザー名/cmd-learn.git ~/.cmd-learn
~/.cmd-learn/cmd-learn
```

---

## 使い方

```
メニュー
  1. 📚 教科書で学ぶ   — 解説を読んで実際に試す
  2. 📝 クイズで練習する — カテゴリ別 / ランダム出題
  3. 📖 コマンド一覧を見る
  4. 📊 学習進捗を確認する
  q. 終了
```

- **教科書モード**: コマンドの説明・構文・オプションを読み、実際にコマンドを実行して結果を確認できます
- **クイズモード**: 4択問題またはコマンド入力形式で腕試しできます
- **進捗管理**: レッスン完了数とクイズ正答率をカテゴリ別に可視化します

---

## アップデート

インストールスクリプトを再実行すると最新版に更新されます：

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/実際のユーザー名/cmd-learn/main/install.sh)"
```

---

## アンインストール

```bash
~/.cmd-learn/uninstall.sh
```

---

## 動作確認済み環境

- macOS 13 以上
- Ubuntu 22.04 以上
- Python 3.9 / 3.10 / 3.11 / 3.12

---

## ライセンス

MIT

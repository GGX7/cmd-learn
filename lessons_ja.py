"""教科書モードのレッスンデータ（日本語）"""

LESSONS: list[dict] = [

    # ──────────────────────────────────────────────────────────
    # ファイル操作
    # ──────────────────────────────────────────────────────────
    {
        "id": "lesson_ls", "category": "file",
        "command": "ls",
        "title": "ファイル・ディレクトリの一覧表示",
        "description": (
            "ls（list の略）はディレクトリの内容を一覧表示するコマンドです。\n"
            "ターミナルを開いたらまず ls で周囲を確認するのが基本です。\n"
            "オプションを組み合わせることで、詳細情報や隠しファイルも確認できます。"
        ),
        "syntax": "ls [オプション] [パス]",
        "options": [
            ("-a",  "隠しファイル（. で始まるファイル）も表示する"),
            ("-l",  "詳細情報（権限・サイズ・日時）を一行ずつ表示する"),
            ("-h",  "-l と組み合わせてサイズを KB/MB 形式で表示する"),
            ("-t",  "更新時刻が新しい順に並べ替えて表示する"),
        ],
        "examples": [
            {"cmd": "ls", "desc": "カレントディレクトリの内容を表示",
             "note": "ファイルとディレクトリが並んで表示されます。", "runnable": True, "cwd": "sandbox"},
            {"cmd": "ls -la", "desc": "隠しファイルも含めて詳細情報を表示",
             "note": "先頭が . のファイルも表示されます。左端の drwxr-xr-x は権限情報です。", "runnable": True, "cwd": "sandbox"},
            {"cmd": "ls -lh docs", "desc": "docs ディレクトリの詳細をサイズ付きで表示",
             "note": "パスを指定すると、そのディレクトリの内容を確認できます。", "runnable": True, "cwd": "sandbox"},
        ],
    },
    {
        "id": "lesson_pwd_cd", "category": "file",
        "command": "pwd / cd",
        "title": "現在地の確認とディレクトリ移動",
        "description": (
            "pwd（print working directory）は現在いるディレクトリのパスを表示します。\n"
            "cd（change directory）はディレクトリを移動するコマンドです。\n"
            "/ で始まる絶対パスと、現在地からの相対パスの両方が使えます。"
        ),
        "syntax": "pwd\ncd [移動先のパス]",
        "options": [
            ("~",  "ホームディレクトリを表す特殊記号（例: cd ~/Desktop）"),
            ("..", "一つ上のディレクトリ（例: cd ..）"),
            ("-",  "直前にいたディレクトリに戻る（例: cd -）"),
        ],
        "examples": [
            {"cmd": "pwd", "desc": "現在のディレクトリ（絶対パス）を表示",
             "note": "/home/ユーザー名 や /Users/ユーザー名 の形式で表示されます。", "runnable": True, "cwd": None},
            {"cmd": "cd /tmp && pwd", "desc": "/tmp ディレクトリに移動して現在地を確認",
             "note": "&& は「前のコマンドが成功したら次を実行」する記号です。", "runnable": True, "cwd": None},
            {"cmd": "cd ~ && pwd", "desc": "ホームディレクトリに移動",
             "note": "~ はログイン中のユーザーのホームディレクトリを指します。", "runnable": True, "cwd": None},
        ],
    },
    {
        "id": "lesson_mkdir_touch", "category": "file",
        "command": "mkdir / touch",
        "title": "ファイルとディレクトリの新規作成",
        "description": (
            "mkdir（make directory）は新しいディレクトリを作成します。\n"
            "touch は空のファイルを新規作成するコマンドです。\n"
            "既存ファイルに対して touch を使うと、更新日時だけが変更されます。"
        ),
        "syntax": "mkdir [オプション] ディレクトリ名\ntouch ファイル名",
        "options": [
            ("mkdir -p", "中間ディレクトリも一括作成する（例: mkdir -p a/b/c）"),
            ("touch -t", "タイムスタンプを指定して作成・更新する"),
        ],
        "examples": [
            {"cmd": "mkdir myproject && ls", "desc": "myproject ディレクトリを作成して確認",
             "note": "ls で新しいディレクトリが増えていることを確認できます。", "runnable": True, "cwd": "sandbox"},
            {"cmd": "mkdir -p myproject/src/utils && ls myproject/src", "desc": "-p で階層ディレクトリを一括作成",
             "note": "深い階層も一度に作れます。-p を付けるとエラーにもなりません。", "runnable": True, "cwd": "sandbox"},
            {"cmd": "touch myproject/README.md && ls myproject", "desc": "README.md を作成してディレクトリ内容を確認",
             "note": "touch で中身が空のファイルが作成されました。", "runnable": True, "cwd": "sandbox"},
        ],
    },
    {
        "id": "lesson_cp_mv", "category": "file",
        "command": "cp / mv",
        "title": "ファイルのコピーと移動・名前変更",
        "description": (
            "cp（copy）はファイルやディレクトリをコピーします。\n"
            "mv（move）はファイルの移動と名前変更の両方に使います。\n"
            "同じディレクトリ内での mv は名前変更として機能します。"
        ),
        "syntax": "cp [オプション] コピー元 コピー先\nmv 移動元 移動先",
        "options": [
            ("cp -r", "ディレクトリを中身ごとコピーする（再帰的コピー）"),
            ("cp -i", "上書き前に確認を求める"),
            ("mv -i", "上書き前に確認を求める"),
        ],
        "examples": [
            {"cmd": "cp hello.txt hello_backup.txt && ls", "desc": "hello.txt を hello_backup.txt にコピー",
             "note": "元のファイルはそのまま残り、コピーが作成されます。", "runnable": True, "cwd": "sandbox"},
            {"cmd": "mv hello_backup.txt docs/hello_backup.txt && ls docs", "desc": "hello_backup.txt を docs ディレクトリに移動",
             "note": "mv はカット＆ペーストに相当します。元の場所のファイルはなくなります。", "runnable": True, "cwd": "sandbox"},
            {"cmd": "mv docs/hello_backup.txt docs/renamed.txt && ls docs", "desc": "ファイル名を renamed.txt に変更",
             "note": "同じディレクトリ内の mv は名前変更になります。", "runnable": True, "cwd": "sandbox"},
        ],
    },
    {
        "id": "lesson_rm", "category": "file",
        "command": "rm",
        "title": "ファイルとディレクトリの削除",
        "description": (
            "rm（remove）はファイルやディレクトリを削除します。\n"
            "⚠️  rm で削除したファイルはゴミ箱に入らず、元に戻せません。\n"
            "特に rm -rf は強力すぎるため、慎重に使いましょう。"
        ),
        "syntax": "rm [オプション] ファイル名",
        "options": [
            ("-r", "ディレクトリを中身ごと削除する（再帰的削除）"),
            ("-f", "確認なしで強制削除する"),
            ("-i", "削除前に確認を求める（初心者に推奨）"),
        ],
        "examples": [
            {"cmd": "touch trash.txt && ls", "desc": "削除用のテストファイルを作成して確認",
             "note": "まず削除するファイルを用意します。", "runnable": True, "cwd": "sandbox"},
            {"cmd": "rm trash.txt && ls", "desc": "trash.txt を削除して結果を確認",
             "note": "ファイルが消えました。ゴミ箱には入りません！", "runnable": True, "cwd": "sandbox"},
            {"cmd": "mkdir tempdir && touch tempdir/a.txt tempdir/b.txt && rm -r tempdir && ls",
             "desc": "ディレクトリを中身ごと削除",
             "note": "-r（recursive）なしではディレクトリは削除できません。", "runnable": True, "cwd": "sandbox"},
        ],
    },
    {
        "id": "lesson_find", "category": "file",
        "command": "find",
        "title": "ファイルの検索",
        "description": (
            "find はディレクトリを再帰的に検索してファイルを探すコマンドです。\n"
            "ファイル名のパターン・種類・更新日時など様々な条件で絞り込みができます。\n"
            "大量のファイルの中から目的のものを探すときに非常に役立ちます。"
        ),
        "syntax": "find 検索開始パス [条件] [アクション]",
        "options": [
            ("-name '*.txt'", "ファイル名のパターンで検索（ワイルドカード使用可）"),
            ("-type f",       "ファイルのみを対象にする"),
            ("-type d",       "ディレクトリのみを対象にする"),
            ("-mtime -7",     "7日以内に更新されたファイルを検索"),
        ],
        "examples": [
            {"cmd": "find . -name '*.txt'", "desc": "カレントディレクトリ以下の .txt ファイルをすべて検索",
             "note": ". は「現在のディレクトリ」です。サブディレクトリも自動で検索されます。", "runnable": True, "cwd": "sandbox"},
            {"cmd": "find . -type d", "desc": "ディレクトリだけを検索",
             "note": "-type d でディレクトリのみが表示されます。", "runnable": True, "cwd": "sandbox"},
            {"cmd": "find . -name '*.txt' -type f", "desc": "条件を組み合わせて .txt ファイルのみ検索",
             "note": "複数の条件は AND で組み合わせられます。", "runnable": True, "cwd": "sandbox"},
        ],
    },
    # ──────────────────────────────────────────────────────────
    # テキスト処理
    # ──────────────────────────────────────────────────────────
    {
        "id": "lesson_cat", "category": "text",
        "command": "cat / head / tail",
        "title": "ファイルの内容表示",
        "description": (
            "cat はファイルの全内容を表示します。\n"
            "head はファイルの先頭（デフォルト10行）、tail は末尾（デフォルト10行）を表示します。\n"
            "tail -f はログファイルのリアルタイム監視によく使われます。"
        ),
        "syntax": "cat [ファイル]\nhead [-n 行数] [ファイル]\ntail [-n 行数] [ファイル]",
        "options": [
            ("cat -n",    "行番号を付けて表示する"),
            ("head -n N", "先頭 N 行を表示する"),
            ("tail -n N", "末尾 N 行を表示する"),
            ("tail -f",   "追記をリアルタイムで追跡する（Ctrl+C で終了）"),
        ],
        "examples": [
            {"cmd": "cat hello.txt", "desc": "hello.txt の全内容を表示",
             "note": "短いファイルは cat が便利。長いファイルは less を使いましょう。", "runnable": True, "cwd": "sandbox"},
            {"cmd": "cat -n log.txt", "desc": "行番号付きで log.txt を表示",
             "note": "-n で行番号が付き、エラーの位置特定などに役立ちます。", "runnable": True, "cwd": "sandbox"},
            {"cmd": "head -n 3 log.txt", "desc": "log.txt の先頭3行を表示",
             "note": "大きなファイルの先頭だけを素早く確認できます。", "runnable": True, "cwd": "sandbox"},
            {"cmd": "tail -n 3 log.txt", "desc": "log.txt の末尾3行を表示",
             "note": "ログファイルは末尾に最新情報があるので tail をよく使います。", "runnable": True, "cwd": "sandbox"},
        ],
    },
    {
        "id": "lesson_grep", "category": "text",
        "command": "grep",
        "title": "テキストのパターン検索",
        "description": (
            "grep はファイルの中から指定したパターン（文字列や正規表現）を含む行を検索します。\n"
            "ログ解析やコードの調査など、日常的に使う重要なコマンドです。\n"
            "パイプ（|）と組み合わせると特に強力になります。"
        ),
        "syntax": "grep [オプション] パターン [ファイル]",
        "options": [
            ("-i", "大文字・小文字を区別しない"),
            ("-n", "一致した行番号も表示する"),
            ("-r", "ディレクトリを再帰的に検索する"),
            ("-v", "パターンに一致しない行を表示する（反転検索）"),
            ("-c", "一致した行数のみを表示する"),
        ],
        "examples": [
            {"cmd": "grep ERROR log.txt", "desc": "log.txt から ERROR を含む行を表示",
             "note": "大文字小文字は区別されます。-i を付けると error も対象になります。", "runnable": True, "cwd": "sandbox"},
            {"cmd": "grep -n INFO log.txt", "desc": "INFO を含む行を行番号付きで表示",
             "note": "-n で何行目に書かれているか分かり、調査が効率的になります。", "runnable": True, "cwd": "sandbox"},
            {"cmd": "grep -c ERROR log.txt", "desc": "ERROR を含む行数だけを表示",
             "note": "-c は count の略。エラー件数の集計などに使えます。", "runnable": True, "cwd": "sandbox"},
            {"cmd": "grep -r txt .", "desc": "現在のディレクトリ以下すべてから txt を含む行を検索",
             "note": "-r でサブディレクトリも対象になります。", "runnable": True, "cwd": "sandbox"},
        ],
    },
    {
        "id": "lesson_wc_sort", "category": "text",
        "command": "wc / sort / uniq",
        "title": "行数カウント・並べ替え・重複排除",
        "description": (
            "wc（word count）は行数・単語数・バイト数を数えます。\n"
            "sort はテキストを行単位で並べ替えます。\n"
            "uniq は連続する重複行を取り除きます。sort と組み合わせるのが定番です。"
        ),
        "syntax": "wc [-l|-w|-c] [ファイル]\nsort [オプション] [ファイル]\nuniq [ファイル]",
        "options": [
            ("wc -l",   "行数のみを表示する"),
            ("sort -n", "数値として並べ替える（文字列順と異なる）"),
            ("sort -r", "逆順で並べ替える"),
            ("sort -u", "並べ替えながら重複を除去する"),
            ("uniq -c", "各行の出現回数を先頭に表示する"),
        ],
        "examples": [
            {"cmd": "wc -l log.txt", "desc": "log.txt の行数を数える",
             "note": "wc -l はログの件数確認によく使います。", "runnable": True, "cwd": "sandbox"},
            {"cmd": "sort numbers.txt", "desc": "numbers.txt を文字列順で並べ替え",
             "note": "デフォルトは文字列順なので 10 < 2 になる点に注意！", "runnable": True, "cwd": "sandbox"},
            {"cmd": "sort -n numbers.txt", "desc": "数値として正しく並べ替え",
             "note": "-n で 1, 2, 3... の正しい数値順になります。", "runnable": True, "cwd": "sandbox"},
            {"cmd": "sort numbers.txt | uniq", "desc": "並べ替えてから重複行を除去",
             "note": "| はパイプ。前のコマンドの出力を次のコマンドに渡します。", "runnable": True, "cwd": "sandbox"},
        ],
    },
    {
        "id": "lesson_sed", "category": "text",
        "command": "sed",
        "title": "テキストの置換と変換",
        "description": (
            "sed（stream editor）はテキストをストリーム処理するコマンドです。\n"
            "最もよく使われる機能は s（substitute）コマンドによる文字列置換です。\n"
            "ファイルを直接編集せずに変換結果を確認してから使うのが安全です。"
        ),
        "syntax": "sed 's/検索/置換/フラグ' ファイル",
        "options": [
            ("s/old/new/",  "最初の一致を置換する"),
            ("s/old/new/g", "行内の全一致を置換する（g = global）"),
            ("-i",          "ファイルを直接書き換える（バックアップ推奨）"),
            ("-n 'Np'",     "N 行目だけを表示する"),
        ],
        "examples": [
            {"cmd": "sed 's/INFO/情報/' log.txt", "desc": "各行の最初の INFO を 情報 に置換して表示",
             "note": "ファイル自体は変更されません。置換結果が標準出力に表示されます。", "runnable": True, "cwd": "sandbox"},
            {"cmd": "sed 's/ERROR/エラー/g' log.txt", "desc": "各行のすべての ERROR をエラーに置換",
             "note": "g フラグで行内のすべての一致が置換されます。", "runnable": True, "cwd": "sandbox"},
            {"cmd": "sed -n '2,3p' log.txt", "desc": "2〜3行目だけを表示",
             "note": "-n で出力を抑制し、p で特定の行だけ表示できます。", "runnable": True, "cwd": "sandbox"},
        ],
    },
    {
        "id": "lesson_pipe", "category": "text",
        "command": "| / > / >>",
        "title": "パイプとリダイレクト",
        "description": (
            "パイプ（|）は複数のコマンドをつなぎ、前の出力を次のコマンドの入力にします。\n"
            "> はコマンドの出力をファイルに書き込みます（上書き）。\n"
            ">> は出力をファイルに追記します。\n"
            "これらを組み合わせることで複雑な処理を一行で書けます。"
        ),
        "syntax": "コマンド1 | コマンド2\nコマンド > ファイル\nコマンド >> ファイル",
        "options": [
            ("|",  "パイプ：前のコマンドの出力を次のコマンドに渡す"),
            (">",  "リダイレクト：出力をファイルに書き込む（上書き）"),
            (">>", "リダイレクト：出力をファイルに追記する"),
            ("2>", "標準エラー出力をファイルにリダイレクトする"),
        ],
        "examples": [
            {"cmd": "grep ERROR log.txt | wc -l", "desc": "ERROR を含む行数をカウント（grep + wc のパイプ）",
             "note": "grep の出力が wc の入力になります。これがパイプの仕組みです。", "runnable": True, "cwd": "sandbox"},
            {"cmd": "sort numbers.txt | uniq | wc -l", "desc": "数値ファイルの重複除去後の行数を確認",
             "note": "3つのコマンドをつないで複雑な処理が一行で書けます。", "runnable": True, "cwd": "sandbox"},
            {"cmd": "echo '追記テキスト' >> hello.txt && cat hello.txt", "desc": "hello.txt にテキストを追記して確認",
             "note": ">> で追記、> で上書きです。> は既存の内容が消えるので注意！", "runnable": True, "cwd": "sandbox"},
        ],
    },
    # ──────────────────────────────────────────────────────────
    # プロセス管理
    # ──────────────────────────────────────────────────────────
    {
        "id": "lesson_ps", "category": "process",
        "command": "ps / top",
        "title": "実行中プロセスの確認",
        "description": (
            "ps（process status）は実行中のプロセスの一覧を表示します。\n"
            "top は CPU・メモリ使用率をリアルタイムで表示するモニタリングツールです。\n"
            "システムの状態確認やリソースを大量消費しているプロセスの特定に使います。"
        ),
        "syntax": "ps [オプション]\ntop",
        "options": [
            ("ps aux",      "すべてのユーザーのプロセスを詳細表示"),
            ("ps -ef",      "フルフォーマットで全プロセスを表示（PPID付き）"),
            ("top -b -n 1", "1回だけ出力して終了（非インタラクティブモード）"),
        ],
        "examples": [
            {"cmd": "ps", "desc": "現在のシェルに関連するプロセスを表示",
             "note": "PID（プロセスID）・TTY・TIME・CMD が表示されます。", "runnable": True, "cwd": None},
            {"cmd": "ps aux | head -10", "desc": "全プロセスを詳細表示（先頭10件）",
             "note": "%CPU と %MEM でリソース使用率が分かります。", "runnable": True, "cwd": None},
            {"cmd": "ps aux | grep python", "desc": "python という名前のプロセスを検索",
             "note": "特定のプロセスが動いているか確認したいときは grep と組み合わせます。", "runnable": True, "cwd": None},
        ],
    },
    {
        "id": "lesson_kill", "category": "process",
        "command": "kill / killall",
        "title": "プロセスの終了",
        "description": (
            "kill はプロセスID（PID）を指定してプロセスにシグナルを送ります。\n"
            "killall はプロセス名を指定して同名の全プロセスを対象にします。\n"
            "デフォルトは SIGTERM（終了要求）で、プロセスは後処理をしてから終了します。\n"
            "SIGKILL（-9）は強制終了ですが、後処理ができないため最後の手段にしましょう。"
        ),
        "syntax": "kill [-シグナル番号] PID\nkillall [-シグナル] プロセス名",
        "options": [
            ("kill PID",    "デフォルト（SIGTERM=15）でプロセスに終了を要求"),
            ("kill -9 PID", "SIGKILL で強制終了（最後の手段）"),
            ("killall 名前","同名の全プロセスに SIGTERM を送る"),
            ("kill -l",     "使えるシグナルの一覧を表示"),
        ],
        "examples": [
            {"cmd": "kill -l | head -5", "desc": "利用可能なシグナルの一覧（先頭5件）",
             "note": "SIGTERM=15（終了要求）と SIGKILL=9（強制終了）が最もよく使われます。", "runnable": True, "cwd": None},
            {"cmd": "sleep 120 & PID=$! && echo \"起動 PID=$PID\" && kill $PID && echo \"終了しました\"",
             "desc": "sleep プロセスを起動して即座に終了させる",
             "note": "$! は直前にバックグラウンド起動したプロセスのPIDです。", "runnable": True, "cwd": None},
            {"cmd": "ps aux | grep sleep", "desc": "sleep という名前のプロセスを検索して確認",
             "note": "先ほど kill したので sleep プロセスが存在しないことが確認できます。", "runnable": True, "cwd": None},
        ],
    },
    {
        "id": "lesson_bg", "category": "process",
        "command": "& / jobs / fg / bg",
        "title": "バックグラウンド実行とジョブ管理",
        "description": (
            "& を末尾に付けるとコマンドをバックグラウンドで実行できます。\n"
            "jobs で現在のバックグラウンドジョブ一覧を確認し、fg で前面に戻せます。\n"
            "Ctrl+Z でプロセスを一時停止し、bg でバックグラウンド再開もできます。"
        ),
        "syntax": "コマンド &\njobs\nfg [%ジョブ番号]\nbg [%ジョブ番号]",
        "options": [
            ("command &", "コマンドをバックグラウンドで起動"),
            ("Ctrl+Z",    "フォアグラウンドのプロセスを一時停止"),
            ("fg %1",     "ジョブ番号1をフォアグラウンドに戻す"),
            ("bg %1",     "停止中のジョブ1をバックグラウンドで再開"),
        ],
        "examples": [
            {"cmd": "sleep 30 & sleep 30 & jobs", "desc": "2つのバックグラウンドジョブを起動して一覧表示",
             "note": "[ ] 内の数字がジョブ番号です。fg %1 で1番目をフォアグラウンドにできます。", "runnable": True, "cwd": None},
            {"cmd": "jobs | wc -l", "desc": "現在のバックグラウンドジョブ数を確認",
             "note": "ジョブが0件のときは何も表示されません。", "runnable": True, "cwd": None},
        ],
    },
    # ──────────────────────────────────────────────────────────
    # ネットワーク
    # ──────────────────────────────────────────────────────────
    {
        "id": "lesson_ping", "category": "network",
        "command": "ping",
        "title": "ネットワーク疎通確認",
        "description": (
            "ping は ICMP エコー要求を送り、指定したホストへの到達性と応答時間を確認します。\n"
            "ネットワーク障害の最初の診断ステップとして使われます。\n"
            "Linux ではデフォルトで無限に送り続けます（Ctrl+C で停止）。"
        ),
        "syntax": "ping [-c 回数] ホスト名またはIPアドレス",
        "options": [
            ("-c N",  "N 回送ったら自動的に停止する"),
            ("-i 秒", "送信間隔を指定する（デフォルト1秒）"),
        ],
        "examples": [
            {"cmd": "ping -c 3 localhost", "desc": "自分自身（localhost）への疎通確認（3回）",
             "note": "localhost（127.0.0.1）は常に応答します。time= が応答時間（ms）です。", "runnable": True, "cwd": None},
            {"cmd": "ping -c 2 8.8.8.8", "desc": "Google の DNS サーバー（8.8.8.8）への疎通確認",
             "note": "インターネット接続がある場合に応答が返ります。", "runnable": True, "cwd": None},
        ],
    },
    {
        "id": "lesson_curl", "category": "network",
        "command": "curl / wget",
        "title": "HTTP リクエストとファイルダウンロード",
        "description": (
            "curl は URL へのリクエストを送り、レスポンスを表示または保存するコマンドです。\n"
            "wget はファイルをダウンロードして保存するコマンドです。\n"
            "API の動作確認やファイルのダウンロードに広く使われます。"
        ),
        "syntax": "curl [オプション] URL\nwget [オプション] URL",
        "options": [
            ("-o ファイル名", "レスポンスをファイルに保存する"),
            ("-I",           "ヘッダーのみ取得する（レスポンスコード確認に便利）"),
            ("-s",           "進捗を表示しない（サイレントモード）"),
            ("-L",           "リダイレクトに従う"),
        ],
        "examples": [
            {"cmd": "curl -I https://example.com", "desc": "example.com の HTTP レスポンスヘッダーを確認",
             "note": "HTTP/1.1 200 OK などのステータスコードとヘッダーが表示されます。", "runnable": True, "cwd": None},
            {"cmd": "curl -s https://httpbin.org/ip", "desc": "自分のパブリック IP アドレスを確認",
             "note": "httpbin.org は HTTP のテスト用公開サービスです。-s で進捗を非表示にします。", "runnable": True, "cwd": None},
        ],
    },
    {
        "id": "lesson_ssh_dns", "category": "network",
        "command": "ssh / nslookup",
        "title": "リモート接続と DNS 確認",
        "description": (
            "ssh（Secure Shell）は暗号化されたリモートログインを行うコマンドです。\n"
            "nslookup はドメイン名を IP アドレスに変換（DNS 問い合わせ）します。\n"
            "サーバー管理やリモートワーク環境では必須の知識です。"
        ),
        "syntax": "ssh [ユーザー名@]ホスト名\nnslookup ドメイン名",
        "options": [
            ("-p ポート",  "接続するポートを指定（デフォルト 22）"),
            ("-i 秘密鍵",  "認証に使う秘密鍵ファイルを指定"),
            ("-L",        "ローカルポートフォワーディングの設定"),
            ("ssh-keygen", "SSH 鍵ペアを生成するコマンド"),
        ],
        "examples": [
            {"cmd": "nslookup google.com", "desc": "google.com の IP アドレスを DNS で確認",
             "note": "Server が DNS サーバー、Address がドメインに紐づく IP アドレスです。", "runnable": True, "cwd": None},
            {"cmd": "nslookup 8.8.8.8", "desc": "IP アドレスからドメイン名を逆引き",
             "note": "逆引き DNS が設定されていればドメイン名が表示されます。", "runnable": True, "cwd": None},
        ],
    },
    # ──────────────────────────────────────────────────────────
    # ファイル操作（追加）
    # ──────────────────────────────────────────────────────────
    {
        "id": "lesson_ln", "category": "file",
        "command": "ln",
        "title": "シンボリックリンクとハードリンク",
        "description": (
            "ln はリンク（別名）を作成するコマンドです。\n"
            "シンボリックリンク（-s）はショートカットのようなもので、元ファイルへのパスを保持します。\n"
            "ハードリンクは同じデータを指す別のファイル名で、元ファイルを削除しても残ります。"
        ),
        "syntax": "ln -s ターゲット リンク名",
        "options": [
            ("-s",          "シンボリックリンクを作成する（ハードリンクがデフォルト）"),
            ("readlink",    "シンボリックリンクの参照先を確認する"),
            ("readlink -f", "シンボリックリンクを解決した絶対パスを取得する"),
        ],
        "examples": [
            {"cmd": "ln -s hello.txt link_to_hello && ls -la link_to_hello",
             "desc": "hello.txt へのシンボリックリンクを作成",
             "note": "ls -la で l (link) と -> hello.txt が表示されます。", "runnable": True, "cwd": "sandbox"},
            {"cmd": "cat link_to_hello", "desc": "リンク経由でファイルを読み込む",
             "note": "シンボリックリンクを通じて元ファイルの内容を参照できます。", "runnable": True, "cwd": "sandbox"},
            {"cmd": "readlink link_to_hello", "desc": "シンボリックリンクの参照先を確認",
             "note": "readlink でリンクが指すパスを確認できます。", "runnable": True, "cwd": "sandbox"},
        ],
    },
    {
        "id": "lesson_chmod_chown", "category": "file",
        "command": "chmod / chown",
        "title": "ファイルの権限とオーナー変更",
        "description": (
            "chmod (change mode) はファイルのアクセス権限を変更します。\n"
            "権限は 読み取り(r=4) / 書き込み(w=2) / 実行(x=1) の組み合わせで、\n"
            "オーナー・グループ・その他 の3者に設定します。\n"
            "chown (change owner) はファイルの所有者を変更します（管理者権限が必要です）。"
        ),
        "syntax": "chmod [モード] ファイル\nchown [ユーザー[:グループ]] ファイル",
        "options": [
            ("chmod 755",  "rwxr-xr-x: オーナーは全操作、他は読み取り・実行のみ"),
            ("chmod 644",  "rw-r--r--: オーナーは読み書き、他は読み取りのみ"),
            ("chmod +x",   "全員に実行権限を追加する"),
            ("chmod -R",   "ディレクトリ内を再帰的に変更する"),
        ],
        "examples": [
            {"cmd": "ls -l hello.txt", "desc": "現在のパーミッションを確認",
             "note": "-rw-r--r-- の形式で表示されます。先頭の - はファイル（d はディレクトリ）です。", "runnable": True, "cwd": "sandbox"},
            {"cmd": "chmod 755 hello.txt && ls -l hello.txt", "desc": "パーミッションを 755（rwxr-xr-x）に変更",
             "note": "7=rwx, 5=r-x。オーナーが全権限、グループとその他が読み取り+実行になります。", "runnable": True, "cwd": "sandbox"},
            {"cmd": "chmod +x hello.txt && ls -l hello.txt", "desc": "実行権限を追加（記号表記）",
             "note": "+x で全員に実行権限を追加します。", "runnable": True, "cwd": "sandbox"},
        ],
    },
    {
        "id": "lesson_tar", "category": "file",
        "command": "tar / gzip / zip",
        "title": "圧縮とアーカイブ",
        "description": (
            "tar は複数のファイルをまとめるアーカイブツールです。\n"
            "gzip と組み合わせることで .tar.gz（tgz）形式の圧縮アーカイブが作れます。\n"
            "zip コマンドは Windows でも扱いやすい .zip 形式を作成します。"
        ),
        "syntax": "tar [オプション] アーカイブ名 対象\ngzip ファイル",
        "options": [
            ("tar -czf",      "gzip 圧縮アーカイブを作成する"),
            ("tar -xzf",      "gzip 圧縮アーカイブを展開する"),
            ("tar -tzf",      "中身を展開せずに一覧表示する"),
            ("tar -xzf -C d/","指定ディレクトリに展開する"),
        ],
        "examples": [
            {"cmd": "tar -czf docs_backup.tar.gz docs/ && ls -lh docs_backup.tar.gz",
             "desc": "docs/ ディレクトリを tar.gz に圧縮",
             "note": "c=create, z=gzip圧縮, f=ファイル名指定。元のディレクトリはそのまま残ります。", "runnable": True, "cwd": "sandbox"},
            {"cmd": "tar -tzf docs_backup.tar.gz", "desc": "アーカイブの中身を一覧表示（展開しない）",
             "note": "t=list。展開前に中身を確認するのが安全です。", "runnable": True, "cwd": "sandbox"},
            {"cmd": "tar -xzf docs_backup.tar.gz -C /tmp/ && ls /tmp/docs",
             "desc": "/tmp に展開して確認",
             "note": "-C で展開先ディレクトリを指定します。", "runnable": True, "cwd": "sandbox"},
            {"cmd": "gzip -k hello.txt && ls -lh hello.txt hello.txt.gz",
             "desc": "hello.txt を gzip 圧縮（元ファイルを残す）",
             "note": "-k（keep）で元ファイルを残します。gunzip で解凍できます。", "runnable": True, "cwd": "sandbox"},
        ],
    },
    {
        "id": "lesson_diff_stat", "category": "file",
        "command": "diff / stat / file",
        "title": "ファイルの比較とメタデータ確認",
        "description": (
            "diff は2つのファイルの差分を表示します。コード差分の確認によく使います。\n"
            "stat はファイルの詳細なメタデータ（iノード・アクセス時刻など）を表示します。\n"
            "file はファイルの種類（テキスト・バイナリ・スクリプトなど）を判定します。"
        ),
        "syntax": "diff [オプション] ファイル1 ファイル2\nstat ファイル\nfile ファイル",
        "options": [
            ("diff -u",  "unified 形式（git diff のような形式）で表示"),
            ("diff -r",  "ディレクトリを再帰的に比較する"),
            ("stat",     "iノード・アクセス/更新/変更時刻・権限などを表示"),
            ("file",     "ファイルの種類を判定する"),
        ],
        "examples": [
            {"cmd": "echo -e 'apple\\nbanana\\ncherry' > /tmp/f1.txt && echo -e 'apple\\nblueberry\\ncherry' > /tmp/f2.txt && diff /tmp/f1.txt /tmp/f2.txt",
             "desc": "2つのファイルの差分を表示",
             "note": "< が f1 のみの行、> が f2 のみの行です。", "runnable": True, "cwd": None},
            {"cmd": "diff -u /tmp/f1.txt /tmp/f2.txt", "desc": "unified 形式で差分を表示",
             "note": "- が削除行、+ が追加行です。git diff もこの形式を使っています。", "runnable": True, "cwd": None},
            {"cmd": "stat hello.txt", "desc": "hello.txt のメタデータを詳しく確認",
             "note": "Access/Modify/Change の3つの時刻の違いに注目です。", "runnable": True, "cwd": "sandbox"},
            {"cmd": "file hello.txt src/main.py /bin/ls", "desc": "複数ファイルの種類を一括判定",
             "note": "テキストファイル・Pythonスクリプト・実行バイナリの違いが確認できます。", "runnable": True, "cwd": "sandbox"},
        ],
    },
    # ──────────────────────────────────────────────────────────
    # テキスト処理（追加）
    # ──────────────────────────────────────────────────────────
    {
        "id": "lesson_awk", "category": "text",
        "command": "awk",
        "title": "フィールド処理と集計（awk）",
        "description": (
            "awk はテキストをフィールド（列）単位で処理するための強力なツールです。\n"
            "CSV などの構造化テキストの加工・集計・フィルタリングに使われます。\n"
            "パターンとアクションの組み合わせで複雑なテキスト処理が1行で書けます。"
        ),
        "syntax": "awk '[パターン] { アクション }' ファイル",
        "options": [
            ("-F ','",       "フィールド区切り文字を指定する（例: CSV はカンマ）"),
            ("$1, $2, ...",  "各フィールドを参照する（$0 は行全体）"),
            ("NR",           "現在の行番号（Number of Record）"),
            ("NF",           "現在行のフィールド数（Number of Field）"),
            ("BEGIN / END",  "処理の前後に実行するブロック"),
        ],
        "examples": [
            {"cmd": "awk -F',' '{print $1}' data.csv", "desc": "CSV の1列目（name）を表示",
             "note": "-F',' でカンマを区切り文字に指定します。$1 が最初のフィールドです。", "runnable": True, "cwd": "sandbox"},
            {"cmd": "awk -F',' 'NR>1 {print $1, $3}' data.csv", "desc": "ヘッダー行をスキップして name と city を表示",
             "note": "NR>1 で2行目以降を対象にします。", "runnable": True, "cwd": "sandbox"},
            {"cmd": "awk -F',' 'NR>1 {sum+=$2} END{print \"平均年齢:\", sum/(NR-1)}' data.csv",
             "desc": "CSV の age 列の平均値を計算",
             "note": "END ブロックは全行処理後に実行されます。", "runnable": True, "cwd": "sandbox"},
            {"cmd": "awk '{print NR\": \"$0}' log.txt", "desc": "ログファイルに行番号を付けて表示",
             "note": "NR は行番号です。cat -n と同様の効果ですが、awk でより柔軟な加工ができます。", "runnable": True, "cwd": "sandbox"},
        ],
    },
    {
        "id": "lesson_cut_tr", "category": "text",
        "command": "cut / tr / paste",
        "title": "列の抽出・文字変換・ファイル結合",
        "description": (
            "cut はテキストの列（フィールド）を切り出します。\n"
            "tr（translate）は文字の変換・削除を行います。\n"
            "paste はファイルを横方向（列）に結合します。"
        ),
        "syntax": "cut -d 区切り -f フィールド [ファイル]\ntr [オプション] 変換元 変換先",
        "options": [
            ("cut -d',' -f2",  "カンマ区切りの2番目のフィールドを取り出す"),
            ("cut -c1-5",      "1〜5文字目を取り出す"),
            ("tr 'a-z' 'A-Z'", "小文字を大文字に変換する"),
            ("tr -d '\\n'",    "改行文字を削除する"),
            ("tr -s ' '",      "連続するスペースを1つにまとめる"),
        ],
        "examples": [
            {"cmd": "cut -d',' -f1,3 data.csv", "desc": "CSV から name と city の列を抽出",
             "note": "-f1,3 で1番目と3番目のフィールドを抽出します。", "runnable": True, "cwd": "sandbox"},
            {"cmd": "echo 'Hello World' | tr 'a-z' 'A-Z'", "desc": "小文字を大文字に変換",
             "note": "tr は文字の1対1変換を行います。", "runnable": True, "cwd": "sandbox"},
            {"cmd": "cat numbers.txt | tr '\\n' ',' | sed 's/,$/\\n/'",
             "desc": "複数行の数値をカンマ区切りの1行にまとめる",
             "note": "tr -d '\\n' で改行を削除→カンマに変換する定番パターンです。", "runnable": True, "cwd": "sandbox"},
            {"cmd": "paste numbers.txt numbers.txt", "desc": "同じファイルを2列に並べて表示",
             "note": "paste はファイルを横方向に結合します。", "runnable": True, "cwd": "sandbox"},
        ],
    },
    {
        "id": "lesson_xargs_tee", "category": "text",
        "command": "xargs / tee",
        "title": "パイプラインの拡張（xargs / tee）",
        "description": (
            "xargs は標準入力を受け取り、それを引数として別のコマンドを実行します。\n"
            "ファイル数が多いときの一括処理に特に便利です。\n"
            "tee はパイプの途中でファイルへの保存と画面表示を同時に行います。"
        ),
        "syntax": "コマンド | xargs [コマンド]\nコマンド | tee [オプション] ファイル",
        "options": [
            ("xargs -I {}", "プレースホルダー {} に引数を埋め込む"),
            ("xargs -P N",  "N 個の並列プロセスで実行する"),
            ("tee -a",      "ファイルに追記する"),
        ],
        "examples": [
            {"cmd": "find . -name '*.txt' | xargs wc -l", "desc": "全 .txt ファイルの行数を一括カウント",
             "note": "xargs は find の出力を wc -l の引数として渡します。", "runnable": True, "cwd": "sandbox"},
            {"cmd": "find . -name '*.py' | xargs grep -l 'def'", "desc": "def を含む Python ファイルを検索",
             "note": "grep -l はファイル名のみを表示します。", "runnable": True, "cwd": "sandbox"},
            {"cmd": "ls | tee filelist.txt | wc -l", "desc": "ls の結果をファイルに保存しながら行数を数える",
             "note": "tee でパイプラインを分岐させます。", "runnable": True, "cwd": "sandbox"},
        ],
    },
    {
        "id": "lesson_less", "category": "text",
        "command": "less / more",
        "title": "ページャー（large ファイルの閲覧）",
        "description": (
            "less は大きなファイルを1画面ずつスクロールして表示するページャーです。\n"
            "cat と違って全行を一度に表示せず、必要な部分だけを読み込むため高速です。\n"
            "ログ調査や man ページの閲覧でよく使います。"
        ),
        "syntax": "less [ファイル]\nコマンド | less",
        "options": [
            ("スペース / f", "次のページへ進む"),
            ("b",            "前のページに戻る"),
            ("/ パターン",   "下方向に検索する"),
            ("q",            "終了する"),
        ],
        "examples": [
            {"cmd": "less log.txt", "desc": "log.txt をページャーで表示",
             "note": "q で終了、/ でテキスト検索ができます。", "runnable": False,
             "simulated_output": "2024-01-01 INFO: サーバーが起動しました\n2024-01-01 ERROR: データベース接続エラー\n...\n[END]  ← q で終了、/ で検索",
             "cwd": "sandbox"},
            {"cmd": "ps aux | less", "desc": "ps aux の長い出力をページャーで見やすく表示",
             "note": "コマンドの出力をパイプで less に渡すと、長い出力を快適に閲覧できます。",
             "runnable": False, "simulated_output": "USER  PID  %CPU  %MEM  COMMAND\n...\n（スクロール可能）", "cwd": None},
        ],
    },
    # ──────────────────────────────────────────────────────────
    # プロセス管理（追加）
    # ──────────────────────────────────────────────────────────
    {
        "id": "lesson_crontab", "category": "process",
        "command": "crontab / at",
        "title": "定期実行スケジューリング",
        "description": (
            "crontab はコマンドを定期的に自動実行するためのスケジューラです。\n"
            "at は一度だけ指定時刻にコマンドを実行します。\n"
            "バックアップ・ログローテーション・監視などの自動化によく使われます。"
        ),
        "syntax": "crontab -e\n分 時 日 月 曜日 コマンド",
        "options": [
            ("crontab -e",  "crontab をエディタで編集する"),
            ("crontab -l",  "現在の crontab を表示する"),
            ("crontab -r",  "crontab を削除する"),
            ("*/5 * * * *", "5分ごとに実行"),
            ("0 2 * * *",   "毎日午前2時に実行"),
        ],
        "examples": [
            {"cmd": "crontab -l", "desc": "現在設定されている crontab を表示",
             "note": "設定がない場合は 'no crontab for user' と表示されます。", "runnable": True, "cwd": None},
            {"cmd": "echo '# 毎日00時に実行: 0 0 * * * /path/to/backup.sh' | cat",
             "desc": "cron 書式の例を確認（実際には crontab -e で編集）",
             "note": "分(0-59) 時(0-23) 日(1-31) 月(1-12) 曜日(0-7)。* は毎回を意味します。", "runnable": True, "cwd": None},
            {"cmd": "at -l 2>/dev/null || echo 'at の待ちキューはありません'",
             "desc": "at コマンドの待ちキューを確認",
             "note": "echo 'cmd' | at now + 1 minute でスケジュール登録できます。", "runnable": True, "cwd": None},
        ],
    },
    {
        "id": "lesson_lsof_watch", "category": "process",
        "command": "lsof / watch / timeout",
        "title": "プロセスとファイルの高度な監視",
        "description": (
            "lsof（list open files）はプロセスが開いているファイルやポートを調べます。\n"
            "watch はコマンドを定期実行してリアルタイムに結果を更新表示します。\n"
            "timeout はコマンドの最大実行時間を制限します。"
        ),
        "syntax": "lsof [オプション]\nwatch -n 秒数 コマンド\ntimeout 秒数 コマンド",
        "options": [
            ("lsof -i",         "ネットワーク接続を開いているプロセスを表示"),
            ("lsof -i :ポート",  "特定ポートを使っているプロセスを確認"),
            ("watch -n 2",      "2秒ごとに更新して表示"),
            ("timeout 5",       "5秒で強制終了"),
        ],
        "examples": [
            {"cmd": "lsof -i :80 2>/dev/null || echo '80番ポートを使用しているプロセスはありません'",
             "desc": "80番ポートを使用しているプロセスを確認",
             "note": "Web サーバーが起動していれば nginx や httpd などが表示されます。", "runnable": True, "cwd": None},
            {"cmd": "lsof /tmp 2>/dev/null | head -5", "desc": "/tmp を使用しているプロセスの先頭5件を表示",
             "note": "ファイルを開いているプロセスを調べるときに使います。", "runnable": True, "cwd": None},
            {"cmd": "timeout 3 sleep 10 && echo '完了' || echo 'タイムアウトしました'",
             "desc": "sleep 10 を3秒でタイムアウト",
             "note": "timeout は指定秒数を超えるとプロセスを終了させます。", "runnable": True, "cwd": None},
        ],
    },
    {
        "id": "lesson_nice", "category": "process",
        "command": "nice / renice",
        "title": "プロセス優先度の制御",
        "description": (
            "nice はコマンドの CPU 優先度（nice 値）を指定して起動します。\n"
            "renice は実行中プロセスの優先度を変更します。\n"
            "nice 値は -20（最高優先度）〜 19（最低優先度）で、\n"
            "バックグラウンドの重い処理を他の作業に影響しないよう実行するのに使います。"
        ),
        "syntax": "nice -n 値 コマンド\nrenice 値 PID",
        "options": [
            ("nice -n 10",       "nice 値 +10（低優先度）でコマンドを起動"),
            ("nice -n -10",      "nice 値 -10（高優先度）※ root のみ"),
            ("renice 5 PID",     "実行中プロセスの nice 値を 5 に変更"),
            ("ps -o pid,ni,comm","PID・nice 値・コマンド名を表示"),
        ],
        "examples": [
            {"cmd": "nice -n 19 sleep 5 & ps -o pid,ni,comm | grep sleep",
             "desc": "低優先度（nice=19）で sleep を起動して確認",
             "note": "ni 列に 19 が表示されます。CPUを大量に使うバッチ処理は低優先度で実行するのが良い習慣です。", "runnable": True, "cwd": None},
            {"cmd": "ps -o pid,ni,comm | head -8", "desc": "実行中プロセスの PID・nice 値・コマンド名を表示",
             "note": "通常のプロセスは nice 値 0 です。", "runnable": True, "cwd": None},
        ],
    },
    # ──────────────────────────────────────────────────────────
    # ネットワーク（追加）
    # ──────────────────────────────────────────────────────────
    {
        "id": "lesson_ip", "category": "network",
        "command": "ip / ifconfig",
        "title": "ネットワークインターフェースの確認",
        "description": (
            "ifconfig は従来のネットワーク設定確認コマンドで、macOS でも使えます。\n"
            "ip コマンドは Linux での現代的な代替で、より多機能です。\n"
            "自分の IP アドレス・サブネット・MAC アドレスなどの確認に使います。"
        ),
        "syntax": "ifconfig [インターフェース名]\nip addr show\nip route show",
        "options": [
            ("ifconfig",      "全インターフェースの設定を表示"),
            ("ip addr show",  "全インターフェースのIPアドレスを表示（Linux）"),
            ("ip route show", "ルーティングテーブルを表示"),
            ("ip link show",  "インターフェースの状態を表示"),
        ],
        "examples": [
            {"cmd": "ifconfig lo0 2>/dev/null || ip addr show lo",
             "desc": "ループバックインターフェース（lo）の情報を表示",
             "note": "inet 127.0.0.1 がループバックIPアドレスです。", "runnable": True, "cwd": None},
            {"cmd": "ip route show 2>/dev/null || netstat -rn | head -10",
             "desc": "ルーティングテーブルを確認",
             "note": "default の行がデフォルトゲートウェイです。", "runnable": True, "cwd": None},
            {"cmd": "hostname", "desc": "このマシンのホスト名を確認",
             "note": "ホスト名はネットワーク上でマシンを識別する名前です。", "runnable": True, "cwd": None},
        ],
    },
    {
        "id": "lesson_netstat_dig", "category": "network",
        "command": "netstat / ss / dig",
        "title": "接続状態の確認と DNS 詳細調査",
        "description": (
            "netstat はネットワーク接続・ルーティング・統計を表示します。\n"
            "ss は netstat の後継で高速です。\n"
            "dig は DNS の詳細情報を確認する強力なツールです。"
        ),
        "syntax": "netstat [オプション]\nss [オプション]\ndig [オプション] ドメイン",
        "options": [
            ("netstat -an",  "全接続とリスニングポートを表示"),
            ("ss -tlnp",     "LISTEN 状態の TCP ポートをプロセス付きで表示"),
            ("dig ドメイン", "DNS 情報を詳細表示"),
            ("dig +short",   "IP アドレスなど結果だけを簡潔に表示"),
        ],
        "examples": [
            {"cmd": "netstat -an 2>/dev/null | head -15",
             "desc": "現在のネットワーク接続を表示（先頭15件）",
             "note": "LISTEN は待ち受け中、ESTABLISHED は接続済みです。", "runnable": True, "cwd": None},
            {"cmd": "ss -tlnp 2>/dev/null | head -10 || netstat -tlnp 2>/dev/null | head -10",
             "desc": "LISTEN 状態の TCP ポートを確認",
             "note": "どのポートでサービスが待ち受けているか確認できます。", "runnable": True, "cwd": None},
            {"cmd": "dig +short google.com", "desc": "google.com の IP アドレスを DNS で確認",
             "note": "+short で IP アドレスだけを表示します。", "runnable": True, "cwd": None},
        ],
    },
    {
        "id": "lesson_scp_rsync", "category": "network",
        "command": "scp / rsync",
        "title": "リモートへの安全なファイル転送",
        "description": (
            "scp（secure copy）は SSH を経由して安全にファイルをコピーします。\n"
            "rsync は差分のみを転送する高速な同期ツールです。\n"
            "大量のファイルの定期バックアップには rsync が特に有効です。"
        ),
        "syntax": "scp [オプション] 送信元 送信先\nrsync [オプション] 送信元 送信先",
        "options": [
            ("scp -r",         "ディレクトリを再帰的にコピーする"),
            ("rsync -av",      "アーカイブモード + 詳細表示"),
            ("rsync -avz",     "gzip 圧縮を有効にして転送する"),
            ("rsync --delete", "送信元に存在しないファイルを削除する"),
            ("rsync -n",       "ドライラン（実際には転送しない）"),
        ],
        "examples": [
            {"cmd": "echo 'scp の使い方:' && echo '  ローカル→リモート: scp file.txt user@host:~/dest/' && echo '  リモート→ローカル: scp user@host:~/file.txt ./dest/'",
             "desc": "scp の基本的な使い方を確認",
             "note": "scp はSSHと同じ鍵・パスワード認証を使います。", "runnable": True, "cwd": None},
            {"cmd": "rsync -av --dry-run /tmp/cmd_learn_sandbox/ /tmp/rsync_test/",
             "desc": "rsync のドライラン（実際には転送しない確認）",
             "note": "--dry-run で実際には転送せず、どのファイルが同期されるかだけ表示します。", "runnable": True, "cwd": None},
        ],
    },
    # ──────────────────────────────────────────────────────────
    # シェル・環境
    # ──────────────────────────────────────────────────────────
    {
        "id": "lesson_man", "category": "shell",
        "command": "man / which / type / help",
        "title": "コマンドのヘルプと場所の確認",
        "description": (
            "man（manual）は詳細なマニュアルページを表示します。\n"
            "which はコマンドの実行ファイルのパスを探します。\n"
            "type はコマンドがシェル組み込みか外部コマンドかを確認します。\n"
            "これらは知らないコマンドを調べるときの第一歩です。"
        ),
        "syntax": "man コマンド\nwhich コマンド\ntype コマンド",
        "options": [
            ("man -k キーワード", "キーワードでマニュアルを検索する"),
            ("man 5 passwd",      "セクション番号を指定して表示する"),
            ("which -a",          "PATH 上の全ての一致を表示する"),
            ("command --help",    "多くのコマンドで使える簡易ヘルプ"),
        ],
        "examples": [
            {"cmd": "which ls", "desc": "ls コマンドの実行ファイルのパスを確認",
             "note": "/bin/ls や /usr/bin/ls のようなパスが表示されます。", "runnable": True, "cwd": None},
            {"cmd": "which python3 2>/dev/null || echo 'python3 が見つかりません'",
             "desc": "python3 のインストール場所を確認",
             "note": "コマンドが見つからない場合は which は何も出力しません。", "runnable": True, "cwd": None},
            {"cmd": "type cd && type ls", "desc": "cd と ls の種類を確認",
             "note": "cd は shell builtin（シェル組み込み）、ls は外部コマンドです。", "runnable": True, "cwd": None},
            {"cmd": "ls --help 2>&1 | head -15", "desc": "ls の簡易ヘルプを確認",
             "note": "--help はほとんどのコマンドで使えます。", "runnable": True, "cwd": None},
        ],
    },
    {
        "id": "lesson_env", "category": "shell",
        "command": "env / export / source",
        "title": "環境変数の設定と管理",
        "description": (
            "環境変数はシェルや子プロセスが参照する設定値です。\n"
            "export で変数を環境変数として設定し、子プロセスに引き継がせます。\n"
            "source（または .）で設定ファイルを現在のシェルに読み込みます。"
        ),
        "syntax": "export 変数名=値\nenv\nsource ファイル",
        "options": [
            ("export VAR=val",   "変数を設定して子プロセスに引き継ぐ"),
            ("env",              "現在の全環境変数を表示する"),
            ("printenv 変数名",  "特定の環境変数の値を表示する"),
            ("unset 変数名",     "環境変数を削除する"),
            ("source ~/.bashrc", "設定ファイルを現在のシェルで再読み込み"),
        ],
        "examples": [
            {"cmd": "echo \"ホームディレクトリ: $HOME\" && echo \"ユーザー名: $USER\" && echo \"シェル: $SHELL\"",
             "desc": "よく使う環境変数を確認",
             "note": "$HOME, $USER, $SHELL, $PATH は主要な環境変数です。", "runnable": True, "cwd": None},
            {"cmd": "export GREETING='Hello!' && echo $GREETING",
             "desc": "新しい環境変数を設定して確認",
             "note": "export で設定した変数は子プロセスにも引き継がれます。", "runnable": True, "cwd": None},
            {"cmd": "env | grep PATH", "desc": "PATH 環境変数の現在の値を確認",
             "note": "PATH はコロン区切りで複数のディレクトリが並んでいます。", "runnable": True, "cwd": None},
            {"cmd": "printenv SHELL", "desc": "現在使っているシェルを確認",
             "note": "printenv は特定の変数だけを表示します。", "runnable": True, "cwd": None},
        ],
    },
    {
        "id": "lesson_alias_history", "category": "shell",
        "command": "alias / history",
        "title": "エイリアスとコマンド履歴",
        "description": (
            "alias は長いコマンドに短い別名（エイリアス）を付けます。\n"
            "よく使うオプションをデフォルトにしたり、タイポを修正するのに使われます。\n"
            "history は過去に実行したコマンドの履歴を管理します。"
        ),
        "syntax": "alias 名前='コマンド'\nhistory [件数]",
        "options": [
            ("alias",        "設定されているエイリアスの一覧を表示"),
            ("unalias 名前", "エイリアスを削除する"),
            ("history N",    "直近 N 件の履歴を表示"),
            ("!番号",        "指定番号のコマンドを再実行"),
            ("!!",           "直前のコマンドを再実行（sudo !! が便利）"),
            ("Ctrl+R",       "履歴をインクリメンタル検索"),
        ],
        "examples": [
            {"cmd": "alias", "desc": "現在設定されているエイリアス一覧を表示",
             "note": "OS やシェルの設定によってデフォルトのエイリアスが設定されています。", "runnable": True, "cwd": None},
            {"cmd": "alias ll='ls -la' && alias gs='git status' && alias",
             "desc": "よく使うエイリアスを設定して確認",
             "note": "永続化するには ~/.bashrc や ~/.zshrc に書いておきます。", "runnable": True, "cwd": None},
            {"cmd": "history | tail -10", "desc": "最近の履歴を10件表示",
             "note": "左の番号で !番号 として再実行できます。Ctrl+R で過去のコマンドをインクリメンタル検索できます。", "runnable": True, "cwd": None},
            {"cmd": "history | grep ls | tail -5", "desc": "ls を含む過去のコマンドを検索",
             "note": "特定コマンドの過去のオプションを確認するのに使えます。", "runnable": True, "cwd": None},
        ],
    },
    {
        "id": "lesson_shell_vars", "category": "shell",
        "command": "変数 / クォート / グロブ",
        "title": "シェル変数・クォート・グロブ展開",
        "description": (
            "シェル変数は値に名前を付けて再利用するための仕組みです。\n"
            "クォートはスペースや特殊文字をエスケープするために使います。\n"
            "グロブ（ワイルドカード）はファイル名のパターンマッチに使います。"
        ),
        "syntax": "変数名=値\n$変数名  ← 参照\n\"...$VAR...\"  ← 変数展開あり\n'...$VAR...'  ← 変数展開なし",
        "options": [
            ("*",               "0文字以上の任意の文字列（例: *.txt）"),
            ("?",               "任意の1文字（例: file?.txt）"),
            ("[abc]",           "a, b, c のいずれか1文字"),
            ("${VAR:-default}", "変数が未設定なら default を使う"),
        ],
        "examples": [
            {"cmd": "NAME='World' && echo \"Hello, $NAME!\" && echo 'Hello, $NAME!'",
             "desc": "ダブルクォートとシングルクォートの違いを確認",
             "note": "ダブルクォートは変数展開されます。シングルクォートはすべて文字通りに扱います。", "runnable": True, "cwd": None},
            {"cmd": "ls /tmp/*.log 2>/dev/null || ls /tmp/*.txt 2>/dev/null || echo 'マッチするファイルがありません'",
             "desc": "グロブ * でパターンに一致するファイルを一覧表示",
             "note": "* はシェルがファイル名に展開してからコマンドに渡します（シェル展開）。", "runnable": True, "cwd": None},
            {"cmd": "for f in /tmp/cmd_learn_sandbox/*.txt; do echo \"ファイル: $f\"; done",
             "desc": "グロブを使って .txt ファイルを for ループで処理",
             "note": "グロブ展開はスクリプトでファイルを一括処理するときの基本パターンです。", "runnable": True, "cwd": None},
            {"cmd": "GREETING=${UNDEFINED_VAR:-'デフォルト値'} && echo $GREETING",
             "desc": "変数が未設定のときのデフォルト値を設定",
             "note": "${VAR:-default} は VAR が未定義または空のときに default を使います。", "runnable": True, "cwd": None},
        ],
    },
    {
        "id": "lesson_shell_script", "category": "shell",
        "command": "シェルスクリプト基礎",
        "title": "シェルスクリプトの書き方",
        "description": (
            "シェルスクリプトはコマンドを自動化するためのプログラムです。\n"
            "繰り返し作業の自動化・デプロイ・バックアップなどに広く使われます。\n"
            "#!/bin/bash（shebang）で始め、chmod +x で実行権限を付けて使います。"
        ),
        "syntax": "#!/bin/bash\n変数・if・for・while・関数",
        "options": [
            ("#!/bin/bash", "スクリプトのインタープリターを指定する shebang"),
            ("set -e",      "エラー発生時に即座に終了する"),
            ("set -u",      "未定義変数をエラーにする"),
            ("if [ 条件 ]", "条件分岐"),
            ("for i in ...", "ループ処理"),
        ],
        "examples": [
            {"cmd": "cat > /tmp/hello.sh << 'EOF'\n#!/bin/bash\nNAME=${1:-World}\necho \"Hello, $NAME!\"\nEOF\nchmod +x /tmp/hello.sh && /tmp/hello.sh && /tmp/hello.sh Claude",
             "desc": "引数を受け取るシェルスクリプトを作成して実行",
             "note": "${1:-World} は第1引数が省略されたとき World を使います。", "runnable": True, "cwd": None},
            {"cmd": "for i in 1 2 3 4 5; do echo \"カウント: $i\"; done",
             "desc": "for ループの基本",
             "note": "for 変数 in リスト; do ... done の構文です。", "runnable": True, "cwd": None},
            {"cmd": "FILE=/tmp/cmd_learn_sandbox/hello.txt; if [ -f \"$FILE\" ]; then echo \"存在します\"; else echo \"存在しません\"; fi",
             "desc": "ファイルの存在確認を if 文で行う",
             "note": "[ -f file ] はファイル存在確認。-d はディレクトリ、-e はファイル・ディレクトリどちらも確認します。", "runnable": True, "cwd": None},
        ],
    },
    # ──────────────────────────────────────────────────────────
    # システム情報
    # ──────────────────────────────────────────────────────────
    {
        "id": "lesson_uname", "category": "system",
        "command": "uname / hostname / uptime",
        "title": "システム基本情報の確認",
        "description": (
            "uname はOSやカーネルのバージョンを表示します。\n"
            "hostname はネットワーク上のコンピューター名を確認します。\n"
            "uptime はシステムの起動時間と負荷状況を表示します。"
        ),
        "syntax": "uname [オプション]\nhostname\nuptime",
        "options": [
            ("uname -a",  "全情報（OS名・ホスト名・カーネルバージョン等）を表示"),
            ("uname -r",  "カーネルバージョンのみを表示"),
            ("uname -s",  "OS名のみを表示"),
            ("uname -m",  "CPU アーキテクチャ（x86_64, arm64等）を表示"),
            ("uptime -p", "起動時間を人間が読みやすい形式で表示（Linux）"),
        ],
        "examples": [
            {"cmd": "uname -a", "desc": "システムの全情報を表示",
             "note": "カーネルバージョン・ホスト名・CPU アーキテクチャが一行で確認できます。", "runnable": True, "cwd": None},
            {"cmd": "uname -s && uname -r && uname -m", "desc": "OS名・カーネルバージョン・アーキテクチャを個別に表示",
             "note": "macOS は Darwin、Linux は Linux と表示されます。", "runnable": True, "cwd": None},
            {"cmd": "hostname", "desc": "このマシンのホスト名を表示",
             "note": "ホスト名はネットワーク上の識別名です。", "runnable": True, "cwd": None},
            {"cmd": "uptime", "desc": "システムの起動時間と負荷平均を表示",
             "note": "load average の3つの数値は1分・5分・15分の平均CPU負荷です。", "runnable": True, "cwd": None},
        ],
    },
    {
        "id": "lesson_df_du", "category": "system",
        "command": "df / du",
        "title": "ディスク使用量の確認",
        "description": (
            "df（disk free）はファイルシステム全体の容量・使用量・空き容量を表示します。\n"
            "du（disk usage）は特定のディレクトリやファイルのディスク使用量を表示します。\n"
            "ディスク容量のトラブルシューティングで必須のコマンドペアです。"
        ),
        "syntax": "df [オプション] [パス]\ndu [オプション] [パス]",
        "options": [
            ("df -h",       "人間が読みやすい形式で表示（KB/MB/GB）"),
            ("df -T",       "ファイルシステムの種類も表示"),
            ("du -sh パス", "そのパスのディスク使用量合計を表示"),
            ("du -sh *",    "カレントディレクトリの各アイテムのサイズを表示"),
            ("du -d 1",     "1階層だけ展開して表示"),
        ],
        "examples": [
            {"cmd": "df -h", "desc": "全ファイルシステムのディスク容量を確認",
             "note": "Use% が 90% を超えるとディスクフルが近いです。", "runnable": True, "cwd": None},
            {"cmd": "du -sh /tmp/cmd_learn_sandbox/*", "desc": "サンドボックス内の各ファイル・ディレクトリのサイズを確認",
             "note": "-s で合計のみ、* でカレント内の各アイテムを対象にします。", "runnable": True, "cwd": None},
            {"cmd": "du -sh /tmp", "desc": "/tmp ディレクトリ全体のディスク使用量を確認",
             "note": "ディスクを圧迫しているディレクトリを特定するには、大きなディレクトリから順に du で掘り下げます。", "runnable": True, "cwd": None},
        ],
    },
    {
        "id": "lesson_who_id", "category": "system",
        "command": "who / id / date",
        "title": "ユーザー情報と日時の確認",
        "description": (
            "who はログイン中のユーザーを表示します。\n"
            "id は現在のユーザーの UID・GID・グループを表示します。\n"
            "date はシステムの日時を表示・操作します。"
        ),
        "syntax": "who\nid [ユーザー名]\ndate [+フォーマット]",
        "options": [
            ("who -a",         "詳細情報（ブート時刻・実行レベルなど）も表示"),
            ("id",             "現在のユーザーのUID/GID/グループを表示"),
            ("date +%Y-%m-%d", "年-月-日 形式で日付を表示"),
            ("date +%s",       "Unix タイムスタンプ（秒）を表示"),
        ],
        "examples": [
            {"cmd": "who", "desc": "ログイン中のユーザーを表示",
             "note": "ユーザー名・端末・ログイン時刻が表示されます。", "runnable": True, "cwd": None},
            {"cmd": "id", "desc": "現在のユーザーの UID/GID/グループを確認",
             "note": "uid=0(root) の場合は root ユーザーです。", "runnable": True, "cwd": None},
            {"cmd": "date", "desc": "現在の日時を表示",
             "note": "システムのタイムゾーンで表示されます。", "runnable": True, "cwd": None},
            {"cmd": "date +\"%Y-%m-%d %H:%M:%S\"", "desc": "日時をファイル名向けのフォーマットで表示",
             "note": "バックアップファイル名に日付を付けるときによく使います。", "runnable": True, "cwd": None},
        ],
    },
    {
        "id": "lesson_sys_info", "category": "system",
        "command": "free / dmesg / sysctl",
        "title": "メモリ・カーネルログ・システムパラメータ",
        "description": (
            "free はメモリ使用状況を表示します（Linux）。\n"
            "dmesg はカーネルのリングバッファ（起動時のログやデバイスエラーなど）を表示します。\n"
            "sysctl はカーネルパラメータの確認と変更に使います。"
        ),
        "syntax": "free -h\ndmesg [| tail]\nsysctl [パラメータ]",
        "options": [
            ("free -h",      "メモリ使用量を人間が読みやすい形式で表示（Linux）"),
            ("dmesg | tail", "カーネルログの最新部分を確認"),
            ("dmesg -T",     "タイムスタンプを人間が読める形式で表示"),
            ("sysctl -a",    "全カーネルパラメータを表示"),
        ],
        "examples": [
            {"cmd": "free -h 2>/dev/null || vm_stat | head -10", "desc": "メモリ使用状況を確認",
             "note": "free は Linux 専用です。macOS では vm_stat コマンドを使います。", "runnable": True, "cwd": None},
            {"cmd": "dmesg 2>/dev/null | tail -10 || log show --predicate 'eventMessage contains \"error\"' --last 1m 2>/dev/null | tail -5 || echo 'ログ確認には管理者権限が必要な場合があります'",
             "desc": "カーネルログの最新メッセージを確認",
             "note": "USB デバイス接続やドライバエラーなどが表示されます。", "runnable": True, "cwd": None},
            {"cmd": "sysctl -a 2>/dev/null | head -10", "desc": "カーネルパラメータの一覧を確認（先頭10件）",
             "note": "sysctl でカーネルの動作パラメータを確認・変更できます。", "runnable": True, "cwd": None},
            {"cmd": "cat /proc/meminfo 2>/dev/null | head -10 || sysctl hw.memsize 2>/dev/null",
             "desc": "物理メモリの詳細情報を確認",
             "note": "Linux は /proc/meminfo、macOS は sysctl hw.memsize でメモリ情報を確認できます。", "runnable": True, "cwd": None},
        ],
    },
]

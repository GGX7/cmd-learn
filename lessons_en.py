"""Textbook lesson data (English)"""

LESSONS: list[dict] = [

    # ──────────────────────────────────────────────────────────
    # File Operations
    # ──────────────────────────────────────────────────────────
    {
        "id": "lesson_ls", "category": "file",
        "command": "ls",
        "title": "List Files and Directories",
        "description": (
            "ls (list) displays the contents of a directory.\n"
            "When you open a terminal, start with ls to see what's around.\n"
            "Combine options to show details and hidden files."
        ),
        "syntax": "ls [options] [path]",
        "options": [
            ("-a",  "Show hidden files (names starting with .)"),
            ("-l",  "Long format: permissions, size, date on each line"),
            ("-h",  "Human-readable sizes when used with -l"),
            ("-t",  "Sort by modification time, newest first"),
        ],
        "examples": [
            {"cmd": "ls", "desc": "List current directory contents",
             "note": "Files and directories are shown side by side.", "runnable": True, "cwd": "sandbox"},
            {"cmd": "ls -la", "desc": "Show all files including hidden, with details",
             "note": "Files starting with . appear too. The drwxr-xr-x on the left is the permission string.", "runnable": True, "cwd": "sandbox"},
            {"cmd": "ls -lh docs", "desc": "Show docs directory with human-readable sizes",
             "note": "Specify a path to list the contents of another directory.", "runnable": True, "cwd": "sandbox"},
        ],
    },
    {
        "id": "lesson_pwd_cd", "category": "file",
        "command": "pwd / cd",
        "title": "Check Location and Change Directory",
        "description": (
            "pwd (print working directory) shows the path of your current directory.\n"
            "cd (change directory) moves you to a different directory.\n"
            "You can use absolute paths (starting with /) or relative paths."
        ),
        "syntax": "pwd\ncd [destination]",
        "options": [
            ("~",  "Home directory shortcut (e.g., cd ~/Desktop)"),
            ("..", "Parent directory (e.g., cd ..)"),
            ("-",  "Return to previous directory (e.g., cd -)"),
        ],
        "examples": [
            {"cmd": "pwd", "desc": "Show current directory (absolute path)",
             "note": "Displays something like /home/user or /Users/user.", "runnable": True, "cwd": None},
            {"cmd": "cd /tmp && pwd", "desc": "Move to /tmp and confirm location",
             "note": "&& means 'run next command only if previous succeeded'.", "runnable": True, "cwd": None},
            {"cmd": "cd ~ && pwd", "desc": "Go to home directory",
             "note": "~ refers to the logged-in user's home directory.", "runnable": True, "cwd": None},
        ],
    },
    {
        "id": "lesson_mkdir_touch", "category": "file",
        "command": "mkdir / touch",
        "title": "Create Files and Directories",
        "description": (
            "mkdir (make directory) creates a new directory.\n"
            "touch creates a new empty file.\n"
            "Using touch on an existing file updates its timestamp without changing its content."
        ),
        "syntax": "mkdir [options] dirname\ntouch filename",
        "options": [
            ("mkdir -p", "Create parent directories as needed (e.g., mkdir -p a/b/c)"),
            ("touch -t", "Set a specific timestamp when creating/updating"),
        ],
        "examples": [
            {"cmd": "mkdir myproject && ls", "desc": "Create myproject directory and verify",
             "note": "ls confirms the new directory was created.", "runnable": True, "cwd": "sandbox"},
            {"cmd": "mkdir -p myproject/src/utils && ls myproject/src", "desc": "Create nested directories with -p",
             "note": "Deep hierarchies can be created at once. -p also prevents errors if directories already exist.", "runnable": True, "cwd": "sandbox"},
            {"cmd": "touch myproject/README.md && ls myproject", "desc": "Create README.md and check directory",
             "note": "touch created an empty file.", "runnable": True, "cwd": "sandbox"},
        ],
    },
    {
        "id": "lesson_cp_mv", "category": "file",
        "command": "cp / mv",
        "title": "Copy, Move, and Rename Files",
        "description": (
            "cp (copy) copies files or directories.\n"
            "mv (move) both moves files and renames them.\n"
            "Using mv within the same directory acts as a rename."
        ),
        "syntax": "cp [options] source dest\nmv source dest",
        "options": [
            ("cp -r", "Copy a directory and all its contents (recursive)"),
            ("cp -i", "Ask before overwriting"),
            ("mv -i", "Ask before overwriting"),
        ],
        "examples": [
            {"cmd": "cp hello.txt hello_backup.txt && ls", "desc": "Copy hello.txt to hello_backup.txt",
             "note": "The original file stays in place; a copy is created.", "runnable": True, "cwd": "sandbox"},
            {"cmd": "mv hello_backup.txt docs/hello_backup.txt && ls docs", "desc": "Move hello_backup.txt into the docs directory",
             "note": "mv is like cut-and-paste. The original location no longer contains the file.", "runnable": True, "cwd": "sandbox"},
            {"cmd": "mv docs/hello_backup.txt docs/renamed.txt && ls docs", "desc": "Rename the file to renamed.txt",
             "note": "mv within the same directory acts as a rename.", "runnable": True, "cwd": "sandbox"},
        ],
    },
    {
        "id": "lesson_rm", "category": "file",
        "command": "rm",
        "title": "Delete Files and Directories",
        "description": (
            "rm (remove) deletes files and directories.\n"
            "⚠️  Files deleted with rm do NOT go to the Trash — they are gone immediately.\n"
            "Be especially careful with rm -rf, which is very powerful."
        ),
        "syntax": "rm [options] filename",
        "options": [
            ("-r", "Delete a directory and all its contents (recursive)"),
            ("-f", "Force deletion without prompting"),
            ("-i", "Prompt before each deletion (recommended for beginners)"),
        ],
        "examples": [
            {"cmd": "touch trash.txt && ls", "desc": "Create a test file to delete",
             "note": "First create the file we'll delete.", "runnable": True, "cwd": "sandbox"},
            {"cmd": "rm trash.txt && ls", "desc": "Delete trash.txt and confirm",
             "note": "The file is gone — it does NOT go to the Trash!", "runnable": True, "cwd": "sandbox"},
            {"cmd": "mkdir tempdir && touch tempdir/a.txt tempdir/b.txt && rm -r tempdir && ls",
             "desc": "Delete a directory with all its contents",
             "note": "Without -r (recursive), rm cannot delete directories.", "runnable": True, "cwd": "sandbox"},
        ],
    },
    {
        "id": "lesson_find", "category": "file",
        "command": "find",
        "title": "Search for Files",
        "description": (
            "find recursively searches directories for files matching your criteria.\n"
            "You can filter by filename pattern, type, modification date, and more.\n"
            "It's extremely useful when looking for specific files in a large tree."
        ),
        "syntax": "find path [conditions] [actions]",
        "options": [
            ("-name '*.txt'", "Search by filename pattern (wildcards allowed)"),
            ("-type f",       "Match regular files only"),
            ("-type d",       "Match directories only"),
            ("-mtime -7",     "Files modified within the last 7 days"),
        ],
        "examples": [
            {"cmd": "find . -name '*.txt'", "desc": "Find all .txt files under current directory",
             "note": ". means 'current directory'. Subdirectories are searched automatically.", "runnable": True, "cwd": "sandbox"},
            {"cmd": "find . -type d", "desc": "Find directories only",
             "note": "-type d limits results to directories.", "runnable": True, "cwd": "sandbox"},
            {"cmd": "find . -name '*.txt' -type f", "desc": "Combine conditions: .txt files only",
             "note": "Multiple conditions are AND-ed together.", "runnable": True, "cwd": "sandbox"},
        ],
    },
    # ──────────────────────────────────────────────────────────
    # Text Processing
    # ──────────────────────────────────────────────────────────
    {
        "id": "lesson_cat", "category": "text",
        "command": "cat / head / tail",
        "title": "Display File Contents",
        "description": (
            "cat shows the full contents of a file.\n"
            "head shows the first N lines (default 10); tail shows the last N lines.\n"
            "tail -f is commonly used to monitor log files in real time."
        ),
        "syntax": "cat [file]\nhead [-n N] [file]\ntail [-n N] [file]",
        "options": [
            ("cat -n",    "Show line numbers"),
            ("head -n N", "Show first N lines"),
            ("tail -n N", "Show last N lines"),
            ("tail -f",   "Follow appended data in real time (Ctrl+C to stop)"),
        ],
        "examples": [
            {"cmd": "cat hello.txt", "desc": "Display all contents of hello.txt",
             "note": "cat is handy for short files. Use less for long files.", "runnable": True, "cwd": "sandbox"},
            {"cmd": "cat -n log.txt", "desc": "Display log.txt with line numbers",
             "note": "-n adds line numbers, useful for locating errors.", "runnable": True, "cwd": "sandbox"},
            {"cmd": "head -n 3 log.txt", "desc": "Show first 3 lines of log.txt",
             "note": "Quickly check the top of a large file.", "runnable": True, "cwd": "sandbox"},
            {"cmd": "tail -n 3 log.txt", "desc": "Show last 3 lines of log.txt",
             "note": "Log files typically have the newest info at the bottom, so tail is often used.", "runnable": True, "cwd": "sandbox"},
        ],
    },
    {
        "id": "lesson_grep", "category": "text",
        "command": "grep",
        "title": "Search Text for Patterns",
        "description": (
            "grep searches files for lines matching a pattern (string or regex).\n"
            "It's an essential everyday command for log analysis and code investigation.\n"
            "Combined with pipes (|), it becomes especially powerful."
        ),
        "syntax": "grep [options] pattern [file]",
        "options": [
            ("-i", "Case-insensitive matching"),
            ("-n", "Show line numbers of matches"),
            ("-r", "Search directories recursively"),
            ("-v", "Show lines that do NOT match (invert)"),
            ("-c", "Show only the count of matching lines"),
        ],
        "examples": [
            {"cmd": "grep ERROR log.txt", "desc": "Show lines containing ERROR in log.txt",
             "note": "Matching is case-sensitive by default. Use -i to also match 'error'.", "runnable": True, "cwd": "sandbox"},
            {"cmd": "grep -n INFO log.txt", "desc": "Show INFO lines with line numbers",
             "note": "-n shows which line number the match is on, making investigation easier.", "runnable": True, "cwd": "sandbox"},
            {"cmd": "grep -c ERROR log.txt", "desc": "Count lines containing ERROR",
             "note": "-c stands for count. Useful for counting error occurrences.", "runnable": True, "cwd": "sandbox"},
            {"cmd": "grep -r txt .", "desc": "Search all files under current directory for 'txt'",
             "note": "-r includes subdirectories in the search.", "runnable": True, "cwd": "sandbox"},
        ],
    },
    {
        "id": "lesson_wc_sort", "category": "text",
        "command": "wc / sort / uniq",
        "title": "Count Lines, Sort, and Remove Duplicates",
        "description": (
            "wc (word count) counts lines, words, and bytes.\n"
            "sort arranges lines of text in order.\n"
            "uniq removes consecutive duplicate lines. It's typically paired with sort."
        ),
        "syntax": "wc [-l|-w|-c] [file]\nsort [options] [file]\nuniq [file]",
        "options": [
            ("wc -l",   "Count lines only"),
            ("sort -n", "Sort numerically (different from alphabetical)"),
            ("sort -r", "Sort in reverse order"),
            ("sort -u", "Sort and remove duplicates at the same time"),
            ("uniq -c", "Prefix each line with its occurrence count"),
        ],
        "examples": [
            {"cmd": "wc -l log.txt", "desc": "Count lines in log.txt",
             "note": "wc -l is often used to count log entries.", "runnable": True, "cwd": "sandbox"},
            {"cmd": "sort numbers.txt", "desc": "Sort numbers.txt alphabetically",
             "note": "Default is alphabetical, so 10 comes before 2. Watch out!", "runnable": True, "cwd": "sandbox"},
            {"cmd": "sort -n numbers.txt", "desc": "Sort numerically",
             "note": "-n gives the correct numeric order: 1, 2, 3...", "runnable": True, "cwd": "sandbox"},
            {"cmd": "sort numbers.txt | uniq", "desc": "Sort then remove duplicate lines",
             "note": "| is a pipe — it passes the output of sort as input to uniq.", "runnable": True, "cwd": "sandbox"},
        ],
    },
    {
        "id": "lesson_sed", "category": "text",
        "command": "sed",
        "title": "Text Substitution and Transformation",
        "description": (
            "sed (stream editor) processes text line by line.\n"
            "The most common use is the s (substitute) command for string replacement.\n"
            "It's safe to check the output first before writing changes back to a file."
        ),
        "syntax": "sed 's/find/replace/flags' file",
        "options": [
            ("s/old/new/",  "Replace first match on each line"),
            ("s/old/new/g", "Replace all matches on each line (g = global)"),
            ("-i",          "Edit the file in place (make a backup first)"),
            ("-n 'Np'",     "Print only line N"),
        ],
        "examples": [
            {"cmd": "sed 's/INFO/[INFO]/' log.txt", "desc": "Replace first INFO with [INFO] on each line",
             "note": "The file itself is unchanged. The result is printed to stdout.", "runnable": True, "cwd": "sandbox"},
            {"cmd": "sed 's/ERROR/[ERR]/g' log.txt", "desc": "Replace all occurrences of ERROR with [ERR]",
             "note": "The g flag replaces every match on a line, not just the first.", "runnable": True, "cwd": "sandbox"},
            {"cmd": "sed -n '2,3p' log.txt", "desc": "Show only lines 2-3",
             "note": "-n suppresses all output; p prints the specified lines.", "runnable": True, "cwd": "sandbox"},
        ],
    },
    {
        "id": "lesson_pipe", "category": "text",
        "command": "| / > / >>",
        "title": "Pipes and Redirection",
        "description": (
            "A pipe (|) connects commands, passing the output of one as input to the next.\n"
            "> writes command output to a file (overwrites).\n"
            ">> appends output to a file.\n"
            "Combining these lets you build complex one-liners."
        ),
        "syntax": "cmd1 | cmd2\ncmd > file\ncmd >> file",
        "options": [
            ("|",  "Pipe: pass output of previous command to next"),
            (">",  "Redirect: write output to a file (overwrites)"),
            (">>", "Redirect: append output to a file"),
            ("2>", "Redirect stderr to a file"),
        ],
        "examples": [
            {"cmd": "grep ERROR log.txt | wc -l", "desc": "Count lines containing ERROR (grep + wc pipe)",
             "note": "grep's output becomes wc's input. That's how pipes work.", "runnable": True, "cwd": "sandbox"},
            {"cmd": "sort numbers.txt | uniq | wc -l", "desc": "Count unique numbers after deduplication",
             "note": "Three commands chained together handle complex processing in one line.", "runnable": True, "cwd": "sandbox"},
            {"cmd": "echo 'Appended text' >> hello.txt && cat hello.txt", "desc": "Append text to hello.txt and verify",
             "note": ">> appends; > overwrites. Be careful with > — existing content is erased!", "runnable": True, "cwd": "sandbox"},
        ],
    },
    # ──────────────────────────────────────────────────────────
    # Process Management
    # ──────────────────────────────────────────────────────────
    {
        "id": "lesson_ps", "category": "process",
        "command": "ps / top",
        "title": "View Running Processes",
        "description": (
            "ps (process status) lists running processes.\n"
            "top is a real-time monitoring tool showing CPU and memory usage.\n"
            "Use these to check system state and identify resource-hungry processes."
        ),
        "syntax": "ps [options]\ntop",
        "options": [
            ("ps aux",      "Show all processes with details for all users"),
            ("ps -ef",      "Full-format listing including PPID"),
            ("top -b -n 1", "Output once and exit (non-interactive mode)"),
        ],
        "examples": [
            {"cmd": "ps", "desc": "Show processes related to the current shell",
             "note": "Columns: PID (process ID), TTY, TIME (CPU time), CMD (command name).", "runnable": True, "cwd": None},
            {"cmd": "ps aux | head -10", "desc": "Show all processes with details (first 10)",
             "note": "%CPU and %MEM show resource usage percentages.", "runnable": True, "cwd": None},
            {"cmd": "ps aux | grep python", "desc": "Search for processes named python",
             "note": "Combine with grep to check if a specific process is running.", "runnable": True, "cwd": None},
        ],
    },
    {
        "id": "lesson_kill", "category": "process",
        "command": "kill / killall",
        "title": "Terminate Processes",
        "description": (
            "kill sends a signal to a process by its PID (process ID).\n"
            "killall targets all processes matching a given name.\n"
            "The default signal is SIGTERM (graceful stop); the process can clean up first.\n"
            "SIGKILL (-9) forces immediate termination — use as a last resort."
        ),
        "syntax": "kill [-signal] PID\nkillall [-signal] name",
        "options": [
            ("kill PID",    "Send default SIGTERM (graceful stop request)"),
            ("kill -9 PID", "Send SIGKILL (forced termination — last resort)"),
            ("killall name","Send SIGTERM to all processes with that name"),
            ("kill -l",     "List available signals"),
        ],
        "examples": [
            {"cmd": "kill -l | head -5", "desc": "List available signals (first 5)",
             "note": "SIGTERM=15 (stop request) and SIGKILL=9 (force kill) are the most used.", "runnable": True, "cwd": None},
            {"cmd": "sleep 120 & PID=$! && echo \"Started PID=$PID\" && kill $PID && echo \"Terminated\"",
             "desc": "Start a sleep process and immediately terminate it",
             "note": "$! holds the PID of the last backgrounded process.", "runnable": True, "cwd": None},
            {"cmd": "ps aux | grep sleep", "desc": "Search for any remaining sleep processes",
             "note": "After the kill, no sleep process should appear.", "runnable": True, "cwd": None},
        ],
    },
    {
        "id": "lesson_bg", "category": "process",
        "command": "& / jobs / fg / bg",
        "title": "Background Execution and Job Control",
        "description": (
            "Append & to run a command in the background.\n"
            "jobs lists current background jobs; fg brings one back to the foreground.\n"
            "Ctrl+Z suspends a foreground process; bg resumes it in the background."
        ),
        "syntax": "command &\njobs\nfg [%job]\nbg [%job]",
        "options": [
            ("command &", "Run command in the background"),
            ("Ctrl+Z",    "Suspend the foreground process"),
            ("fg %1",     "Bring job 1 to the foreground"),
            ("bg %1",     "Resume stopped job 1 in the background"),
        ],
        "examples": [
            {"cmd": "sleep 30 & sleep 30 & jobs", "desc": "Start two background jobs and list them",
             "note": "The number in [ ] is the job number. Use fg %1 to bring job 1 to the foreground.", "runnable": True, "cwd": None},
            {"cmd": "jobs | wc -l", "desc": "Count current background jobs",
             "note": "No output means no background jobs.", "runnable": True, "cwd": None},
        ],
    },
    # ──────────────────────────────────────────────────────────
    # Networking
    # ──────────────────────────────────────────────────────────
    {
        "id": "lesson_ping", "category": "network",
        "command": "ping",
        "title": "Test Network Connectivity",
        "description": (
            "ping sends ICMP echo requests to check if a host is reachable and measure response time.\n"
            "It's typically the first step when diagnosing network issues.\n"
            "On Linux, ping runs indefinitely by default (Ctrl+C to stop)."
        ),
        "syntax": "ping [-c count] hostname_or_IP",
        "options": [
            ("-c N",  "Stop after sending N packets"),
            ("-i sec","Set sending interval (default 1 second)"),
        ],
        "examples": [
            {"cmd": "ping -c 3 localhost", "desc": "Test connectivity to localhost (3 packets)",
             "note": "localhost (127.0.0.1) always responds. time= shows response time in ms.", "runnable": True, "cwd": None},
            {"cmd": "ping -c 2 8.8.8.8", "desc": "Test connectivity to Google's DNS server (8.8.8.8)",
             "note": "Requires internet access. A response confirms your connection is working.", "runnable": True, "cwd": None},
        ],
    },
    {
        "id": "lesson_curl", "category": "network",
        "command": "curl / wget",
        "title": "HTTP Requests and File Downloads",
        "description": (
            "curl sends requests to URLs and displays or saves the response.\n"
            "wget downloads files from URLs and saves them locally.\n"
            "Both are widely used for testing APIs and downloading files."
        ),
        "syntax": "curl [options] URL\nwget [options] URL",
        "options": [
            ("-o filename", "Save response to a file"),
            ("-I",          "Fetch headers only (useful for checking status codes)"),
            ("-s",          "Silent mode (no progress output)"),
            ("-L",          "Follow redirects"),
        ],
        "examples": [
            {"cmd": "curl -I https://example.com", "desc": "Check HTTP response headers for example.com",
             "note": "Shows the status code (e.g., HTTP/1.1 200 OK) and headers.", "runnable": True, "cwd": None},
            {"cmd": "curl -s https://httpbin.org/ip", "desc": "Check your public IP address",
             "note": "httpbin.org is a public HTTP testing service. -s hides the progress bar.", "runnable": True, "cwd": None},
        ],
    },
    {
        "id": "lesson_ssh_dns", "category": "network",
        "command": "ssh / nslookup",
        "title": "Remote Login and DNS Lookup",
        "description": (
            "ssh (Secure Shell) establishes an encrypted remote login session.\n"
            "nslookup resolves domain names to IP addresses (DNS query).\n"
            "Both are essential knowledge for server administration."
        ),
        "syntax": "ssh [user@]hostname\nnslookup domain",
        "options": [
            ("-p port",    "Specify port (default 22)"),
            ("-i keyfile", "Specify private key file for authentication"),
            ("-L",         "Local port forwarding"),
            ("ssh-keygen", "Generate an SSH key pair"),
        ],
        "examples": [
            {"cmd": "nslookup google.com", "desc": "Resolve google.com to an IP address via DNS",
             "note": "Server is the DNS server; Address is the IP for the domain.", "runnable": True, "cwd": None},
            {"cmd": "nslookup 8.8.8.8", "desc": "Reverse-lookup an IP address to a hostname",
             "note": "Returns a hostname if reverse DNS is configured for that IP.", "runnable": True, "cwd": None},
        ],
    },
    # ──────────────────────────────────────────────────────────
    # File Operations (additional)
    # ──────────────────────────────────────────────────────────
    {
        "id": "lesson_ln", "category": "file",
        "command": "ln",
        "title": "Symbolic and Hard Links",
        "description": (
            "ln creates a link (an alias) to a file.\n"
            "A symbolic link (-s) works like a shortcut and stores the path to the original.\n"
            "A hard link is another name for the same data; it persists even if the original is deleted."
        ),
        "syntax": "ln -s target linkname",
        "options": [
            ("-s",          "Create a symbolic link (hard link is the default)"),
            ("readlink",    "Show where a symbolic link points"),
            ("readlink -f", "Resolve the symlink to an absolute path"),
        ],
        "examples": [
            {"cmd": "ln -s hello.txt link_to_hello && ls -la link_to_hello",
             "desc": "Create a symbolic link to hello.txt",
             "note": "ls -la shows l (link) and -> hello.txt indicating the target.", "runnable": True, "cwd": "sandbox"},
            {"cmd": "cat link_to_hello", "desc": "Read a file through a symbolic link",
             "note": "The symlink transparently accesses the original file's contents.", "runnable": True, "cwd": "sandbox"},
            {"cmd": "readlink link_to_hello", "desc": "Show where the symlink points",
             "note": "readlink displays the path the link points to.", "runnable": True, "cwd": "sandbox"},
        ],
    },
    {
        "id": "lesson_chmod_chown", "category": "file",
        "command": "chmod / chown",
        "title": "Change File Permissions and Ownership",
        "description": (
            "chmod (change mode) changes a file's access permissions.\n"
            "Permissions are combinations of read (r=4), write (w=2), execute (x=1)\n"
            "applied separately to owner, group, and others.\n"
            "chown (change owner) changes file ownership (requires admin privileges)."
        ),
        "syntax": "chmod [mode] file\nchown [user[:group]] file",
        "options": [
            ("chmod 755",  "rwxr-xr-x: owner has full access; others can read and execute"),
            ("chmod 644",  "rw-r--r--: owner can read/write; others can only read"),
            ("chmod +x",   "Add execute permission for everyone"),
            ("chmod -R",   "Apply change recursively to a directory"),
        ],
        "examples": [
            {"cmd": "ls -l hello.txt", "desc": "Check current permissions",
             "note": "Displayed as -rw-r--r--. The leading - means file (d means directory).", "runnable": True, "cwd": "sandbox"},
            {"cmd": "chmod 755 hello.txt && ls -l hello.txt", "desc": "Set permissions to 755 (rwxr-xr-x)",
             "note": "7=rwx, 5=r-x. Owner gets full access; group and others get read+execute.", "runnable": True, "cwd": "sandbox"},
            {"cmd": "chmod +x hello.txt && ls -l hello.txt", "desc": "Add execute permission (symbolic notation)",
             "note": "+x grants execute to everyone. u+x adds only for the owner.", "runnable": True, "cwd": "sandbox"},
        ],
    },
    {
        "id": "lesson_tar", "category": "file",
        "command": "tar / gzip / zip",
        "title": "Archiving and Compression",
        "description": (
            "tar bundles multiple files into a single archive.\n"
            "Combined with gzip, it creates .tar.gz (tgz) compressed archives.\n"
            "zip creates .zip archives, which are easy to share with Windows users."
        ),
        "syntax": "tar [options] archive target\ngzip file",
        "options": [
            ("tar -czf",     "Create a gzip-compressed archive"),
            ("tar -xzf",     "Extract a gzip-compressed archive"),
            ("tar -tzf",     "List archive contents without extracting"),
            ("tar -xzf -C d/","Extract into a specific directory"),
        ],
        "examples": [
            {"cmd": "tar -czf docs_backup.tar.gz docs/ && ls -lh docs_backup.tar.gz",
             "desc": "Compress the docs/ directory into a tar.gz archive",
             "note": "c=create, z=gzip, f=filename. The original directory remains.", "runnable": True, "cwd": "sandbox"},
            {"cmd": "tar -tzf docs_backup.tar.gz", "desc": "List archive contents without extracting",
             "note": "t=list. Always verify archive contents before extracting.", "runnable": True, "cwd": "sandbox"},
            {"cmd": "tar -xzf docs_backup.tar.gz -C /tmp/ && ls /tmp/docs",
             "desc": "Extract the archive into /tmp",
             "note": "-C specifies the extraction directory.", "runnable": True, "cwd": "sandbox"},
            {"cmd": "gzip -k hello.txt && ls -lh hello.txt hello.txt.gz",
             "desc": "Compress hello.txt with gzip (keep original)",
             "note": "-k (keep) retains the original. gunzip decompresses it.", "runnable": True, "cwd": "sandbox"},
        ],
    },
    {
        "id": "lesson_diff_stat", "category": "file",
        "command": "diff / stat / file",
        "title": "Compare Files and Check Metadata",
        "description": (
            "diff shows differences between two files — great for reviewing code changes.\n"
            "stat shows detailed file metadata (inode, timestamps, etc.).\n"
            "file determines the type of a file (text, binary, script, etc.)."
        ),
        "syntax": "diff [options] file1 file2\nstat file\nfile file",
        "options": [
            ("diff -u",  "Unified format (like git diff output)"),
            ("diff -r",  "Compare directories recursively"),
            ("stat",     "Show inode, access/modify/change times, permissions"),
            ("file",     "Determine file type"),
        ],
        "examples": [
            {"cmd": "echo -e 'apple\\nbanana\\ncherry' > /tmp/f1.txt && echo -e 'apple\\nblueberry\\ncherry' > /tmp/f2.txt && diff /tmp/f1.txt /tmp/f2.txt",
             "desc": "Show differences between two files",
             "note": "< means line only in f1; > means line only in f2.", "runnable": True, "cwd": None},
            {"cmd": "diff -u /tmp/f1.txt /tmp/f2.txt", "desc": "Show diff in unified format",
             "note": "- is a removed line; + is an added line. git diff uses this format.", "runnable": True, "cwd": None},
            {"cmd": "stat hello.txt", "desc": "Show detailed metadata for hello.txt",
             "note": "Note the three timestamps: Access, Modify (data), and Change (metadata).", "runnable": True, "cwd": "sandbox"},
            {"cmd": "file hello.txt src/main.py /bin/ls", "desc": "Determine the type of multiple files",
             "note": "Shows differences between a text file, a Python script, and an executable binary.", "runnable": True, "cwd": "sandbox"},
        ],
    },
    # ──────────────────────────────────────────────────────────
    # Text Processing (additional)
    # ──────────────────────────────────────────────────────────
    {
        "id": "lesson_awk", "category": "text",
        "command": "awk",
        "title": "Field Processing and Aggregation (awk)",
        "description": (
            "awk is a powerful tool for processing text field by field (column by column).\n"
            "It's used for filtering, transforming, and aggregating structured text like CSV.\n"
            "Pattern-action pairs let you express complex text processing in a single line."
        ),
        "syntax": "awk '[pattern] { action }' file",
        "options": [
            ("-F ','",      "Set field separator (e.g., comma for CSV)"),
            ("$1, $2, ...", "Reference each field ($0 = entire line)"),
            ("NR",          "Current record (line) number"),
            ("NF",          "Number of fields in the current line"),
            ("BEGIN / END", "Blocks that run before/after all lines"),
        ],
        "examples": [
            {"cmd": "awk -F',' '{print $1}' data.csv", "desc": "Print the first column (name) from the CSV",
             "note": "-F',' sets comma as the field separator. $1 is the first field.", "runnable": True, "cwd": "sandbox"},
            {"cmd": "awk -F',' 'NR>1 {print $1, $3}' data.csv", "desc": "Skip header row and print name and city",
             "note": "NR>1 processes rows from line 2 onward.", "runnable": True, "cwd": "sandbox"},
            {"cmd": "awk -F',' 'NR>1 {sum+=$2} END{print \"Average age:\", sum/(NR-1)}' data.csv",
             "desc": "Calculate the average age from the CSV",
             "note": "The END block runs after all lines are processed.", "runnable": True, "cwd": "sandbox"},
            {"cmd": "awk '{print NR\": \"$0}' log.txt", "desc": "Add line numbers to the log file",
             "note": "NR is the line number. Similar to cat -n but awk allows more flexible processing.", "runnable": True, "cwd": "sandbox"},
        ],
    },
    {
        "id": "lesson_cut_tr", "category": "text",
        "command": "cut / tr / paste",
        "title": "Extract Columns, Translate Chars, Merge Files",
        "description": (
            "cut extracts columns (fields) from text.\n"
            "tr (translate) converts or deletes characters.\n"
            "paste joins files horizontally (column-by-column)."
        ),
        "syntax": "cut -d delim -f fields [file]\ntr [options] set1 set2",
        "options": [
            ("cut -d',' -f2",  "Extract the 2nd field of a comma-separated file"),
            ("cut -c1-5",      "Extract characters 1–5"),
            ("tr 'a-z' 'A-Z'", "Convert lowercase to uppercase"),
            ("tr -d '\\n'",    "Delete newlines"),
            ("tr -s ' '",      "Squeeze consecutive spaces into one"),
        ],
        "examples": [
            {"cmd": "cut -d',' -f1,3 data.csv", "desc": "Extract the name and city columns from the CSV",
             "note": "-f1,3 extracts fields 1 and 3. -f1-3 extracts a range.", "runnable": True, "cwd": "sandbox"},
            {"cmd": "echo 'Hello World' | tr 'a-z' 'A-Z'", "desc": "Convert to uppercase",
             "note": "tr does one-to-one character substitution.", "runnable": True, "cwd": "sandbox"},
            {"cmd": "cat numbers.txt | tr '\\n' ',' | sed 's/,$/\\n/'",
             "desc": "Join multiple lines of numbers into one comma-separated line",
             "note": "Replacing newlines with commas is a classic tr pattern.", "runnable": True, "cwd": "sandbox"},
            {"cmd": "paste numbers.txt numbers.txt", "desc": "Display the same file as two side-by-side columns",
             "note": "paste joins files horizontally, unlike cat which joins vertically.", "runnable": True, "cwd": "sandbox"},
        ],
    },
    {
        "id": "lesson_xargs_tee", "category": "text",
        "command": "xargs / tee",
        "title": "Extend Pipelines with xargs and tee",
        "description": (
            "xargs reads from stdin and uses the input as arguments for another command.\n"
            "It's especially useful for batch-processing many files at once.\n"
            "tee splits a pipeline — simultaneously saving to a file and passing through."
        ),
        "syntax": "cmd | xargs [command]\ncmd | tee [options] file",
        "options": [
            ("xargs -I {}", "Use {} as a placeholder for each input item"),
            ("xargs -P N",  "Run N parallel processes"),
            ("tee -a",      "Append to the file instead of overwriting"),
        ],
        "examples": [
            {"cmd": "find . -name '*.txt' | xargs wc -l", "desc": "Count lines in all .txt files at once",
             "note": "xargs passes find's output as arguments to wc -l.", "runnable": True, "cwd": "sandbox"},
            {"cmd": "find . -name '*.py' | xargs grep -l 'def'", "desc": "Find Python files containing 'def'",
             "note": "grep -l prints only filenames. A classic batch search pattern with xargs.", "runnable": True, "cwd": "sandbox"},
            {"cmd": "ls | tee filelist.txt | wc -l", "desc": "Save ls output to a file while also counting lines",
             "note": "tee splits the pipeline: output goes to the file AND continues to wc -l.", "runnable": True, "cwd": "sandbox"},
        ],
    },
    {
        "id": "lesson_less", "category": "text",
        "command": "less / more",
        "title": "Pager (Browse Large Files)",
        "description": (
            "less shows a large file one screen at a time.\n"
            "Unlike cat, it doesn't load the whole file at once, making it faster.\n"
            "It's commonly used for browsing log files and man pages."
        ),
        "syntax": "less [file]\ncmd | less",
        "options": [
            ("Space / f", "Go to next page"),
            ("b",         "Go back one page"),
            ("/ pattern", "Search forward"),
            ("q",         "Quit"),
        ],
        "examples": [
            {"cmd": "less log.txt", "desc": "Browse log.txt in the pager",
             "note": "Press q to quit, / to search text.", "runnable": False,
             "simulated_output": "2024-01-01 INFO: Server started\n2024-01-01 ERROR: Database connection error\n...\n[END]  <- press q to quit, / to search",
             "cwd": "sandbox"},
            {"cmd": "ps aux | less", "desc": "Browse long ps output comfortably",
             "note": "Piping command output into less lets you scroll through long results.", "runnable": False,
             "simulated_output": "USER  PID  %CPU  %MEM  COMMAND\n...\n(scrollable)", "cwd": None},
        ],
    },
    # ──────────────────────────────────────────────────────────
    # Process Management (additional)
    # ──────────────────────────────────────────────────────────
    {
        "id": "lesson_crontab", "category": "process",
        "command": "crontab / at",
        "title": "Scheduled Task Automation",
        "description": (
            "crontab schedules commands to run automatically at regular intervals.\n"
            "at runs a command once at a specified time.\n"
            "Both are used for automating backups, log rotation, and monitoring."
        ),
        "syntax": "crontab -e\nmin hr day month weekday command",
        "options": [
            ("crontab -e",  "Edit your crontab in an editor"),
            ("crontab -l",  "List your current crontab"),
            ("crontab -r",  "Remove your crontab"),
            ("*/5 * * * *", "Run every 5 minutes"),
            ("0 2 * * *",   "Run at 2 AM every day"),
        ],
        "examples": [
            {"cmd": "crontab -l", "desc": "Show current crontab entries",
             "note": "If no crontab is set, you'll see 'no crontab for user'.", "runnable": True, "cwd": None},
            {"cmd": "echo '# Run daily at midnight: 0 0 * * * /path/to/backup.sh' | cat",
             "desc": "Review cron syntax (edit with crontab -e in practice)",
             "note": "Format: min(0-59) hr(0-23) day(1-31) month(1-12) weekday(0-7). * means every.", "runnable": True, "cwd": None},
            {"cmd": "at -l 2>/dev/null || echo 'No pending at jobs'",
             "desc": "Check the at job queue",
             "note": "Schedule with: echo 'cmd' | at now + 1 minute", "runnable": True, "cwd": None},
        ],
    },
    {
        "id": "lesson_lsof_watch", "category": "process",
        "command": "lsof / watch / timeout",
        "title": "Advanced Process and File Monitoring",
        "description": (
            "lsof (list open files) shows which files and ports a process has open.\n"
            "watch reruns a command periodically and updates the display in real time.\n"
            "timeout limits how long a command can run before being killed."
        ),
        "syntax": "lsof [options]\nwatch -n secs command\ntimeout secs command",
        "options": [
            ("lsof -i",         "Show processes with open network connections"),
            ("lsof -i :port",   "Show which process is using a specific port"),
            ("watch -n 2",      "Update display every 2 seconds"),
            ("timeout 5",       "Kill the command after 5 seconds"),
        ],
        "examples": [
            {"cmd": "lsof -i :80 2>/dev/null || echo 'No process is using port 80'",
             "desc": "Check which process is using port 80",
             "note": "If a web server is running, you'll see nginx or httpd.", "runnable": True, "cwd": None},
            {"cmd": "lsof /tmp 2>/dev/null | head -5", "desc": "Show first 5 processes using /tmp",
             "note": "Useful when a filesystem can't be unmounted — find who has files open.", "runnable": True, "cwd": None},
            {"cmd": "timeout 3 sleep 10 && echo 'Done' || echo 'Timed out'",
             "desc": "Time out sleep 10 after 3 seconds",
             "note": "timeout kills the process after the specified seconds.", "runnable": True, "cwd": None},
        ],
    },
    {
        "id": "lesson_nice", "category": "process",
        "command": "nice / renice",
        "title": "Control Process Priority",
        "description": (
            "nice starts a command with a specified CPU priority (nice value).\n"
            "renice changes the priority of an already-running process.\n"
            "Nice values range from -20 (highest) to 19 (lowest priority).\n"
            "Run heavy background jobs at low priority so they don't slow down other work."
        ),
        "syntax": "nice -n value command\nrenice value PID",
        "options": [
            ("nice -n 10",        "Start at nice +10 (lower priority)"),
            ("nice -n -10",       "Start at nice -10 (higher priority, root only)"),
            ("renice 5 PID",      "Change a running process's nice value to 5"),
            ("ps -o pid,ni,comm", "Show PID, nice value, and command name"),
        ],
        "examples": [
            {"cmd": "nice -n 19 sleep 5 & ps -o pid,ni,comm | grep sleep",
             "desc": "Start sleep at low priority (nice=19) and verify",
             "note": "The ni column shows 19. Low-priority batch jobs won't interrupt your other work.", "runnable": True, "cwd": None},
            {"cmd": "ps -o pid,ni,comm | head -8", "desc": "Show PID, nice value, and command for running processes",
             "note": "Normal processes have a nice value of 0.", "runnable": True, "cwd": None},
        ],
    },
    # ──────────────────────────────────────────────────────────
    # Networking (additional)
    # ──────────────────────────────────────────────────────────
    {
        "id": "lesson_ip", "category": "network",
        "command": "ip / ifconfig",
        "title": "Check Network Interfaces",
        "description": (
            "ifconfig is the traditional network configuration command, available on macOS too.\n"
            "ip is its modern replacement on Linux with more features.\n"
            "Use these to check your IP address, subnet, and MAC address."
        ),
        "syntax": "ifconfig [interface]\nip addr show\nip route show",
        "options": [
            ("ifconfig",      "Show all interface settings"),
            ("ip addr show",  "Show all interface IP addresses (Linux)"),
            ("ip route show", "Show routing table"),
            ("ip link show",  "Show interface status"),
        ],
        "examples": [
            {"cmd": "ifconfig lo0 2>/dev/null || ip addr show lo",
             "desc": "Show loopback interface (lo) information",
             "note": "inet 127.0.0.1 is the loopback address. macOS uses lo0; Linux uses lo.", "runnable": True, "cwd": None},
            {"cmd": "ip route show 2>/dev/null || netstat -rn | head -10",
             "desc": "Check the routing table",
             "note": "The 'default' row shows your default gateway (your router's IP).", "runnable": True, "cwd": None},
            {"cmd": "hostname", "desc": "Show this machine's hostname",
             "note": "The hostname is how this machine identifies itself on the network.", "runnable": True, "cwd": None},
        ],
    },
    {
        "id": "lesson_netstat_dig", "category": "network",
        "command": "netstat / ss / dig",
        "title": "Connection Status and DNS Investigation",
        "description": (
            "netstat shows network connections, routing tables, and statistics.\n"
            "ss is netstat's faster successor.\n"
            "dig is a powerful tool for querying DNS in detail."
        ),
        "syntax": "netstat [options]\nss [options]\ndig [options] domain",
        "options": [
            ("netstat -an",  "Show all connections and listening ports"),
            ("ss -tlnp",     "Show LISTEN TCP ports with process names"),
            ("dig domain",   "Show detailed DNS information"),
            ("dig +short",   "Show only the result (e.g., IP address)"),
        ],
        "examples": [
            {"cmd": "netstat -an 2>/dev/null | head -15",
             "desc": "Show current network connections (first 15)",
             "note": "LISTEN = waiting; ESTABLISHED = connected; TIME_WAIT = closing.", "runnable": True, "cwd": None},
            {"cmd": "ss -tlnp 2>/dev/null | head -10 || netstat -tlnp 2>/dev/null | head -10",
             "desc": "Show LISTEN TCP ports",
             "note": "Useful for checking which services are running on which ports.", "runnable": True, "cwd": None},
            {"cmd": "dig +short google.com", "desc": "Look up google.com's IP address via DNS",
             "note": "+short prints just the IP. dig google.com A shows the full record.", "runnable": True, "cwd": None},
        ],
    },
    {
        "id": "lesson_scp_rsync", "category": "network",
        "command": "scp / rsync",
        "title": "Secure Remote File Transfer",
        "description": (
            "scp (secure copy) copies files securely over SSH.\n"
            "rsync transfers only changed parts, making it fast for large syncs.\n"
            "rsync is especially effective for regular backups of many files."
        ),
        "syntax": "scp [options] source dest\nrsync [options] source dest",
        "options": [
            ("scp -r",         "Copy a directory recursively"),
            ("rsync -av",      "Archive mode + verbose output"),
            ("rsync -avz",     "Enable gzip compression during transfer"),
            ("rsync --delete", "Delete files on dest that no longer exist on source"),
            ("rsync -n",       "Dry run (show what would be transferred)"),
        ],
        "examples": [
            {"cmd": "echo 'scp usage:' && echo '  local -> remote: scp file.txt user@host:~/dest/' && echo '  remote -> local: scp user@host:~/file.txt ./dest/'",
             "desc": "Review basic scp usage",
             "note": "scp uses the same key/password authentication as SSH.", "runnable": True, "cwd": None},
            {"cmd": "rsync -av --dry-run /tmp/cmd_learn_sandbox/ /tmp/rsync_test/",
             "desc": "rsync dry run (no actual transfer)",
             "note": "--dry-run shows what would be synced without actually doing it. Always test first.", "runnable": True, "cwd": None},
        ],
    },
    # ──────────────────────────────────────────────────────────
    # Shell & Environment
    # ──────────────────────────────────────────────────────────
    {
        "id": "lesson_man", "category": "shell",
        "command": "man / which / type / help",
        "title": "Get Help and Find Commands",
        "description": (
            "man (manual) shows the full manual page for a command.\n"
            "which finds the path of the executable for a command.\n"
            "type tells you whether a command is a shell built-in or an external program.\n"
            "These are your first stop when learning an unfamiliar command."
        ),
        "syntax": "man command\nwhich command\ntype command",
        "options": [
            ("man -k keyword",  "Search manuals by keyword (same as apropos)"),
            ("man 5 passwd",    "Show a specific manual section"),
            ("which -a",        "Show all matches in PATH"),
            ("command --help",  "Brief help available for most commands"),
        ],
        "examples": [
            {"cmd": "which ls", "desc": "Find the path of the ls executable",
             "note": "Shows something like /bin/ls or /usr/bin/ls.", "runnable": True, "cwd": None},
            {"cmd": "which python3 2>/dev/null || echo 'python3 not found'",
             "desc": "Check where python3 is installed",
             "note": "which prints nothing if the command isn't found.", "runnable": True, "cwd": None},
            {"cmd": "type cd && type ls", "desc": "Check the type of cd and ls",
             "note": "cd is a shell builtin; ls is an external command (/bin/ls).", "runnable": True, "cwd": None},
            {"cmd": "ls --help 2>&1 | head -15", "desc": "Show brief help for ls",
             "note": "--help works for most commands and is more concise than man.", "runnable": True, "cwd": None},
        ],
    },
    {
        "id": "lesson_env", "category": "shell",
        "command": "env / export / source",
        "title": "Manage Environment Variables",
        "description": (
            "Environment variables are named values available to the shell and child processes.\n"
            "export sets a variable and passes it down to child processes.\n"
            "source (or .) runs a file in the current shell context."
        ),
        "syntax": "export VAR=value\nenv\nsource file",
        "options": [
            ("export VAR=val",   "Set a variable and export it to child processes"),
            ("env",              "List all current environment variables"),
            ("printenv VAR",     "Show the value of a specific variable"),
            ("unset VAR",        "Delete an environment variable"),
            ("source ~/.bashrc", "Reload your shell config in the current shell"),
        ],
        "examples": [
            {"cmd": "echo \"Home: $HOME\" && echo \"User: $USER\" && echo \"Shell: $SHELL\"",
             "desc": "Check commonly used environment variables",
             "note": "$HOME, $USER, $SHELL, and $PATH are the most important ones.", "runnable": True, "cwd": None},
            {"cmd": "export GREETING='Hello!' && echo $GREETING",
             "desc": "Set a new environment variable and verify it",
             "note": "Exported variables are passed to child processes. Without export, it stays in the current shell only.", "runnable": True, "cwd": None},
            {"cmd": "env | grep PATH", "desc": "Check the current value of PATH",
             "note": "PATH is a colon-separated list of directories. Commands are searched in this order.", "runnable": True, "cwd": None},
            {"cmd": "printenv SHELL", "desc": "Show which shell you are using",
             "note": "printenv prints one variable. Same as: env | grep ^SHELL=", "runnable": True, "cwd": None},
        ],
    },
    {
        "id": "lesson_alias_history", "category": "shell",
        "command": "alias / history",
        "title": "Aliases and Command History",
        "description": (
            "alias gives a short name to a long command.\n"
            "Use it to set default options or fix common typos.\n"
            "history manages the record of commands you've run."
        ),
        "syntax": "alias name='command'\nhistory [n]",
        "options": [
            ("alias",        "List all current aliases"),
            ("unalias name", "Remove an alias"),
            ("history N",    "Show the last N history entries"),
            ("!N",           "Re-run command number N"),
            ("!!",           "Re-run the previous command (handy with sudo !!)"),
            ("Ctrl+R",       "Incremental search through history"),
        ],
        "examples": [
            {"cmd": "alias", "desc": "List all current aliases",
             "note": "Your OS or shell may have default aliases already configured.", "runnable": True, "cwd": None},
            {"cmd": "alias ll='ls -la' && alias gs='git status' && alias",
             "desc": "Set useful aliases and confirm",
             "note": "To persist aliases across sessions, add them to ~/.bashrc or ~/.zshrc.", "runnable": True, "cwd": None},
            {"cmd": "history | tail -10", "desc": "Show the last 10 history entries",
             "note": "Use !N to re-run entry N. Ctrl+R searches history interactively.", "runnable": True, "cwd": None},
            {"cmd": "history | grep ls | tail -5", "desc": "Search history for commands containing ls",
             "note": "Useful for recalling past options you used with a command.", "runnable": True, "cwd": None},
        ],
    },
    {
        "id": "lesson_shell_vars", "category": "shell",
        "command": "Variables / Quoting / Globbing",
        "title": "Shell Variables, Quoting, and Glob Expansion",
        "description": (
            "Shell variables let you name and reuse values.\n"
            "Quoting controls how special characters and spaces are handled.\n"
            "Globbing (wildcards) matches filenames by pattern."
        ),
        "syntax": "VAR=value\n$VAR  <- reference\n\"...$VAR...\"  <- variable expanded\n'...$VAR...'  <- literal, no expansion",
        "options": [
            ("*",               "Any string of 0 or more characters (e.g., *.txt)"),
            ("?",               "Any single character (e.g., file?.txt)"),
            ("[abc]",           "One of a, b, or c"),
            ("${VAR:-default}", "Use default if VAR is unset or empty"),
        ],
        "examples": [
            {"cmd": "NAME='World' && echo \"Hello, $NAME!\" && echo 'Hello, $NAME!'",
             "desc": "See the difference between double and single quotes",
             "note": "Double quotes expand variables. Single quotes treat everything literally.", "runnable": True, "cwd": None},
            {"cmd": "ls /tmp/*.log 2>/dev/null || ls /tmp/*.txt 2>/dev/null || echo 'No matching files found'",
             "desc": "Use glob * to list files matching a pattern",
             "note": "* is expanded by the shell into matching filenames before the command runs.", "runnable": True, "cwd": None},
            {"cmd": "for f in /tmp/cmd_learn_sandbox/*.txt; do echo \"File: $f\"; done",
             "desc": "Process .txt files in a for loop using glob expansion",
             "note": "Glob expansion is a fundamental pattern for batch file processing in scripts.", "runnable": True, "cwd": None},
            {"cmd": "GREETING=${UNDEFINED_VAR:-'default value'} && echo $GREETING",
             "desc": "Use a default value when a variable is unset",
             "note": "${VAR:-default} uses default when VAR is unset or empty. A safe scripting pattern.", "runnable": True, "cwd": None},
        ],
    },
    {
        "id": "lesson_shell_script", "category": "shell",
        "command": "Shell Script Basics",
        "title": "Writing Shell Scripts",
        "description": (
            "A shell script automates sequences of commands.\n"
            "Common uses include deployment, backups, and repetitive tasks.\n"
            "Start with #!/bin/bash (shebang), then chmod +x to make it executable."
        ),
        "syntax": "#!/bin/bash\nvariables, if, for, while, functions",
        "options": [
            ("#!/bin/bash", "Shebang: specifies the interpreter for the script"),
            ("set -e",      "Exit immediately if any command fails"),
            ("set -u",      "Treat unset variables as errors"),
            ("if [ cond ]", "Conditional branching"),
            ("for i in ...", "Loop processing"),
        ],
        "examples": [
            {"cmd": "cat > /tmp/hello.sh << 'EOF'\n#!/bin/bash\nNAME=${1:-World}\necho \"Hello, $NAME!\"\nEOF\nchmod +x /tmp/hello.sh && /tmp/hello.sh && /tmp/hello.sh Claude",
             "desc": "Create and run a script that accepts an argument",
             "note": "${1:-World} uses World as the default when no argument is given.", "runnable": True, "cwd": None},
            {"cmd": "for i in 1 2 3 4 5; do echo \"Count: $i\"; done",
             "desc": "Basic for loop",
             "note": "Syntax: for VAR in LIST; do ... done. Also works for looping over files.", "runnable": True, "cwd": None},
            {"cmd": "FILE=/tmp/cmd_learn_sandbox/hello.txt; if [ -f \"$FILE\" ]; then echo \"Exists\"; else echo \"Not found\"; fi",
             "desc": "Check if a file exists with an if statement",
             "note": "[ -f file ] checks for a regular file. -d for directory, -e for either.", "runnable": True, "cwd": None},
        ],
    },
    # ──────────────────────────────────────────────────────────
    # System Info
    # ──────────────────────────────────────────────────────────
    {
        "id": "lesson_uname", "category": "system",
        "command": "uname / hostname / uptime",
        "title": "Check System Information",
        "description": (
            "uname shows the OS name and kernel version.\n"
            "hostname displays the machine's network name.\n"
            "uptime shows how long the system has been running and the load average."
        ),
        "syntax": "uname [options]\nhostname\nuptime",
        "options": [
            ("uname -a",  "Show all info (OS, hostname, kernel version, etc.)"),
            ("uname -r",  "Show kernel version only"),
            ("uname -s",  "Show OS name only"),
            ("uname -m",  "Show CPU architecture (e.g., x86_64, arm64)"),
            ("uptime -p", "Show uptime in human-readable form (Linux)"),
        ],
        "examples": [
            {"cmd": "uname -a", "desc": "Show all system information",
             "note": "Kernel version, hostname, and CPU architecture are all on one line.", "runnable": True, "cwd": None},
            {"cmd": "uname -s && uname -r && uname -m", "desc": "Show OS name, kernel version, and architecture separately",
             "note": "macOS shows Darwin; Linux shows Linux. Architecture is x86_64 (Intel) or arm64 (Apple Silicon/ARM).", "runnable": True, "cwd": None},
            {"cmd": "hostname", "desc": "Show this machine's hostname",
             "note": "The hostname is the name used to identify this machine on the network.", "runnable": True, "cwd": None},
            {"cmd": "uptime", "desc": "Show uptime and load averages",
             "note": "The three load average numbers are 1-min, 5-min, and 15-min CPU load. Values above the number of cores indicate overload.", "runnable": True, "cwd": None},
        ],
    },
    {
        "id": "lesson_df_du", "category": "system",
        "command": "df / du",
        "title": "Check Disk Usage",
        "description": (
            "df (disk free) shows capacity, used space, and free space for filesystems.\n"
            "du (disk usage) shows how much space a specific directory or file uses.\n"
            "These two commands are essential for troubleshooting disk space issues."
        ),
        "syntax": "df [options] [path]\ndu [options] [path]",
        "options": [
            ("df -h",       "Human-readable sizes (KB/MB/GB)"),
            ("df -T",       "Also show filesystem type"),
            ("du -sh path", "Show total disk usage for that path"),
            ("du -sh *",    "Show usage for each item in current directory"),
            ("du -d 1",     "Show only one level deep"),
        ],
        "examples": [
            {"cmd": "df -h", "desc": "Show disk capacity for all filesystems",
             "note": "If Use% exceeds 90%, you're running low on space.", "runnable": True, "cwd": None},
            {"cmd": "du -sh /tmp/cmd_learn_sandbox/*", "desc": "Show size of each item in the sandbox",
             "note": "-s shows totals only (no subdirectory expansion); * targets each item.", "runnable": True, "cwd": None},
            {"cmd": "du -sh /tmp", "desc": "Show total size of the /tmp directory",
             "note": "To find what's eating disk space, drill down from the largest directories using du.", "runnable": True, "cwd": None},
        ],
    },
    {
        "id": "lesson_who_id", "category": "system",
        "command": "who / id / date",
        "title": "User Information and Date/Time",
        "description": (
            "who shows currently logged-in users.\n"
            "id shows the current user's UID, GID, and group memberships.\n"
            "date displays and formats the system date and time."
        ),
        "syntax": "who\nid [username]\ndate [+format]",
        "options": [
            ("who -a",         "Show detailed info including boot time"),
            ("id",             "Show current user's UID/GID/groups"),
            ("date +%Y-%m-%d", "Show date as YYYY-MM-DD"),
            ("date +%s",       "Show Unix timestamp (seconds since epoch)"),
        ],
        "examples": [
            {"cmd": "who", "desc": "Show logged-in users",
             "note": "Shows username, terminal, and login time.", "runnable": True, "cwd": None},
            {"cmd": "id", "desc": "Show current user's UID, GID, and groups",
             "note": "uid=0(root) means you're the root user. Having sudo/wheel in groups grants admin access.", "runnable": True, "cwd": None},
            {"cmd": "date", "desc": "Show current date and time",
             "note": "Displayed in the system's timezone.", "runnable": True, "cwd": None},
            {"cmd": "date +\"%Y-%m-%d %H:%M:%S\"", "desc": "Show date/time in a format suitable for filenames",
             "note": "Useful for naming backup files: backup_$(date +%Y%m%d).tar.gz", "runnable": True, "cwd": None},
        ],
    },
    {
        "id": "lesson_sys_info", "category": "system",
        "command": "free / dmesg / sysctl",
        "title": "Memory, Kernel Logs, and System Parameters",
        "description": (
            "free shows memory usage (Linux).\n"
            "dmesg displays the kernel ring buffer — boot messages, device errors, etc.\n"
            "sysctl reads and modifies kernel parameters."
        ),
        "syntax": "free -h\ndmesg [| tail]\nsysctl [param]",
        "options": [
            ("free -h",      "Show memory usage in human-readable form (Linux)"),
            ("dmesg | tail", "Check the most recent kernel messages"),
            ("dmesg -T",     "Show timestamps in human-readable form"),
            ("sysctl -a",    "List all kernel parameters"),
        ],
        "examples": [
            {"cmd": "free -h 2>/dev/null || vm_stat | head -10", "desc": "Check memory usage",
             "note": "free is Linux-only. On macOS, use vm_stat instead.", "runnable": True, "cwd": None},
            {"cmd": "dmesg 2>/dev/null | tail -10 || log show --predicate 'eventMessage contains \"error\"' --last 1m 2>/dev/null | tail -5 || echo 'Admin privileges may be needed to view logs'",
             "desc": "Check the most recent kernel messages",
             "note": "Shows USB device events, driver errors, etc. macOS uses the log command.", "runnable": True, "cwd": None},
            {"cmd": "sysctl -a 2>/dev/null | head -10", "desc": "List kernel parameters (first 10)",
             "note": "sysctl works on both macOS and Linux.", "runnable": True, "cwd": None},
            {"cmd": "cat /proc/meminfo 2>/dev/null | head -10 || sysctl hw.memsize 2>/dev/null",
             "desc": "Check physical memory details",
             "note": "Linux uses /proc/meminfo; macOS uses sysctl hw.memsize.", "runnable": True, "cwd": None},
        ],
    },
]

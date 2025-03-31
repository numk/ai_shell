# ai_shell

命令行上的AI助手


**如何设置和使用:**

1.  **安装依赖:**
    ```bash
    pip install requests
    ```

2.  **设置 API Key:**
    * **Windows (CMD):** `set GEMINI_API_KEY=你的API密钥` (仅对当前窗口有效) 或通过系统环境变量设置。
    * **Windows (PowerShell):** `$env:GEMINI_API_KEY="你的API密钥"` (仅对当前窗口有效) 或通过系统环境变量设置。
    * **Linux/macOS (Bash/Zsh):** `export GEMINI_API_KEY='你的API密钥'` (添加到 `.bashrc` 或 `.zshrc` 使其永久生效)。
    * 确保你的 API Key 已经启用 Gemini API。

3.  **保存脚本:** 将上面的代码保存为 `ai.py` 文件。

4.  **使其可执行 (Linux/macOS):**
    ```bash
    chmod +x ai.py
    ```

5.  **创建别名或放入 PATH:**
    * **Linux/macOS:**
        * **选项 A (推荐):** 将 `ai.py` 移动到一个已经在你的 `PATH` 环境变量中的目录，比如 `~/bin` 或 `/usr/local/bin`，并重命名为 `ai`。
            ```bash
            # 假设你有一个 ~/bin 目录且它在 PATH 中
            mkdir -p ~/bin
            mv ai.py ~/bin/ai
            ```
        * **选项 B (别名):** 在你的 shell 配置文件 (`.bashrc`, `.zshrc` 等) 中添加别名:
            ```bash
            alias ai='/path/to/your/ai.py'
            ```
            然后运行 `source ~/.bashrc` (或对应文件) 使别名生效。

    * **Windows:**
        * **选项 A (推荐 - 使用 .bat 批处理):**
            1.  将 `ai.py` 放在一个固定位置，例如 `C:\Scripts\ai.py`。
            2.  创建一个名为 `ai.bat` 的文本文件，内容如下 (确保路径正确)：
                ```batch
                @echo off
                python C:\Scripts\ai.py %*
                ```
            3.  将包含 `ai.bat` 的目录 (例如 `C:\Scripts\`) 添加到系统的 `Path` 环境变量中。你需要重启 CMD 或 PowerShell 才能使更改生效。
        * **选项 B (Python Launcher):** 如果你安装 Python 时勾选了 "Add Python to PATH" 和 "Install launcher for all users (py.exe)"，你可以直接将 `ai.py` 放在 PATH 中的某个目录里，并确保文件第一行的 `#!/usr/bin/env python3` (shebang) 对于 Python Launcher 是有效的 (虽然在 Windows 上 Shebang 不直接起作用，但 `py` 启动器可以识别)。或者直接用 `py C:\path\to\ai.py ...` 调用。但为了简单输入 `ai ...`，使用 `.bat` 文件是 Windows 上更常见的方式。

6.  **运行:**
    打开新的命令行/终端窗口，然后尝试：
    ```bash
    ai 通过端口查询进程ID并杀掉该进程
    ```
    或者
    ```bash
    ai 列出当前目录下所有py文件
    ```

**关于流式输出:**

* 代码中已经实现了流式请求 (`stream=True`)。
* 然而，`rich.markdown.Markdown` 需要完整的 Markdown 文本才能正确渲染。实时地、逐块地渲染 Markdown 很复杂。
* 因此，当前代码会收集所有流式返回的块，然后在最后一次性使用 `rich` 渲染。这提供了一个较好的折中：你能看到 AI 正在处理（通过 `console.status`），并且最终得到格式正确的输出。
* 如果你不需要 Markdown 格式，只想看到原始文本流，可以取消 `print(chunk.text, end="", flush=True)` 的注释，并注释掉最后用 `rich` 渲染的部分。

这个脚本现在应该能满足你的需求了。记得根据你的实际情况调整路径和配置。

```shell
ai docker安装mysql,通过环境变量设置密码
```

```shell
# 安装Docker
curl -fsSL https://get.docker.com | bash

# 拉取MySQL镜像
docker pull mysql:latest

# 运行MySQL容器并设置环境变量
docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=your-password -d mysql:latest

# 查看MySQL服务状态
docker ps -a
```



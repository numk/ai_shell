from os import getenv
import sys
import platform
from textwrap import dedent
from requests import session


class AI:
    def __init__(self, api_key=None):
        self.session = session()
        self.api_key = api_key if api_key else getenv('AI_API_KEY')
        self.system_name = self.get_os_name()

    def get_os_name(self):
        """检测当前操作系统名称"""
        system_name = platform.system()
        if system_name == "Windows":
            return "Windows (cmd/powershell)"
        elif system_name == "Linux":
            return "Linux (bash)"
        elif system_name == "Darwin":
            return "macOS (bash/zsh)"
        else:
            return system_name

    def build_prompt(self, ):
        prompt = f"""
        请扮演一个命令行助手。根据用户的请求和指定的操作系统，提供相应的命令行指令。

        请遵循以下规则：
        1.  **仅** 回复解决用户问题的核心命令行代码。
        2.  使用适合目标操作系统的 Markdown 代码块（例如 ```bash ... ``` 或 ```powershell ... ``` 或 ```cmd ... ``` 或 ```python ... ``` 或 ``` ... ```）来包裹命令。
        3.  **不要** 包含任何解释、说明、介绍、警告、附加说明或任何非命令代码的文字。
        4.  如果需要多个命令或步骤，请按顺序清晰列出，每个命令仍在代码块内。
        5.  如果命令中需要用户替换占位符（如端口号、进程ID），请使用尖括号明确标出，例如 `<端口号>` 或 `<进程ID>`。
        6.  确保输出极其简洁，直接给出命令代码。

        示例:
        用户请求: "通过端口查询进程ID并杀掉该进程"
        目标操作系统: Linux (bash)
        你的回答应该是类似这样（具体命令可能不同）:
        
        ```bash
        # 查找监听指定端口的进程 (将 <端口号> 替换为实际端口)
        sudo lsof -i :<端口号>

        # 找到 PID 后，杀掉进程 (将 <进程ID> 替换为实际 PID)
        sudo kill <进程ID>
        ```
        用户请求: "通过端口查询进程ID并杀掉该进程"
        目标操作系统: Windows (cmd/powershell)
        你的回答应该是类似这样（具体命令可能不同）:
        
        ```powershell
        # 查找使用指定端口的进程并获取其 PID (将 <端口号> 替换为实际端口)
        $process = Get-NetTCPConnection -LocalPort <端口号> | Select-Object -ExpandProperty OwningProcess
        Write-Host "进程 ID (PID): $process"
        
        # 强制停止该进程 (将 <进程ID> 替换为上面找到的 PID)
        Stop-Process -Id <进程ID> -Force
        ```
        
        或者
        
        ```cmd
        :: 查找监听指定端口的进程 PID (将 <端口号> 替换为实际端口)
        netstat -ano | findstr ":<端口号>"
        
        :: 找到 PID 后，强制结束进程 (将 <进程ID> 替换为实际 PID)
        taskkill /PID <进程ID> /F
        ```
        """
        return dedent(prompt)

    def get_answer_by_xunfei(self, user_query):
        prompt = self.build_prompt()
        user_query_ = f'用户请求: "{user_query}"\n目标操作系统: {self.system_name}'
        messages = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_query_}
        ]
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": 'lite',
            "messages": messages,
            # "stream": True,
        }
        response = self.session.post("https://spark-api-open.xf-yun.com/v1/chat/completions", headers=headers, json=payload)
        response_data = response.json()
        print(response_data)
        content = response_data["choices"][0]["message"]["content"]
        return content

    def run(self):
        if len(sys.argv) < 2:
            print("用法: ai <你的问题>")
            print("例如: ai 通过端口查询进程ID并杀掉该进程")
            sys.exit(1)
        user_query = " ".join(sys.argv[1:])
        print(f'用户请求: {user_query}')
        answer = self.get_answer_by_xunfei(user_query)
        print(answer)


if __name__ == '__main__':
    app = AI()
    app.run()

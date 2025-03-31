#! /bin/bash

PYTHON_PATH="/usr/bin/python3"

# 检查python3是否存在
if [ ! -f "$PYTHON_PATH" ]; then
    echo "python3 not found"
    exit 1
fi

# 进入当前目录
cd "$(dirname "$0")"

# 执行python3脚本
"$PYTHON_PATH" ai.py "$@"


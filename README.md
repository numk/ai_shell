# ai_shell

命令行上的AI助手

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

    

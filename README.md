# 图像识别应用

这是一个基于 Gradio 的图像识别应用，使用 OpenAI 的 API 来分析图像并返回描述信息。

## 功能介绍

这款产品是一款专业的图像识别软件，可以将任何类型的照片（包括证件照片、风景照、人物照等）上传到大模型。由大模型进行主体解析，返回主体内容。

## 先决条件

在开始之前，请确保你已经安装了以下软件：

- [Docker](https://www.docker.com/)
- [Python 3.11](https://www.python.org/downloads/)

## 安装依赖

如果你想在本地运行应用，请按照以下步骤操作：

```bash
pip install -r requirements.txt
```

## 环境变量配置

在项目根目录下`.env` 文件，并修改以下内容

请将 `your_api_key` 和 `your_api_base` 替换为你的 OpenAI API 密钥和基 URL。

## 本地运行

在配置好环境变量后，你可以使用以下命令运行应用：

```bash
python main.py
```

## 使用 Docker

### 构建 Docker 镜像

在项目根目录下执行以下命令来构建 Docker 镜像：

```bash
docker build -t your_image_name .
```

### 运行 Docker 容器

```bash
docker run -d -p 7860:7860 --name your_container_name your_image_name
```

## 访问应用

在成功启动应用后，你可以通过浏览器访问以下 URL 来使用图像识别功能：

```
http://localhost:7860
```

## 目录结构

以下是项目的目录结构：

```
.
├── Dockerfile
├── .dockerignore
├── README.md
├── requirements.txt
├── main.py
├── LICENSE
└── .env
```

## 贡献

如果你想为本项目做出贡献，请 fork 此仓库并提交 pull request。

## 许可证

本项目遵循 MIT 许可证。详细信息请参阅 [LICENSE](LICENSE) 文件。
```
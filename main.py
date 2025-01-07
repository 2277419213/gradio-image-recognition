import gradio as gr
import openai
import base64
import requests
from PIL import Image
import io
import os
from dotenv import load_dotenv

# 加载 .env 文件中的环境变量
load_dotenv()

# 设置 OpenAI API 密钥和 base_url
api_key = os.getenv('OPENAI_API_KEY')
if os.getenv('OPENAI_API_BASE'):
    api_base = os.getenv('OPENAI_API_BASE')

def encode_image(image):
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')

def analyze_image(image):
    base64_image = encode_image(image)
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    payload = {
        "model": os.getenv('OPENAI_API_MODEL','gpt-4o'),
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "请仔细观察这张照片，找到照片的主体进行描述，先介绍主体的名称，再介绍主体，使用markdown格式回复，可以加粗重点内容，但是不要用```代码块"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{base64_image}"
                        }
                    }
                ]
            }
        ]
    }
    
    response = requests.post(f"{api_base}/chat/completions", headers=headers, json=payload)
    result = response.json()
    
    # 返回解析结果
    return f"### 图片解析结果\n\n{result['choices'][0]['message']['content']}"

# 自定义CSS样式
css = """
.image-container {
    width: 100%;
    height: 500px;
    display: flex;
    justify-content: center;
    align-items: center;
    border: 1px solid #ccc;
    margin-bottom: 20px;
    overflow: hidden;
}

.image-container img {
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
}
"""

# 创建 Gradio 界面
with gr.Blocks(css=css) as demo:
    gr.Markdown("## 图像识别")
    with gr.Row():
        with gr.Column():
            image_input = gr.Image(label="选择图片上传", type="pil", elem_id="image-input")
            analyze_button = gr.Button("识别")
        with gr.Column():
            output_md = gr.Markdown("### 图片解析结果\n\n\n\n\n\n\n\n\n\n\n\n  -")
    
    analyze_button.click(analyze_image, inputs=image_input, outputs=output_md)

    gr.Markdown("""
    ### 工具介绍及使用方法
    这款产品是一款专业的图像识别软件，可以将任何类型的照片（包括证件照片、风景照、人物照等）上传到大模型。由大模型进行主体解析，返回主体内容。
    """)

# 启动 Gradio 应用
demo.launch(server_name=os.getenv("SERVER_HOST", "0.0.0.0"), server_port=7860)
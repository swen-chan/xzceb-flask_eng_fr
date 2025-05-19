## 🔧 项目简介

本项目是一个基于 Flask 的英法翻译 Web 应用。用户在浏览器输入英文句子后，后台调用 deep_translator 中的 MyMemoryTranslator 接口进行翻译，并将结果返回展示在页面上。该项目适用于客服场景或语言学习工具的原型开发。

## 🚀 技术栈

- Python 3.x
- Flask
- deep_translator（MyMemoryTranslator）
- HTML / CSS (Jinja 模板)
- unittest（用于测试）

## 📁 项目结构

final_project/
├── app.py # Flask 主入口
├── translator.py # 封装翻译函数
├── test_module.py # 单元测试
├── templates/
│ └── index.html # 前端表单页面
├── static/ # 样式文件夹（可选）
└── README.md


## 📦 安装依赖

确保你已经安装 Python，然后运行：

pip install flask deep_translator

▶️ 启动方式
在终端进入项目目录并运行：

python app.py
然后在浏览器中访问：
http://127.0.0.1:5000/

✅ 使用说明
输入英文句子

点击“翻译”按钮

页面下方将显示对应的法文翻译

🧪 测试说明
运行以下命令进行单元测试：
python -m unittest test_module.py

📌 注意事项
本项目使用 MyMemoryTranslator 免费接口，适合演示与测试用途；

翻译质量依赖于第三方接口服务，适合原型开发；

如需扩展为生产服务建议更换为专业翻译 API（如 DeepL、Google Translate）。

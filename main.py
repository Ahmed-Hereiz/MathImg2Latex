from customAgents.agent_llm import SimpleMultiModal
from customAgents.agent_prompt import SimplePrompt
from draw import gui_draw
from prompt import extraction_prompt
from pathlib import Path
from PIL import Image
import json
import markdown
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

with open('config/llm.json', 'r') as json_file:
    config = json.load(json_file)

gui_draw()
image = Image.open("math2latex.png")
multimodal = SimpleMultiModal(api_key=config['api_key'], model=config['model'], temperature=0.7)
prompt = SimplePrompt(text=extraction_prompt, image=image)
prompt.construct_prompt()

output = multimodal.multimodal_generate(prompt=prompt.text, img=prompt.image, stream=True)
html_body = markdown.markdown(output)

html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Markdown with Math</title>
    <script type="text/javascript">
      MathJax = {{
        tex: {{
          inlineMath: [['$', '$'], ['\\(', '\\)']],
          displayMath: [['$$', '$$'], ['\\[', '\\]']]
        }}
      }};
    </script>
    <script type="text/javascript" async
      src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-mml-chtml.min.js">
    </script>
</head>
<body>
    {html_body}
</body>
</html>
"""

output_path = Path('output.html')
with open(output_path, 'w') as html_file:
    html_file.write(html_template)


class MathMarkdownViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Markdown Viewer with Math")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.web_view = QWebEngineView()
        layout.addWidget(self.web_view)
        self.web_view.setHtml(html_template)


# Run the PyQt5 Application
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    viewer = MathMarkdownViewer()
    viewer.show()
    sys.exit(app.exec())

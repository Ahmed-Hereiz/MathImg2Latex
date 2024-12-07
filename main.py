from customAgents.agent_llm import SimpleMultiModal
from customAgents.agent_prompt import SimplePrompt
from customAgents.runtime import SimpleRuntime
from draw import gui_draw
from prompt import extaction_prompt
import json 
from PIL import Image

with open('config/llm.json', 'r') as json_file:
    config = json.load(json_file)

gui_draw()
image = Image.open("math2latex.png")
multimodal = SimpleMultiModal(api_key=config['api_key'],model=config['model'],temperature=0.7)
prompt = SimplePrompt(text=extaction_prompt,image=image)
prompt.construct_prompt()
print(multimodal.multimodal_generate(prompt=prompt.text,img=prompt.image))

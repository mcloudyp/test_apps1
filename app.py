import gradio
def greet(name):
    return "Hello" + name + "!!"
    
iface = gr.Interface(fn=greet, inputs="text", outputs="text")
iface.launch()
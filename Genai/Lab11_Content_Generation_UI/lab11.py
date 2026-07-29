import gradio as gr
from transformers import pipeline

# 1. Text Generator (GPT-2)
text_gen = pipeline("text-generation", model="gpt2")

# 2. Text Summarizer (BART)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_text(prompt):
    result = text_gen(prompt, max_length=100, do_sample=True, temperature=0.7)
    return result[0]["generated_text"]

def summarize_text(text):
    if len(text.split()) < 30:
        return "Please enter a longer text to generate a summary."
    result = summarizer(text, max_length=50, min_length=15, do_sample=False)
    return result[0]["summary_text"]

# Build Gradio Tabbed Interface
with gr.Blocks(title="AI Multimodal Content Generation System") as demo:
    gr.Markdown("# AI Multimodal Content Generation Studio")
    
    with gr.Tab("Text Generation"):
        prompt_input = gr.Textbox(label="Enter Prompt", placeholder="Write a short story about...")
        gen_button = gr.Button("Generate Text")
        gen_output = gr.Textbox(label="Generated Output")
        gen_button.click(generate_text, inputs=prompt_input, outputs=gen_output)
        
    with gr.Tab("Text Summarization"):
        sum_input = gr.Textbox(label="Enter Long Article Text", lines=5)
        sum_button = gr.Button("Summarize Text")
        sum_output = gr.Textbox(label="Summary")
        sum_button.click(summarize_text, inputs=sum_input, outputs=sum_output)

demo.launch()

import gradio as gr
from transformers import pipeline
import evaluate

# Deployment using Gradio
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_and_evaluate(article_text):
    summary = summarizer(article_text, max_length=50, min_length=20, do_sample=False)
    return summary[0]["summary_text"]

app = gr.Interface(
    fn=summarize_and_evaluate,
    inputs=gr.Textbox(lines=6, placeholder="Paste article content here..."),
    outputs=gr.Textbox(label="Generated Summary"),
    title="Deployed Generative AI Summarization Service"
)

# ROUGE Metric Evaluation
rouge = evaluate.load("rouge")

generated_summaries = [
    "Generative AI models produce new content such as text and images."
]
reference_summaries = [
    "Generative AI models are capable of producing new content including text and images."
]

scores = rouge.compute(predictions=generated_summaries, references=reference_summaries)
print("ROUGE Evaluation Scores:", scores)

app.launch(share=True)

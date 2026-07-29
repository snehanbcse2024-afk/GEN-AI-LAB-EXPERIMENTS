# Lab 11: AI-Based Content Generation System (Gradio UI)

## Objective
To build an interactive web-based UI for text generation and text summarization using Gradio and Hugging Face pipelines.

## Theory
Gradio is an open-source Python library for quickly creating machine learning web interfaces. It allows building demos with minimal code and provides:
- Tabbed interfaces for multiple models
- Input/output components (textboxes, buttons)
- One-click deployment with `demo.launch()`

## Code Explanation

### Text Generation Tab
1. Uses GPT-2 pipeline for text generation
2. User enters a prompt
3. Model generates up to 100 tokens with temperature sampling

### Text Summarization Tab
1. Uses BART-large-CNN for summarization
2. User enters long article text (30+ words)
3. Model generates a concise summary

## Dependencies
```
transformers
gradio
torch
```

## Expected Output
- Launches a local web server with a tabbed interface
- Tab 1: Text Generation with prompt input and output
- Tab 2: Text Summarization with article input and summary output

## References
- [Gradio Documentation](https://www.gradio.app/docs)
- [Hugging Face — Gradio](https://huggingface.co/docs/hub/en-gb/gradio)

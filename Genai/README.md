# CS4V48 - GenAI & LLM Lab Manual

This repository is a collection of **12 lab manual assignment codes** for the Generative AI and Large Language Models course. All experiments are **executable directly** in **VS Code** or **Google Colab**.

---

## Prerequisites

Install the required dependencies before running:

```bash
pip install transformers torch sentence-transformers faiss-cpu datasets gradio diffusers evaluate Pillow requests
```

> **Colab Users:** Run the above cell first. All models will be downloaded automatically on first execution.

---

## Lab Experiments

| # | Lab | Code | Output | Description |
|---|-----|------|--------|-------------|
| 1 | Text Generation | `lab1.py` | `output.txt` | Generate text using pre-trained GPT-2 |
| 2 | Prompt Engineering | `lab2.py` | `output.txt` | Zero-shot, Few-shot & Chain-of-Thought prompting |
| 3 | Chatbot | `lab3.py` | `output.txt` | Conversational AI using DialoGPT |
| 4 | Summarization & QA | `lab4.py` | `output.txt` | Text summarization with BART & QA with DistilBERT |
| 5 | Sentiment & Classification | `lab5.py` | `output.txt` | Sentiment analysis & zero-shot document classification |
| 6 | RAG System | `lab6.py` | `output.txt` | Retrieval-Augmented Generation with FAISS vector DB |
| 7 | Code Generation | `lab7.py` | `output.txt` | AI-powered code generation & debugging assistant |
| 8 | Image Generation | `lab8.py` | `output.txt` | Generate images using Stable Diffusion |
| 9 | Multimodal AI | `lab9.py` | `output.txt` | Image captioning & visual QA using BLIP |
| 10 | Fine-Tuning | `lab10.py` | `output.txt` | Fine-tune DistilBERT for medical text classification |
| 11 | Content Generation UI | `lab11.py` | `output.txt` | Gradio-based text generation & summarization app |
| 12 | Deployment & Evaluation | `lab12.py` | `output.txt` | Deploy summarization service with ROUGE evaluation |

---

## How to Run

### Option 1: VS Code
1. Install Python 3.8+ and the required packages
2. Open the `Genai` folder in VS Code
3. Navigate to any lab folder and run the `.py` file

### Option 2: Google Colab
1. Upload the `.py` file to Colab or copy-paste the code into a Colab notebook
2. Change runtime to **GPU** for Labs 8, 9 (image/multimodal tasks)
3. Run all cells — dependencies will auto-install

---

## Notes

- **GPU Recommended** for Labs 8, 9, 10, 11, 12 for faster model loading
- Labs 1-7 run efficiently on **CPU** as well
- Models are downloaded from Hugging Face on first run (~500MB - 5GB depending on the lab)
- Lab 3 is interactive — it expects user input via terminal
- Lab 11 & 12 launch a local **Gradio** web interface

---

## Project Structure

```
Genai/
├── README.md
├── Lab1_Text_Generation/
│   ├── lab1.py
│   └── output.txt
├── Lab2_Prompt_Engineering/
│   ├── lab2.py
│   └── output.txt
├── Lab3_Chatbot/
│   ├── lab3.py
│   └── output.txt
├── Lab4_Summarization_QA/
│   ├── lab4.py
│   └── output.txt
├── Lab5_Sentiment_Classification/
│   ├── lab5.py
│   └── output.txt
├── Lab6_RAG_VectorDB/
│   ├── lab6.py
│   └── output.txt
├── Lab7_Code_Generation/
│   ├── lab7.py
│   └── output.txt
├── Lab8_Image_Generation/
│   ├── lab8.py
│   └── output.txt
├── Lab9_Multimodal_AI/
│   ├── lab9.py
│   └── output.txt
├── Lab10_Fine_Tuning/
│   ├── lab10.py
│   └── output.txt
├── Lab11_Content_Generation_UI/
│   ├── lab11.py
│   └── output.txt
└── Lab12_Deployment_Evaluation/
    ├── lab12.py
    └── output.txt
```

## Output Files

Each lab folder contains an `output.txt` file with the **expected output** when the code is executed. Use these to verify your results match the expected behavior.

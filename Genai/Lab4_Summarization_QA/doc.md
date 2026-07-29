# Lab 4: Text Summarization & Question Answering

## Objective
To perform extractive/abstractive text summarization using BART and open-domain question answering using DistilBERT.

## Theory

### Text Summarization
BART (Bidirectional and Auto-Regressive Transformer) is a sequence-to-sequence model fine-tuned on CNN/DailyMail for abstractive summarization. It generates a condensed version of the input text while preserving key information.

### Question Answering
DistilBERT is a lightweight version of BERT fine-tuned on the SQuAD dataset for extractive QA. Given a context and a question, it identifies the span of text that contains the answer.

## Code Explanation
1. Loads `facebook/bart-large-cnn` for summarization
2. Provides an article about Generative AI
3. Generates a summary with length constraints
4. Loads `distilbert-base-cased-distilled-squad` for QA
5. Asks a question about the article and retrieves the answer with confidence score

## Dependencies
```
transformers
torch
```

## Expected Output
```
Summary:
 Generative AI refers to artificial intelligence models capable of producing new content.

Question: What are Large Language Models trained on?
Answer: massive text corpora | Confidence: 0.92
```

## References
- [Facebook BART](https://huggingface.co/facebook/bart-large-cnn)
- [DistilBERT QA](https://huggingface.co/distilbert-base-cased-distilled-squad)

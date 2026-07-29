# Lab 5: Sentiment Analysis & Document Classification

## Objective
To perform sentiment analysis on reviews and zero-shot document classification without task-specific training.

## Theory

### Sentiment Analysis
A binary classification task where the model assigns a Positive or Negative label to text based on emotional tone. Pre-trained models like `distilbert-base-uncased-finetuned-sst-2-english` are fine-tuned on the SST-2 dataset.

### Zero-Shot Classification
Uses NLI (Natural Language Inference) to classify text into arbitrary labels without retraining. The model checks if the text "entails" each candidate label.

## Code Explanation
1. Loads sentiment analysis pipeline
2. Analyzes two sample reviews (positive and negative)
3. Loads zero-shot classification pipeline (BART-MNLI)
4. Classifies a financial document into candidate categories (Politics, Economy, Sports, Technology)

## Dependencies
```
transformers
torch
```

## Expected Output
```
Review: The new smartphone has an amazing camera! -> POSITIVE (0.999)
Review: The delivery was late and damaged. -> NEGATIVE (0.987)

Document: The central bank raised interest rates...
Economy: 0.89
Politics: 0.07
Technology: 0.03
Sports: 0.01
```

## References
- [Hugging Face — Sentiment Analysis](https://huggingface.co/docs/transformers/tasks/sequence_classification)
- [Zero-Shot Classification](https://huggingface.co/docs/transformers/tasks/zero_shot_classification)

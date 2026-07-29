# Lab 10: Fine-Tuning a Pre-Trained Language Model

## Objective
To fine-tune DistilBERT for domain-specific text classification using the Hugging Face Trainer API.

## Theory
Fine-tuning adapts a pre-trained model to a specific task by continuing training on a smaller, task-specific dataset. This leverages **transfer learning** — the model already understands language, so it only needs to learn the new classification mapping.

### Pipeline
1. Load pre-trained model and tokenizer
2. Tokenize the custom dataset
3. Define training arguments (epochs, batch size, logging)
4. Train using the `Trainer` API
5. Evaluate the fine-tuned model

## Code Explanation
1. Defines a small medical dataset with 4 samples
2. Labels: `1` = needs urgent attention, `0` = normal/routine
3. Loads `distilbert-base-uncased` tokenizer and model with 2 labels
4. Tokenizes all samples with padding and truncation
5. Configures training: 3 epochs, batch size 2, logging every step
6. Trains and prints completion message

## Dependencies
```
transformers
torch
datasets
```

## Expected Output
```
{'loss': 0.693, 'learning_rate': 5e-5, 'epoch': 0.5}
{'loss': 0.521, 'learning_rate': 3.3e-5, 'epoch': 1.0}
...
Fine-tuning completed successfully!
```

## Notes
- Real-world applications require much larger datasets (100+ samples)
- This demo uses 4 samples to illustrate the fine-tuning pipeline
- Extend `data["text"]` and `data["label"]` for production use

## References
- [Hugging Face — Fine-Tuning](https://huggingface.co/docs/transformers/training)
- [Trainer API](https://huggingface.co/docs/transformers/main_classes/trainer)

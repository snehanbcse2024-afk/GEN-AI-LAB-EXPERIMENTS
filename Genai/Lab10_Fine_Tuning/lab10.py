from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import Dataset

# Sample medical domain dataset
data = {
    "text": [
        "Patient exhibits acute severe headache and persistent nausea.",
        "Routine general checkup shows normal vitals and healthy baseline.",
        "High blood pressure and elevated resting heart rate observed during exam.",
        "Patient reports fully recovering with no residual secondary symptoms."
    ],
    "label": [1, 0, 1, 0]  # 1: Needs urgent attention, 0: Normal / Routine
}

dataset = Dataset.from_dict(data)

model_name = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)

def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True, max_length=32)

tokenized_datasets = dataset.map(tokenize_function, batched=True)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)

training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=3,
    per_device_train_batch_size=2,
    logging_steps=1,
    save_strategy="no"
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets,
)

trainer.train()
print("Fine-tuning completed successfully!")

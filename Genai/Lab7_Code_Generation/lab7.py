from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("Salesforce/codegen-350M-mono")
model = AutoModelForCausalLM.from_pretrained("Salesforce/codegen-350M-mono")

# Code Generation Prompt
prompt_gen = "def calculate_factorial(n):\n    \"\"\"Return the factorial of a given non-negative integer n.\"\"\""

inputs = tokenizer(prompt_gen, return_tensors="pt")
outputs = model.generate(**inputs, max_length=100, pad_token_id=tokenizer.eos_token_id)
print("=== Generated Code ===")
print(tokenizer.decode(outputs[0], skip_special_tokens=True))

# Debugging Assistance Prompt
buggy_code = """
# Fix the bug in this function that should calculate average
def calculate_average(numbers):
    total = sum(numbers)
    # Bug: dividing by fixed length instead of len(numbers)
    return total / 10
"""

inputs_debug = tokenizer(buggy_code, return_tensors="pt")
outputs_debug = model.generate(**inputs_debug, max_length=150, pad_token_id=tokenizer.eos_token_id)
print("\n=== Debugging Suggestion ===")
print(tokenizer.decode(outputs_debug[0], skip_special_tokens=True))

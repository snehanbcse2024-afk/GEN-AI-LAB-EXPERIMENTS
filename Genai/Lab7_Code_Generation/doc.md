# Lab 7: AI-Powered Code Generation & Debugging

## Objective
To generate Python code from docstrings and assist in debugging using Salesforce CodeGen, a code-specific language model.

## Theory
CodeGen is a GPT-based auto-regressive model trained on The Stack dataset (programming code from 6+ languages). It understands code syntax, patterns, and can generate functions from descriptions or suggest fixes for buggy code.

## Code Explanation

### Part 1: Code Generation
1. Loads `Salesforce/codegen-350M-mono` (Python-specific)
2. Provides a function signature with docstring
3. Model generates the complete function body

### Part 2: Debugging Assistance
1. Provides a buggy `calculate_average` function with a known bug
2. Model identifies and suggests the fix

## Dependencies
```
transformers
torch
```

## Expected Output
```
=== Generated Code ===
def calculate_factorial(n):
    """Return the factorial of a given non-negative integer n."""
    if n == 0:
        return 1
    return n * calculate_factorial(n - 1)

=== Debugging Suggestion ===
def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)  # Fixed: use len(numbers) instead of 10
```

## References
- [Salesforce CodeGen](https://huggingface.co/Salesforce/codegen-350M-mono)
- [CodeParrot](https://github.com/huggingface/transformers)

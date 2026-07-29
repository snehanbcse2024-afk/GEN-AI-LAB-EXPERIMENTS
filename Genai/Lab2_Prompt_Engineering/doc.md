# Lab 2: Prompt Engineering Techniques

## Objective
To understand and implement Zero-shot, Few-shot, and Chain-of-Thought prompting techniques for content generation, reasoning, and task automation.

## Theory
Prompt engineering is the practice of designing input prompts to guide language models toward desired outputs without modifying model weights.

### Techniques Covered

| Technique | Description |
|-----------|-------------|
| **Zero-shot** | Prompt the model with only the task instruction, no examples |
| **Few-shot** | Provide a few input-output examples before asking the model to complete a new task |
| **Chain-of-Thought (CoT)** | Encourage the model to reason step-by-step before giving a final answer |

## Code Explanation
1. Loads GPT-2 text generation pipeline
2. Defines three prompts demonstrating each technique:
   - Zero-shot: Direct sentiment classification
   - Few-shot: Provides examples, then asks for classification
   - Chain-of-Thought: Walks through arithmetic step-by-step
3. Generates and prints output for each prompt type

## Dependencies
```
transformers
torch
```

## Expected Output
```
=== Zero-shot ===
<model classifies sentiment directly>

=== Few-shot ===
<model follows the pattern and classifies>

=== Chain-of-Thought ===
<model reasons step-by-step and computes the answer>
```

## References
- [OpenAI — Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903)

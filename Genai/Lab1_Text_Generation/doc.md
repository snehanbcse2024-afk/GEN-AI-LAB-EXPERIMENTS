# Lab 1: Text Generation Using Pre-Trained Foundation Models

## Objective
To generate coherent text using a pre-trained GPT-2 language model from Hugging Face Transformers.

## Theory
Text generation is a core capability of autoregressive language models like GPT-2. These models predict the next token in a sequence given a prompt. By sampling from the probability distribution over tokens, the model can produce varied and creative outputs.

Key parameters controlling generation:
- **temperature** — Controls randomness. Higher = more creative, lower = more deterministic.
- **top_k** — Limits sampling to the top K most probable tokens.
- **top_p** (nucleus sampling) — Samples from the smallest set of tokens whose cumulative probability exceeds p.
- **max_length** — Maximum number of tokens in the generated output.

## Code Explanation
1. Loads the `gpt2` model via Hugging Face's `pipeline` API
2. Sets a random seed for reproducibility
3. Provides a text prompt about Artificial Intelligence
4. Generates 2 text completions with sampling enabled
5. Prints both generated outputs

## Dependencies
```
transformers
torch
```

## Expected Output
```
--- Generated Text 1 ---
Artificial Intelligence will transform the future of <generated continuation>...

--- Generated Text 2 ---
Artificial Intelligence will transform the future of <generated continuation>...
```
> Output varies each run due to sampling.

## References
- [Hugging Face — Text Generation](https://huggingface.co/docs/transformers/main/en/tasks/text_generation)
- [OpenAI — GPT-2](https://openai.com/research/better-language-models)

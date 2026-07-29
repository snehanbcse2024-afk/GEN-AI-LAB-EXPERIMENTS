# Lab 12: Deployment & Evaluation of Generative AI Application

## Objective
To deploy a summarization service via Gradio with a public link and evaluate output quality using ROUGE metrics.

## Theory

### Deployment
Gradio's `share=True` creates a temporary public URL, making the model accessible to anyone without server setup. This is useful for demos, testing, and lightweight production use.

### Evaluation — ROUGE Metrics
ROUGE (Recall-Oriented Understudy for Gisting Evaluation) measures summary quality by comparing generated text against reference summaries:

| Metric | Measures |
|--------|----------|
| **ROUGE-1** | Unigram overlap (word-level recall/precision) |
| **ROUGE-2** | Bigram overlap (phrase-level similarity) |
| **ROUGE-L** | Longest Common Subsequence (structural similarity) |

## Code Explanation
1. Loads BART summarization pipeline
2. Creates a Gradio interface with input textbox and output summary
3. Launches with a public shareable link
4. Computes ROUGE scores between generated and reference summaries
5. Prints evaluation metrics

## Dependencies
```
transformers
gradio
evaluate
torch
```

## Expected Output
```
ROUGE Evaluation Scores: {'rouge1': 0.85, 'rouge2': 0.65, 'rougeL': 0.80, 'rougeLsum': 0.80}
* Running on public URL: https://xxxx.gradio.live
```

## References
- [Gradio Interface](https://www.gradio.app/docs/gradio/interface)
- [ROUGE Metric](https://huggingface.co/docs/evaluate/main/en/transformers_tasks/summarization)
- [Evaluate Library](https://huggingface.co/docs/evaluate)

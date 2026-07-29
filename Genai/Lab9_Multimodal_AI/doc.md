# Lab 9: Multimodal AI — Text & Image Integration

## Objective
To perform image captioning and visual question answering (VQA) using the BLIP model that integrates both text and image inputs.

## Theory
BLIP (Bootstrapping Language-Image Pre-training) is a multimodal model that bridges vision and language. It can:
- **Image Captioning** — Generate a natural language description of an image
- **Conditional Captioning** — Generate text conditioned on a text prefix
- **Visual QA** — Answer questions about an image content

BLIP uses a Vision Transformer (ViT) encoder for images and a language model decoder for text generation.

## Code Explanation
1. Loads BLIP processor and model for image captioning
2. Downloads a sample image from the web
3. **Task 1 — Image Captioning:** Generates an unconditional caption
4. **Task 2 — Conditional Captioning:** Generates text with a given prompt prefix

## Dependencies
```
transformers
torch
Pillow
requests
```

## Expected Output
```
Generated Caption: a photograph of a dog sitting on a bench
Conditional Text Output: a photograph of a dog sitting on a bench in a park
```

## References
- [Salesforce BLIP](https://huggingface.co/Salesforce/blip-image-captioning-base)
- [BLIP Paper](https://arxiv.org/abs/2201.12086)

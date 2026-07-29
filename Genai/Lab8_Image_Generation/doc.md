# Lab 8: Image Generation Using Diffusion Models

## Objective
To generate high-quality images from text prompts using Stable Diffusion, a latent diffusion model.

## Theory
Stable Diffusion is a **latent diffusion model** that works in compressed latent space rather than pixel space:
1. **Text Encoder** (CLIP) — Converts the prompt into a text embedding
2. **U-Net** — Iteratively denoises a random noise tensor conditioned on the text embedding
3. **VAE Decoder** — Converts the final latent representation back to a pixel image

### Key Parameters
- **num_inference_steps** — Number of denoising steps (more = higher quality, slower)
- **guidance_scale** — How closely the image follows the prompt (7-12 typical)
- **negative_prompt** — Describes what to avoid in the output

## Code Explanation
1. Loads `runwayml/stable-diffusion-v1-5` pipeline
2. Moves to GPU if available (CPU is very slow)
3. Defines a creative prompt and negative prompt
4. Generates image with 30 inference steps
5. Saves the output as `futuristic_city.png`

## Dependencies
```
diffusers
torch
transformers
accelerate
```

## Expected Output
- Generates and saves `futuristic_city.png` in the working directory

## References
- [Stable Diffusion](https://huggingface.co/runwayml/stable-diffusion-v1-5)
- [Diffusers Library](https://github.com/huggingface/diffusers)
- [Stability AI](https://stability.ai/)

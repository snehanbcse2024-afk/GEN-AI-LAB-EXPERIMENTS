import torch
from diffusers import StableDiffusionPipeline

# Load pre-trained Stable Diffusion pipeline
model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32)

if torch.cuda.is_available():
    pipe = pipe.to("cuda")

prompt = "A futuristic city skyline at sunset with flying vehicles, digital art style"
negative_prompt = "blurry, low quality, distorted, extra limbs"

image = pipe(
    prompt=prompt,
    negative_prompt=negative_prompt,
    num_inference_steps=30,
    guidance_scale=7.5
).images[0]

image.save("futuristic_city.png")
print("Image generated and saved as 'futuristic_city.png'.")

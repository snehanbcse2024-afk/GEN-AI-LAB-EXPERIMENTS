from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import requests

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Load a sample image
url = "https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg"
image = Image.open(requests.get(url, stream=True).raw)

# 1. Image Captioning
inputs = processor(image, return_tensors="pt")
out = model.generate(**inputs)
caption = processor.decode(out[0], skip_special_tokens=True)
print("Generated Caption:", caption)

# 2. Visual Question Answering (VQA) / Conditional Captioning
text_prompt = "a photography of"
inputs_prompt = processor(image, text_prompt, return_tensors="pt")
out_prompt = model.generate(**inputs_prompt)
print("Conditional Text Output:", processor.decode(out_prompt[0], skip_special_tokens=True))

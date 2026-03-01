import torch
from PIL import Image
from transformers import AutoProcessor, AutoModelForVision2Seq

MODEL_NAME = "Qwen/Qwen2-VL-7B-Instruct"
IMAGE_PATH = "Train_images/2.jpg"
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

processor = AutoProcessor.from_pretrained(MODEL_NAME)
model = AutoModelForVision2Seq.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16,
    device_map="auto"
)
model.eval()

def extract_text_qwen(image_path):
    image = Image.open(image_path).convert("RGB")

    messages = [
        {
            "role": "user",
            "content": [
                {"type": "image", "image": image},
                {
                    "type": "text",
                    "text": (
                        "Read all visible English text in this image. "
                        "Return ONLY the text exactly as it appears. "
                        "Do not explain. Do not paraphrase."
                    )
                }
            ]
        }
    ]

    prompt = processor.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    inputs = processor(
        text=prompt,
        images=image,
        return_tensors="pt"
    ).to(DEVICE)

    with torch.no_grad():
        output_ids = model.generate(
            **inputs,
            max_new_tokens=256,
            do_sample=False
        )

    text = processor.batch_decode(
        output_ids,
        skip_special_tokens=True
    )[0]

    return text.strip()

ocr_text = extract_text_qwen(IMAGE_PATH)
print("QWEN OCR OUTPUT:")
print(ocr_text)

from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

prompt = "Hello, I am"

temps = [0.2, 0.5, 0.7, 1.0, 1.5]

for t in temps:
    print(f"\nTemperature = {t}")
    print(
        generator(
            prompt,
            max_new_tokens=40,
            do_sample=True,
            temperature=t,
            top_k=50,
            top_p=0.9,
            repetition_penalty=1.2,
            clean_up_tokenization_spaces=False,
        )[0]["generated_text"]
    )
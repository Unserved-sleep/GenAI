import time
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

start = time.time()
resp = generator("Hello world!", max_length=50)
elapsed = time.time() - start
print(f"Latency: {elapsed:.2f} sec")

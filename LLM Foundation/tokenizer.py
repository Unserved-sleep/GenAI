from transformers import GPT2Tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
text = "Hello, world!"
tokens = tokenizer.encode(text)
print(tokens)
print(tokenizer.decode(tokens))

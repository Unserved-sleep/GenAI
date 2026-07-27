text = """
Health insurance covers hospitalization, cashless treatment,
and ambulance expenses.

Motor insurance covers accidental damage,
third-party liability, and theft.

Travel insurance protects against trip cancellation
and medical emergencies abroad.
"""

chunk_size = 80
overlap = 20

chunks = []

start = 0

while start < len(text):
    end = start + chunk_size
    chunks.append(text[start:end])
    start += chunk_size - overlap

for i, chunk in enumerate(chunks, start=1):
    print(f"\nChunk {i}")
    print("-" * 40)
    print(chunk)
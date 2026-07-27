text = """
## Health Insurance
Health insurance covers hospitalization.
Cashless treatment is available.
Day-care procedures are covered.

## Motor Insurance
Motor insurance covers accidental damage.
Third-party insurance is mandatory.

## Travel Insurance
Travel insurance covers medical emergencies abroad.
Trip cancellation is included.
"""

# Split by headings
chunks = [chunk.strip() for chunk in text.split("##") if chunk.strip()]

for i, chunk in enumerate(chunks, start=1):
    print(f"\nChunk {i}")
    print("-" * 40)
    print(chunk)
import time
from openai import OpenAI

client = OpenAI(
base_url="http://172.16.180.19:8001/v1",
api_key="sk-no-key-required",
)

start = time.time()
resp = client.chat.completions.create(
model="unsloth/gemma-4-26B-A4B-it-GGUF",
messages=[{"role":"user","content":"hi how are you"}],
)
elapsed = time.time() - start

print(resp.choices[0].message.content)
print(f"\n[Prompt-to-response time for Gemma-4-26B-A4B-it-GGUF: {elapsed:.3f}s]")
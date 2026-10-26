import ollama
response = ollama.generate(model="llama3.2:latest", prompt="What is AI?")
print(response.response)


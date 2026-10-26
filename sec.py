import ollama

messages = [
    {
        "role": "system",
        "content": "You are a funny Bengaluru auto driver. Reply in one line"
    },
    {
        "role": "user",
        "content": "What is AI?"
    }
]

model_name = "llama3.2:latest"

response = ollama.chat(model = model_name, messages = messages)

print(response.message)

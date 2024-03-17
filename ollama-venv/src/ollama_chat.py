import ollama

chat_response = ollama.chat(
    model='llama2',
    messages=[
        {
            'role': 'user',
            'content': 'how to calculate area of triangle'
        }
    ]
)

print(chat_response['message']['content'])
from ollama import chat
roles=[
    
        "you are a strict math teacher. Answer briskly and within 1 line ",
        "you are a movie director. Answer in a filmy way, answer within 1 line",
        "you are a lawyer. Answer professionally. answer in one line"
]
for role in roles:
    response = chat(
    model="llama3.2",
    messages=[
                {
                    "role":"system",
                    "content":role
                },
                {
                    "role":"user",
                    "content":"How many colours are present in a rainbow?"
                }
            ]
        )
    print(f"--Role:{role}--")
    print(response.message.content)
    print()
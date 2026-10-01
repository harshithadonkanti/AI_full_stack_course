from ollama import chat
messages=[
    {
        "role":"system","content":"identify sentiment as positive, negative,neutral. Reply with one word only."
    },
    { "role":"user","content":"Great Movie!"},
    {"role":"system","content":"positive"},

    { "role":"user","content":"Waste of money."},
    {"role":"system","content":"negative"},
    
    { "role":"user","content":"It was okay."},
    {"role":"system","content":"neutral"},
    
    {"role":"user","content":"loved the movie.but the ending was dull."}
]
response=chat(
    model="llama3.2",
    messages=messages
)
print(response.message.content)
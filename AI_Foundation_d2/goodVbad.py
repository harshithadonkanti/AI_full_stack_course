from ollama import chat
bad="Tell me about flowers."
good="tell me about flowers in a poetic way.it must be of five lines."
responseB=chat(
    model="llama3.2",
    messages=[
        {
            "role":"user",
            "content":bad
        }
    ]
)
responseG=chat(
    model="llama3.2",
    messages=[
        {
            "role":"user",
            "content":good
        }
    ]
)
print(f"Bad prompt Result:{responseB.message.content}")
print()
print(f"Good prompt Result:{responseG.message.content}")

from ollama import chat
response=chat(
    model="llama3.2",
    messages=[
        {
            "role":"user",
            "content":"Create a 7-day Python learning schedule. I am a beginner and can study for 1 hour per day.Present the schedule as a numbered list with Day, Topic, and Activity.Include only beginner-level topics."
        }
    ]
)
print(response.message.content)

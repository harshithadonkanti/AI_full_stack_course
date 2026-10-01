from ollama import chat
system_msg="you are a teacher.Answer in english.Answer in one sentence"
history=[
    {"role":"system","content":system_msg }]
question_counter=0
while True:
    question =input("you:")
    if question=="":
        print("DOREAMON 🤖. please type something")
        continue
    if question.lower().strip()=="/history":
        print("---your convertion so far---")
        if len(history)<2:
            print("nothing here so far!")
        for msg in history[1:]:
            if msg["role"]=="user":
                speaker="you"
            else:
                speaker="DOREAMON "
            print(f"{speaker}:{msg['content']}")
        print("----------------------------")
        print()
        continue
    if question.lower().strip()=="/clear":
        history=[{"role":"system","content":system_msg }]
        print("DOREAMON 🤖:History cleared!")
        print()
        continue
    if question.lower().strip()=="/help":
        print("-----Available commands-----")
        print("/history: show the conversation history")
        print("/clear: clear the conversation history")
        print("/help: show available commands")
        print("exit: exit the chat")
        print("----------------------------")
        print()
        continue
    if question.lower().strip()=="exit":
        print("DOREAMON 🤖:GoodBye user.Please come back soon!😒😒")
        print(f"you asked {question_counter} questions in this session.good job!")
        break
    
    history.append({"role":"user","content":question})
    question_counter += 1
    try:
        response=chat(
            model="llama3.2",
            messages= history
        )
        reply=response.message.content
        history.append({"role":"assistant","content":reply})
        print(f"DOREAMON 🤖:{reply}")
        print()
        print("--------------------------------------------------------")
    except Exception as e:
        print("Unknown issue.Is Ollama running?")
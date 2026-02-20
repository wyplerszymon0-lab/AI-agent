from agent import ask_agent
from memory import save_memory

while True:
    q = input("You: ")

    if q.lower() == "exit":
        break

    answer = ask_agent(q)
    print("Agent:", answer)

    save_memory(q, answer)

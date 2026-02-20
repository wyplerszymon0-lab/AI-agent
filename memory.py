def save_memory(question, answer):
    with open("memory.txt", "a", encoding="utf-8") as f:
        f.write(f"Q: {question}\nA: {answer}\n\n")

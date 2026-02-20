from openai import OpenAI

client = OpenAI(api_key="OPEN_API_KEY")

def ask_agent(question):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=question
    )
    return response.output_text

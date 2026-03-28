import openai
def analyze_logs(logs):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": logs}]
    )
    return response['choices'][0]['message']['content']

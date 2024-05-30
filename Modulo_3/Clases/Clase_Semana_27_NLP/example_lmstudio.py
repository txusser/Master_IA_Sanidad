import openai

openai.api_key = "..."

# all client options can be configured just like the `OpenAI` instantiation counterpart
openai.base_url = "http://localhost:1234/v1/"
openai.default_headers = {"x-foo": "true"}

completion = openai.chat.completions.create(
    model="llmware/bling-phi-3-gguf",
    messages=[
        {
            "role": "user",
            "content": "How do I output all files in a directory using Python?",
        },
    ],
)
print(completion.choices[0].message.content)

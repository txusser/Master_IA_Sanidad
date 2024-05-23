from openai import OpenAI
from textwrap import dedent

client = OpenAI(api_key='')

role = '''
Eres un experto procesador de texto que prepara textos para su uso en machine learning y NLP. 
Eres capaz de tokenizar, normalizar, retirar stop words y lematizar un texto nada más verlo. 
No necesitas utilizar código, simplemente lo sabes. 
Recibiras como entrada un texto médico. 
Debes devolverlo completamente procesado entre corchetes y con los lemas separados por comas. 
No debes devolver ningúna otra información o interactuar con el usuario.
'''

content = '''

'''

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": dedent(role)},
        {"role": "user", "content": dedent(content)}
    ]
)

print(completion.choices[0].message)

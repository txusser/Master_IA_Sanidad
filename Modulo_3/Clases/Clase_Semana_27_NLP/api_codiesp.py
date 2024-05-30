import os
from os.path import exists, join
from textwrap import dedent

import openai

openai.base_url = "http://localhost:1234/v1/"
openai.default_headers = {"x-foo": "true"}
openai.api_key = "..."
# client = OpenAI(api_key="sk-proj-8MLXIAqHDaUPSdGjEAFYT3BlbkFJf6Awvsmv9PfOOpGAyDW7")
# assistantID = "asst_KFiIWwwb0xGwOfcTI1mKrOKS"

ROLE = """
Eres un experto procesador de texto que prepara textos para su uso en machine learning y NLP. 
Eres capaz de tokenizar, normalizar, retirar stop words y lematizar un texto nada más verlo. 
No necesitas utilizar código, simplemente lo sabes. 
Recibiras como entrada un texto médico.
Debes devolverlo completamente preprocesado para NLP.
La salida sera una lista de lemas entre corchetes y separados por comas. 
No debes devolver ningúna otra información o interactuar con el usuario. El texto a procesar es el siguiente: 
"""


DIR_FILE = "./final_dataset_v4_to_publish/train/text_files/"
DIR_OUT = "./processed"

if not exists(DIR_OUT):
    os.makedirs(DIR_OUT)


files_to_process = os.listdir(DIR_FILE)

for i in files_to_process[0:2]:
    file_in = join(DIR_FILE, i)

    with open(file_in, "r") as file:
        CONTENT = file.read()

    completion = openai.chat.completions.create(
        model="llmware/bling-phi-3-gguf",
        messages=[
            {
                "role": "user",
                "content": dedent(ROLE) + dedent(CONTENT),
            },
        ],
    )

    proc_ = completion.choices[0].message.content

    print(proc_)

    file_out = join(DIR_OUT, i)
    with open(file_out, "w") as file:
        file.write(proc_)

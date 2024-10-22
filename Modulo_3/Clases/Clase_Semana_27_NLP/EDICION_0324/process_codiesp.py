import os
import subprocess
import cleantext
from os.path import join
from io import StringIO
import pandas as pd

dir_textos = "/Users/jsilva/repositories/Master_IA_Sanidad/Modulo_3/Clases/Clase_Semana_27_NLP/final_dataset_v4_to_publish/dev/text_files"

text_files = os.listdir(dir_textos)

df = pd.DataFrame(columns = ['Archivo', 'Categoría', 'Código CIE-10', 'Descripción'])

for text_file in text_files[0:10]:


    f_path = join(dir_textos, text_file)
    with open(f_path, 'r', encoding='utf8') as f:

        text= f.read()
        texto_limpio = cleantext.clean(
                text,
                extra_spaces=True,
                lowercase=True,
                numbers=True,
                punct=True
                )

        command = f"echo '{text}' | fabric -m llama3.2:latest -p procesar_texto_medico"

        output = subprocess.run(command, shell=True, capture_output=True)
        decoded_output = output.stdout.decode('utf8')

        df_temp = pd.read_csv(StringIO(decoded_output), sep = ';')
        df_temp['Archivo'] = text_file


        df = pd.concat([df, df_temp], ignore_index=True)
out = "/Users/jsilva/repositories/Master_IA_Sanidad/Modulo_3/Clases/Clase_Semana_27_NLP/EDICION_0324/test.csv"
df.to_csv(out, index=False)
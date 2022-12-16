import openai
import sys

# Ejemplo de ejecucion de script
# python3 nombre_del_archivo.py "¿Cuál es la capital de Francia?"
# Puedes probar la version v0.2 que es mas comoda de usar

openai.api_key = "Write_your_API-Key_Here"

# Leer la pregunta de la línea de comandos
prompt = sys.argv[1]

# Hacer una pregunta al modelo
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    temperature=0.5,
)

# Imprimir la respuesta del modelo
print(response["choices"][0]["text"])


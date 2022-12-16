import openai

# Para poder hacer uso de esta herramienta es necesario -
# que agregues la pregunta o busqueda dentro del codigo 
# en el renglon 12 dentro de las comillas.

openai.api_key = "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"

# Hacer una pregunta al modelo
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt="¿Cúal es la capital de Francia?",
    max_tokens=1024,
    temperature=0.5,
)

# Imprimir la respuesta del modelo
print(response["choices"][0]["text"])


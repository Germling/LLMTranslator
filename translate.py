import openai

# Function to chunk source text
def chunk_source_text(file_path, chunk_size):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Chunking the text
    for i in range(0, len(lines), chunk_size):
        yield ''.join(lines[i:i + chunk_size])


# Load the API key
with open("apiKey.txt", "r") as file:
    api_key = file.read().strip()

# Set up OpenAI API key
openai.api_key = api_key

# Load the prompt
with open("prompts.txt", "r") as file:
    prompt = file.read().strip()


# Define a function to translate text
def translate_text(text, prompt):
    try:
        response = openai.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[
                {'role':'system', 'content':'You are a high-quality machine translation engine. Translate the provided text from English into German. '
                                            'The first content will be a prompt. '
                                            'The second content will be a text. '
                                            'Make sure not to add any line breaks that are not in the source text, as this will lead to formatting issues.'},
                {'role': 'user', 'content': prompt},
                {'role': 'user', 'content': text}
            ]
        )
        return response.choices[0].message.content

    except Exception as e:
        print(f"Error translating text: {e}")
        print('\n\n\n')


# Process and translate the source text in chunks
translated_texts = []
for chunk in chunk_source_text("sourcetext.txt", 25):  # Adjust the chunk size as necessary
    translated_text = translate_text(chunk, prompt)
    print(translated_text)
    print('\n')
    if translated_text:
        translated_texts.append(translated_text)

# Write the translated text to the target file
with open("targettext.txt", "w") as file:
    for text in translated_texts:
        file.write(text + "\n")

print("Translation completed and saved to targettext.txt.")
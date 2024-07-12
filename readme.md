
# Text Translation Script

This script reads the contents of `sourcetext.txt` and translates them to German using the OpenAI API.

## Prerequisites

- Python 3.x
- OpenAI API key

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install the required Python packages:**

   ```bash
   pip install openai
   ```

## Setup

1. **Provide your OpenAI API key:**

   - Create a file named `apikey.txt` in the root directory of the repository.
   - Add your OpenAI API key to this file.

2. **Place the source text file:**

   - Ensure that `sourcetext.txt` is present in the root directory of the repository.
   - This file should contain the text you want to translate.

## Usage

To run the script, execute the following command in your terminal:

```bash
python translate.py
```

## Customization

- **Change the target language:**

  To change the target language, modify the system prompt in `translate.py`. For example, to translate to French, you can change the prompt as follows:

  ```python
  system_prompt = "Translate the following text to French:"
  ```

- **Use a different language model:**

  To use a different language model, update the `model` variable in `translate.py`. For example, to use a different model, you can change the model as follows:

  ```python
  model = "text-davinci-003"  # Replace with your desired model
  ```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgements

This project uses the OpenAI API for translation.

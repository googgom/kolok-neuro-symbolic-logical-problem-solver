import os
import requests

DEEPSEEK_API_KEY = "sk-8bac82531d764dcc86b09768d62d33f3"
PROMPT_FILE = "prompt.txt"
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read().strip()

def main():
    system_prompt = read_file(PROMPT_FILE)
    user_message = read_file(INPUT_FILE)

    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}"
    }
    data = {
        "model": "deepseek-coder",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}

        ],
        "temperature": 0.1
    }

    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()

    result = response.json()['choices'][0]['message']['content']
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(result)


if __name__ == "__main__":
    main()
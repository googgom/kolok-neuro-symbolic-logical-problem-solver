import sys

def formalize(text: str) -> str:
    # Здесь можно использовать LLM API, но для примера — простая логика
    if "Сократ" in text and "человек" in text and "смертен" in text:
        return "Человек(Сократ), ¬Человек(x) ∨ Смертен(x), ¬Смертен(Сократ)"
    else:
        return "Человек(Сократ), ¬Человек(x) ∨ Смертен(x)"

if __name__ == "__main__":
    user_input = sys.stdin.read().strip()
    result = formalize(user_input)
    print(result)

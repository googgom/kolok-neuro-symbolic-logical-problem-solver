import subprocess
import sys
import os

def run_module(module_dir: str, input_data: str) -> str:
    """
    Запускает main.py из указанного каталога и передаёт input_data на stdin.
    Возвращает stdout.
    """
    module_path = os.path.join(module_dir, "main.py")
    result = subprocess.run(
        [sys.executable, module_path],
        input=input_data,
        text=True,
        capture_output=True,
        encoding='utf-8',
    )
    if result.returncode != 0:
        print(f"Ошибка в модуле {module_dir}: {result.stderr}", file=sys.stderr)
        sys.exit(1)
    return result.stdout.strip()

def main():
    # Проверяем наличие файла input.txt
    input_file = "input.txt"
    if not os.path.exists(input_file):
        print(f"Ошибка: файл '{input_file}' не найден в корневой директории.", file=sys.stderr)
        sys.exit(1)

    # Считываем текст задачи из файла
    with open(input_file, "r", encoding="utf-8") as f:
        user_input = f.read().strip()

    if not user_input:
        print("Ошибка: файл 'input.txt' пуст.", file=sys.stderr)
        sys.exit(1)

    print(f"[DEBUG] Входные данные: {user_input}")

    # 1. Перевод с русского на логику
    logic_formulas = run_module("1-rus-to-log", user_input)
    print(f"[DEBUG] Вывод 1-го модуля: {logic_formulas}")

    # 2. Движок резолюций
    proof_log = run_module("2-strict-resolution-engine", logic_formulas)
    print(f"[DEBUG] Вывод 2-го модуля: {proof_log}")

    # 3. Перевод логики на русский
    explanation = run_module("3-log-to-rus", proof_log)
    print(f"[DEBUG] Вывод 3-го модуля: {explanation}")

    # Финальный вывод
    print("\n--- Результат ---")
    print(explanation)

if __name__ == "__main__":
    main()

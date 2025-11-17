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
    )
    if result.returncode != 0:
        print(f"Ошибка в модуле {module_dir}: {result.stderr}", file=sys.stderr)
        sys.exit(1)
    return result.stdout.strip()

def main():
    # Пример: текст задачи можно передавать как аргумент или читать из stdin
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
    else:
        print("Введите текст задачи (например, 'Сократ — человек. Все люди смертны. Докажи, что Сократ смертен.'):")
        user_input = sys.stdin.read().strip()

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

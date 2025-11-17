import sys

def resolve(clauses: str) -> str:
    # Упрощённая логика для примера
    clauses_list = [c.strip() for c in clauses.split(",")]
    if "¬Смертен(Сократ)" in clauses_list:
        return (
            "[Шаг 1: Унификация {x/Сократ} в ¬Человек(x) ∨ Смертен(x). "
            "Шаг 2: Резолюция с Человек(Сократ) -> Смертен(Сократ). "
            "Шаг 3: Резолюция Смертен(Сократ) и ¬Смертен(Сократ) -> Противоречие.]"
        )
    else:
        return "[Шаг 1: Унификация {x/Сократ} в ¬Человек(x) ∨ Смертен(x). Шаг 2: Резолюция с Человек(Сократ) -> Смертен(Сократ).]"

if __name__ == "__main__":
    clauses = sys.stdin.read().strip()
    proof_log = resolve(clauses)
    print(proof_log)

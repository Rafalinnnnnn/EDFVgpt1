import json
from typing import List

def load_query_synonyms() -> List[str]:
    try:
        with open("query_synonyms.json", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list) and all(isinstance(x, str) for x in data):
                return data
            else:
                raise ValueError("Formato inesperado")
    except Exception as e:
        # Si falla, uso una lista por defecto muy básica
        print(f"[WARN] No se pudo cargar query_synonyms.json: {e}")
        return [
            "instaladores de ascensores",
            "distribuidores de ascensores",
            "elevator distributors",
            "lift suppliers"
        ]

QUERY_SYNONYMS = load_query_synonyms()

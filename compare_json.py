import json
import os

# Пути к JSON-файлам
ts_file_path = "integration_TS.json"
xml_file_path = "integration_XML.json"

# Читаем JSON-файлы
with open(ts_file_path, "r", encoding="utf-8") as ts_file:
    ts_data = json.load(ts_file)

with open(xml_file_path, "r", encoding="utf-8") as xml_file:
    xml_data = json.load(xml_file)

# Преобразуем XML JSON в словарь для быстрого поиска по type
xml_dict = {entry["type"]: entry for entry in xml_data}

# Список для хранения логов
log_results = []

for ts_entry in ts_data:
    ts_type = ts_entry["type"]

    if ts_type not in xml_dict:
        log_results.append(f"Type '{ts_type}' not found in XML JSON.")
    else:
        xml_entry = xml_dict[ts_type]
        changes = []

        # Проверка изменённых ключей
        for key in ts_entry.keys():
            if key in xml_entry and ts_entry[key] != xml_entry[key]:
                changes.append(f"{key}: '{xml_entry[key]}' -> '{ts_entry[key]}'")

        # Проверка удалённых ключей (которые есть в XML, но отсутствуют в TS)
        missing_keys = [key for key in xml_entry.keys() if key not in ts_entry]
        if missing_keys:
            changes.append(f"Missing keys in TS: {', '.join(missing_keys)}")

        # Проверка новых ключей (которые есть в TS, но отсутствуют в XML)
        new_keys = [key for key in ts_entry.keys() if key not in xml_entry]
        if new_keys:
            changes.append(f"New keys in TS: {', '.join(new_keys)}")

        if not changes:
            log_results.append(f"Type '{ts_type}': OK")
        else:
            log_results.append(f"Type '{ts_type}': Changes found - {', '.join(changes)}")


# Добавляем порядок блоков в лог
log_results.append("\n=== Order of Blocks in file_TS.json ===")
log_results.append(" -> ".join([entry["type"] for entry in ts_data]))

log_results.append("\n=== Order of Blocks in file_XML.json ===")
log_results.append(" -> ".join([entry["type"] for entry in xml_data]))

# Проверяем, существует ли папка 'compare', если нет — создаём её
os.makedirs("compare", exist_ok=True)

# Записываем результаты в файл
with open("compare/log.txt", "w", encoding="utf-8") as log_file:
    log_file.write("\n".join(log_results))

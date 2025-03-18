import json

# Загружаем исходный geojson файл
# with open('initial_data/ufa_districts.geojson', 'r', encoding='utf-8') as f:
#     export_data = json.load(f)

with open('initial_data/parts_ufa.geojson', 'r', encoding='utf-8') as f:
    export_data = json.load(f)

# Создаем новый словарь для преобразованного файла
bashkortostan_regions = {
    "type": "FeatureCollection",
    "features": []
}
region_names = set()
# Проходим по каждому элементу в export.geojson
for feature in export_data['features']:
    # Попытка получить 'name' из основной части данных
    region_name = feature['properties'].get('name', None)

    # Если 'name' нет в основной части, пытаемся получить его из вложенных relations
    if not region_name:
        relations = feature['properties'].get('@relations', [])
        if relations:
            # Берем первый элемент из списка @relations, где скорее всего и содержится нужное имя
            relation = relations[0]
            region_name = relation['reltags'].get('name', None)

    # Если все равно не нашли 'name', то ставим значение по умолчанию
    if not region_name:
        region_name = "Unknown Region"

    # Выводим на экран регион (name) для каждой итерации
    region_names.add(region_name)

    geometry = feature['geometry']  # Получаем геометрию (LineString или другой тип)

    # Создаем новый feature для bashkortostan_regions
    new_feature = {
        "type": "Feature",
        "properties": {
            "region_name": region_name  # Используем название региона на английском
        },
        "geometry": geometry  # Сохраняем геометрию без изменений
    }

    # Добавляем новый feature в список
    bashkortostan_regions['features'].append(new_feature)

# Записываем результат в новый JSON файл
# with open('operational_data/ufa_district.json.json', 'w', encoding='utf-8') as f:
#     json.dump(bashkortostan_regions, f, ensure_ascii=False, indent=4)

with open('operational_data/parts_ufa.json', 'w', encoding='utf-8') as f:
    json.dump(bashkortostan_regions, f, ensure_ascii=False, indent=4)


print("Преобразование завершено успешно.")
print(sorted(region_names))

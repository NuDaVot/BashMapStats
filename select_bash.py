import json
from pprint import pprint


def extract_bashkortostan(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Фильтруем только объекты, относящиеся к Башкортостану
    bashkortostan_features = []
    region_names = set()

    for feature in data["features"]:
        if feature["properties"].get("NAME_1") == "Bashkortostan":
            region_name = feature["properties"].get("NL_NAME_2", "Unknown")
            region_names.add(region_name)
            bashkortostan_features.append({
                "type": "Feature",
                "properties": {"region_name": region_name},
                "geometry": feature["geometry"]
            })

    output_data = {
        "type": "FeatureCollection",
        "features": bashkortostan_features
    }

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=4)

    print(f"Данные сохранены в {output_file}\n")
    print("Список всех NL_NAME_2 в Башкортостане:")
    pprint(sorted(region_names))


# Использование
extract_bashkortostan("gadm41_RUS_3.json", "bashkortostan.json")
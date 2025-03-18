import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import random

# Шаг 1. Создание тестовых данных для всех регионов
# regions = [
#     "Уфа", "Стерлитамак", "Салават", "Нефтекамск", "Октябрьский", "Белорецк", "Мелеуз", "Туймазы", "Бирск",
#     "Абзелиловский район", "Альшеевский район", "Архангельский район", "Аскинский район", "Аургазинский район",
#     "Бакалинский район", "Балтачевский район", "Баймак", "Баймакский район", "Белебеевский район", "Белебей",
#     "Белокатайский район", "Белорецкий район", "Бирский район", "Бижбулякский район", "Благоварский район",
#     "Благовещенск", "Благовещенский район", "Бураевский район", "Бурзянский район", "Буздякский район",
#     "Чекмагушевский район", "Чишминский район", "Давлеканово", "Давлекановский район", "Дуванский район",
#     "Дюртюли", "Дюртюлинский район", "Федоровский район", "Гафурийский район", "Иглинский район",
#     "Илишевский район", "Ишимбай", "Ишимбайский район", "Калтасинский район", "Караидельский район",
#     "Кармаскалинский район", "Хайбуллинский район", "Кигинский район", "Краснокамский район",
#     "Кугарчинский район", "Кумертау", "Кушнаренковский район", "Куюргазинский район", "Мечетлинский район",
#     "Мелеузовский район", "Мишкинский район", "Миякинский район", "Нуримановский район", "Салаватский район",
#     "Шаранский район", "Сибай", "Стерлибашевский район", "Стерлитамакский район", "Татышлинский район",
#     "Туймазинский район", "Учалинский район", "Уфимский район", "Янаул", "Янаульский район", "Ермекеевский район",
#     "Зианчуринский район", "Зилаирский район"
# ]

regions = ['"Урал" Восточный подъезд к Уфе', 'Unknown Region', 'Авдон', 'Авдонский сельсовет', 'Алексеевка',
           'Алексеевский сельсовет', 'Белая', 'Берсианка', 'Булгаково', 'Булгаковский сельсовет',
           'Городской округ Уфа', 'Дмитриевка', 'Дмитриевский сельсовет', 'Дёма', 'Ерик', 'Жуково',
           'Жуковский сельсовет', 'Зубово', 'Зубовский сельсовет', 'Кармасан', 'Кармасанский сельсовет',
           'Каряка', 'Кириллово', 'Кирилловский сельсовет', 'Красноярский сельсовет', 'Красный Яр', 'Миловка',
           'Миловский сельсовет', 'Михайловка', 'Михайловский сельсовет', 'Николаевка', 'Николаевский сельсовет',
           'Ольховое', 'Ольховский сельсовет', 'Русский Юрмаш', 'Русско-Юрмашский сельсовет', 'СУ-820', 'Сартовка',
           'Сикиязка', 'Таптыково', 'Таптыковский сельсовет', 'Таушка', 'Уршак', 'Уфа', 'Черкасский сельсовет',
           'Черкассы', 'Чесноковка', 'Чесноковский сельсовет', 'Шакша', 'Шемяк', 'Шемякский сельсовет',
           'Юматовский сельсовет', 'Юрмаш', 'санатория Юматово имени 15-летия БАССР']

# Генерация случайного количества записей для каждого региона
data = {"region": regions, "count": [random.randint(10, 200) for _ in regions]}
df = pd.DataFrame(data)

# Шаг 2. Загрузка GeoJSON с регионами Башкортостана
# geo_path = "bashkortostan.json"
geo_path = "ufa_district.json"
geo_df = gpd.read_file(geo_path)

# Шаг 3. Объединение данных по полю "region_name" из GeoJSON и "region" из df
merged = geo_df.merge(df, left_on="region_name", right_on="region", how="left")

# Шаг 4. Построение карты
fig, ax = plt.subplots(1, figsize=(12, 10))
merged.plot(column="count",
            ax=ax,
            cmap="OrRd",           # цветовая схема
            edgecolor="black",
            legend=True,
            legend_kwds={"label": "Количество записей", "orientation": "horizontal"},
            missing_kwds={"color": "lightgrey", "edgecolor": "red", "label": "Нет данных"})

# # Шаг 5. Добавление подписей для каждого региона (Polygon или MultiPolygon)
# for idx, row in merged.iterrows():
#     geom = row["geometry"]
#     if geom and geom.geom_type in ["Polygon", "MultiPolygon"]:
#         centroid = geom.centroid
#         ax.text(centroid.x, centroid.y, row["region_name"], fontsize=8, ha='center', va='center',
#                 color="black", weight='bold')

ax.set_title("Социальная активность жителей регионов", fontsize=16)
ax.axis("off")
plt.show()
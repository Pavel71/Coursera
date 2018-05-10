import numpy as np
import pandas as pd
avg_ocean_depth = pd.Series({
                            'Arctic': 1205,
                            'Atlantic': 3646,
                            'Indian': 3741,
                            'Pacific': 4080,
                            'Southern': 3270})


max_ocean_depth = pd.Series({
'Arctic': 5567,
'Atlantic': 8486,
'Indian': 7906,
'Pacific': 10803,
'Southern': 7075
})



ocean_depths = pd.DataFrame({
                            'Avg. Depth (m)': avg_ocean_depth,
                            'Max. Depth (m)': max_ocean_depth})

print(ocean_depths)

print("\n--------------------Сортировака-----------------------\n")

print(ocean_depths.sort_values('Avg. Depth (m)', ascending = True))

#count 	Подсчёт частоты того или иного события (сколько раз произошло событие?).
# mean 	Среднее значение.
# std 	Стандартное отклонение (числовое значение, которое отображает изменение пределов данных).
# min 	Наименьшее число в наборе данных.
# 25% 	25-й процентиль.
# 50% 	50-й процентиль.
# 75% 	75-й процентиль.
# max 	Максимальное число в наборе данных.

print("\n--------------------Статистика!------------------------\n")

print(ocean_depths.describe())


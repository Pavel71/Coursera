import pandas as pd
import numpy as np
import seaborn as sns
import re
from collections import Counter
import modulre as m



data = pd.read_csv("C:\projects\Python/data/titanic.csv", index_col = 'PassengerId')

# Survaivorssort = data['Survived'].sort_values;
#
# print(data.dtypes)
#
# print(data[:10])
#
#
# #Отбираем количество пассажиров по классам
# Class_count = data['Pclass'].value_counts()
#
# #Отбираем количество пассажиров по полу
# Sex_pasangear = data['Sex'].value_counts()
#
# #Отбираем количество пассажиров по выжившым
# Survaivor_count = data['Survived'].value_counts()
#
# #Создаем Data с возрастом
# Age_count = data['Age'].value_counts()
#
# Age_data = data[['Age']].copy()
#
# #Средни возраст
# X = np.mean(data['Age'])
#
# #Медиана возраста
#
# X = data['Age'].median()
# print("Median ", X)
#
# #Корреляия по родственникам
#
# SibSp = data['SibSp'].value_counts()
# Parch = data['Parch'].value_counts()
#
# SibSp_Parch = data[['SibSp', 'Parch']]
#
# # Correlation
# X = SibSp_Parch.corr()
#
# # print(X)
#
#
#
# #Выбрать самое популярное женское имя
#
# Famel_Name = data.groupby(['Name', 'Sex'])
#
# #CrossTab
#
# print(pd.crosstab(data['Survived'], data['Pclass'], margins=True))
#
# print(sns.countplot(x = 'Pclass', hue = 'Survived', data= data))

# pattern = re.compile('(?:Mrs.|Miss.) *(\w* .*)')

i ='Honkanen, Miss. Eliina, Bazzani, Miss. Albina'

array = ['Cumings, Mrs. John Bradley (Florence Briggs Thayer)',
       'Heikkinen, Miss. Laina',
       'Futrelle, Mrs. Jacques Heath (Lily May Peel)']

list_clear=[]

for s in array:

    list_clear.append(s.replace('Mrs.', '').replace('(', '').replace(')', '').replace('Miss.', '')\
                                       .replace('"', '').replace(',', '').split())

print(list_clear)


List2 = np.concatenate(list_clear)
print(List2)





#Отбираем количество пассажиров по выжившым
# Survaivor_count = data['Survived'].value_counts()
#
#
# Name = data['Name'].values
#
# List_Found_Name = m.get_List_Found_Text(Name)
#
# print(List_Found_Name)

#
# pattern = re.compile('(?:\(|Miss.) *(\w*)')
#
#
#
#
# Found_Name = []
#
# for element in Name:
#
#     found = pattern.findall(element)
#
#     if found:
#
#      for element2 in found:
#
#          Found_Name.append(element2)
#
# print(Counter(Found_Name))






















# string = 'This Mrs.filly a simple Mrs.  test message Miss. for test'
# found = re.findall(pattern, string)
#
# if found:
#
#     print(found)
#
# else:
#
#     print("Not found")







# Name = data.as_matrix(['Name'])
#
# Pattern = r"Mrs.|Miss."
#
#
# def Regular_Pattern(String):
#
#     name_found = re.findall('Mary', String)
#
#
# for j in Name:
#
#     Regular_Pattern(j)













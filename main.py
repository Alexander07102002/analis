import pandas as pd

# Создаем DataFrame из списка
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

# Создаем столбцы one-hot
data['is_robot'] = data['whoAmI'].map({'robot': 1, 'human': 0})
data['is_human'] = data['whoAmI'].map({'robot': 0, 'human': 1})

# Удаляем исходный столбец
data.drop('whoAmI', axis=1, inplace=True)

# Выводим результат
print(data.head())
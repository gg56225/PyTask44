import pandas as pd
import random

# Генерация данных
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Преобразование в one-hot вид
data['whoAmI_code'] = pd.factorize(data['whoAmI'])[0]
one_hot = pd.DataFrame({f'whoAmI_{i}': (data['whoAmI_code'] == i).astype(int) for i in range(data['whoAmI_code'].nunique())})

# Объединение с исходным DataFrame
data = data.join(one_hot)
data = data.drop('whoAmI_code', axis=1)

print(data.head())

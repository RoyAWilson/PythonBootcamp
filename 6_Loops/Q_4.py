# Amend Q_3 so that it just prints out all times tables.

for t_table in range(1, 13):
    print(f'\nThis is the {t_table} times table\n')
    for result in range(1, 13):
        print(f'{t_table} x {result} = {t_table * result}')
print('Done')

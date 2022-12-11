geusts = ['Сильвестр Сталонне', "Роберт Дауни Младший", "Дженифер Энистон"]
# print(f'Дорогой {geusts[0].title()}, приглашаю вас на праздничный обед')
# print(f'Дорогой {geusts[1].title()}, приглашаю вас на праздничный обед')
# print(f'Дорогая {geusts[2].title()}, приглашаю вас на праздничный обед')
print(geusts[0])
geusts[0] = 'Арнольд Шварцнеггер'
print(geusts)

print(f'Дорогой {geusts[0].title()}, приглашаю вас на праздничный обед')
print(f'Дорогой {geusts[1].title()}, приглашаю вас на праздничный обед')
print(f'Дорогая {geusts[2].title()}, приглашаю вас на праздничный обед')

geusts.insert(0, 'Генри Кевилл')
geusts.insert(2,'Маршал Метерс')
geusts.append('Дженифер Лоуренс')
print(geusts)

# print(f'Дорогой {geusts[0].title()}, приглашаю вас на праздничный обед')
# print(f'Дорогой {geusts[1].title()}, приглашаю вас на праздничный обед')
# print(f'Дорогой {geusts[2].title()}, приглашаю вас на праздничный обед')
# print(f'Дорогой {geusts[3].title()}, приглашаю вас на праздничный обед')
# print(f'Дорогая {geusts[4].title()}, приглашаю вас на праздничный обед')
# print(f'Дорогая {geusts[5].title()}, приглашаю вас на праздничный обед')
print('К сожалению на обеде смогут присутствовать только два гостя')
print(geusts)
arni = geusts.pop(1)
print(geusts)
print(f'Дорогой {arni}, мне очень жаль что вы не сможете присутствовать на обеде')
robert = geusts.pop(2)
print(geusts)
print(f'Дорогой {robert}, мне очень жаль что вы не сможете присутствовать на обеде')
eminem = geusts.pop(1)
print(geusts)
print(f'Дорогой {eminem}, мне очень жаль что вы не сможете присутствовать на обеде')
jen = geusts.pop(1)
print(geusts)
print(f'Дорогая {jen}, мне очень жаль что вы не сможете присутствовать на обеде')

print(geusts)
print(f'Уважаемые {geusts[0].title()} и {geusts[1]},для вас приглашение на обед остается в силе')
del geusts[0]
print(geusts)
del geusts[0]
print(geusts)

heroes = ['spider-man', 'captain america', 'Doctor Strange', 'Iron Man', 'Logan', 'Hulk']
print(heroes)
print(heroes[4].title())
heroes[0] = 'Thor'
print(heroes)
heroes.append('Hawkeye')
print(heroes)
heroes.insert(0, 'spider-man')
print(heroes)
del heroes[7]
print(heroes)
poped_heroes = heroes.pop(5)
print(heroes)
print(poped_heroes)
heroes.remove('Thor')
print(heroes)
print(sorted(heroes))
print(sorted(heroes, reverse=True))
print(heroes)
heroes.reverse()
print(heroes)
heroes.sort()
print(heroes)
heroes.sort(reverse=True)
print(heroes)
#8.1
e2f = {'dog':'chien', 'cat':'chat', 'walrus':'morse'} #walrus 바다코끼리
print(e2f)

#8.2
e2f = {'dog':'chien', 'cat':'chat', 'walrus':'morse'}
print(e2f['walrus'])

#8.3
e2f = {'dog':'chien', 'cat':'chat', 'walrus':'morse'}
f2e={value:key for key, value in e2f.items()}
print(f2e)

#8.4
e2f = {'dog':'chien', 'cat':'chat', 'walrus':'morse'}
f2e={value:key for key, value in e2f.items()}
print(f2e['chien'])

#8.5
e2f = {'dog':'chien', 'cat':'chat', 'walrus':'morse'}
for english_words in e2f.keys():
    print(english_words)
#8.5 another method(list)
english_words = list(e2f.keys())
print(english_words)

#8.6
life = {'animals':{'cats':'Henri', 'octopi':'Grumpy', 'emus':'Lucy'}, 'plants' : {}, 'other' : {} }
empty_dict = {}
print(life)

#8.7
life = list(life.keys())
print(life)

#8.8***
life_animals_keys = list(life['animals'].keys())
print(life_animals_keys)

#8.9

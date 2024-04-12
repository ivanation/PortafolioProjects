from instagrapi import Client

cl = Client()
cl.login('xxxx', 'xxxx')

# usuario target
id = cl.user_id_from_username('dinglish.academy')
#id = cl.user_id
print(f'usuario: {id}')

# recojo los seguidos
following = cl.user_following(id)
print(f'siguiendo: {len(following)}')

# recojo los seguidores
followers = cl.user_followers(id)
print(f'seguidores: {len(followers)}')


# imprimo los que me siguen
# print(following[user_id].username)
culpables = []
for user_id in following.keys():
    if user_id not in followers.keys():
        culpables.append(following[user_id].username)

print(f'culpables: {len(culpables)}')

# salvo en un texto
with open("file.txt", "w") as output:
    output.write(str(culpables))

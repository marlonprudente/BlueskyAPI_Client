from atproto import Client, client_utils


def getSegue(client, profile):
    lista = []
    seguindo = client.get_follows(profile.did, limit=100)

    while True:
        for i in seguindo.follows:
            lista.append(i)

        if(seguindo.cursor == None):
            break
        seguindo = client.get_follows(profile.did, cursor=seguindo.cursor, limit=100)


    print('Quantidade Seguindo: ' + str(len(lista)))
    return lista

def getSeguidores(client, profile):
    lista = []
    seguidores = client.get_followers(profile.did, limit=100)

    while True:
        for i in seguidores.followers:
            lista.append(i)

        if(seguidores.cursor == None):
            break
        seguidores = client.get_followers(profile.did, cursor=seguidores.cursor, limit=100)


    print('Quantidade Seguidores: ' + str(len(lista)))
    return lista


if __name__ == '__main__':
    client = Client()
    profile = client.login('login', 'password')
    seguindo = getSegue(client=client, profile=profile)
    seguidores = getSeguidores(client=client, profile=profile)

    print('Seguidores: ' + str(profile.followers_count))
    print('Seguindo: ' + str(profile.follows_count))

    for i in seguidores:
        client.follow(i.did)

    for i in seguindo:
        if i not in seguidores:
            print(i.handle)
            client.delete_follow(client.follow(i.did).uri)





def make_album(artist_name, album_title, tracks = ''):
    """builds a dictionary describing a music album"""
    if tracks:
        album = {'artist': artist_name, 'album': album_title,
                 'tracks': tracks}        
    else:    
        album = {'artist': artist_name, 'album': album_title}
    return album

    
while True:
    print("Tell me your favorite artist and album name.")
    print("enter 'q' to quit at any time.")
        
    art_name = input("whats the artists name?")
    if art_name == 'q':
        break
        
    alb_name = input("what's the album name?")
    if alb_name == 'q':
        break
                         

tragic_kingdom = make_album('no doubt', 'tragic kingdom', 13)
print(tragic_kingdom)

album_1 = make_album('nine inch nails', 'hurt')
print(album_1)

album_2 = make_album('ariana grande', 'breathe')
print(album_2)

my_album = make_album(art_name, alb_name)
print(my_album)

print("Thanks for playing!")
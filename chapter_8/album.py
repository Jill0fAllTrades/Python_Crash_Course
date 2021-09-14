def make_album(artist_name, album_title, tracks = ''):
    """builds a dictionary describing a music album"""
    if tracks:
        album = {'artist': artist_name, 'album': album_title,
                 'tracks': tracks}        
    else:    
        album = {'artist': artist_name, 'album': album_title}
    return album

tragic_kingdom = make_album('no doubt', 'tragic kingdom', 13)
print(tragic_kingdom)

album_1 = make_album('nine inch nails', 'hurt')
print(album_1)

album_2 = make_album('ariana grande', 'breathe')
print(album_2)

    

#TODO add that value to albums dictionary
#TODO make one new function call that includes # of tracks on the album    
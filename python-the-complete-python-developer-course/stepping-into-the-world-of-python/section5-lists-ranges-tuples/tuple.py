imelda = "More Mayhem", "Emilda May", 2011, ([(
    1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")])

print(imelda)

imelda[3].append((5, "All For You"))

title, artist, year, tracks = imelda
print(title)
tracks.append((5, "Eternity"))
print(artist)
for song in tracks:
    tracks, title = song
    print("\t Track number {}, Title: {}".format(tracks, title))

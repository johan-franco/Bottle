f = open('storyboard.txt', 'r')
raw_data = f.read()
f.close()

raw_places = raw_data.split('+++')

places = []
for raw_place in raw_places:
    place = raw_place.split('***')
    places.append((place[0].strip(), place[1].strip(), place[2].strip(),
                 eval(place[3].strip())))


#print(places)

f1 = open('locations.sql', 'w')
f2 = open('paths.sql', 'w')

for place in places:
    s = 'INSERT INTO Location VALUES ({0}, "{1}", "{2}");\n'
    f1.write(s.format(place[0], place[1], place[2]))

    for key in place[3]:
        s2 = 'INSERT INTO Path VALUES ({0}, "{1}", {2});\n'
        f2.write(s2.format(place[0], key, place[3][key]))

import  geohash_hilbert as ghh
import  mmh3, statistics
from    haversine import haversine, Unit

from washington import points
from places     import pl_points

_BASE64 = (
    '0123456789'  # noqa: E262    #   10    0x30 - 0x39
    '@'                           # +  1    0x40
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # + 26    0x41 - 0x5A
    '_'                           # +  1    0x5F
    'abcdefghijklmnopqrstuvwxyz'  # + 26    0x61 - 0x7A
)                                 # = 64    0x30 - 0x7A
_BASE64_MAP = {c: i for i, c in enumerate(_BASE64)}

def decode_int64(t):
    code = 0
    for ch in t:
        code <<= 6
        code += _BASE64_MAP[ch]
    return code


def analyzeGeoHash(g):
    rect        = ghh.rectangle(g)
    neigh       = ghh.neighbours(g)
    rectNW      = rect['geometry']['coordinates'][0][0]
    rectNE      = rect['geometry']['coordinates'][0][1]
    rectSE      = rect['geometry']['coordinates'][0][2]
    rectSW      = rect['geometry']['coordinates'][0][3]
    rectCT      = (rect['properties']['lat'],rect['properties']['lng'])
    answer      = (haversine(rectNW, rectNE, unit=Unit.MILES), haversine(rectNE, rectSE, unit=Unit.MILES), Unit.MILES, rectCT, decode_int64(g), neigh)
    if answer[0] < 0.8:
        answer      = (haversine(rectNW, rectNE, unit=Unit.METERS), haversine(rectNE, rectSE, unit=Unit.METERS), Unit.METERS, rectCT, decode_int64(g), neigh)


    return answer



print(f'CPYTHON? {ghh._hilbert.CYTHON_AVAILABLE} {ghh.rectangle("Z7fe2G")} {ghh.neighbours("Z7fe2G")}')
print(f'{ghh.rectangle("Z7fe2")}')
# print(f'{points}')

# https://geojson.io/#map=18/38.96381/-77.34241
home = (38.96381, -77.34241, '11500 Fairway Dr')

features = [(ghh.encode(f['geometry']['coordinates'][0], f['geometry']['coordinates'][1]), f['geometry']['coordinates'][1],f['geometry']['coordinates'][0],f['properties']['name'],f['properties']['address'] ) for f in points['features']]
print(f'{features}')
places = {}
for (ghhcode, lat, lng, name, address) in features:
    rect    = ghh.rectangle(ghhcode)
    fID     = mmh3.hash(name+f'{lat}:{lng}', signed=False)
    int64   = decode_int64(ghhcode)
    # print(f'{fID:012d} <{name:40s}>  {ghhcode[:-4]} {ghhcode} {int64:,d}')
    places[fID] = (ghhcode[:-5], ghhcode, int64, f'{int64:064b}', lat, lng, name, address)

mycoord = (statistics.mean([v[4] for k,v in places.items()]), statistics.mean([v[5] for k,v in places.items()]))
myghh   = ghh.encode(mycoord[1],mycoord[0])
myID    = decode_int64(myghh)


features.extend([(ghh.encode(f['geometry']['coordinates'][0], f['geometry']['coordinates'][1]), f['geometry']['coordinates'][1],f['geometry']['coordinates'][0],f['properties']['name'],f['properties']['name'] ) for f in pl_points['features']])

places = {}
for (ghhcode, lat, lng, name, address) in features:
    rect    = ghh.rectangle(ghhcode)
    fID     = mmh3.hash(name+f'{lat}:{lng}', signed=False)
    int64   = decode_int64(ghhcode)
    print(f'{fID:012d} <{name:60s}>  {ghhcode[:-4]} {ghhcode} {int64:,d}')
    places[fID] = (ghhcode[:-5], ghhcode, int64, f'{int64:064b}', lat, lng, name, address)

# lvl | bits |   error       |    base4   |  base16  |  base64
# -------------------------------------------------------------
#   0 |   0  |  20015.087 km |   prec  0  |  prec 0  |  prec 0
#   1 |   2  |  10007.543 km |   prec  1  |          |
#   2 |   4  |   5003.772 km |   prec  2  |  prec 1  |
#   3 |   6  |   2501.886 km |   prec  3  |          |  prec 1
#   4 |   8  |   1250.943 km |   prec  4  |  prec 2  |
#   5 |  10  |    625.471 km |   prec  5  |          |
#   6 |  12  |    312.736 km |   prec  6  |  prec 3  |  prec 2
#   7 |  14  |    156.368 km |   prec  7  |          |
#   8 |  16  |     78.184 km |   prec  8  |  prec 4  |
#   9 |  18  |     39.092 km |   prec  9  |          |  prec 3
#  10 |  20  |     19.546 km |   prec 10  |  prec 5  |
#  11 |  22  |   9772.992  m |   prec 11  |          |
#  12 |  24  |   4886.496  m |   prec 12  |  prec  6 |  prec 4
#  13 |  26  |   2443.248  m |   prec 13  |          |
#  14 |  28  |   1221.624  m |   prec 14  |  prec  7 |
#  15 |  30  |    610.812  m |   prec 15  |          |  prec 5
#  16 |  32  |    305.406  m |   prec 16  |  prec  8 |
#  17 |  34  |    152.703  m |   prec 17  |          |
#  18 |  36  |     76.351  m |   prec 18  |  prec  9 |  prec 6
#  19 |  38  |     38.176  m |   prec 19  |          |
#  20 |  40  |     19.088  m |   prec 20  |  prec 10 |
#  21 |  42  |    954.394 cm |   prec 21  |          |  prec 7
#  22 |  44  |    477.197 cm |   prec 22  |  prec 11 |
#  23 |  46  |    238.598 cm |   prec 23  |          |
#  24 |  48  |    119.299 cm |   prec 24  |  prec 12 |  prec 8
#  25 |  50  |     59.650 cm |   prec 25  |          |
#  26 |  52  |     29.825 cm |   prec 26  |  prec 13 |
#  27 |  54  |     14.912 cm |   prec 27  |          |  prec 9
#  28 |  56  |      7.456 cm |   prec 28  |  prec 14 |
#  29 |  58  |      3.728 cm |   prec 29  |          |
#  30 |  60  |      1.864 cm |   prec 30  |  prec 15 |  prec 10
#  31 |  62  |      0.932 cm |   prec 31  |          |
#  32 |  64  |      0.466 cm |   prec 32  |  prec 16 |
#  -------------------------------------------------------------

sortedPlaces = {k: v for k, v in sorted(places.items(), key=lambda item: item[0])}
for k,v in sortedPlaces.items():
    dist = haversine(mycoord, (v[4], v[5]), unit=Unit.MILES)
    print(f'{k:012d}: <{myID}> <<{myghh}>> {dist:.2f}m  {v} ')

print(f'CPYTHON? {ghh._hilbert.CYTHON_AVAILABLE} {ghh.rectangle("SSNo")} {ghh.neighbours("SSNo")}')
print(f'{ghh.rectangle("SSN")} {ghh.neighbours("SSN")}')
print('----')
h = 'SSNoWqX4bQ'
for i in range(1,len(h)+1):
    print(f'for {h} {h[:i]:12s} {analyzeGeoHash(h[:i])}')

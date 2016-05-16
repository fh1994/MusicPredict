from numpy import *
import datetime

def easyhandle():
    f = open('result2.csv')
    artists = {}
    f.readline()
    basetime = datetime.date(2015,3,1)

    for d in f.readlines():
        des = d.split(',')
        artist = des[0]
        date = datetime.date(*[int(x) for x in des[1].split('-')])
        if artist in artists:
            artists[artist][(date - basetime).days][1] = int(des[2])
        else:
            artists[artist] = zeros([183,2])
            artists[artist][(date - basetime).days][1] = int(des[2])

    for artist in artists:
        for i in range(1,artists[artist].shape[0]):
            artists[artist][i][0] = artists[artist][i-1][1]

    return artists

# replace easyhandle
def onlyKsumHandle(k):
    f = open('result2.csv')
    artists = {}
    f.readline()
    basetime = datetime.date(2015,3,1)

    for d in f.readlines():
        des = d.split(',')
        artist = des[0]
        date = datetime.date(*[int(x) for x in des[1].split('-')])
        if artist in artists:
            artists[artist][(date - basetime).days][1] = int(des[2])
        else:
            artists[artist] = zeros([183,2])
            artists[artist][(date - basetime).days][1] = int(des[2])

    for artist in artists:
        for i in range(1,artists[artist].shape[0]):
            for j in range(1,k+1):
                if i-j < 0:
                    break
                artists[artist][i][0] = artists[artist][i][0] + artists[artist][i-j][1]

    return artists

if __name__ == '__main__':
    artists = onlyKsumHandle(k=1)
    print(artists['8fb3cef29f2c266af4c9ecef3b780e97'])
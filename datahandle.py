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

def averageHandle():
    artists = easyhandle()
    f = open('average.csv')
    f.readline()
    for i in f.readlines():
        dd = i.split(',')
        artist = dd[0]
        for k in range(183):
            artists[artist][k][0] = int(dd[1])

    return artists

if __name__ == '__main__':
    artists = averageHandle()
    print(artists['8fb3cef29f2c266af4c9ecef3b780e97'])
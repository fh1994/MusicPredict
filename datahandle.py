from numpy import *
import datetime

def easyAllhandle():
    f = open('result2.csv')
    artists = {}
    f.readline()
    basetime = datetime.date(2015,3,1)

    for d in f.readlines():
        des = d.split(',')
        artist = des[0]
        date = datetime.date(*[int(x) for x in des[1].split('-')])
        if artist in artists:
            pass
            # artists[artist][(date - basetime).days][1] = int(des[2])
        else:
            artists[artist] = zeros([183,3])

        artists[artist][(date - basetime).days][0] = int(des[3])
        artists[artist][(date - basetime).days][1] = int(des[4])
        artists[artist][(date - basetime).days][2] = int(des[2])
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

def allonehandle():
    artists = easyAllhandle()
    aid = {}
    basetime = datetime.date(2015,3,1)
    train = []
    artistid = 0
    for artist in artists:
        id = 0
        if artist in aid:
            # artists[artist][(date - basetime).days][1] = int(des[2])
            id = aid[artist][0]
        else:
            id = artistid
            aid[artist] = [id , artists[artist][0][0]]
            artistid = artistid + 1

        for i in range(len(artists[artist])):
            if i != 0:
                traincell = [id,i,artists[artist][i][0],artists[artist][i-1][2],artists[artist][i][2]]
            # traino = [id,days,int(des[2]),int(des[4]),int(des[3]),int(des[2])]
                train.append(traincell)

    train = array(train)
    train.astype(float32)

    return train,aid,artists

if __name__ == '__main__':
    # a = easyAllhandle()
    # print(a['023406156015ef87f99521f3b343f71f'])
    train = onlyKsumHandle(1)
    for i in train:
        print(train[i])
    # print(train.dtype)

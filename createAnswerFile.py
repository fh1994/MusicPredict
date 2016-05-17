

######################################################################
## the artists must fit the struct bellow
## artist
######################################################################
def output(artists):
    output = open('mars_tianchi_artist_plays_predict.csv','w')
    begindate = datetime.date(2015,9,1)
    for artist in artists:
        for i in range(len(artist[artist])):
                currentdate = begindate + datetime.timedelta(days = i)
                ytest = clf.predict(xtest)
                ytest = int(ytest)
                output.write(artist+','+str(ytest)+','+str(currentdate).replace('-','')+'\n')
                xtest = ytest

    output.close()
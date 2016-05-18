import datetime
import datahandle
import evaluation
import numpy as np

from sklearn import ensemble

########################################################################
## simple test for dataset
########################################################################
def simpleGbdt():
    output = open('mars_tianchi_artist_plays_predict.csv','w')
    begindate = datetime.date(2015,9,1)
    baisdate = datetime.date(2015,3,1)
    train,aid,artists = datahandle.allonehandle()
    X = train[:,0:4]
    Y = train[:,4]
    print(X)
    print(Y)
    params = {'n_estimators': 500, 'max_depth': 5, 'min_samples_split': 2,
                  'learning_rate': 0.01, 'loss': 'ls'}
    clf = ensemble.GradientBoostingRegressor(**params)
    clf.fit(X,Y)

    for artist in artists:
        xtest = artists[artist][-1][2]
        for i in range(60):
            currentdate = begindate + datetime.timedelta(days = i)
            Xtest = [ aid[artist][0], (currentdate - begindate).days, aid[artist][1], xtest]
            Xtest = np.array(Xtest)
            Xtest.astype(np.float32)
            Xtest = Xtest.reshape(1, -1)
            print(Xtest)
            ytest = clf.predict(Xtest)
            ytest = int(ytest)
            output.write(artist+','+str(ytest)+','+str(currentdate).replace('-','')+'\n')
            xtest = ytest

        '''
        for i in range(60):
            currentdate = begindate + datetime.timedelta(days = i)
            ytest = clf.predict(xtest)
            ytest = int(ytest)
            output.write(artist+','+str(ytest)+','+str(currentdate).replace('-','')+'\n')
            xtest = ytest
        '''

########################################################################
## simple create answer for dataset
########################################################################
def createKnumAnswer(k):
    output = open('mars_tianchi_artist_plays_predict.csv','w')
    begindate = datetime.date(2015,9,1)
    artists = datahandle.onlyKsumHandle(k)
    for artist in artists:
        test = artists[artist]
        test = test.astype(np.float32)
        X = test[:,0]
        y = test[:,1]
        X_train, y_train = X, y

        X_train = X_train.reshape(-1,1)

        params = {'n_estimators': 500, 'max_depth': 5, 'min_samples_split': 2,
                  'learning_rate': 0.01, 'loss': 'ls'}
        clf = ensemble.GradientBoostingRegressor(**params)
        clf.fit(X_train, y_train)
        ##### axiba
        xtest = y_train[-1]
        ytest = 0
        for i in range(60):
            currentdate = begindate + datetime.timedelta(days = i)
            ytest = clf.predict(xtest)
            ytest = int(ytest)
            output.write(artist+','+str(ytest)+','+str(currentdate).replace('-','')+'\n')
            xtest = ytest
    output.close()

########################################################################
## simple k sum train for dataset
########################################################################
def onlyKsumGbdt(k):
    artists = datahandle.onlyKsumHandle(k)
    mall = 0
    for artist in artists:
        test = artists[artist]
        test = test.astype(np.float32)
        X = test[:,0]
        y = test[:,1]
        offset = 62
        X_train, y_train = X[offset:], y[offset:]
        X_test, y_test = X[:offset], y[:offset]

        X_train = X_train.reshape(-1,1)
        X_test = X_test.reshape(-1,1)

        params = {'n_estimators': 1400, 'max_depth': 3, 'min_samples_split': 101,
                  'learning_rate': 0.01, 'loss': 'lad'}
        clf = ensemble.GradientBoostingRegressor(**params)

        clf.fit(X_train, y_train)
        # print(y_test)
        mse = evaluation.Fij(clf.predict(X_test) ,y_test )
        mall = mall + mse
        # print("Fij: %.4f" % mse)

    return mall

########################################################################
## simple average train for dataset
########################################################################
def averageFeature():
    mall = 0
    artists = datahandle.averageHandle()
    for artist in artists:
        test = artists[artist]
        X = test[:,0]
        y = test[:,1]
        offset = 62
        X_train, y_train = X[offset:], y[offset:]
        X_test, y_test = X[:offset], y[:offset]
        mse = evaluation.Fij(X_test, y_test)
        mall = mall + mse
        print(mse)

    return mall

def createSimpleAnswer():
    output = open('mars_tianchi_artist_plays_predict.csv','w')
    begindate = datetime.date(2015,9,1)
    artists = datahandle.onlyKsumHandle(1)
    for artist in artists:
        test = artists[artist]
        test = test.astype(np.float32)
        X = test[:,0]
        y = test[:,1]
        X_train, y_train = X, y

        X_train = X_train.reshape(-1,1)

        params = {'n_estimators': 1400, 'max_depth': 3, 'min_samples_split': 101,
                  'learning_rate': 0.01, 'loss': 'lad'}
        clf = ensemble.GradientBoostingRegressor(**params)
        clf.fit(X_train, y_train)
        ##### axiba
        xtest = y_train[-1]
        ytest = 0
        for i in range(60):
            currentdate = begindate + datetime.timedelta(days = i)
            ytest = clf.predict(xtest)
            ytest = int(ytest)
            output.write(artist+','+str(ytest)+','+str(currentdate).replace('-','')+'\n')
            xtest = ytest
    output.close()

if __name__ == '__main__':
    createSimpleAnswer()
    # print(simpleGbdt())

    # print(onlyKsumGbdt(1))
    '''
    max = [0,0]
    for k in range(85,115):
        x = onlyKsumGbdt(1,k)
        if max[1] < x :
            max[0] = k
            max[1] = x
        print('%d : %f'%(k,x))

    print(max[0])
    print(max[1])
'''
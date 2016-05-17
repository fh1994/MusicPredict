import datetime
import datahandle
import evaluation
import numpy as np

from sklearn import ensemble

########################################################################
## simple test for dataset
########################################################################
def simpleGbdt():
    artists = datahandle.easyhandle()
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

        params = {'n_estimators': 500, 'max_depth': 5, 'min_samples_split': 2,
                  'learning_rate': 0.01, 'loss': 'ls'}
        clf = ensemble.GradientBoostingRegressor(**params)

        clf.fit(X_train, y_train)
        mse = evaluation.Fij( clf.predict(X_test), y_test)
        mall = mall + mse
        print("Fij: %.4f" % mse)

    return mall

########################################################################
## simple create answer for dataset
########################################################################
def createSimpleAnswer(k):
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

        params = {'n_estimators': 500, 'max_depth': 5, 'min_samples_split': 1,
                  'learning_rate': 0.01, 'loss': 'ls'}
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

if __name__ == '__main__':
    # createSimpleAnswer()
    for k in range(1,30):
       print(onlyKsumGbdt(k))
    print(averageFeature())
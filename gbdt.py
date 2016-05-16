import datetime
import datahandle
import evaluation
import numpy as np

from sklearn import ensemble

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
        mse = evaluation.Fij(y_test, clf.predict(X_test))
        mall = mall + mse
        print("Fij: %.4f" % mse)

    return mall


def createSimpleAnswer():
    output = open('mars_tianchi_artist_plays_predict.csv','w')
    begindate = datetime.date(2015,9,1)
    artists = datahandle.easyhandle()
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

        xtest = y_train[-1]
        ytest = 0
        for i in range(60):
            currentdate = begindate + datetime.timedelta(days = i)
            ytest = clf.predict(xtest)
            ytest = int(ytest)
            output.write(artist+','+str(ytest)+','+str(currentdate).replace('-','')+'\n')
            xtest = ytest
    output.close()

# replace simpleGbdt
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

        params = {'n_estimators': 500, 'max_depth': 5, 'min_samples_split': 2,
                  'learning_rate': 0.01, 'loss': 'ls'}
        clf = ensemble.GradientBoostingRegressor(**params)

        clf.fit(X_train, y_train)
        mse = evaluation.Fij(y_test, clf.predict(X_test))
        mall = mall + mse
        # print("Fij: %.4f" % mse)

    return mall
'''
test_score = np.zeros((params['n_estimators'],), dtype=np.float64)

for i, y_pred in enumerate(clf.staged_predict(X_test)):
    test_score[i] = clf.loss_(y_test, y_pred)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title('Deviance')
plt.plot(np.arange(params['n_estimators']) + 1, clf.train_score_, 'b-',
         label='Training Set Deviance')
plt.plot(np.arange(params['n_estimators']) + 1, test_score, 'r-',
         label='Test Set Deviance')
plt.legend(loc='upper right')
plt.xlabel('Boosting Iterations')
plt.ylabel('Deviance')
'''

###############################################################################
# Plot feature importance

'''
feature_importance = clf.feature_importances_
# make importances relative to max importance
feature_importance = 100.0 * (feature_importance / feature_importance.max())
sorted_idx = np.argsort(feature_importance)
pos = np.arange(sorted_idx.shape[0]) + .5
plt.subplot(1, 2, 2)
plt.barh(pos, feature_importance[sorted_idx], align='center')
plt.yticks(pos, boston.feature_names[sorted_idx])
plt.xlabel('Relative Importance')
plt.title('Variable Importance')
plt.show()
'''


if __name__ == '__main__':
    # createSimpleAnswer()
    for k in range(1,30):
        print(onlyKsumGbdt(k))
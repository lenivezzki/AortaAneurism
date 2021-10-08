from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_selection import RFE
from sklearn.linear_model import SGDRegressor
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.linear_model import Lasso


def get_featureKBest(df, target, headers, num):
    X = df.loc[:, headers]
    Y = df.loc[:, target]
    test = SelectKBest(score_func=chi2, k=num)
    fit = test.fit(X, Y)
    features_scores = fit.scores_
    features = {}
    if len(headers) != len(features_scores):
        return features
    for i in range(len(features_scores)):
        features[headers[i]] = features_scores[i]
    sorted_tuple = sorted(features.items(), key=lambda x: x[1], reverse=True)
    return dict(sorted_tuple)


def get_featureRFE(df, target, headers, num):
    X = df.loc[:, headers]
    Y = df.loc[:, target]
    model = SGDRegressor()
    rfe = RFE(estimator=model, n_features_to_select=num)
    fit = rfe.fit(X, Y)
    features_scores = fit.ranking_
    features = {}
    if len(headers) != len(features_scores):
        return features
    for i in range(len(features_scores)):
        features[headers[i]] = features_scores[i]
    sorted_tuple = sorted(features.items(), key=lambda x: x[1], reverse=False)
    return dict(sorted_tuple)

def get_featureExtraTrees(df, target, headers, num):
    X = df.loc[:, headers]
    Y = df.loc[:, target]
    model = ExtraTreesClassifier()
    model.fit(X, Y)
    features_scores = model.feature_importances_
    features = {}
    if len(headers) != len(features_scores):
        return features
    for i in range(len(features_scores)):
        features[headers[i]] = features_scores[i]
    sorted_tuple = sorted(features.items(), key=lambda x: x[1], reverse=True)
    return dict(sorted_tuple)

def get_featureLasso(df, target, headers, num=10):
    X = df.loc[:, headers]
    Y = df.loc[:, target]
    clf = Lasso(alpha=0.01)
    clf.fit(X, Y)
    features_scores = clf.coef_
    features = {}
    if len(headers) != len(features_scores):
        return features
    for i in range(len(features_scores)):
        if features_scores[i] != 0.0:
            features[headers[i]] = features_scores[i]
    sorted_tuple = sorted(features.items(), key=lambda x: x[1], reverse=True)
    return dict(sorted_tuple)

def feature_vote(features_KBest, features_RFE, features_ET, features_L):
    #Отбор фич по принципу: берем из каждого полученного 10 позиций, если совпадают голосованием, то берем
    k = 10
    f_1 = list(features_KBest)
    f_1 = f_1[:k]
    f_2 = list(features_RFE)
    f_2 = f_2[:k]
    f_3 = list(features_ET)
    f_3 = f_3[:k]
    f_4 = list(features_L)
    all_features = f_1+f_2+f_3+f_4

    to_vote_features = list(set(all_features))
    important_features_GL = []

    for f in to_vote_features:
        score = 0
        if f in f_1: score += 1
        else: score -= 1
        if f in f_2: score += 1
        else: score -= 1
        if f in f_3: score += 1
        else: score -= 1
        if f in f_4: score += 1
        else: score -= 1
        if score >= 0: #не знаю, ставить равно или нет (поставила, улучшает прогноз)
            important_features_GL.append(f)
    return important_features_GL

def feature_weights(df, model, headers, target):
    #list_d = list(vocabulary.items())
    #list_d.sort(key=lambda i: i[1], reverse=False)
    k=0
    feature_importance = abs(model.coef_[0])
    features = {}

    for i in headers:
        features[i] = feature_importance[k]
        k += 1

    list_f = list(features.items())
    list_f.sort(key=lambda i: i[1], reverse=True)
    return list_f
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import NearMiss
from sklearn.model_selection import train_test_split

from evaluation import evaluate_model


def simple_pred(df, important_features, target, model):
    X = df[important_features]
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=51, stratify=y)
    return evaluate_model(X_train, X_test, y_train, y_test, important_features, model)

def SMOTE_pred(df, important_features, target, model):
    smote = SMOTE()
    X, y = smote.fit_resample(df[important_features], df[target])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=51, stratify=y)
    return evaluate_model(X_train, X_test, y_train, y_test, important_features, model)

def NearMiss_pred(df, important_features, target, model):
    nr = NearMiss()
    X, y = nr.fit_sample(df[important_features], df[target])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=51, stratify=y)
    return evaluate_model(X_train, X_test, y_train, y_test, important_features, model)
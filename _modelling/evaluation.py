from sklearn import linear_model
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, r2_score, roc_auc_score, accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import cross_validate
import pandas as pd
import numpy as np


def evaluate_model(X_train, X_test, y_train, y_test, features, est):
    # min_max_scaler = MinMaxScaler()
    # X_train_scaled = min_max_scaler.fit_transform(X_train)
    # X_test_scaled = min_max_scaler.transform(X_test)

    all_accuracies = cross_validate(estimator=est, X=X_train, y=y_train, cv=20, scoring=['roc_auc', 'accuracy', 'f1'])
    est.fit(X_train, y_train)
    pred_test = est.predict(X_test)
    pred_train = est.predict(X_train)
    # rounded_pred = [round(value) for value in pred_test]
    # for i in range(len(rounded_pred)):
    #    if rounded_pred[i] > 1.0:
    #        rounded_pred[i] = 1.0
    # rounded_pred_train = [round(value) for value in pred_train]
    # for i in range(len(rounded_pred_train)):
    #    if rounded_pred_train[i] > 1.0:
    #        rounded_pred_train[i] = 1.0

    return pd.DataFrame({
        'train_MSE': [np.sqrt(mean_squared_error(y_train, pred_train))],  # отслеживание переобучения
        'train_ROC_AUC': [roc_auc_score(y_train, pred_train)],
        'train_accuracy': [accuracy_score(y_train, pred_train)],
        'train_f-score': [r2_score(y_train, pred_train)],
        'MSE': [np.sqrt(mean_squared_error(y_test, pred_test))],  # оценка теста
        'ROC_AUC': [roc_auc_score(y_test, pred_test)],
        'accuracy': [accuracy_score(y_test, pred_test)],
        'f-score': [f1_score(y_test, pred_test)],
        'recall': [recall_score(y_test, pred_test)],
        'precision': [precision_score(y_test, pred_test)],
        'crossval_ROC_AUC-mean': [all_accuracies['test_roc_auc'].mean()],
        'crossval_f-score-mean': [all_accuracies['test_f1'].mean()],
    }), pred_test, y_test

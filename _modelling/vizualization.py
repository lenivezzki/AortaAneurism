import seaborn as sns
import matplotlib.pyplot as plt

def vis_TruePredicted(true_value, predicted_value):
    plt.figure(figsize=(10, 10))
    plt.scatter(true_value, predicted_value, c='crimson')
    sns.scatterplot(x=true_value, y=predicted_value)
    plt.xticks([0, 1])
    plt.yticks([0, 1])
    plt.xlabel('True Values', fontsize=15)
    plt.ylabel('Predictions', fontsize=15)
    plt.axis('equal')
    plt.show()


from sklearn.metrics import confusion_matrix


def vis_confusionMatrix(true_value, predicted_value):
    tn, fp, fn, tp = confusion_matrix(true_value, predicted_value).ravel()
    cm = [[tn, fn], [fp, tp]]
    # print(cm)
    sns.heatmap(cm, annot=True, fmt='g', cmap="mako")
    plt.tick_params(axis='both', which='major', labelsize=15)
    plt.title('Матрица ошибок', fontsize=15)
    plt.xlabel('Истинный класс', fontsize=15)
    plt.ylabel('Предсказанный класс', fontsize=15)
    plt.axis('equal')
    plt.show()


def vis_histogram(true_value, predicted_value):
    tn, fp, fn, tp = confusion_matrix(true_value, predicted_value).ravel()
    x = ['True Negative', 'True Positive', 'False Negative', 'False Positive']
    y = [tn, tp, fn, fp]
    sns.set_context("paper", font_scale=1.5)
    plt.figure(figsize=(8, 6))
    ax = sns.barplot(x=x, y=y)
    ax.set_ylabel('Количество')
    # sns.displot(data=false, color='red')
    plt.show()
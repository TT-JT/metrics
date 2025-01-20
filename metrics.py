from preprocess import DataProcessor
from sklearn.metrics import precision_score, recall_score, accuracy_score, f1_score
dp=DataProcessor()
'''
准确率acc=(TP+TN)/(TP+FP+FN+TN)
召回率recall：TP/(TP+FN)
精确率precision：TP/(TP+FP)
F1score：2*recall*precision/(precision+recall)=2TP/(2TP+FP+FN)
'''
class ClassificationMetrics:
    def __init__(self, y_true, y_pred):
        self.y_true = y_true
        self.y_pred = y_pred

    def precision(self):
        return precision_score(self.y_true, self.y_pred)

    def recall(self):
        return recall_score(self.y_true, self.y_pred)

    def accuracy(self):
        return accuracy_score(self.y_true, self.y_pred)

    def f1_score(self):
        return f1_score(self.y_true, self.y_pred)
    def lift(self):
        return self.precision()/((len([i for i in self.y_true if i!=0])+1)/(len(self.y_true)+1))
    def metrics(self):
        return [self.accuracy(),self.recall(),self.precision(),self.f1_score(),self.lift()]

        
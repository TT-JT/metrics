import pandas as pd
class DataProcessor:
    def __init__(self,input_path=None):
        self.data=None
    def load_data(self,input_path):
        if input_path.endswith('.json'):
            data=pd.read_json(input_path)
        elif input_path.endswith('.csv') or input_path.endswith('.txt'):
            data=pd.read_csv(input_path)
        elif input_path.endswith('.xlsx'):
            data=pd.read_xlsx(input_path)
        else:
            raise ValueError('不支持的文件格式')
        labels_true,scores=[],[]
    # for content in data.content:
    #     content.append(content)
        for label in data.label:
            labels_true.append(label if type(label)==int or float else float(label))
        for score in data.score:
            scores.append(float(score))
        return labels_true,scores
        
    def label_processor(self,input_path,target_label,threshold):
        i=0
        labels_true,scores=self.load_data(input_path)
        labels_pred=[]
        # if target_label==1:
        #     for i in range(len(scores)):
        #         if scores[i]>threshold :
        #             labels_pred.append(1)
        #         else:
        #             #标签是0，1
        #             labels_pred.append(0)
        # elif taget_label==0:
        #     #将原有的标签进行转换
        for i in range(len(scores)):
            if scores[i]>threshold :
                labels_pred.append(1)
            else:
                #标签是0，1
                labels_pred.append(0)
        if target_label=='0':
            labels_pred=[1 - x for x in labels_pred]
            labels_true=[1 - x for x in labels_true]
        elif target_label!='1' and target_label!='0':
            raise ValueError('target_label is not available')
            
        return labels_true,labels_pred   
        
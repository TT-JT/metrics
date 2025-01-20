
#配置环境
import pandas as pd
import numpy as np
from preprocess import DataProcessor
from metrics import ClassificationMetrics


#文件输入输出位置、指定阈值及其分割间隔
target_label='1'
input_path='data.csv'
output_path=f'label_{target_label}'+'_metrics.csv'
threshold=0.5
interval=0.05
#输入模式
# target_label=input('请输入target_label:')
# input_path=input('请输入文件路径：')
# output_path=f'label_{target_label}'+'_metrics.csv'
# threshold=0.5
# interval=input('请输入阈值间隔：')

#创建实例得到指定阈值对应的标签预测结果及其指标
dp=DataProcessor()
labels_true,labels_pred=dp.label_processor(input_path,target_label,threshold)
class_m=ClassificationMetrics(labels_true,labels_pred)
print(labels_true,labels_pred)
print(class_m.metrics())

#根据不同阈值计算对应指标
threshold_and_metrics=[]
for ther in np.arange(0,1,0.05):
    labels_true,labels_pred=dp.label_processor(input_path,target_label,ther)
    ClaMe=ClassificationMetrics(labels_true,labels_pred)
    threshold_and_metrics.append([ther]+ClaMe.metrics())

# 将数据列表转换为DataFrame并写入csv文件
headers=['threshold','acc','recall','precision','f1_score','lift']
df = pd.DataFrame(threshold_and_metrics, columns=headers)
df.to_csv(output_path, index=False)


























                
            
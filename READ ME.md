### 可读取的文件形式：csv、xlsx、json、txt
## 内容包括：content、label、score

### 内容格式要求：
#### csv、xlsx文件

| 左对齐 | 居中对齐 | 右对齐 |
| :------ | :------: | ------: |
| 内容 1  |  内容 2  |   内容 3 |
| 内容 4  |  内容 5  |   内容 6 |




｜0	﻿｜content｜	label｜	score｜
｜------｜--------｜------｜-----｜
｜1｜	a ｜0｜0.4｜
｜2｜	b	｜1｜0.7｜
3	c	1	0.8
4	d	0	0.68
5	e	1	0.47
6	f	0	0.44


#### txt文件
content,label,score
a,	0,	0.4
b,	1,	0.7
c,	1,	0.8
d,	0,	0.68
e,	1,	0.47
f,	0,	0.44

#### json文件
[{"content":"a","label":'0',"score":0.4},
 {"content":"b","label":'1',"score":0.7},
 {"content":"c","label":'1',"score":0.8},
 {"content":"d","label":'0',"score":0.68},
 {"content":"e","label":'1',"score":0.47},
 {"content":"f","label":'0',"score":0.44}
 ]
### 指标
#### 评测指标
主要用到的指标是准确率accuracy、召回率recall、精确率precsion、F1score，需要根据混淆矩阵计算它们在不同阈值下的值，根据需要选取阈值。
混淆矩阵：
｜ 正例标签为0时｜预测为0｜预测为1｜
｜---｜---｜---｜
｜真实值为0｜TP｜FN｜
｜真实值为1｜FP｜TN｜
TP（True Positives)：真正例，即预测为正例而且实际上也是正例；
FP（False Positives)：假正例，即预测为正例然而实际上却是负例；
FN（false Negatives)：假负例，即预测为负例然而实际上却是正例；
TN（True Negatives)：真负例，即预测为负例而且实际上也是负例。

准确率accuracy：(TP+TN)/(TP+FP+FN+TN)
召回率recall：TP/(TP+FN)
精确率precision：TP/(TP+FP)
F1score：2*recall*precision/(precision+recall)=2TP/(2TP+FP+FN)
提升度lift：precison/样本正例比率

重点关注的指标是召回率和精确率。

阈值：在预测时，每个标签都有对应的分数，标签阈值指的是在分数大于该阈值时将其分为对应标签。

### 使用
如一个二分类问题，关于一句话表达的情感是‘好’或‘不好’，模型推理时对应标签为‘好’：‘1’、‘不好’：‘0’，那么产生的score是对应于标签‘好’，在进行指标评测时，target_label输入1代表计算标签为‘好’的对应指标，反之，计算标签为‘不好’的对应指标。

python main.py

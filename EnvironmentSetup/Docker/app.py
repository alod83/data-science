#!/usr/bin/env python
# coding: utf-8

# # Data Analysis with Scikit-learn
# In this short tutorial I illustrate a complete data analysis process which exploits the `scikit-learn` Python library. The process includes
# * preprocessing, which includes features selection, normalization and balancing
# * model selection with parameters tuning
# * model evaluation

# ## Load Dataset
# Firstly, I load the dataset through the Python `pandas` library. I exploit the `heart.csv` dataset, provided by the [Kaggle repository](https://www.kaggle.com/rashikrahmanpritom/heart-attack-analysis-prediction-dataset).

# In[132]:
import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np

images_dir = 'images'
df = pd.read_csv('source/heart.csv')
df.head()


# In[133]:


df.shape


# ## Features selection
# Now, I split the columns of the dataset in input (`X`) and output (`Y`). I use all the columns but `output` as input features. 

# In[134]:


features = []
for column in df.columns:
    if column != 'output':
        features.append(column)
features


# In[135]:


X = df[features]
Y = df['output']


# In order to select the minimum set of input features, I calculate the Pearson correlation coefficient among features, through `corr()` function, provided by a `pandas dataframe`.

# In[136]:


X.corr()


# I note that all the features have a low correlation, thus I can keep all of them as input features.

# ## Data Normalization
# Data Normalization scales all the features in the same interval. I exploit the `MinMaxScaler()` provided by the `scikit-learn` library. I dealt with Data Normalization in `scikit-learn` in my [previous article](https://towardsdatascience.com/data-normalization-with-python-scikit-learn-e9c5640fed58), while I [this](https://towardsdatascience.com/data-preprocessing-with-python-pandas-part-3-normalisation-5b5392d27673) article I described the general process of Data Normalization without `scikit-learn`.

# In[137]:


X.describe()


# For each input feature I calculate the `MinMaxScaler()` and I store the result in the same `X` column. The `MinMaxScaler()` must be fitted firstly through the `fit()` function and then can be applied for a transformation through the `transform()` function. Note that I must reshape every feature in the format (-1,1) in order to be passed as input parameter of the scaler. For example, `Reshape(-1,1)` transforms the array `[0,1,2,3,5]` into `[[0],[1],[2],[3],[5]]`.

# In[138]:


from sklearn.preprocessing import MinMaxScaler

for column in X.columns:
    feature = np.array(X[column]).reshape(-1,1)
    scaler = MinMaxScaler()
    scaler.fit(feature)
    feature_scaled = scaler.transform(feature)
    X[column] = feature_scaled.reshape(1,-1)[0]


# In[139]:


X.describe()


# ## Split the dataset in Training and Test
# Now I split the dataset into two parts: training and testset. The test set size is 20% of the whole dataset. I exploit the `scikit-learn` function `train_test_split()`. I will use the training set to train the model and the testset to test the performance of the model.

# In[140]:


import numpy as np
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size=0.20, random_state=42)


# ## Balancing
# I check whether the dataset is balanced or not, i.e. if the output classes in the training set are equally represented. I can use the `value_counts()` function to calculate the number of records in each output class.

# In[141]:


y_train.value_counts()


# The output classes are not balanced, thus I can balance it. I can exploit the `imblearn` library, to perform balancing. I try both oversampling the minority class and undersampling the majority class. More details related to the Imbalanced Learn library can be found [here](https://imbalanced-learn.org/stable/).
# Firstly, I perform over sampling through the `RandomOverSampler()`. I create the model and then I fit with the training set. The `fit_resample()` function returns the balanced training set.

# In[142]:


from imblearn.over_sampling import RandomOverSampler
over_sampler = RandomOverSampler(random_state=42)
X_bal_over, y_bal_over = over_sampler.fit_resample(X_train, y_train)


# I calculate the number of records in each class through the `value_counts()` function and I note that now the dataset is balanced.

# In[143]:


y_bal_over.value_counts()


# Secondly, I perform under sampling through the `RandomUnderSampler()` model.

# In[144]:


from imblearn.under_sampling import RandomUnderSampler

under_sampler = RandomUnderSampler(random_state=42)
X_bal_under, y_bal_under = under_sampler.fit_resample(X_train, y_train)


# In[145]:


y_bal_under.value_counts()


# ## Model Selection and Training

# Now, I'm ready to train the model. I choose a `KNeighborsClassifier` and firstly I train it with imbalanced data. I exploit the `fit()` function to train the model and then the`predict_proba()` function to predict the values of the test set.

# In[120]:


from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)
y_score = model.predict_proba(X_test)


# I calculate the performance of the model. In particular, I calculate the `roc_curve()` and the `precision_recall()` and  then I plot them. I exploit the `scikitplot` library to plot curves. 
# 
# From the plot I note that there is a roc curve for each class. With respect to the precision recall curve, the class 1 works better than class 0, probably because it is represented by a greater number of samples.

# In[121]:


import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve
from scikitplot.metrics import plot_roc,auc
from scikitplot.metrics import plot_precision_recall

fpr0, tpr0, thresholds = roc_curve(y_test, y_score[:, 1])

# Plot metrics 
plot_roc(y_test, y_score)
plt.savefig(f"{images_dir}/roc.png")
#plt.show()
    
plot_precision_recall(y_test, y_score)
plt.savefig(f"{images_dir}/precision_recall.png")
#plt.show()


# Now, I recalculate the same things with oversampling balancing. I note that the precision recall curve of class 0 increases, while that of class 1 decreases.

# In[122]:


model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_bal_over, y_bal_over)
y_score = model.predict_proba(X_test)


# In[123]:


fpr0, tpr0, thresholds = roc_curve(y_test, y_score[:, 1])

# Plot metrics 
plot_roc(y_test, y_score)
plt.savefig(f"{images_dir}/roc-oversampling.png")
#plt.show()
    
plot_precision_recall(y_test, y_score)
plt.savefig(f"{images_dir}/precision_recall-oversampling.png")
#plt.show()


# Finally, I train the model through under sampled data and I note a general deterioration of the performance.

# In[124]:


model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_bal_under, y_bal_under)
y_score = model.predict_proba(X_test)


# In[125]:


fpr0, tpr0, thresholds = roc_curve(y_test, y_score[:, 1])

# Plot metrics 
plot_roc(y_test, y_score)
#plt.show()
plt.savefig(f"{images_dir}/roc-undersampling.png")
    
plot_precision_recall(y_test, y_score)
plt.savefig(f"{images_dir}/precision_recall-undersampling.png")
#plt.show()


# ## Parameters Tuning
# In the last part of this tutorial, I try to improve the performance of the model by searching for best parameters for my model. I exploit the `GridSearchCV` mechanism provided by the `scikit-learn` library. I select a range of values for each parameter to be tested and I put them in the `param_grid` variable. I create a `GridSearchCV()` object, I fit with the training set and then I retrieve the best estimator, contained in the `best_estimator_` variable.

# In[126]:


from sklearn.model_selection import GridSearchCV

model = KNeighborsClassifier()

param_grid = {
   'n_neighbors': np.arange(2,8),
   'algorithm' : ['auto', 'ball_tree', 'kd_tree', 'brute'],
    'metric' : ['euclidean','manhattan','chebyshev','minkowski']
}

grid = GridSearchCV(model, param_grid = param_grid)
grid.fit(X_train, y_train)


best_estimator = grid.best_estimator_
best_estimator


# I exploit the best estimator as model for my predictions and I calculate the performance of the algorithm.

# In[127]:


best_estimator.fit(X_train, y_train)
y_score = best_estimator.predict_proba(X_test)


# In[128]:


fpr0, tpr0, thresholds = roc_curve(y_test, y_score[:, 1])

# Plot metrics 
plot_roc(y_test, y_score)
plt.savefig(f"{images_dir}/roc-cv.png")
#plt.show()
    
plot_precision_recall(y_test, y_score)
plt.savefig(f"{images_dir}/precision_recall-cv.png")
#plt.show()


# I note that the roc curve has improved. I try now with the over sampled training set.

# In[129]:


grid = GridSearchCV(model, param_grid = param_grid)
grid.fit(X_bal_over, y_bal_over)


best_estimator = grid.best_estimator_
best_estimator


# In this case I obtain the best performance.

# In[130]:


best_estimator.fit(X_bal_over, y_bal_over)
y_score = best_estimator.predict_proba(X_test)


# In[131]:


fpr0, tpr0, thresholds = roc_curve(y_test, y_score[:, 1])
roc_auc0 = auc(fpr0, tpr0)

# Plot metrics 
plot_roc(y_test, y_score)
plt.savefig(f"{images_dir}/roc-cv-oversampling.png")
#plt.show()
    
plot_precision_recall(y_test, y_score)
plt.savefig(f"{images_dir}/precision_recall-cv-oversampling.png")
#plt.show()


# In[ ]:





from sklearn.tree import DecisionTreeClassifier
import pandas as pd 
import utils
import random
import numpy as np

from modAL.models import ActiveLearner
from modAL.uncertainty import uncertainty_sampling





class AI():
    
    
    def __init__(self):
        self.clf = DecisionTreeClassifier(random_state=0)

    def fit_predict(self, x_dim,y_dim,real_value,known_data):
        df = pd.DataFrame()

        df['x_dim'] = x_dim
        df['y_dim'] = y_dim
        df['y'] = real_value
        df['known_data'] = known_data

        df_train = df[df['known_data'] == 1].reset_index(drop = True)

        FEATURES = ['x_dim','y_dim']
        
        self.clf.fit(df_train[FEATURES], df_train['y'])

        return self.clf.predict(df[FEATURES])


# class Active_AI():
    
    
#     def __init__(self):
#         self.learner = ActiveLearner(
#                                 estimator=DecisionTreeClassifier(random_state=0),
#                                 query_strategy=uncertainty_sampling
#                                 )

#     def next_data(self, x_dim,y_dim,real_value,known_data):
#         df = pd.DataFrame()

#         df['x_dim'] = x_dim
#         df['y_dim'] = y_dim
#         df['y'] = real_value
#         df['known_data'] = known_data

#         df_train = df[df['known_data'] == 1].reset_index(drop = True)

#         FEATURES = ['x_dim','y_dim']
        
#         self.learner.fit(df_train[FEATURES], df_train['y'])
        
#         print(df.x_dim)
#         query_idx, query_inst = self.learner.query(df_train.iloc[FEATURES])
#         return print(query_idx)


#     # def fit_predict(self, x_dim,y_dim,real_value,known_data):
#     #     df = pd.DataFrame()

#     #     df['x_dim'] = x_dim
#     #     df['y_dim'] = y_dim
#     #     df['y'] = real_value
#     #     df['known_data'] = known_data

#     #     df_train = df[df['known_data'] == 1].reset_index(drop = True)

#     #     FEATURES = ['x_dim','y_dim']
        
#     #     self.clf.fit(df_train[FEATURES], df_train['y'])

#     #     return self.clf.predict(df[FEATURES])





# COEF_A = random.random()*4
# COEF_B = random.randint(0, 20)
# SIDE = random.random()

# clickedObj = []

# PointsTrueValue = []
# PaintedPoints = []

# x = []
# y = []
# for i in range(0, 100):
#     x1, y1 = utils.on_grid_random(SCREEN_SIZE = 300, SURFACE = 10)
#     x.append(x1)
#     y.append(y1)

#     if SIDE < 0.5:
#         if x1*COEF_A + COEF_B <= y1:
#             PointsTrueValue.append(1)
#         else:
#             PointsTrueValue.append(0)
#     else:
#         if x1*COEF_A + COEF_B >= y1:
#             PointsTrueValue.append(1)
#         else:
#             PointsTrueValue.append(0)
#     if random.random() < 0.05:
#         clickedObj.append(1)
#     else :
#         clickedObj.append(0)

# learner = ActiveLearner(
#                       estimator=DecisionTreeClassifier(random_state=0),
#                       query_strategy=uncertainty_sampling
#                       )
# df = pd.DataFrame()

# df['x_dim'] = x
# df['y_dim'] = y
# df['y'] = PointsTrueValue
# df['known_data'] = clickedObj

# df_train = df[df['known_data'] == 1]
# df_pool = df[df['known_data'] == 0]

# np.vstack((x,y,PointsTrueValue,clickedObj))

# FEATURES = ['x_dim','y_dim']







# X_raw = np.stack((x,y), axis = 1)
# y_raw = np.asarray(PointsTrueValue)

# X_train = X_raw[np.where(np.asarray(clickedObj) == 1)]
# y_train = y_raw[np.where(np.asarray(clickedObj) == 1)]

# X_pool = X_raw[np.where(np.asarray(clickedObj) == 0)]
# y_pool = y_raw[np.where(np.asarray(clickedObj) == 0)]


# learner.fit(X_train, y_train)
 

# performance_history = []
# model_accuracy = learner.score(X_raw, y_raw)
# print('Accuracy after query 0: {acc:0.4f}'.format(acc=model_accuracy))
# for index in range(10):
#     query_index, query_instance = learner.query(X_pool)
#     # Teach our ActiveLearner model the record it has requested.
#     X, y = X_pool[query_index].reshape(1, -1), y_pool[query_index].reshape(1, )
#     learner.teach(X=X, y=y)

#     # Remove the queried instance from the unlabeled pool.
#     X_pool, y_pool = np.delete(X_pool, query_index, axis=0), np.delete(y_pool, query_index)


#     # Calculate and report our model's accuracy.
#     model_accuracy = learner.score(X_raw, y_raw)
#     print('Accuracy after query {n}: {acc:0.4f}'.format(n=index + 1, acc=model_accuracy))

#     # Save our model's performance for plotting.
#     performance_history.append(model_accuracy)

#     print(query_index, query_instance )
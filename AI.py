from sklearn.tree import DecisionTreeClassifier
import pandas as pd 
import utils
import random





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

        x = self.clf.predict(df[FEATURES])
        
        return x

    



COEF_A = random.random()*4
COEF_B = random.randint(0, 20)
SIDE = random.random()

clickedObj = []

PointsTrueValue = []
PaintedPoints = []

for i in range(0, 100):
    x, y = utils.on_grid_random(SCREEN_SIZE = 300, SURFACE = 10)
    
    if SIDE < 0.5:
        if x*COEF_A + COEF_B <= y:
            PointsTrueValue.append(1)
        else:
            PointsTrueValue.append(0)
    else:
        if x*COEF_A + COEF_B >= y:
            PointsTrueValue.append(1)
        else:
            PointsTrueValue.append(0)
    if random.random() < 0.2:
        clickedObj.append(1)
    else :
        clickedObj.append(0)

AI = AI()
print(AI.fit_predict(x_dim = x, y_dim = y, real_value = PointsTrueValue, known_data = clickedObj))
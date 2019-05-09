from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


model = LinearRegression()


def linear_model_predict(xTrain, yTrain, xTest, yTest):

    model.fit(xTrain, yTrain)
    prediction = model.predict(xTest)

    coefficients = model.coef_
    mse = mean_squared_error(prediction, yTest)
    variance = r2_score(yTest, prediction)  # 1 is perfect prediction



import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
import numpy as np

df = pd.read_csv("historical_sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

df["Month_Index"] = range(len(df))

X = df[["Month_Index"]]
y = df["Sales"]

split = int(len(df) * 0.8)
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

model = LinearRegression()
model.fit(X_train, y_train)

pred = model.predict(X_test)

mae = mean_absolute_error(y_test, pred)
rmse = np.sqrt(mean_squared_error(y_test, pred))
r2 = r2_score(y_test, pred)

print("MAE:", round(mae, 2))
print("RMSE:", round(rmse, 2))
print("R2 Score:", round(r2, 2))

future_index = pd.DataFrame({
    "Month_Index": range(len(df), len(df)+12)
})

future_pred = model.predict(future_index)

plt.figure(figsize=(10,5))
plt.plot(df["Date"], df["Sales"], label="Historical Data")
plt.plot(df["Date"].iloc[split:], pred, label="Test Predictions")
plt.legend()
plt.title("Historical Sales vs Predictions")
plt.tight_layout()
plt.savefig("prediction_plot.png")
plt.show()

print("Next 12 Month Forecast")
print(future_pred)

import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("game-ratings-by-release-dates.csv")

# Pre-processing data
df["first_release_date"] = pd.to_datetime(df["first_release_date"])

# Visualize data.
plt.scatter(df["first_release_date"], df["critic_rating_value"], color = "black", alpha = 0.75, label = "Critic Ratings")
plt.scatter(df["first_release_date"], df["user_rating_value"], color = "green", alpha = 0.75, label = "User Ratings")

plt.legend(loc = "upper left")

plt.show()
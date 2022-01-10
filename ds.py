import plotly.figure_factory as ff
import statistics
import random
import pandas as pd

df = pd.read_csv("data.csv")
nums = df["reading_time"].to_list()

mean = statistics.mean(nums)
print("original set mean: " + str(mean))

means = []
for i in range(0, 100):
    d = [(nums[random.randint(0, len(nums) - 1)]) for i in range(0, 30)]
    means.append(statistics.mean(d))

mean = statistics.mean(means)

print("sampled set mean: " + str(mean))

graph = ff.create_distplot([nums], ["numbers"], show_hist=False)
graph.show()
sampGraph = ff.create_distplot([means], ["numbers"], show_hist=False)
sampGraph.show()
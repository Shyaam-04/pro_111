import random
import statistics
import plotly.graph_objects as go
import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean


# Function to get the mean of 100 data sets
mean_list = []
for i in range(0,1000):
    set_of_means= random_set_of_mean(100)
    mean_list.append(set_of_means)

std_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)

print("mean of sampling distribution:- ",mean)
print("Standard deviation of sampling distribution:- ",std_deviation)

first_sd_st,first_sd_end = mean-std_deviation, mean+std_deviation
second_sd_st,second_sd_end = mean-(2*std_deviation),mean+(2*std_deviation)
third_sd_st,third_sd_end = mean-(3*std_deviation),mean+(3*std_deviation)

df = pd.read_csv("sample_2.csv")
data = df["reading_time"].tolist()
mean_of_sample2 = statistics.mean(data)
print("mean of sample 2:- ",mean_of_sample2)
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean], y=[0, 1.4], mode="lines", name="MEAN OF SAMPLE DATA"))
fig.add_trace(go.Scatter(x=[first_sd_st, first_sd_st], y=[0, 1.4], mode="lines", name="STANDARD DEVIATION 1 START"))
fig.add_trace(go.Scatter(x=[second_sd_st, second_sd_st], y=[0, 1.4], mode="lines", name="STANDARD DEVIATION 1 START"))
fig.add_trace(go.Scatter(x=[third_sd_st, third_sd_st], y=[0, 1.4], mode="lines", name="STANDARD DEVIATION 1 START"))
fig.add_trace(go.Scatter(x=[first_sd_end, first_sd_end], y=[0, 1.4], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_sd_end, second_sd_end], y=[0, 1.4], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_sd_end, third_sd_end], y=[0, 1.4], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()

z_score = (mean-mean_of_sample2)/std_deviation
print("The z score is:- ",z_score)



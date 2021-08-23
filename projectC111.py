import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as stat
import random

def sample():
    random_data = []
    for i in range(0,100):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        random_data.append(value)
    return stat.mean(random_data)

def main():
    m_list = []
    for i in range(0,1000):
        m = sample()
        m_list.append(m)
    
    sample_std = stat.stdev(m_list)
    sample_mean = stat.mean(m_list)
    print("The standard devination for sample data mean is, ",sample_std)
    print("The sample data mean is, ",sample_mean)

    first_std_deviation_start, first_std_deviation_end = sample_mean-sample_std, sample_mean+sample_std
    second_std_deviation_start, second_std_deviation_end = sample_mean-(2*sample_std), sample_mean+(2*sample_std)
    third_std_deviation_start, third_std_deviation_end = sample_mean-(3*sample_std), sample_mean+(3*sample_std)

    # finding the mean of  and plotting on graph
    df = pd.read_csv("medium_data.csv")
    data = df["reading_time"].tolist()
    mean = stat.mean(data)

    print("Mean of sample", mean)

    #finding z scores
    #if the z score < 1 or < 2,  the impact of the intervention might not be statistically significant.
    z = (sample_mean - mean_sample1)/sample_std
    print("z score", z)


    fig = ff.create_distplot([m_list], ["student marks"], show_hist=False)

    fig.add_trace(go.Scatter(x=[sample_mean, sample_mean], y=[0, 0.17], mode="lines", name="Mean"))

    fig.add_trace(go.Scatter(x=[mean_sample1, mean_sample1], y=[0, 0.17], mode="lines", name="Mean"))
    
    fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
    fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
    fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
    
    fig.show()
main()
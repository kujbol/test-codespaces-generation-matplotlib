
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Display dependencies
st.write("Streamlit version:", st.__version__)
st.write("Matplotlib version:", plt.__version__)
st.write("Numpy version:", np.__version__)

# Set page title
st.title("Matplotlib Demo")

# Plot a simple line graph
def line_graph():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    plt.title("Line Graph")
    st.pyplot()

# Plot a bar chart
def bar_chart():
    labels = ['A', 'B', 'C', 'D', 'E']
    values = [4, 6, 8, 2, 7]
    plt.bar(labels, values)
    plt.xlabel("Labels")
    plt.ylabel("Values")
    plt.title("Bar Chart")
    st.pyplot()

# Plot a scatter plot
def scatter_plot():
    x = np.random.randn(100)
    y = np.random.randn(100)
    plt.scatter(x, y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Scatter Plot")
    st.pyplot()

# Display a dropdown select box to choose the plot type
plot_type = st.sidebar.selectbox("Select a plot type", ("Line Graph", "Bar Chart", "Scatter Plot"))

# Call the respective function based on the selected plot type
if plot_type == "Line Graph":
    line_graph()
elif plot_type == "Bar Chart":
    bar_chart()
elif plot_type == "Scatter Plot":
    scatter_plot()

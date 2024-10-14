import matplotlib.pyplot as plt

def create_bar_chart(data, title="Bar Chart"):
    plt.figure(figsize=(10, 6))
    plt.bar(data.keys(), data.values())
    plt.title(title)
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.show()

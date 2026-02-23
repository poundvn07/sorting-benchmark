import numpy as np
import matplotlib.pyplot as plt
from sorting_benchmark import chart_data

def draw_chart(chart_data):
    labels = chart_data['labels']
    x = np.arange(len(labels))
    width = 0.2

    fig, ax = plt.subplots(figsize=(12, 6))
    bars = []
    for i, algo in enumerate(['QuickSort', 'HeapSort', 'MergeSort', 'NumPySort']):
        times = chart_data[algo]
        bar = ax.bar(x + i*width, times, width, label=algo)
        bars.append(bar)
        for rect, time_val in zip(bar, times):
            ax.text(
                rect.get_x() + rect.get_width() / 2,
                rect.get_height(),
                round(time_val),
                ha='center',
                va='bottom',
                fontsize=8,
                rotation=90
            )

    ax.set_xlabel('Datasets')
    ax.set_ylabel('Time (ms)')
    ax.set_title('Sorting Algorithm Performance')
    ax.set_xticks(x + width * 1.5)
    ax.set_xticklabels(labels)
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

draw_chart(chart_data)

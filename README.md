# Sorting Algorithm Benchmark

Performance comparison of sorting algorithms on datasets containing **1,000,000 elements**.

## Algorithms

- QuickSort (Median-of-Three pivot)
- HeapSort
- MergeSort
- NumPy Sort (`numpy.sort`)

---

## Dataset

Each algorithm is tested on **10 datasets**:

- Sorted ascending floats
- Sorted descending floats
- Random floats (3 sets)
- Random integers (5 sets)
- The data size for each dataset: 1.000.000 elements

---

## Requirements

- Python 3.x  
- NumPy  
- Matplotlib
---

This project is developed for educational and research purposes, aiming to:

- Analyze practical performance of O(n log n) algorithms

- Compare pure Python implementations with optimized NumPy backend

- Study the impact of input order on sorting efficiency

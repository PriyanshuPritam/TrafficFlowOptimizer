# TrafficFlowOptimizer (CLI)  

A **Real-Time Traffic Congestion Predictor** that models a city's road network as a **graph** and predicts congestion using **graph algorithms** and **time-series forecasting**. This project is implemented in **pure Python** with no external libraries.  

---

## 📌 Features  

✅ **Graph Construction** – Models the road network as a **weighted graph** (nodes = intersections, edges = roads).  
✅ **Traffic Data Input** – Simulates live and historical traffic data (random congestion levels).  
✅ **Congestion Prediction** – Uses **exponential smoothing** to forecast congestion trends.  
✅ **Shortest Path Calculation** – Implements **Dijkstra’s algorithm** to find the optimal route.  
✅ **Dynamic Rerouting** – Suggests alternate routes in case of high congestion.  
✅ **Priority Queues & Heaps** – Manages congested roads efficiently.  
✅ **Breadth-First Search (BFS)** – Detects high-congestion zones in the road network.  

---

## 🛠 Data Structures & Algorithms Used  

- **Graph (Adjacency List)** – To represent the city’s road network.  
- **Min-Heap (Priority Queue)** – Used in **Dijkstra’s Algorithm** for efficient shortest-path computation.  
- **Breadth-First Search (BFS)** – Identifies highly congested zones in the road network.  
- **Circular Buffer** – Stores time-series traffic data for recent hours.  
- **Dijkstra’s Algorithm** – Computes the shortest and least congested path.  
- **Exponential Smoothing** – Forecasts future congestion trends.  

---

## 🎮 How It Works  

1️⃣ **View Current Traffic Congestion** – Check live congestion levels of all roads.  
2️⃣ **Find the Best Route** – Get the optimal path between two locations, considering congestion.  
3️⃣ **Predict Future Congestion** – Forecast congestion levels on a specific route.  
4️⃣ **Exit** – Quit the program.  

---

## 🏙 Example Road Network  
```
 A -- B  
 |    |  
 C -- D -- E
```

🚀 Getting Started

1. Clone the Repository
git clone https://github.com/PriyanshuPritam/TrafficFlowOptimizer.git
cd TrafficFlowOptimizer

2. Run the Program
python traffic_predictor.py


🔮 Future Enhancements
🔹 Support for real-world GPS data integration.
🔹 Advanced machine learning models for better congestion prediction.
🔹 Web or GUI interface for user-friendly interaction.


Developed with 🚀 & ☕


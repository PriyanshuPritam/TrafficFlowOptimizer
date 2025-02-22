import heapq
import random
import time


class TrafficGraph:
    def __init__(self):
        self.graph = {}
        self.congestion = {}

    def add_road(self, u, v, weight):
        u, v = u.upper(), v.upper()
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))
        self.congestion[(u, v)] = self.congestion[(v, u)] = random.randint(1, 10)

    def update_congestion(self):
        for key in self.congestion:
            self.congestion[key] = max(1, min(10, self.congestion[key] + random.choice([-1, 0, 1])))

    def bfs_congestion_zones(self, threshold=7):
        congested_roads = [road for road, level in self.congestion.items() if level >= threshold]
        return congested_roads

    def dijkstra(self, start, end):
        start, end = start.upper(), end.upper()
        pq = [(0, start)]  # (cost, node)
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        prev_nodes = {}

        while pq:
            current_cost, current_node = heapq.heappop(pq)

            if current_node == end:
                break

            for neighbor, weight in self.graph[current_node]:
                congestion_level = self.congestion.get((current_node, neighbor), 1)
                new_cost = current_cost + weight + congestion_level

                if new_cost < distances[neighbor]:
                    distances[neighbor] = new_cost
                    prev_nodes[neighbor] = current_node
                    heapq.heappush(pq, (new_cost, neighbor))

        path, node = [], end
        while node in prev_nodes:
            path.insert(0, node)
            node = prev_nodes[node]
        if path:
            path.insert(0, start)
        return path, distances[end]

    def predict_congestion_for_route(self, start, end):
        path, _ = self.dijkstra(start, end)
        if not path:
            return "Invalid route"
        congestion_values = [self.congestion.get((path[i], path[i + 1]), 1) for i in range(len(path) - 1)]
        return exponential_smoothing(congestion_values)


def exponential_smoothing(data, alpha=0.3):
    smoothed = [data[0]]
    for i in range(1, len(data)):
        smoothed.append(alpha * data[i] + (1 - alpha) * smoothed[-1])
    return smoothed[-1]


# Example Usage
def main():
    city = TrafficGraph()
    roads = [("A", "B", 5), ("A", "C", 3), ("B", "D", 4), ("C", "D", 2), ("D", "E", 6)]
    for u, v, w in roads:
        city.add_road(u, v, w)

    while True:
        print("\nCity Map (Rough Layout):")
        print(" A -- B")
        print(" |    |")
        print(" C -- D -- E")
        print("\nAvailable Locations: A, B, C, D, E")

        print("\nOptions:")
        print("1. View Current Traffic Congestion")
        print("2. Find Best Route")
        print("3. Predict Future Congestion for a Route")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            city.update_congestion()
            print("\nCurrent Traffic Congestion Levels:")
            for road, level in city.congestion.items():
                print(f"Road {road}: Congestion {level}/10")
            print("\nHigh Congestion Roads:", city.bfs_congestion_zones())

        elif choice == "2":
            start = input("Enter start location: ").strip().upper()
            end = input("Enter destination: ").strip().upper()
            if start in city.graph and end in city.graph:
                path, cost = city.dijkstra(start, end)
                print(f"\nBest Route from {start} to {end}: {path} with cost {cost}")
            else:
                print("Invalid locations. Please try again.")

        elif choice == "3":
            start = input("Enter start location: ").strip().upper()
            end = input("Enter destination: ").strip().upper()
            if start in city.graph and end in city.graph:
                prediction = city.predict_congestion_for_route(start, end)
                print(f"Predicted Future Congestion for {start} to {end}: {prediction:.2f}")
            else:
                print("Invalid locations. Please try again.")

        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
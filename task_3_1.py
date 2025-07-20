import networkx as nx
import pandas as pd

G = nx.DiGraph()

edges = [
    ("Термінал 1", "Склад 1", 25),
    ("Термінал 1", "Склад 2", 20),
    ("Термінал 1", "Склад 3", 15),
    ("Термінал 2", "Склад 3", 15),
    ("Термінал 2", "Склад 4", 30),
    ("Термінал 2", "Склад 2", 10),
    ("Склад 1", "Магазин 1", 15),
    ("Склад 1", "Магазин 2", 10),
    ("Склад 1", "Магазин 3", 20),
    ("Склад 2", "Магазин 4", 15),
    ("Склад 2", "Магазин 5", 10),
    ("Склад 2", "Магазин 6", 25),
    ("Склад 3", "Магазин 7", 20),
    ("Склад 3", "Магазин 8", 15),
    ("Склад 3", "Магазин 9", 10),
    ("Склад 4", "Магазин 10", 20),
    ("Склад 4", "Магазин 11", 10),
    ("Склад 4", "Магазин 12", 15),
    ("Склад 4", "Магазин 13", 5),
    ("Склад 4", "Магазин 14", 10),
]

for u, v, c in edges:
    G.add_edge(u, v, capacity=c)

G.add_node("Джерело")
G.add_edge("Джерело", "Термінал 1", capacity=float("inf"))
G.add_edge("Джерело", "Термінал 2", capacity=float("inf"))

G.add_node("Сток")
for i in range(1, 15):
    G.add_edge(f"Магазин {i}", "Сток", capacity=float("inf"))

flow_value, flow_dict = nx.maximum_flow(G, "Джерело", "Сток")

result = []
for terminal in ["Термінал 1", "Термінал 2"]:
    for warehouse in G.successors(terminal):
        for shop in G.successors(warehouse):
            flow = flow_dict[warehouse].get(shop, 0)
            if flow > 0:
                result.append({
                    "Термінал": terminal,
                    "Магазин": shop,
                    "Фактичний Потік (одиниць)": flow
                })

df = pd.DataFrame(result)
print(df)

print(f"\nЗагальний максимальний потік: {flow_value} одиниць")

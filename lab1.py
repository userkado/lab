import networkx as nx
import matplotlib.pyplot as plt

# Создаем граф сети
G = nx.Graph()

# Добавляем маршрутизаторы (узлы)
routers = ['R1', 'R2', 'R3', 'R4']
G.add_nodes_from(routers)

# Добавляем каналы (ребра) между маршрутизаторами с указанием стоимости (метрики)
G.add_edge('R1', 'R2', weight=10)
G.add_edge('R1', 'R3', weight=15)
G.add_edge('R2', 'R4', weight=12)
G.add_edge('R3', 'R4', weight=10)

# Визуализация топологии сети
pos = nx.spring_layout(G)
plt.figure(figsize=(8, 6))

# Отображаем граф топологии сети
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Network Topology")
plt.show()

# Функция для расчета кратчайшего пути с использованием алгоритма Дейкстры
def calculate_shortest_path(graph, source):
    shortest_paths = nx.single_source_dijkstra_path_length(graph, source, weight='weight')
    return shortest_paths

# Симуляция OSPF: расчёт кратчайших путей от маршрутизатора R1 до всех остальных
source_router = 'R1'
shortest_paths = calculate_shortest_path(G, source_router)

# Вывод результатов
print(f"Kратчайшие пути от маршрутизатора {source_router}:")
for target, distance in shortest_paths.items():
    print(f"До маршрутизатора {target}: {distance}")

# Визуализация кратчайших путей
plt.figure(figsize=(8, 6))

# Отображаем весь граф снова
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10, font_weight='bold')

# Выделяем кратчайшие пути от R1 до остальных маршрутизаторов
shortest_path_edges = []
for target in shortest_paths.keys():
    if target != source_router:  # Исключаем сам маршрут до R1
        path = nx.shortest_path(G, source=source_router, target=target, weight='weight')
        path_edges = list(zip(path, path[1:]))  # Получаем список ребер кратчайшего пути
        shortest_path_edges.extend(path_edges)

# Рисуем кратчайшие пути на графике
nx.draw_networkx_edges(G, pos, edgelist=shortest_path_edges, edge_color='red', width=3)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title(f"Kратчайшие пути от маршрутизатора {source_router}")
plt.show()

"""
310. Minimum Height Trees
(Medium complexity)

A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
"""


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [set() for _ in range(n)]  # граф
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        leav = [v for v in range(n) if len(graph[v]) <= 1]  # массив текущие листья
        prev_leav = leav  # массив предыдущие листья
        while leav:  # пока есть листья
            new_leav = []  # массив новые листья
            for lf in leav:  # проходим по текущим листьям
                if not graph[lf]:  # если текущий лист не соединен ни с кем - значит мы убрали листья, не корни для MHTs
                    return leav  # возвращаем текущие листья
                neig = graph[lf].pop()  # получаем соседа у текущего листа и убираем его
                graph[neig].remove(lf)  # убираем текущий лист у соседа, удаляем его из дерева
                if len(graph[neig]) == 1:  # если сосед стал листом - добавляем в новые листья
                    new_leav.append(neig)
            prev_leav, leav = leav, new_leav  # переходим к новым листьяем, усеченному дереву
        # если последние листья взаимноудалились- возвращаем их
        return prev_leav




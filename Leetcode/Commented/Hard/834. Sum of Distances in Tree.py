"""
834. Sum of Distances in Tree
(Hard complexity)

There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.
 """


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)  # граф
        for a, b in edges:  # добавляем значения в граф
            graph[a].append(b)
            graph[b].append(a)

        count = [1] * n  # текущее число узлов в поддереве
        ans = [0] * n  # ответ

        def dfs(node, par):  # dfs подсчитывает количество узлов в поддереве и сумму расстояний в поддереве
            for child in graph[node]:
                if child != par:
                    dfs(child, node)
                    count[node] += count[child]  # увеличиваем количество узлов в поддереве
                    ans[node] += ans[child] + count[child]  # увеличиваем расстояние в поддереве на расстояние у ребенка

        def dfs2(node, par):  # dfs2 корректирует ans, при движении корневого узла по дереву
            for child in graph[node]:
                if child != par:
                    # при движении корневого узла по дереву уменьшаем расстояние на число узлов в поддереве и увеличиваем на все оставшиеся узлы
                    ans[child] = ans[node] - count[child] + (n - count[child])
                    dfs2(child, node)

        dfs(0, -1)  # вызов dfs
        dfs2(0, -1)  # вызов dfs2
        # ответ
        return ans

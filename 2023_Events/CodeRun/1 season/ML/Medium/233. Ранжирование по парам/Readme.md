# Ранжирование по парам

ОИмеются 
�
n объектов: 
�
=
{
�
1
,
�
2
,
…
,
�
�
}
A={a 
1
​
 ,a 
2
​
 ,…,a 
n
​
 }. Для этих объектов известны результаты 
�
m попарных сравнений, заданных матрицей 
�
=
[
�
11
,
�
12
�
21
,
�
22
…
�
�
1
,
�
�
2
]
T= 
⎣
⎡
​
  
a 
11
​
 ,a 
12
​
 
a 
21
​
 ,a 
22
​
 
…
a 
m1
​
 ,a 
m2
​
 
​
  
⎦
⎤
​
 .

Элементы матрицы трактуются следующим образом: если при сравнении объектов 
�
�
a 
i
​
  и 
�
�
a 
j
​
  предпочтительнее оказался объект 
�
�
a 
i
​
 , то в 
�
T добавляется строка 
[
�
�
,
�
�
]
[ 
a 
i
​
 ,a 
j
​
 
​
 ]. Требуется построить скоринговую функцию 
�
:
�
→
�
f:A→R, максимизирующую правдоподобие правильного ранжирования пар. Скажем, что при заданной скоринговой функции объект 
�
�
a 
i
​
  оказывается предпочтительнее объекта 
�
�
a 
j
​
  с вероятностью
Тогда задача — построить функцию 
�
f, для которой значение функционала качества



достигает максимума. После построения скоринговой функции объекты можно отсортировать по убыванию предсказания:



Можно считать, что входные данные таковы, что предсказания оптимальной функции 
�
f гарантированно различны. Необходимо вывести номера объектов, упорядоченных по убыванию скоринговой функции.
## Формат ввода
Входной файл в первой строчке содержит два числа: 
�
n и 
�
m, 
1
≤
�
≤
1
0
2
1≤n≤10 
2
 , 
1
≤
�
≤
1
0
4
1≤m≤10 
4
 . Каждая из следующих 
�
m строчек содержит пару чисел 
1
≤
�
�
,
�
�
≤
�
1≤a 
i
​
 ,a 
j
​
 ≤n.


## Формат вывода
Выходной файл должен содержать перестановку чисел от 
1
1 до 
�
n, соответствующую оптимальной скоринговой функции.

### Пример 1
### Ввод
```text
5 10 
1 2 
2 3 
3 4 
4 5 
1 2 
2 1 
1 2 
2 1 
1 2 
1 2
```

### Вывод
```text
1 
2 
3 
4 
5
```

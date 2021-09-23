# algo-stduy

## 사용 언어

-   Python3
-   Javascript

## 학습 카테고리

-   (1) 문자열
-   (2) 자료구조
    -   스택&큐
    -   연결리스트
    -   그래프
-   (3) 최단거리
    -   다익스트라
    -   플로이드

## 문제 출처

-   [BOJ](https://www.acmicpc.net/)
-   [프로그래머스](https://programmers.co.kr/)
-   [코딩테스트 대비 문제집](https://github.com/tony9402/baekjoon)

## JS로 Pythonic하게 풀어보기..

### 1. indexing(first, idx, last)

-   String, Array

```js
const str = '12345';

console.log(str.slice(0)); // first
console.log(str.charAt(2)); // random idx
console.log(str.slice(-1)); // last
```

### 2. slicing

```python
# python
a = [1,2,3,4,5]
print(a[0:-1]); # [1,2,3,4]
```

```javascript
// js
const arr = [1, 2, 3, 4, 5];
console.log(arr.slice(0, -1));
```

### 3. list comprehension

```python
# python
size = 10
arr1 = [i * 2 for i in range(size)]
arr2 = [i for i in range(size) if i % 2 == 0]
```

```js
// js
const size = 10;
const arr1 = [...new Array(size).keys()].map((el) => el * 2);
const arr2 = [...new Array(size).keys()].filter((el) => el % 2 === 0);
```

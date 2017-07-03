# 632. Smallest Range
You have `k` lists of sorted integers in ascending order. Find the **smallest** range that includes at least one number from each of the k lists.

We define the range [a,b] is smaller than range [c,d] if `b-a < d-c` or `a < c` if `b-a == d-c`.

#### Example 1:
```
Input:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
```
#### Note:
1. The given list may contain duplicates, so ascending order means >= here.
2. 1 <= k <= 3500
3. $-10^5$ <= `value of elements` <= $10^5$.
4. **For Java users, please note that the input type has been changed to List<List<Integer>>. And after you reset the code template, you'll see this point.**
***

# 633. Sum of Square Numbers

Given a non-negative integer `c`, your task is to decide whether there're two integers `a` and `b` such that a2 + b2 = c.

#### Example 1:
```
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
```

#### Example 2:
```
Input: 3
Output: False
```
***

# 634. Find the Derangement of An Array
In combinatorial mathematics, a derangement is a permutation of the elements of a set, such that no element appears in its original position.

There's originally an array consisting of `n` integers from 1 to `n` in ascending order, you need to find the number of derangement it can generate.

Also, since the answer may be very large, you should return the output mod $10^9 + 7$.

#### Example 1:
```
Input: 3
Output: 2
Explanation: The original array is [1,2,3]. The two derangements are [2,3,1] and [3,1,2].
```
#### Note:
`n` is in the range of [1, $10^6$].
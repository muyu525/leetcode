# 628. Maximum Product of Three Numbers

Given an integer array, find three numbers whose product is maximum and output the maximum product.

#### Example 1:
```
Input: [1,2,3]
Output: 6
```
#### Example 2:
```
Input: [1,2,3,4]
Output: 24
```
#### Note:
The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
***

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
***
# 635. Design Log Storage System

You are given several logs that each log contains a unique id and timestamp. Timestamp is a string that has the following format: `Year:Month:Day:Hour:Minute:Second`, for example, `2017:01:01:23:59:59`. All domains are zero-padded decimal numbers.

Design a log storage system to implement the following functions:

`void Put(int id, string timestamp)`: Given a log's unique id and timestamp, store the log in your storage system.


`int[] Retrieve(String start, String end, String granularity)`: Return the id of logs whose timestamps are within the range from start to end. Start and end all have the same format as timestamp. However, granularity means the time level for consideration. For example, start = "2017:01:01:23:59:59", end = "2017:01:02:23:59:59", granularity = "Day", it means that we need to find the logs within the range from Jan. 1st 2017 to Jan. 2nd 2017.

#### Example 1:
```
put(1, "2017:01:01:23:59:59");
put(2, "2017:01:01:22:59:59");
put(3, "2016:01:01:00:00:00");
retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Year"); // return [1,2,3], because you need to return all logs within 2016 and 2017.
retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Hour"); // return [1,2], because you need to return all logs start from 2016:01:01:01 to 2017:01:01:23, where log 3 is left outside the range.
```

#### Note:
1. There will be at most 300 operations of Put or Retrieve.
2. Year ranges from [2000,2017]. Hour ranges from [00,23].
3. Output for Retrieve has no order required.
***
# 637. Average of Levels in Binary Tree
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

#### Example 1:
```
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
```
#### Note:
The range of node's value is in the range of 32-bit signed integer.
***
# 638. Shopping Offers
In LeetCode Store, there are some kinds of items to sell. Each item has a price.

However, there are some special offers, and a special offer consists of one or more different kinds of items with a sale price.

You are given the each item's price, a set of special offers, and the number we need to buy for each item. The job is to output the lowest price you have to pay for **exactly** certain items as given, where you could make optimal use of the special offers.

Each special offer is represented in the form of an array, the last number represents the price you need to pay for this special offer, other numbers represents how many specific items you could get if you buy this offer.

You could use any of special offers as many times as you want.
#### Example 1:
```
Input: [2,5], [[3,0,5],[1,2,10]], [3,2]
Output: 14
Explanation: 
There are two kinds of items, A and B. Their prices are $2 and $5 respectively. 
In special offer 1, you can pay $5 for 3A and 0B
In special offer 2, you can pay $10 for 1A and 2B. 
You need to buy 3A and 2B, so you may pay $10 for 1A and 2B (special offer #2), and $4 for 2A.
```
#### Example 2:
```
Input: [2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]
Output: 11
Explanation: 
The price of A is $2, and $3 for B, $4 for C. 
You may pay $4 for 1A and 1B, and $9 for 2A ,2B and 1C. 
You need to buy 1A ,2B and 1C, so you may pay $4 for 1A and 1B (special offer #1), and $3 for 1B, $4 for 1C. 
You cannot add more items, though only $9 for 2A ,2B and 1C.
```
#### Note:
1. There are at most 6 kinds of items, 100 special offers.
2. For each item, you need to buy at most 6 of them.
3. You are **not** allowed to buy more items than you want, even if that would lower the overall price.
***
# 639. Decode Ways II
A message containing letters from `A-Z` is being encoded to numbers using the following mapping way:
```
'A' -> 1
'B' -> 2
...
'Z' -> 26
```
Beyond that, now the encoded string can also contain the character '*', which can be treated as one of the numbers from 1 to 9.

Given the encoded message containing digits and the character '*', return the total number of ways to decode it.

Also, since the answer may be very large, you should return the output mod $10^9 + 7$.

#### Example 1:
```
Input: "*"
Output: 9
Explanation: The encoded message can be decoded to the string: "A", "B", "C", "D", "E", "F", "G", "H", "I".
```
#### Example 2:
```
Input: "1*"
Output: 9 + 9 = 18
```
#### Note:
1. The length of the input string will fit in range [1, 10^5].
2. The input string will only contain the character '*' and digits '0' - '9'.
# 640. Solve the Equation
Solve a given equation and return the value of `x` in the form of string "x=#value". The equation contains only '+', '-' operation, the variable `x` and its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value of `x` is an integer.
#### Example 1:
```
Input: "x+5-3+x=6+x-2"
Output: "x=2"
```
#### Example 2:
```
Input: "x=x"
Output: "Infinite solutions"
```
#### Example 3:
```
Input: "2x=x"
Output: "x=0"
```
#### Example 4:
```
Input: "2x+3x-6x=x+2"
Output: "x=-1"
```
#### Example 5:
```
Input: "x=x+2"
Output: "No solution"
```
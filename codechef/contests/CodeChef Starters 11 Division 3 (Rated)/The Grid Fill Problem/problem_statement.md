You are given a N × N grid. You need to fill each cell of the grid with 1 or −1. You need to fill the grid in a way such that the following conditions are met :-

For every column - (Sum of values present in the column) x (Product of values present in the column) < 0
For every row - (Sum of values present in the row) x (Product of values present in the row) < 0
It is guaranteed that there exists at least one way to fill the grid under given constraints such that both the conditions are satisifed. If there exists multiple ways to fill the grid by satisfying both the conditions, you can print any.

### Input Format
* First line will contain T, number of testcases. Then the testcases follow.
* Each testcase contains a single integer N
### Output Format
* For each test case, print the grid of size N × N . Print N lines where each line will contain N integers ( 1 or −1 ) separated by a space.

### Constraints
* 1≤T≤10
* 2≤N≤500

### Sample Input 1 
    2
    2
    3
### Sample Output 1 
    -1 -1
    -1 -1 
    1 -1 1
    -1 1 1
    1 1 -1
    
### Explanation
* Test Case 1: Consider the given output :
  * For each row, sum of the elements is −2.
  * For each column, sum of the elements is −2.
  * For each row, product of the elements is 1.
  * For each column, product of the elements is 1.
Clearly, both the conditions are satisfied.

* Test Case 2: Consider the given output :
  * For each row, sum of the elements is 1.
  * For each column, sum of the elements is 1.
  * For each row, product of the elements is −1.
  * For each column, product of the elements is −1.
Clearly, both the conditions are satisfied.

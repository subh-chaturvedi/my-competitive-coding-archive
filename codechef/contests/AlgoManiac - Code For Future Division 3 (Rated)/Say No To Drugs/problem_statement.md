There are N people participating in a race. The Nth participant is your friend, so you want him to win. You are not a man of ethics, so you decided to inject some units of a Performance Enhancement Drug (don't ask where that came from) in your friend's body.

From the charts, you came to know the speed of every player. Formally, for a player i, his speed is denoted by Si.
The change in speed with one unit of the drug is K units. Note that K can be negative, which means the drug has more side effects than benefits.
Of course, there will be a drug test before the race, so your friend will be caught if the number of units of the drug in his blood is greater than or equal to L.
You need to determine whether you can help your friend to win the race (with or without drugs), without getting caught.

Note: A player wins the race if he has the maximum speed among all the participants. If there are more than one people with a maximal speed, they tie at first place, and no one wins!

### Input Format
* First line will contain a single integer T, the number of test cases. Description of the test cases follows.
* First line of each test case will contain three space-separated integers, N - the number of participants, K - the change in speed with one unit of the drug, and L - minimum units of the drug that can be detected in the drug test.
* Second line of each test case will contain N space-separated integers Si, the speeds of the participants.
### Output Format
For each test case print "Yes" if you can help your friend to win the race, otherwise "No" in a single line.

### Constraints
* 1≤T≤200
* 1≤N,L≤1000
* −1000≤K≤1000
* 1≤Si≤1000

### Sample Input 1 
    3
    4 2 2
    2 1 3 2
    4 2 2
    2 1 4 2
    3 -10 100
    12 11 9
### Sample Output 1 
    Yes
    No
    No

### Explanation
* In test case 1, initial speeds are {2,1,3,2}. You can inject 1 unit of the drug into your friend's body, and increase his speed from 2 to 4. 4 is the fastest speed, thus you helped your friend win the race. Hence, the answer is "Yes".
* In test case 2, initial speeds are {2,1,4,2}. You can inject 1 unit of the drug into your friend's body, and increase his speed from 2 to 4. But you can not inject any more units of the drug, and with speed 4 your friend can only tie at rank 1 and not Win. Hence, the answer is "No".
* In test case 3, initial speeds are {12,11,9}. Note that the impact of the drug in this case is negative, which means that the speed will only decrease if you inject it. So, there is no way you can help your friend to win. Hence, the answer is "No".

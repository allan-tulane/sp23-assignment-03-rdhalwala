# CMPS 2200 Assignment 3
## Answers

**Name:**___Raiya Dhalwala________________


Place all written answers from `assignment-03.md` here for easier grading.






- **b.**
*I think these are wrong*
Work: W(n) just increases with input list
Span:S(n) no parallel

The work and span big Oh is O(n) which is linear because the function is dependent on the size of the input list.


- **d.**
Work:map is n/p 
scan is log(n/p) bc recursively divides
reduce is also log(n/p)
W(n/p+2log(n/p))
Span:is the same but we take the longest one
S(log(n/p))



- **f.**
Work:
First you divide which takes O(1)
Then you take two recursive calls from the half lists
2W(n/2)

So work is 2W(n/2) + 1

Span is very similar
First you divide which takes O(1)
Then you take two recursive calls from the half lists
2W(n/2)
So the span is the longer/max of these two
max(O(1), 2W(n/2))

Big O for Work
2W(n/2) + 1
c=0, c<lo22
logv22 = 1
O(nlog22) = O(n)

Big O for Span
Parallel recursive calls dividing by 2 each time
O(logn)
# Instagram_contest_scraper
My friend competed in an Instagram contest so I made this script to count the votes.

## Overview
In the contest thpostere were three images in a  labeled 1 -> 3. People submitted their votes by typing 
the number of their favorite submission in the comments.

## Problem
As you can imagine, if my friend wanted to see if he was in the lead for votes, he would have to manually count 1k+ comments and keep track of them.

# How this works
This script utilizes Selenium for automation to click through the 'more comments' box and BeautifulSoup4 for collecting the votes. For comments that have more than just the numbers: '1', '2', or '3' the script will parse the comment into a string then go through each index until it finds the vote. This is not completely accurate as some comments will have multiple votes which shouldn't be counted. This can easily be solved in the next push by throwing out comments that vote more than once. The script stores each vote into an array and when it's done counting all the comments will graphically display the vote distribution on a nice bar graph. 

# Result
My friend won the contest and we actually forecasted his victory a couple days in advanced based on the rate at which he was garning votes.

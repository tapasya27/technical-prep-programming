# 💻Technical prep programming 💻

## NeetCode 150 Solutions Repository

This repository contains my solutions to the famously known **NeetCode 150** questions, a curated set of problems aimed at technical interview preparations. 
Feel free to explore, contribute, or suggest optimizations. 

## Strategies:

### Arrays and Hashing
1. Unique element in a list -> Whenever encountering a need to find a unique element, think if a set can be utilised over sorting as sets are optimised structures that only hold unique elements. They also save on space complexity as a set will occupy a maximum of O(n) space whereas sorting will take O(n log n) 

2. Counting -> Whenever in a requirement to count anything, see if a dictionary can be used to save frequencies of letters. Lookup is only O(1) as well.

3. Two sum/tracking indices -> The key to this problem is a hash map or a dictionary. We must remember that since a solution is unique, there will be a unique number that equates to the target minus the index. We also have to make sure we keep track of the indices we have seen by adding them to a hashmap. 

4. Group Anagrams -> Alot of new learnings. Default dict for all empty values in a list, tuple is hashable but dictionary is not. This is important to think when storing any data structure as the key. Ord to find values and doing a minus ord("a") which is the ASCII value gives the alphaet index in terms of 26 letters


# Longest Common Subsequence Problem
CSCI_6212_12(Friday section) Team 4

## Problem Description
Given two strings (sequences of characters), the longest common subsequence (LCS) problem is to find the longest subsequence (not necessarily contiguous) that exists in both of the input strings. For example, given strings “mangoes” and “mementos”, the subsequence “mnos” is common in both and is, in fact, the longest common subsequence. Given two strings of sizes n1 and n2 respectively, the goal is to find a dynamic programming algorithm to find the longest common subsequence in O(n1 * n2) time complexity.

## Solution Overview
This repository contains a Python implementation of a dynamic programming algorithm to solve the Longest Common Subsequence problem. The `longestCommonSubsequence` function in the provided Python script calculates the length of the longest common subsequence between two input strings.

## Implementation Details
The `longestCommonSubsequence` function uses dynamic programming to compute the length of the LCS. The function takes two input strings as arguments and returns the length of their longest common subsequence.

## Running the Tests

To run the tests, execute the following command in your terminal or command prompt:

```bash
python3 lcs.py


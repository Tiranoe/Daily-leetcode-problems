#13. Roman to Integer

# Given a roman numeral, convert it to an integer.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# *note that 4, and 9 are IV, and IX and so on.

# Example
# Input: s = "III"
# Output: 3
# Explanation: III = 3.

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

def romanToInteger(s):
    rti = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }
    s = s.replace('IV','IIII').replace('IX', 'VIIII').replace('XL','XXXX').replace('XC', 'LXXXX').replace('CD','CCCC').replace('CM','DCCCC')
    sum = 0
    for char in s:
        sum += rti.get(char)
    print(sum)

#leetcode accetped solution
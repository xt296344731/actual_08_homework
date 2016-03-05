#!/usr/bin/python27
#encoding=utf-8
#
NumList = [1,2,-3,2,65535,12,3,-1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]

max1 = None
max2 = None
for i in NumList:
    if i > max1:
        tmp = max1
        max1 = i
        i = tmp
    if max1 > max2:
        max1,max2 = max2,max1

print max1
print max2
         


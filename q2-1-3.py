s = "azcbobobegghakl"
num=0
maxnum=0
pos=0
for i in range(0,len(s)):
    j=i
    num=1
    while  (j+1<len(s)) and (s[j+1]>=s[j]):
        num+=1
        j+=1
    if num>maxnum :
        maxnum=num
        pos=i
print("Longest substring in alphabetical order is: "+s[pos:pos+maxnum])

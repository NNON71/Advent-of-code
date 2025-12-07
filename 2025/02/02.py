test_case = [
    '11-22','95-115','998-1012','1188511880-1188511890','222220-222224',
    '1698522-1698528','446443-446449','38593856-38593862','565653-565659',
    '824824821-824824827','2121212118-2121212124']


ans = [] 

def find_pattern(number) :
    s = str(number)
    for i in range(1, len(s)//2 + 1) :
        pattern = s[:i]
        length = len(pattern)
        flag = True
        for j in range(i, len(s), length) :
            if s[j:j+length] != pattern :
                flag = False
                break
        if flag :
            return True
        
for line in test_case:
    a, b = map(int, line.split('-'))
    for num in range(a, b+1) :
        if find_pattern(num) :
            ans.append(num)
            
print(ans)
print(sum(ans))
    
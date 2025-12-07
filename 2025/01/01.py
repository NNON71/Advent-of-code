with open('./input.txt', 'r') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]  

# print(lines) 
test_case = [
    'L68',
    'L30',
    'R48',
    'L5',
    'R60',
    'L55',
    'L1',
    'L99',
    'R14',
    'L82',
]

pointing = 50
ans = 0

for text in lines:
    turn = text[0]
    degree = int(text[1:])
    
    
    if turn == 'L' :
        while degree > 0 : 
            pointing -= 1
            degree -= 1
            if pointing < 0 : 
                pointing = 99
            if pointing == 0 : 
                ans += 1
    else : 
        while degree > 0 : 
            pointing += 1
            degree -= 1
            if pointing > 99 : 
                pointing = 0
            if pointing == 0 : 
                ans += 1
                
                
    # if turn == 'L' : 
    #     direction = pointing - degree
    #     if direction < 0 and pointing != 0 : ans += 1
    #     pointing = direction % 100
        
    # else : 
    #     direction = pointing + degree
    #     if direction > 100 and pointing != 0 : ans += 1
    #     pointing = direction % 100
    # ans += 1 if pointing == 0 else 0
    # print(f'turn: {turn}, degree: {degree}, pointing: {pointing}, ans: {ans}')
    
print(ans)
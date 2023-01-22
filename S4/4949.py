import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline

def checkBrackets(statement):
    stack = []
    for ch in statement:  
        if ch in ('{', '[', '('):
            stack.append(ch)
        elif ch in ('}', ']', ')'):
            if len(stack)==0 :
                return False  #조건2위반  스택 공백 오류
            else :
                left = stack.pop() #오류 검색  } 이고 } 이면 오류
                if (ch == "}" and left != "{") or \
                   (ch == "]" and left != "[") or \
                   (ch == ")" and left != "(") :
                    return False  #조건3위반
    return len(stack)==0    #조건 1위반

while True:
    stack = list(str(input().rstrip()))
    if stack == ["."]:
        break
    result = checkBrackets(stack)
    print("yes" if result else "no")
    

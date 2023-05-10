"""
여러분들은 새로운 컴퓨터를 만들고 8바이트 단위로 관리하는 타입별 메모리 관리 방식을 시뮬레이션하려고 합니다.
지원하는 타입별 크기는 다음과 같습니다.
BOOL 1바이트
SHORT 2바이트
FLOAT 4바이트
INT 8바이트
LONG 16바이트

매개변수 param0에 타입들을 입력한 순서대로 메모리를 할당한 결과를 8바이트 단위로 구분해서 return해주는 solution 함수를 작성하세요.
단, BOOL을 제외한 8바이트보다 작은 타입들이 연속될 경우에는 사이에 패딩(.)을 붙여야 합니다.
SHORT는 2배수, FLOAT는 4배수가 되도록 메모리를 할당해야 합니다.
예를 들어 BOOL 타입 이후에 BOOL 타입은 바로 붙어서 할당할 수 있습니다. 
 "BOOL", "BOOL" → "##......"
그렇지만 BOOL 타입 이후에 SHORT, FLOAT를 할당하기 위해서는 각각 1개, 3개 패딩을 붙여야 합니다.
"BOOL", "SHORT" → "#.##...."
"BOOL", "FLOAT" → "#...####"
"BOOL", "SHORT", "FLOAT" → "#.######"
BOOL 타입 이후에 크기가 8바이트 이상인 타입은 7개 패딩을 붙여야 합니다.
"BOOL", "INT" → "#.......,########"
BOOL과 마찬가지로 8바이트보다 작은 SHORT, FLOAT도 뒤에 패딩을 붙여야 합니다.
"SHORT", "BOOL" → "###....."
"FLOAT", "SHORT" → "######.."
제한 사항
입력 타입은 1개 이상, 100개 이하까지만 가능합니다.
출력하는 메모리 최대 크기는 128바이트를 기준으로 동작합니다. 따라서 128바이트보다 큰 메모리 할당은 불가능합니다.
만약 타입 하나라도 더 이상 할당할 수 없는 경우는 "HALT"를 리턴합니다.
"""


def solution(arr):
    memory = []
    mes = ""
    for i in range(0, len(arr)):
        # 마지막이면 나머지 공간에 .부여
        idx = i
        i = arr[i]
        print(mes)
        print(memory)
        if i == "BOOL":
            mes += "#"
            if idx == len(arr)-1:
                mes = sudo_push(mes, memory)

                continue
        elif i == "SHORT":
            if len(mes) <= 2 and len(mes) >= 1:
                mes += "."
            mes += "##"
            if idx == len(arr)-1:
                mes = sudo_push(mes, memory)
                continue
        elif i == "FLOAT":
            if len(mes) < 4 and len(mes) >= 2:
                mes += ".."
            mes += "####"
            if idx == len(arr)-1:
                mes = sudo_push(mes, memory)
                continue
        if len(mes) == 8:
            memory.append(mes)
            mes = ""
        if i == "INT":
            if len(mes) > 0:
                mes = sudo_push(mes, memory)
            memory.append("########")
        elif i == "LONG":
            if len(mes) > 0:
                mes = sudo_push(mes, memory)
            memory.append("########")
            memory.append("########")
    print(memory)
    if len("".join(memory)) > 128:
        return "HART"
    return memory


def sudo_push(mes, memory):
    count = 8 - len(mes)
    mes += "."*count
    memory.append(mes)
    return ""


print(solution(["INT", "INT", "BOOL", "SHORT", "LONG"]))
print(solution(["INT", "SHORT", "FLOAT", "INT", "BOOL"]))
print(solution(["FLOAT", "SHORT", "BOOL", "BOOL", "BOOL", "INT"]))
print(solution(["BOOL", "LONG", "SHORT", "LONG", "BOOL",
      "LONG", "BOOL", "LONG", "SHORT", "LONG", "LONG"]))
"""
➡️ return "########,########,#.##....,########,########"
➡️ return "########,##..####,########,#......."
➡️ return "########,#.......,########"
➡️ return "HALT"
입출력 예 설명
1. BOOL 이후에 SHORT 선언해서 1바이트 패딩,
    SHORT 이후에 LONG 선언해서 4바이트 패딩
2. SHORT 이후에 FLOAT 선언해서 2바이트 패딩,
    마지막에 BOOL이 나와서 7바이트 패딩
3. FLOAT 이후에 SHORT 선언, SHORT 이후 BOOL, BOOL 두 번 선언해서 8바이트 가득 채움
    이후 BOOL 타입 선언으로 다음 영역에서 7바이트 패딩
4. BOOL 이나 SHORT 이후에 LONG 선언해서 8+16+8+16+8+16+8+16+8+16+16 = 136바이트
    메모리 최대 크기 128바이트를 넘기 때문에 HALT
"""
age = int(input("나이를 입력하세요:"))
if age >= 19:
    print("성인입니다")
    print("입장 제한이 없습니다.")
elif age >= 13:
    print("청소년입니다.")
    print("청소년 관람불가는 시청할 수 없습니다.")
else :
    print("어린이 입니다.")

print("나이 구분을 끝냅니다.")

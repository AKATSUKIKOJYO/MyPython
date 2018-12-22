age = int(input("나이를 입력하세요: "))

if age >= 18:
    print("성인입니다.")
    print("청소년 출입금지시간에 출입 가능합니다.")

if age < 18:
    print("청소년입니다.")
    print("청소년은 22시부터 09시까지 출입금지입니다.")

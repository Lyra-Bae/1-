# 3. 

students = {
    "전주원" : ["노래", "피아노"],
    "김기정" : ["영화", "음주"],
    "박동하" : ["운동", "게임"],
    "배희은" : ["시골", "게임"]
}

show = False

while not show:
    name_input = input("이름을 입력하세요: ")

    print(students[f"{name_input}"])
    continue_input = input("계속하시겠습니까?(y/n): ")
    continue_input.lower()

    if continue_input == 'y':
        pass
    elif continue_input == 'n':
        exit()
    else:
        print('\n입력 값을 확인해주세요.')
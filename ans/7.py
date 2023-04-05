# # 7.
# ### ✅7번
# *movies.py* 의 Movie 클래스와 Cinema 클래스를 상속받는 *RandomMovie 클래스*를 만들고 새로운 함수를 추가해봅시다.
# 함수의 이름은 RandomCinema이고, 다음과 같이 하나의 영화를 입력하면 영화관을 무작위로 짝지어 출력해야합니다!<br>
# **🤔 random 모듈**을 이용해주세요
# 단, 모든 과정은 *7.py*에서 이뤄져야합니다.
# <br>
# # class RandomCinema():

# from movies import *
import random

cinema_1=Cinema()

class RandomMovie(Movie, Cinema):
    def __init__(self, name, genre, produce):
        self.name = name
        self.genre = genre
        self.produce = produce

    def RandomCinema(self):
        cinema_1=Cinema()
        random_number=random.randint(1,100)
        c=random_number%3
        print(cinema_1.cinema_list[c])

movie_1=RandomMovie('a','a','a')   
name_1=input("영화제목을 입력하세요")
movie_1.new(name_1,"ss","ss")
movie_1.RandomCinema()
# random_1=RandomMoive("어벤져스","액션","marvel")
# random_2=RandomMoive("7번방의 선물","가족","cj")
# random_3=RandomMoive("레미제라블","드라마","fddfd")
# random_4=RandomMoive("스즈메의 문단속","애니","1231")


    
    






import os
import pygame
import datetime

# 기본색깔 설정
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (128, 0, 0)
blue = (000, 000, 255)
white = (255, 255, 255)
black = (0, 0, 0)
###########################################################################################################

# 텍스트 관련 객체를 만들 때 쓰는 클래스


class Caption:
    # 텍스트 생성 시 모든 정보(크기, 입력할 글, 폰트, 색깔, 위치) 입력
    def __init__(self, size, text, pos, font='BMJUA_ttf.ttf', color=black):
        self.__text = text
        self.__size = size
        self.__font = font
        self.__color = color
        self.__pos = pos

    # 텍스트 그리기
    def write_caption(self):

        if type(self.__text) == str:    # 한 줄 렌더 시
            caption_font = pygame.font.Font(self.__font, self.__size)
            final_caption = caption_font.render(
                self.__text, True, self.__color)
      
        else:                           # 여러 줄 렌더 시(size, text, pos, color 모두 튜플형태로 가져와야함)
            for i in range(0, len(self.__text)):
                caption_font = pygame.font.Font(self.__font, self.__size[i])
                final_caption = caption_font.render(
                    self.__text[i], True, self.__color[i])
                screen.blit(final_caption, self.__pos[i])

# 그림 관련 객체를 만들때 쓰는 클래스


class Png:

    # 그림 객체 생성 시 이미지와 위치 입력
    def __init__(self, object, pos):
        self.__png_information = {
            'object':   object,
            'pos':   pos
        }

    # 그림 객체 그리기
    def draw_Png(self):
        screen.blit(
            self.__png_information['object'], self.__png_information['pos'])


###########################################################################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()

# 화면 크기 설정
screen_width = 400  # 화면 가로 크기
screen_height = 800  # 화면 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('MOBA.IL STUDY')

# FPS
clock = pygame.time.Clock()


# 배경 생성
pygame.draw.rect(screen, white, [0, 0, screen_width, screen_height])
###########################################################################################################
# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
# 텍스트 객체 정의
d_day_exam_caption_x_pos = 20
d_day_exam_caption_y_pos = 80
d_day_exam_caption = Caption(
    size=(20, 20), text=("1학기 중간고사", "D-30"), pos=((d_day_exam_caption_x_pos, d_day_exam_caption_y_pos),
                                                   (d_day_exam_caption_x_pos, d_day_exam_caption_y_pos+20)), color=(black, black))          # 조건문 작성 필요
# 텍스트 객체 생성
d_day_exam_caption.write_caption()


# 이미지 객체 정의
# 시작할때 제목
starting_caption_object = pygame.image.load(
    'C:\\Users\\user\\Desktop\\coding\\pygame\\pygame_project_oracsil_game\\starting_caption.png')

starting_caption = Png(object=starting_caption_object, pos=(0, 0))

# 미오튜터
mio_object = pygame.image.load(
    'C:\\Users\\user\\Desktop\\coding\\pygame\\pygame_project_oracsil_game\\미오.png')
# 화면 전체크기의 객체가 아니기 때문에 사이즈 등의 지정이 필요
mio_rect = mio_object.get_rect().size
mio_width = mio_rect[0]
mio_height = mio_rect[1]
mio_x_pos = (screen_width - mio_width) / 2
mio_y_pos = screen_height - mio_height

mio = Png(object=mio_object, pos=(mio_x_pos, mio_y_pos))

weapon = pygame.image.load(
    'C:\\Users\\user\\Desktop\\coding\\pygame\\pygame_project_oracsil_game\\weapon.png')
weapon_rect = weapon.get_rect().size
weapon_width = weapon_rect[0]
weapon_height = weapon_rect[1]
weapon_x_pos = 0
weapon_y_pos = 0


# 캐릭터 이동방향
character_to_x = 0

# 캐릭터 이동속도
character_speed = 0.2


# 무기 이동 속도
weapon_speed = 0.3


# 이벤트 루프
running = True
while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:  # 창이  닫히는 이벤트가 발생하였는가?
            running = False  # 게임 진행중이 아님
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pass
            elif event.key == pygame.K_RIGHT:
                pass
            elif event.key == pygame.K_SPACE:
                pass

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                pass
            elif event.key == pygame.K_RIGHT:
                pass

    # 3. 게임 캐릭터 위치 정의
    # 5. 화면에 그리기
    starting_caption.draw_Png()
    mio.draw_Png()

    pygame.display.update()  # 게임화면을 다시 그리기!

 # 4. 충돌 처리
    # 정의한 폰트로 쓰고싶은 글을 쓸 때


pygame.display.update()


pygame.time.delay(2000)
# pygame 종료
pygame.quit()

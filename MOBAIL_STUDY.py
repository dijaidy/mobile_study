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

# 기본 초기화
pygame.init()

# 화면 크기 설정
screen_width = 400  # 화면 가로 크기
screen_height = 800  # 화면 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("MOBA.IL STUDY")

# FPS
clock = pygame.time.Clock()


# 배경 생성
pygame.draw.rect(screen, white, [0, 0, screen_width, screen_height])

###########################################################################################################

# 텍스트 관련 객체를 생성하는 클래스


class Caption:
    # 텍스트 생성 시 모든 정보(크기, 입력할 글, 폰트, 색깔, 위치) 입력
    def __init__(self, text, pos, size, font="BMJUA_ttf.ttf", color=black):
        self.__text = text
        self.__size = size
        self.__font = font
        self.__color = color
        self.__pos = pos

    # 텍스트 그리기
    def write_caption(self):

        if type(self.__text) == str:  # 한 줄 렌더 시
            caption_font = pygame.font.Font(self.__font, self.__size)
            final_caption = caption_font.render(self.__text, True, self.__color)
            screen.blit(final_caption, self.__pos)

        else:  # 여러 줄 렌더 시(size, text, pos, color 모두 튜플형태로 가져와야함)
            for i in range(0, len(self.__text)):
                caption_font = pygame.font.Font(self.__font, self.__size[i])
                final_caption = caption_font.render(self.__text[i], True, self.__color[i])
                screen.blit(final_caption, self.__pos[i])


class BigCategory(Caption):

    # 초기 활성화된 카테고리는 없음
    activated_category = 0  # 입력받아야함
    deactivated_font_size = 0  # 입력받아야함

    activated_font_size = 25  # 상수 변수

    def __init__(
        self,
        text,
        pos,
        link_to_small_category,
        box_pos_and_size,
        size=20,
        font="BMJUA_ttf.ttf",
        color=white,
    ):
        super().__init__(text, size, font, color, pos)
        self.__link = link_to_small_category  # 하위카테고리를 연결
        self.__box_pos_and_size = box_pos_and_size

        # 처음 정의되는 큰 카테고리에 대한 작업
        if BigCategory.activated_category == 0:  # 아직 활성화된 카테고리 없으면
            BigCategory.activated_category = self  # 처음 정의되는 객체를 활성화(기존의 객체 자체가 변화함(파괴적임))
            BigCategory.deactivated_font_size = self.__size  # 기존의 폰트 사이즈 미리 저장
            BigCategory.activated_category.__size = BigCategory.activated_font_size  # 글씨크기는 키우고
            BigCategory.activated_category.__link.present_small_category()  # 큰 카테고리 아래의 작은 카테고리를 표시

    def activate_category(self):
        # 기존의 활성화 카테고리에 대한 작업
        BigCategory.activated_category.__size = BigCategory.deactivated_font_size  # 글씨크기 원래대로

        # 새 활성화 카테고리에 대한 작업
        BigCategory.activated_category = self  # 객체를 활성화(기존의 객체 자체가 변화함(파괴적임))
        BigCategory.activated_category.__size = 25  # 글씨크기는 키우고

    def write_caption(self):
        # 큰 카테고리 그림
        if type(self.__text) == str:  # 한 줄 렌더 시
            caption_font = pygame.font.Font(self.__font, self.__size)
            final_caption = caption_font.render(self.__text, True, self.__color)
            screen.blit(final_caption, self.__pos)

        else:  # 여러 줄 렌더 시(size, text, pos, color 모두 튜플형태로 가져와야함)
            for i in range(0, len(self.__text)):
                caption_font = pygame.font.Font(self.__font, self.__size[i])
                final_caption = caption_font.render(self.__text[i], True, self.__color[i])
                screen.blit(final_caption, self.__pos[i])

        # 현재 객체가 활성화된 객체면
        if BigCategory.activated_category == self:
            for i in range(0, len(self.__link.__text)):  # 큰 카테고리에 연결된 작은 카테고리 그림
                caption_font = pygame.font.Font(self.__link.__font, self.__link.__size[i])
                final_caption = caption_font.render(
                    self.__link.__text[i], True, self.__link.__color[i]
                )
                screen.blit(final_caption, self.__link.__pos[i])
            # 활성화된 큰 카테고리의 위치에 활성상태를 표시하는 박스 그림
            pygame.draw.rect(screen, blue, self.__box_pos_and_size)  # 튜플 형태의 박스에 대한 위치, 사이즈 정보


class SmallCategory(Caption):
    def __init__(self, text, pos, size=10, font="BMJUA_ttf.ttf", color=white):
        super().__init__(text, size, font, color, pos)

    def 안에_화면으로_넘기기(self):
        pass


# 그림 관련 객체를 만들때 쓰는 클래스
class Png:

    # 그림 객체 생성 시 이미지와 위치 입력
    def __init__(self, object, pos):
        self.__png_information = {"object": object, "pos": pos}

    # 그림 객체 그리기
    def draw_Png(self):
        screen.blit(self.__png_information["object"], self.__png_information["pos"])


###########################################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
# 텍스트 객체 정의
# 처음 dday 표시
d_day_exam_caption_x_pos = 20
d_day_exam_caption_y_pos = 80
d_day_exam_caption = Caption(
    size=(20, 20),
    text=("1학기 중간고사", "D-30"),
    pos=(
        (d_day_exam_caption_x_pos, d_day_exam_caption_y_pos),
        (d_day_exam_caption_x_pos, d_day_exam_caption_y_pos + 20),
    ),
    color=(black, black),
)  # 조건문 작성 필요

# 각 카테고리 제목


# 텍스트 객체 생성
d_day_exam_caption.write_caption()


# 이미지 객체 정의
# 시작화면 제목
starting_caption_object = pygame.image.load(
    "C:\\Users\\user\\Desktop\\내자료\\정보영재원\\MOBAIL_STUDY_prototype\\starting_caption.png"
)

starting_caption = Png(object=starting_caption_object, pos=(0, 0))

# 시작화면 배경
starting_screen_background_object = pygame.image.load(
    "C:\\Users\\user\\Desktop\\내자료\\정보영재원\\MOBAIL_STUDY_prototype\\starting_screen_background.png"
)

starting_screen_background = Png(object=starting_screen_background_object, pos=(0, 0))

# 미오튜터
mio_object = pygame.image.load(
    "C:\\Users\\user\\Desktop\\내자료\\정보영재원\\MOBAIL_STUDY_prototype\\미오.png"
)
# 화면 전체크기의 객체가 아니기 때문에 사이즈 등의 지정이 필요
mio_rect = mio_object.get_rect().size
mio_width = mio_rect[0]
mio_height = mio_rect[1]
mio_x_pos = (screen_width - mio_width) / 2
mio_y_pos = screen_height - mio_height

mio = Png(object=mio_object, pos=(mio_x_pos, mio_y_pos))


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
    starting_screen_background.draw_Png()

    pygame.display.update()  # 게임화면을 다시 그리기!

# 4. 충돌 처리
# 정의한 폰트로 쓰고싶은 글을 쓸 때


pygame.display.update()


pygame.time.delay(2000)
# pygame 종료
pygame.quit()

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
light_blue = (121, 220, 255)
light_green = (159, 255, 63)

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
each_scene_dict = {}


class Caption:
    caption_bundle_dict = {}
    # 텍스트 생성 시 모든 정보(크기, 입력할 글, 폰트, 색깔, 위치) 입력
    def __init__(
        self, text, pos, size, right_below_dot_pos=(0, 0), font="BMJUA_ttf.ttf", color=black
    ):
        # 일반 인스턴스 선언
        self.__text = text
        self.__size = size
        self.__font = font
        self.__color = color
        self.__pos = pos

        # 특수한 인스턴스 선언

        # 클릭을 체크하는 네모에 관한 정보
        self.click_checking_rect = (
            (pos[0], right_below_dot_pos[0]),
            (pos[1], right_below_dot_pos[1]),
        )

    # 텍스트 그리기
    def write_caption(self):

        caption_font = pygame.font.Font(self.__font, self.__size)
        final_caption = caption_font.render(self.__text, True, self.__color)
        screen.blit(final_caption, self.__pos)

    def sort_caption(self, scene_of_object, caption_bundle):
        # 어느 장면인지(ex:시작장면, 내교재찜하기 장면 등)
        if scene_of_object not in each_scene_dict:
            each_scene_dict[scene_of_object] = [self]
        else:
            each_scene_dict[scene_of_object].append(self)

        if caption_bundle not in Caption.caption_bundle_dict:
            Caption.caption_bundle_dict[caption_bundle] = [self]
        else:
            Caption.caption_bundle_dict[caption_bundle].append(self)


class BigCategory(Caption):

    # 초기 활성화된 카테고리는 없음
    activated_category = 0  # 입력받아야함
    deactivated_font_size = 0  # 입력받아야함

    activated_font_size = 25  # 상수 변수

    def __init__(
        self,
        text,
        pos,
        right_below_dot_pos=(0, 0),
        size=20,
        font="BMJUA_ttf.ttf",
        color=black,
    ):

        # 일반 인스턴스 선언
        self.__text = text
        self.__size = size
        self.__font = font
        self.__color = color
        self.__pos = pos

        self.click_checking_rect = (
            (pos[0], right_below_dot_pos[0]),
            (pos[1], right_below_dot_pos[1]),
        )

        # 작은 카테고리 링크 작업
        self.__linked_small_category = Caption.caption_bundle_dict[self.__text]

        # 처음 정의되는 큰 카테고리에 대한 활성화 작업
        if BigCategory.activated_category == 0:  # 아직 활성화된 카테고리 없으면
            BigCategory.activated_category = self  # 처음 정의되는 객체를 활성화(기존의 객체 자체가 변화함(파괴적임))
            BigCategory.deactivated_font_size = self.__size  # 기존의 폰트 사이즈 미리 저장
            BigCategory.activated_category.__size = BigCategory.activated_font_size  # 글씨크기는 키우기

    def activate_category(self):
        # 기존의 활성화 카테고리에 대한 작업
        BigCategory.activated_category.__size = BigCategory.deactivated_font_size  # 글씨크기 원래대로

        # 새 활성화 카테고리에 대한 작업
        BigCategory.activated_category = self  # 객체를 활성화(기존의 객체 자체가 변화함(파괴적임))
        BigCategory.activated_category.__size = 25  # 글씨크기는 키우고

    def write_caption(self):
        # 큰 카테고리 그림
        caption_font = pygame.font.Font(self.__font, self.__size)
        final_caption = caption_font.render(self.__text, True, self.__color)
        screen.blit(final_caption, self.__pos)

        # 현재 객체가 활성화된 객체면
        if BigCategory.activated_category == self:
            # 링크된 작은카테고리 표시
            for linked_small_category in self.__linked_small_category:
                linked_small_category.write_caption()
            # 활성화된 큰 카테고리의 위치에 활성상태를 표시하는 박스 그림
            pygame.draw.rect(
                screen,
                blue,
                [
                    self.__pos[0],
                    self.__pos[1],
                    self.click_checking_rect[0][1] - self.click_checking_rect[0][0],
                    self.click_checking_rect[1][1] - self.click_checking_rect[1][0],
                ],
            )  # 튜플 형태의 박스에 대한 위치, 사이즈 정보
            # self.click_checking_rect =((윗점x, 아랫점x), (윗점y, 아랫점y))


class SmallCategory(Caption):
    def __init__(
        self,
        text,
        pos,
        right_below_dot_pos=(0, 0),
        size=10,
        font="BMJUA_ttf.ttf",
        color=black,
    ):
        self.__text = text
        self.__size = size
        self.__font = font
        self.__color = color
        self.__pos = pos

        self.click_checking_rect = (
            (pos[0], right_below_dot_pos[0]),
            (pos[1], right_below_dot_pos[1]),
        )

    def write_caption(self):

        caption_font = pygame.font.Font(self.__font, self.__size)
        final_caption = caption_font.render(self.__text, True, self.__color)
        screen.blit(final_caption, self.__pos)

    def scene_transform(self):
        pass


# 그림 관련 객체를 만들때 쓰는 클래스
class Png:

    # 그림 객체 생성 시 이미지와 위치 입력
    def __init__(self, object, pos, parameter=(0, 0)):
        self.__object = object
        self.__pos = pos
        self.__click_checking_rect = (
            (pos[0], pos[0] + parameter[0]),
            (pos[1], pos[1] + parameter[1]),
        )

    # 그림 객체 그리기
    def draw_Png(self):
        screen.blit(self.__object, self.__pos)


###########################################################################################################
# 장면 나누기


# 텍스트 객체 정의
# 처음 dday 표시
if True:  # 시험기간이면
    d_day_exam_caption_x_pos_list = [20, 20]
    d_day_exam_caption_y_pos_list = [80, 100]
    d_day_exam_caption_text_list = ["1학기 중간고사", "D-30"]
    d_day_exam_caption_pos_list = [
        (d_day_exam_caption_x_pos_list[0], d_day_exam_caption_y_pos_list[0]),
        (d_day_exam_caption_x_pos_list[0], d_day_exam_caption_y_pos_list[1]),
    ]
    d_day_exam_caption_right_below_dot_pos_list = [(50, 100), (40, 120)]

    for i in range(0, 2):
        d_day_exam_caption = Caption(
            size=20,
            text=d_day_exam_caption_text_list[i],
            pos=d_day_exam_caption_pos_list[i],
            color=black,
            right_below_dot_pos=d_day_exam_caption_right_below_dot_pos_list[i],
        )
        d_day_exam_caption.sort_caption("start_scene", "d_day_exam_caption")
        d_day_exam_caption.write_caption()


# 큰 카테고리, 작은 카테고리 만들기
big_category_list = []
big_category_str_list = ["내교재 찜하기", "공부계획", "공부방", "커뮤니티", "현재성과"]

small_category_list = []
small_category_str_list = [
    ("교재검색", "찜한 교재 목록"),
    ("공부계획"),
    ("오늘의 공부", "학교수업 복습"),
    ("학교정보"),
    ("나의 성취도", "랭킹"),
]

# 작은 카테고리 위치
small_category_x_pos = 20
small_category_y_pos_list = [100, 120, 140, 160]
small_category_right_below_dot_pos_list = [(50, 120), (50, 140), (50, 160), (50, 180)]

caption_bundle_variable = 0
for small_category_str_tuple in small_category_str_list:
    for i in range(0, len(small_category_str_tuple)):  # 각각의 작은 카테고리에 대한 반복 작업
        small_category_pos_tuple = tuple(
            [
                (small_category_x_pos, small_category_y_pos_list[i])
                for i in range(0, len(small_category_str_tuple))
            ]  # 작은 카테고리 개수에 따라 위치정보 양을 달리함
        )  # 작은 카테고리의 위치정보
        small_category = SmallCategory(
            text=small_category_str_tuple[i],
            pos=small_category_pos_tuple[i],
            right_below_dot_pos=small_category_right_below_dot_pos_list[i],
            size=10,
        )  # 수정필요
        small_category.sort_caption("start_scene", big_category_str_list[caption_bundle_variable])
    caption_bundle_variable += 1


for i in range(0, len(big_category_str_list)):
    big_category_x_pos = ((screen_width / 5) * i) - 30
    big_category_y_pos = 50
    big_category = BigCategory(
        text=big_category_str_list[i], pos=(big_category_x_pos, big_category_y_pos)
    )
    big_category.sort_caption("start_scene", "big_category")
    big_category.write_caption()  # 빅 카테고리를 그리면, 연결된 작은 카테고리도 함께 그림


# 이미지 객체 정의
# 시작화면 제목
starting_caption_object = pygame.image.load(
    "C:\\Users\\user\\Desktop\\내자료\\정보영재원\\MOBAIL_STUDY_prototype\\starting_caption.png"
)

starting_caption = Png(object=starting_caption_object, pos=(0, 0))
each_scene_dict["start_scene"].append(starting_caption)

# 시작화면 배경
starting_scene_background_object = pygame.image.load(
    "C:\\Users\\user\\Desktop\\내자료\\정보영재원\\MOBAIL_STUDY_prototype\\starting_screen_background.png"
)

starting_scene_background = Png(object=starting_scene_background_object, pos=(0, 0))
each_scene_dict["start_scene"].append(starting_scene_background)

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


# 이벤트 루프
running = True
while running:
    dt = clock.tick(30)
    mouse_pos = pygame.mouse.get_pos()
    print(pygame.mouse.get_pos())

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?

        if event.type == pygame.QUIT:  # 창이  닫히는 이벤트가 발생하였는가?
            running = False  # 게임 진행중이 아님
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for object in each_scene_dict["start_scene"]:
                if type(object) == SmallCategory:  # 텍스트가 여러개이면(작은 카테고리)
                    if (
                        mouse_pos >= object.click_checking_rect[0][0]
                        and mouse_pos <= object.click_checking_rect[0][1]
                    ):
                        if (
                            mouse_pos >= object.click_checking_rect[1][0]
                            and mouse_pos <= object.click_checking_rect[1][1]
                        ):  # object를 클릭했으면
                            object.scene_transform()
                elif type(object) == BigCategory:  # 텍스트가 한개면(큰 카테고리)
                    if (
                        mouse_pos >= object.click_checking_rect[0][0]
                        and mouse_pos <= object.click_checking_rect[0][1]
                    ):
                        if (
                            mouse_pos >= object.click_checking_rect[1][0]
                            and mouse_pos <= object.click_checking_rect[1][1]
                        ):  # object를 클릭했으면
                            object.activate_category()

    # 3. 게임 캐릭터 위치 정의
    # 5. 화면에 그리기
    starting_caption.draw_Png()
    mio.draw_Png()
    starting_scene_background.draw_Png()

    pygame.display.update()  # 게임화면을 다시 그리기!

# 4. 충돌 처리
# 정의한 폰트로 쓰고싶은 글을 쓸 때


pygame.display.update()


pygame.time.delay(2000)
# pygame 종료
pygame.quit()

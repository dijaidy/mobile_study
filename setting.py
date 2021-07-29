import pygame

# cl 캡션
# cl 픽쳐
# cl 씬

# 기본 색깔 설정
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (128, 0, 0)
blue = (000, 000, 255)
white = (255, 255, 255)
black = (0, 0, 0)
light_blue = (121, 220, 255)
light_green = (159, 255, 63)

# pygame 실행과 관련된 기본 설정
def set_pygame():
    # 기본 초기화
    pygame.init()

    # 화면 크기 설정
    screen_width = 400  # 화면 가로 크기
    screen_height = 800  # 화면 세로 크기
    screen = pygame.display.set_mode((screen_width, screen_height))

    # 화면 타이틀 설정
    title = "Mobile Study"
    pygame.display.set_caption(title)

    # FPS
    clock = pygame.time.Clock()

    # 배경 생성
    pygame.draw.rect(screen, white, [0, 0, screen_width, screen_height])


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


# 그림 관련 객체를 만들때 쓰는 클래스
class Picture:

    # 그림 객체 생성 시 이미지와 위치 입력
    def __init__(self, object, pos, parameter=(0, 0)):
        self.__object = object
        self.__pos = pos
        self.__click_checking_rect = (
            (pos[0], pos[0] + parameter[0]),
            (pos[1], pos[1] + parameter[1]),
        )

    # 그림 객체 그리기
    def draw_Picture(self):
        screen.blit(self.__object, self.__pos)

class A:  #개인정보 저장, 반환, 접근
    def __init__(self, nickname, icon, birth, classroom, admin, aready):  #생성자
        self.__nickname=nickname
        self.__icon=icon
        self.__birth=birth
        self.__classroom=classroom
        self.__admin=admin
        self.__aready=aready
    
    def get_nickname(self):  #각각 객체들을 반환
        return self.__nickname
    def get_icon(self):
        return self.__icon
    def get_birth(self):
        return self.__birth
    def get_classroom(self):
        return self.__classroom
    def get_admin(self):
        return self.__admin
    def get_aready(self):
        return self.__aready
    
    def s_nickname(self, nickname):  #각각 객체들에 접근
        self.__nickname=nickname
    def s_icon(self, icon):
        self.__icon=icon
    def s_birth(self, birth):
        self.__birth=birth
    def s_classroom(self, classroom):
        self.__classroom=classroom
    def s_admin(self, admin):
        self.__admin=admin
    def s_aready(self, aready):
        self.__aready=aready

class A1 (A):  #개인정보 입력 받기
    def __init__(self, nickname, icon, birth, classroom, admin, aready):  #생성자
        super().__init__(nickname, icon, birth, classroom, admin, aready)
    def input (nickname, icon, birth, classroom, admin, aready):  #개인정보 입력
        if aready==False:
            pass  #처음 앱 설치 시(5번째 슬라이드) UI 보여주기
            self.s_nickname(nickname)
            self.s_icon(icon)
            self.s_birth(birth)
            self.s_classroom(classroom)
            self.s_
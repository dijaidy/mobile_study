import pygame

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
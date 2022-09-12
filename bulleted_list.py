from manim import *

PAN_CAMERA_DOWN = 0
PAN_CAMERA_LEFT = 0
DEFAULT_WIDTH = 8 * (16 / 9)
FRAME_WIDTH = 2 * DEFAULT_WIDTH


class BulletedListImproved(MovingCameraScene):
    def __init__(self, camera_class=MovingCamera):
        super().__init__(camera_class)
        self.frame = self.camera.frame
        self.number_plane = NumberPlane()
        self.title = None
        self.underline = None
        self.networks = None
        self.title_group = None

    def setup(self):
        MovingCameraScene.setup(self)
        self.frame.width = FRAME_WIDTH
        self.frame.move_to(PAN_CAMERA_LEFT * LEFT + PAN_CAMERA_DOWN * DOWN)
        # self.add(self.number_plane)
        self.number_plane.width = FRAME_WIDTH
        self.number_plane.move_to(PAN_CAMERA_LEFT * LEFT + PAN_CAMERA_DOWN * DOWN)

    # noinspection PyTypeChecker
    def construct(self):
        # Title
        title = Text("Example Networks", color=YELLOW)
        title.scale(1.2)
        title.to_edge(UP).shift(LEFT * 0 + DOWN * 0)

        # Title underline
        underline = Line(LEFT, RIGHT, color=YELLOW)
        underline.width = 1.1 * title.width
        underline.next_to(title, DOWN)
        underline.shift(UP * 0.1)

        self.play(FadeIn(title, shift=LEFT), GrowFromCenter(underline))
        self.wait(3)

        networks = Tex("Antennas", "Dummy Loads", "Filters", "Attenuators", "Circulators", "Isolators",
                       "Amplifiers")  # , height=5, width=5, dot_scale_factor=3.5)
        for network in networks:
            dot = MathTex("\\cdot").scale(3)
            dot.next_to(network[0], LEFT * 0.4, buff=0.4)
            network.add_to_back(dot)
        networks.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        # networks.set_color_by_tex("Antennas", WHITE)

        networks.scale(1.45)
        networks.next_to(underline, DOWN)
        networks.set_opacity(0.5)
        self.play(Write(networks))
        self.play(networks.submobjects[0].animate.set_opacity(1))


with tempconfig(
        {"quality": "high_quality", "preview": True, "disable_caching": False, "from_animation_number": 0}):
    scene = BulletedListImproved()
    scene.render()

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

    def setup(self):
        MovingCameraScene.setup(self)
        self.frame.width = FRAME_WIDTH
        self.frame.move_to(PAN_CAMERA_LEFT * LEFT + PAN_CAMERA_DOWN * DOWN)
        # self.add(self.number_plane)
        self.number_plane.width = FRAME_WIDTH
        self.number_plane.move_to(PAN_CAMERA_LEFT * LEFT + PAN_CAMERA_DOWN * DOWN)

    def construct(self):
        def create():
            self.title = Text("Example Networks", color=YELLOW)
            self.underline = Line(LEFT, RIGHT, color=YELLOW)
            self.networks = Tex("Antennas", "Dummy Loads", "Filters", "Attenuators", "Circulators", "Isolators",
                                "Amplifiers")
            for network in self.networks:
                dot = MathTex("\\cdot").scale(3)
                dot.next_to(network[0], LEFT * 0.4, buff=0.4)
                network.add_to_back(dot)

        def stage():
            self.title.scale(1.2)
            self.title.to_edge(UP).shift(LEFT * 0 + DOWN * 0)

            self.underline.width = 1.1 * self.title.width
            self.underline.next_to(self.title, DOWN)
            self.underline.shift(UP * 0.1)

            self.networks.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            self.networks.scale(1.45)
            self.networks.next_to(self.underline, DOWN)
            self.networks.set_opacity(0.5)

        def animate():
            self.play(FadeIn(self.title, shift=LEFT), GrowFromCenter(self.underline))
            self.play(Write(self.networks))
            self.play(self.networks.submobjects[0].animate.set_opacity(1))

        create()
        stage()
        animate()


with tempconfig({"quality": "high_quality", "preview": True, "disable_caching": False, "from_animation_number": 0}):
    scene = BulletedListImproved()
    scene.render()

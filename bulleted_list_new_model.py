from manim import *

PAN_CAMERA_DOWN = 0
PAN_CAMERA_LEFT = 0
DEFAULT_WIDTH = 8 * (16 / 9)
FRAME_WIDTH = 2 * DEFAULT_WIDTH


class BulletedListNewModel(MovingCameraScene):
    def __init__(self, camera_class=MovingCamera):
        super().__init__(camera_class)
        self.frame = self.camera.frame
        self.number_plane = NumberPlane()
        self.title = None
        self.dot = None

    def setup(self):
        MovingCameraScene.setup(self)
        self.frame.width = FRAME_WIDTH
        self.frame.move_to(PAN_CAMERA_LEFT * LEFT + PAN_CAMERA_DOWN * DOWN)
        self.add(self.number_plane)
        self.number_plane.width = FRAME_WIDTH
        self.number_plane.move_to(PAN_CAMERA_LEFT * LEFT + PAN_CAMERA_DOWN * DOWN)

    def construct(self):
        def create():
            self.dot = Dot()
            return

        def stage():
            self.add(self.dot)
            return

        def animate():
            self.play(self.dot.animate.move_to(2 * RIGHT))
            return

        create()
        stage()
        animate()


with tempconfig(
        {"quality": "high_quality", "preview": True, "disable_caching": False, "from_animation_number": 0}):
    scene = BulletedListNewModel()
    scene.render()

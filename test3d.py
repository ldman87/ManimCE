from manim import *

class ThreeDExample(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(x_range=[-4,4], x_length=8, y_range=[-4,4], y_length=8, z_range=[-3,3], z_length=6)
        x_label = axes.get_x_axis_label(Tex("x"))
        y_label = axes.get_y_axis_label(Tex("y"))
        z_label = axes.get_z_axis_label(Tex("z"))
        arrowx = Arrow3D(
            start=np.array([-4, 0, 0]),
            end=np.array([4, 0, 0]),
            resolution=16
        )
        arrowy = Arrow3D(
            start=np.array([0, -4, 0]),
            end=np.array([0, 4, 0]),
            resolution=16
        )
        arrowz = Arrow3D(
            start=np.array([0, 0, -4]),
            end=np.array([0, 0, 4]),
            resolution=16
        )
        group1 = VGroup(arrowx, arrowy, arrowz)
        surface = Surface(
        	lambda u, v: axes.c2p(v*np.cos(u), v*np.sin(u),0.5*v**2),
        	v_range=[0, 2.5],
            u_range=[0, 2*PI],
            resolution=150,
        ).fade(0.5)
        surface.set_style(fill_opacity=1,fill_color=PURPLE)
        text = Text("MẶT TRÒN XOAY",font="Arial").set_color_by_gradient(PINK,YELLOW).to_corner(DOWN)
        self.add_fixed_in_frame_mobjects(text)
        self.set_camera_orientation(zoom=0.5)
        self.play(FadeIn(group1), FadeIn(x_label), FadeIn(y_label), FadeIn(z_label))
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES, zoom=1, run_time=1.5)
        self.wait()
        self.play(Create(surface),run_time=4)
        self.wait()
        self.play(Write(text), run_time=2)
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(5)
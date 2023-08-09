from manim import *


class Intro(Scene):
    def construct(self):
        # Định nghĩa hình vuông, tam giác, đường tròn
        square = Square(color=RED).shift(LEFT * 2.5)	# Vị trí bên trái cách trung tâm 2.5 đơn vị
        triangle = Triangle(color=GREEN)				# Vị trí trung tâm
        circle = Circle(color=BLUE).shift(RIGHT * 2.5)	# Vị trí bên phải cách trung tâm 2.5 đơn vị

        # Hoạt cảnh 1: Vẽ hình vuông, tam giác, đường tròn
        self.play(Write(square), Write(triangle), Write(circle))

        # Hoạt cảnh 2: Di chuyển các hình
        self.play(
            square.animate.shift(UP),					# Di chuyển hình vuông lên trên 1 đơn vị
            triangle.animate.shift(DOWN * 0.5),			# Di chuyển tam giác xuống dưới 0.5 đơn vị
            circle.animate.shift(UP * 0.5+RIGHT*1)		# DI chuyển đường tròn lên trên 0.5 đơn vị và sang phải 1 đơn vị
        )

        # Hoạt cảnh 3: Xoay hình, tô nền
        self.play(
            square.animate.rotate(PI/2).set_fill(RED, 0.8),			# Xoay hình vuông một góc 90 độ và tô nền ĐỎ, độ trong suốt 80%
            triangle.animate.rotate(-2*PI/3).set_fill(GREEN, 0.5),	# Xoay hình tam giác một góc 120 độ và tô nền XANH LÁ, độ trong suốt 50%
            circle.animate.set_fill(BLUE, 0.8),							# Tô nền hình tròn bởi màu XANH BIỂN, độ trong suốt 80%
        )

        # Hoạt cảnh 4: Nhóm các đối tượng
        group = VGroup(square, triangle, circle)					# Nhóm 3 hình và đặt tên nhóm là group
        self.play(group.animate.scale(0.5).arrange(buff=2))			# Sắp xếp các phần tử trong nhóm group theo hàng ngang từ trái sang phải, khoảng cách các hình 2 đơn vị

        # Hoạt cảnh 5: Hoán đổi vị trí các hình
        self.play(Swap(square, triangle))
        self.play(Swap(square, circle, path_arc=160 * DEGREES))		# Hoán đổi hình vuông, hình tròn theo cung 160 độ.

        # Hoạt cảnh 6: Ẩn các hình
        self.play(
        	FadeOut(square), FadeOut(triangle), FadeOut(circle), run_time=2		# Ẩn các hình, thời gian thực hiện trong 2 giây.
        )

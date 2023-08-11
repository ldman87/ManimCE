from manim import *

class TextMathExample(Scene):
    def construct(self):
        title = Text("NỘI DUNG BÀI HỌC", font="Arial", weight=BOLD).set_color_by_gradient(PINK,YELLOW).to_corner(UP,buff=0.1) # Văn bản dùng font Arial, in đậm, được trộn hai màu và đặt ở trên cùng của màn hình. Cách mép trên màn hình 0.1 đơn vị.
        
        text1 = Text("Lê Đình Mẫn", font="Times New Roman", color=PURPLE, slant=ITALIC).scale(0.5).next_to(title,DOWN) # Văn bản dùng font Times New Roman sử dụng màu Purple, in nghiêng, giảm cỡ chữ 50% và đặt ngay dưới title.
        
        para = Paragraph("Khi tôi bắt đầu biết về thư viện Manim, tôi đã rất thích nó. Tôi đã tìm hiểu về cách sử \ndụng thư viện Manim.",
            "Manim rất thuận tiện khi thực hiện các bài giảng dưới dạng video. Vì thế, càng ngày sẽ có \nnhiều người sử dụng thư viện này.",
            "Điều kiện cần để sử dụng thành thạo thư viện Manim là:",
            font="Times New Roman", line_spacing=1, alignment='left', width=14,
        ) # Lênh này gồm 3 đoạn văn, khoảng cách giữa các dòng bằng 1 đơn vị, độ rộng văn bản bằng 14.
        
        blist = BulletedList("Biết sử dụng Python cơ bản", "Biết sử dụng Latex cơ bản. Ví dụ: $\\sqrt{2x-1}=\\dfrac{x+2}{3}$", "Biết vẽ hình với code Tikz/Asym/...", height=2, width=14).scale(0.6).next_to(para,DOWN).shift(LEFT*2) # Văn bản dạng Danh sách Bullet đặt ở dưới para và dịch sang trái 2 đơn vị.
        blist.set_color_by_tex("Biết lập trình Python", RED)
        blist.set_color_by_tex("Biết sử dụng Latex", GREEN)
        blist.set_color_by_tex("Biết vẽ hình", BLUE)

        text2 = Text("Yếu tố quan trọng nhất vẫn là  Ý TƯỞNG.", font="Times New Roman", color=BLUE).scale(0.5).next_to(para,DOWN)

        self.add(title) # Hiển thị nội dung title
        self.wait() # Đợi lệnh trước nó hoàn thành
        self.play(Write(text1), run_time=2) # Viết nội dung text1
        self.wait()
        self.play(Write(para), run_time=2) # Viết nội dung para
        self.wait()
        self.play(FadeIn(blist)) # Xuất hiện nội dung danh sách
        self.wait(2)
        self.play(blist[2].animate(run_time=3).shift(RIGHT * 2)) # Di chuyển item3 sang phải 2 đơn vị
        self.wait()
        self.play(Transform(blist,text2))
        self.wait(2)
        self.play(text2.animate.scale(2))
        self.wait()
        self.play(text2.animate.scale(0.5))
        self.wait(2)
        self.play(FadeOut(text2),FadeOut(para)) # Ẩn text2 và para

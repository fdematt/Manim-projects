from manim import *

config.pixel_height = 1080
config.pixel_width = 864

class Conditional(Scene):
    def construct(self):

        tlt = Tex(r'\underline{Probabilidad Condicional}', font_size = 100).move_to(7*UP)

        self.add(tlt)

        set1 = Circle(radius=2.5, stroke_color=WHITE).move_to(1.5*LEFT+1.5*UP).set_stroke_width(6)
        set1_lb= MathTex(r'A', font_size = 70).next_to(set1, UL, buff=0.1)
        set1_gp = VGroup(set1, set1_lb)

        self.play(Create(set1_gp), run_time=2)

        set2 = Circle(radius=2.5, stroke_color=WHITE).move_to(1.5*RIGHT+1.5*UP).set_stroke_width(6)
        set2_lb = MathTex(r'B', font_size = 70).next_to(set2, UR, buff=0.1)
        set2_gp = VGroup(set2, set2_lb)

        self.play(Create(set2_gp), run_time=2)
        
        lbl = MathTex(r'P(A|B)=', font_size=70).move_to(6*DOWN + 3*LEFT)
        lin = Line().next_to(lbl, RIGHT)
        lbl_gp = VGroup(lbl,lin)

        lbl1 = Tex(r'Ha ocurrido \\ el evento B').next_to(set2, DR)
        arr = Arrow(start=set2, end=lbl1)
        arr_gp = VGroup(lbl1, arr)

        self.play(Create(lbl_gp), run_time=1.5)

        txt1 = MathTex(r'=', font_size=70).next_to(lin, RIGHT)
        lin2 = Line().next_to(txt1, 3.7*RIGHT).set_length(3.5)
        lin2_gp = VGroup(txt1,lin2)

        self.play(Create(lin2_gp), run_time=1.5)

        txt2 = MathTex(r'P(B)', font_size=40).move_to(set1.get_center()+4*RIGHT)
        txt2.generate_target()
        txt2.target.move_to(lin2.get_bottom()+1*DOWN).scale(2)

        self.play(Succession(set1.animate.set_stroke(opacity=0.2),
                             set2.animate.set_fill('#107a8b', opacity=0.4),
                             Create(arr_gp),
                             Indicate(set2)))
        
        set2.generate_target()
        set2.target.move_to(lin.get_bottom()+1*DOWN).scale(0.2)
        
        self.play(Succession(MoveToTarget(set2.copy()),
                             MoveToTarget(txt2)))

        int = Intersection(set1, set2, fill_color='#2cb978', fill_opacity=0.5).set_stroke_width(6)  

        lbl2 = Tex(r'Proporción del evento A \\ dentro de B').next_to(set2,DL)
        arr2 = Arrow(start=int, end=lbl2)
        arr2_gp = VGroup(lbl2,arr2)
        
        self.play(Succession(DrawBorderThenFill(int), 
                             Create(arr2_gp),
                             Indicate(int)))

        int.generate_target()
        int.target.move_to(lin.get_top()+1*UP).scale(0.3)

        txt3 = MathTex(r'P(A \cap B)', font_size=40).move_to(int.get_center())
        txt3.generate_target()
        txt3.target.move_to(lin2.get_top()+1*UP).scale(2)

        self.play(Succession(MoveToTarget(int.copy()),
                             MoveToTarget(txt3)))

        self.wait(2)
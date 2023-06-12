from manim import *

config.pixel_height = 1080
config.pixel_width = 864

class Polar(Scene):
    def construct(self):

        logo = MathTex('@fdematt', font_size=90, color = '#F7D060').move_to(8*DOWN).set_color(color_gradient(('#FFDD00','#FBB034'), 3))
        self.add(logo)

        e = ValueTracker(0.01)

        plane = PolarPlane(radius_max=4,
                           background_line_style={'stroke_color':'#ECF8F9','stroke_opacity':0.3,'stroke_width':6}).add_coordinates()
        plane.shift(DOWN*2)

        graph1 = always_redraw(lambda: 
                               ParametricFunction(lambda t: plane.polar_to_point(3*np.sin(2*t), t), t_range=[0, e.get_value()], color=GREEN, stroke_width=5))
        
        dot1 = always_redraw(lambda: Dot(fill_color = GREEN, fill_opacity=0.8).scale(0.5).move_to(graph1.get_end()))


        axes = Axes(x_range=[0,7,1], x_length=7, y_range=[-6,6,1], y_length=6, stroke_width=6).shift(UP*5)
        axes.add_coordinates()

        graph2 = always_redraw(lambda: axes.plot(lambda x: 3*np.sin(2*x), x_range=[0, e.get_value()], color=GREEN, stroke_width=5))

        dot2 = always_redraw(lambda: Dot(fill_color=GREEN, fill_opacity=0.8).scale(0.5).move_to(graph2.get_end()))

        title = MathTex('f(\\theta) = 3sin(2\\theta)', color = '#FFF5B8', font_size=70).move_to(8*UP)

        self.play(LaggedStart(
            Write(plane), Create(axes), Write(title), run_time = 6, lag_ratio = 0.5
        ))

        self.add(graph1, graph2, dot1, dot2)
        self.play(e.animate.set_value(2*PI), run_time = 14, rate_func = linear)
        self.wait()
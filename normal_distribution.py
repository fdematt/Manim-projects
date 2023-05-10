from manim import *
from math import sqrt
import math

config.pixel_height = 1080
config.pixel_width = 864

def PDF_normal(x, mu, sigma):
        return math.exp(-((x-mu)**2)/(2*sigma**2))/(sigma*math.sqrt(2*math.pi))

class NormalDistribution(Scene):

    def construct(self):

        mu = ValueTracker(0)
        sigma = ValueTracker(1)

        plane = Axes(
            x_range=[-3.8, 3.8, 1], y_range=[0, 1, 0.2],
            axis_config={
                "font_size": 60,
                'stroke_width': 5
            }, tips=False
        ).add_coordinates().set_color(WHITE).scale(1.1).move_to(4*DOWN)

        curve = always_redraw(
        lambda: plane.plot(
            lambda x: PDF_normal(x, mu.get_value(), sigma.get_value()), color=YELLOW).set_stroke_width(7)
    )

        func_label = MathTex('f(\mu,\sigma)=\\frac1{\sqrt{2\pi}\sigma}{e}^{-\\frac{(x-\mu)^{2}}{2\sigma^{2}}}', font_size=90)
        rect = SurroundingRectangle(func_label,color='#caf0f8', buff=MED_LARGE_BUFF)
        func_rect = VGroup(func_label, rect)

        self.play(Create(func_label), run_time=1.5)
        self.play(Create(rect))
        self.play(func_rect.animate.move_to(5.5*UP))
        self.play(Create(plane))
        self.play(Create(curve))
        self.wait()

        mu_label = MathTex('\mu =', font_size=90)
        mu_tex = DecimalNumber(mu.get_value()).add_updater(lambda v: v.set_value(mu.get_value())).set_color(GREEN).scale(2)
        mu_label.next_to(mu_tex,LEFT,aligned_edge=mu_label.get_bottom()).set_color(GREEN)
        mu_group = VGroup(mu_label, mu_tex).next_to(func_label, 2*DOWN, buff=0.5)

        sigma_label = MathTex('\sigma=', font_size=90)
        sigma_tex = DecimalNumber(sigma.get_value()).add_updater(lambda c: c.set_value(sigma.get_value())).next_to(mu_tex, DOWN, buff=0.6).set_color('#E86A33').scale(2)
        sigma_label.next_to(sigma_tex,LEFT,aligned_edge=sigma_label.get_bottom()).set_color('#E86A33')
        sigma_group = VGroup(sigma_label, sigma_tex)

        mu_point = always_redraw(lambda: Dot(point=plane.c2p(mu.get_value(),0,0)).set_color(GREEN))
        mu_point_label = always_redraw(lambda: MathTex('\mu', font_size = 90).next_to(mu_point, DOWN).set_color(GREEN))
        mu_point_group = VGroup(mu_point,mu_point_label)

        self.play(Create(mu_group),run_time=0.5)
        self.play(Create(mu_point_group),run_time=0.5)
        self.play(Create(sigma_group),run_time=0.5)
        self.wait(1)
        self.play(
            mu.animate.set_value(2),
            rate_func=smooth,
            run_time=2.5
            )
        self.play(
            mu.animate.set_value(0),
            rate_func=smooth,
            run_time=2.5
            )
        self.wait(1)
        self.play(
             sigma.animate.set_value(3),
             rate_func=smooth,
             run_time=2.5
        )
        self.play(
             sigma.animate.set_value(0.5),
             rate_func=smooth,
             run_time=2.5
        )
        self.play(
             sigma.animate.set_value(1),
             rate_func=smooth,
             run_time=2.5
        )
        self.wait()

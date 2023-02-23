from manim import *

class TLabelExample(Scene):
    def construct(self):
        # defines the axes and linear function
        axes = Axes(x_range=[-7, 8], y_range=[-2, 9], x_length=9, y_length=6)
        func = axes.plot(lambda x: x, color=BLUE)
        func2 = axes.plot(lambda x: (x**2)/4, color=BLUE)
        func3 = axes.plot(lambda x: (x**3)/4, color=BLUE)

        self.play(Create(axes, run_time=1.5))
        self.wait()
        self.play(Create(func, run_time=1.5))
        self.wait()
        self.play(Transform(func, func2))
        self.wait()
        self.play(Transform(func, func3))
        self.wait()
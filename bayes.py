from manim import *

config.pixel_height = 1080
config.pixel_width = 864

class MyTex(Tex):
    def __init__(self, *args, j_width=4, **kwargs):
        super().__init__(*args, tex_environment="\\begin{tabular}{p{%s cm}}"%j_width, **kwargs)

class Bayes(Scene):
    def construct(self):

        logo = Tex(
            '@fdematt', 
            font_size = 75, 
            color = '#F7D060'
            ).move_to(8*DOWN).set_color(color_gradient(('#FFDD00','#FBB034'), 3))
        self.add(
            logo
        )

        texto1 = MyTex(
            'Sean los eventos $A_{1}$ y $A_{2}$ mutuamente excluyentes y colectivamente exhaustivos con probabilidades conocidas.',
            j_width=9,
            tex_to_color_map = {
                '$A_{1}$': YELLOW,
                '$A_{2}$': YELLOW
            },
            font_size = 52
            ).move_to(5*UP)       
        
        A1 = Rectangle(height=4, width=1).move_to(UP + 1.5*LEFT).set_stroke_width(5)
        A1_etiqueta = Tex('P($A_{1}$)',
                          tex_to_color_map = {
                              '$A_{1}$': YELLOW
                          },
                          font_size = 60).next_to(A1, UP)
        A1_grupo = VGroup(A1, A1_etiqueta)

        A2 = Rectangle(height=4, width=3).next_to(A1, 2*RIGHT).set_stroke_width(5)
        A2_etiqueta = Tex('P($A_{2}$)',
                          tex_to_color_map = {
                              '$A_{2}$': YELLOW
                          },
                          font_size = 60).next_to(A2, UP)
        A2_grupo = VGroup(A2, A2_etiqueta)
        self.play(
            Write(texto1)
            )
        self.play(
            Write(A1_grupo),
            Write(A2_grupo)
            )

        self.play(
            Wiggle(A1_etiqueta),
            Wiggle(A2_etiqueta)
            )
        
        texto2 = MyTex(
            'Si ha ocurrido un evento B del que se conocen sus propabilidades condicionales.',
            j_width=9, 
            tex_to_color_map = {
                'B': BLUE_B
            },
            font_size = 52).move_to(3*DOWN)
        self.play(Write(texto2))

        B1 = Polygon(A1.get_corner(DL),
                     A1.get_corner(DR),
                     A1.get_top()+[0.5,-2.5,0],
                     A1.get_top()+[-0.5,-2.5,0], color = WHITE).set_fill([BLUE_E, BLUE_A], opacity = 0.9)
        
        B2 = Polygon(A2.get_corner(DL),
                     A2.get_corner(DR),
                     A2.get_top()+[1.5,-2.7,0],
                     A2.get_top()+[-1.5,-2.7,0], color = WHITE).set_fill([BLUE_A, BLUE_E], opacity = 0.9)
        
        B = VGroup(B1, B2)

        B1_etiqueta = Tex('P(B$|$$A_{1}$)',
                          tex_to_color_map ={
                              '$A_{1}$': YELLOW,
                              'B': BLUE_B
                          },
                          font_size = 60).next_to(B1, LEFT)
        B2_etiqueta = Tex('P(B$|$$A_{2}$)',
                          tex_to_color_map = {
                              '$A_{2}$': YELLOW,
                              'B': BLUE_B
                          },
                          font_size = 60).next_to(B2, RIGHT)

        B_etiquetas = VGroup(B1_etiqueta, B2_etiqueta)
        self.play(
            Write(B),
            Write(B_etiquetas)
            )
        self.play(
            Wiggle(B1_etiqueta),
            Wiggle(B2_etiqueta)
        )
        
        texto3 = Tex(
            '¿Cómo cambian las probabilidades de $A_{1}$ y $A_{2}$?',
            tex_to_color_map = {
                '$A_{1}$': YELLOW,
                '$A_{2}$': YELLOW
            },
            font_size = 60
            ).next_to(texto2, 2*DOWN)
        self.play(
            Write(texto3)
            )
        self.wait()
        
        self.play(
            Uncreate(texto1),
            Uncreate(texto2)
        )
        self.play(
            texto3.animate.move_to(7*UP).set_font_size(65),
            VGroup(A1_grupo, A2_grupo,B, B_etiquetas).animate.move_to(3.5*UP)
        )

        A1_B = Tex('P($A_{1}$$|$B) = ',
                   tex_to_color_map = {
                       '$A_{1}$': YELLOW,
                       'B': BLUE_B
                   }, 
                   font_size = 60).move_to(2.7*LEFT + 2.4*DOWN)
        linea = Line(
            start = A1_B.get_right(),
            end = A1_B.get_right() + np.array([6,0,0]),
            buff = 0.4
        )
        self.play(
            Write(A1_B),
            Write(linea)
        )

        llave = Brace(B, DOWN)
        llave_texto = llave.get_text('Ha ocurrido el evento B!')
        llave_texto.scale(1.2)
        self.play(
            GrowFromCenter(llave),
            FadeIn(llave_texto),
            VGroup(A1, A2).animate.set_stroke(opacity = 0.4),
            run_time = 3
        )

        B1_copia = B1.copy()
        B1_copia.move_to(linea.get_center() + np.array([-1.7,-0.9,0])).scale(0.8)        

        B2_copia = B2.copy()
        B2_copia.move_to(linea.get_center() + np.array([1,-0.9,0])).scale(0.8)        

        mas = Tex('+', font_size = 60).next_to(B1_copia, RIGHT + np.array([0.5,0,0]))
        self.play(
            Circumscribe(B1),
            Circumscribe(B2)
        )
        self.play(
            TransformFromCopy(B1, B1_copia),
            TransformFromCopy(B2, B2_copia),
            Write(mas)
        )

        B1_copia_2 = B1.copy()
        B1_copia_2.move_to(linea.get_center() + np.array([0,0.9,0])).scale(0.8)
        self.play(
            Circumscribe(B1)
        )
        self.play(
            TransformFromCopy(B1, B1_copia_2)
        )
        self.wait()

        A1_etiqueta_copia = A1_etiqueta.copy()
        A1_etiqueta_copia.move_to(linea.get_center() + np.array([-1.2,0.5,0])).set_font_size(60)

        B1_etiqueta_copia = B1_etiqueta.copy()
        B1_etiqueta_copia.next_to(A1_etiqueta_copia, 1.5*RIGHT).set_font_size(60)

        A1_B1_etiquetas_copias = VGroup(A1_etiqueta_copia, B1_etiqueta_copia)
        self.play(
            FadeOut(B1_copia_2),
            TransformFromCopy(
                VGroup(A1_etiqueta, B1_etiqueta), A1_B1_etiquetas_copias
            )
        )
        self.wait()

        B_etiqueta = Tex('P(B)',
                         tex_to_color_map = {
                             'B': BLUE_B
                         }, 
                         font_size = 60).move_to(linea.get_center() + np.array([0,-0.5,0]))
        B1_B2_copias = VGroup(B1_copia, B2_copia, mas)
        self.play(
            Transform(
                B1_B2_copias, B_etiqueta
            )
        )

        rectangulo = SurroundingRectangle(
            VGroup(A1_B, A1_etiqueta_copia, B1_etiqueta_copia, B1_B2_copias, linea),
            corner_radius = 0.2,
            buff = 0.3
        ).set_color_by_gradient('#FFA585','#FFEDA0')
        self.play(
            Write(rectangulo),
            rate_func = smooth
        )

        A2_B = Tex('P($A_{2}$$|$B) = ',
                   tex_to_color_map = {
                       '$A_{2}$': YELLOW,
                       'B': BLUE_B
                   }, 
                   font_size = 60).move_to(2.7*LEFT + 5.3*DOWN)
        linea_2 = Line(
            start = A2_B.get_right(),
            end = A2_B.get_right() + np.array([6,0,0]),
            buff = 0.4
        )
        self.play(
            Write(A2_B),
            Write(linea_2)
        )
        self.play(
            Wiggle(llave_texto)
        )

        B1_copia_3 = B1.copy()
        B1_copia_3.move_to(linea_2.get_center() + np.array([-1.7,-0.9,0])).scale(0.8)        

        B2_copia_2 = B2.copy()
        B2_copia_2.move_to(linea_2.get_center() + np.array([1,-0.9,0])).scale(0.8)        

        mas_2 = Tex('+', font_size = 60).next_to(B1_copia_3, RIGHT + np.array([0.5,0,0]))
        self.play(
            Circumscribe(B1),
            Circumscribe(B2)
        )
        self.play(
            TransformFromCopy(B1, B1_copia_3),
            TransformFromCopy(B2, B2_copia_2),
            Write(mas_2)
        )

        B2_copia_3 = B2.copy()
        B2_copia_3.move_to(linea_2.get_center() + np.array([0,0.9,0])).scale(0.8)
        self.play(
            Circumscribe(B2)
        )
        self.play(
            TransformFromCopy(B2, B2_copia_3)
        )
        self.wait()

        A2_etiqueta_copia = A2_etiqueta.copy()
        A2_etiqueta_copia.move_to(linea_2.get_center() + np.array([-1.2,0.5,0])).set_font_size(60)

        B2_etiqueta_copia = B2_etiqueta.copy()
        B2_etiqueta_copia.next_to(A2_etiqueta_copia, 1.5*RIGHT).set_font_size(60)

        A2_B2_etiquetas_copias = VGroup(A2_etiqueta_copia, B2_etiqueta_copia)
        self.play(
            FadeOut(B2_copia_3),
            TransformFromCopy(
                VGroup(A2_etiqueta, B2_etiqueta), A2_B2_etiquetas_copias
            )
        )
        self.wait()

        B_etiqueta_2 = Tex('P(B)',
                         tex_to_color_map = {
                             'B': BLUE_B
                         }, 
                         font_size = 60).move_to(linea_2.get_center() + np.array([0,-0.5,0]))
        B1_B2_copias_2 = VGroup(B1_copia_3, B2_copia_2, mas_2)
        self.play(
            Transform(
                B1_B2_copias_2, B_etiqueta_2
            )
        )

        rectangulo_2 = SurroundingRectangle(
            VGroup(A2_B, A2_etiqueta_copia, B2_etiqueta_copia, B1_B2_copias_2, linea_2),
            corner_radius = 0.2,
            buff = 0.3
        ).set_color_by_gradient('#FFA585','#FFEDA0')
        self.play(
            Write(rectangulo_2),
            rate_func = smooth
        )

        self.wait()
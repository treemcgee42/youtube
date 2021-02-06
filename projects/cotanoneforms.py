from manimlib.imports import *
from NumberCreature.NumberCreature import *

class title(Scene):
    def construct(self):
        dforms = TextMobject("Differential Forms")\
                .shift(.5*UP)
        p1 = TextMobject("Part 2: Cotangent Spaces and 1-forms")\
                .scale(.75)\
                .next_to(dforms, direction=DOWN, buff=MED_SMALL_BUFF)

        self.wait()
        self.play(  Write(dforms,run_time=3))
        self.wait()
        self.play(  FadeIn(p1, run_time=3))
        self.wait(2)
        self.play(  *[FadeOut(mob)for mob in self.mobjects])

class dx(GraphScene):
    def construct(self):
        integral = TexMobject("\\int","_a^b", "f(x)","dx").scale(.75).shift(2*UP)
        integral[1].set_color(RED)
        integral[-1].set_color(YELLOW)
        self.play(  FadeIn(integral))
        self.wait()

        self.setup_axes(animate=True)

        apt = self.coords_to_point(2,0)
        a = Dot(apt).set_color(RED)
        alabel = TexMobject("a").scale(.5).next_to(a,direction=DOWN,buff=MED_SMALL_BUFF)
        bpt = self.coords_to_point(8,0)
        b = Dot(bpt).set_color(RED)
        blabel = TexMobject("b").scale(.5).next_to(b,direction=DOWN,buff=MED_SMALL_BUFF)
        self.play(*[FadeIn(mob)for mob in [a,b, alabel, blabel]])
        atob = Line(apt,bpt).set_color(RED)
        self.play(  ShowCreation(atob))
        self.wait()

        # moving arrow
        arrowdot = a.copy().set_color(YELLOW).scale(.75)
        vec = Line(apt, arrowdot.copy().shift(.5*RIGHT)).add_tip(tip_length=.2).set_color(YELLOW)
        self.play(  FadeIn(arrowdot), FadeIn(vec))
        self.wait()
        
        def val(obj):
            obj.become(
                Line(arrowdot.get_center(), arrowdot.copy().shift(.5*RIGHT)).add_tip(tip_length=.2).set_color(YELLOW)
            )
        vec.add_updater(val)

        self.play(  MoveAlongPath(arrowdot,atob, run_time = 6))
        self.wait()
        vec.remove_updater(val)
        self.play(  *[FadeOut(mob)for mob in self.mobjects])

class ds(Scene):
    CONFIG = {
        "x_start": 2,
        "x_end": 8,
        "axes_config": {
            "center_point": [-4.5,-2.5,0],
            "x_axis_config": {
                "x_min": 0,
                "x_max": 10,
                "include_numbers": False
            },
            "y_axis_config": {
                "label_direction": UP,
                "x_min": 0,
                "x_max": 6,
                "include_numbers": False
            },
        },
        "func": lambda x : (np.sin((2*PI /6)*(x-2))+2),
        "func_config": {
            "color": RED,
            "x_min": 2,
            "x_max": 8,
        },
        "dot_radius": 0.1,
        "line_config": {}
    }
    def construct(self):
        integral = TexMobject("\\int","_C", "\\vec{F}\cdot","d\\vec{r}").scale(.75).shift(2*UP)
        integral[-1].set_color(YELLOW)
        integral[1].set_color(RED)
        self.play(  FadeIn(integral))
        self.wait()

        axes = self.get_axes()
        func = self.get_graph(self.func,**self.func_config)
        dot_start = self.get_dot_from_x_coord(self.x_start)
        dot_end   = self.get_dot_from_x_coord(self.x_end)
        self.play(
            Write(axes)
        )
        self.wait()
        self.play(  ShowCreation(func))
        self.wait()

        line = VMobject()
        line.add_updater(self.get_derivative_updater(dot_start))
        self.play(  ShowCreation(line), GrowFromCenter(dot_start))
        self.wait()
        self.move_dot(
            dot_start,
            self.x_start, 8,
            run_time=6,
        )
        self.wait()
        line.remove_updater(self.get_derivative_updater(dot_start))
        self.play(  *[FadeOut(mob)for mob in self.mobjects])

    def get_axes(self):
        self.axes = Axes(**self.axes_config)
        return self.axes
    def get_graph(self,func,**kwargs):
        return self.axes.get_graph(
                                    func,
                                    **kwargs
                                )
    def get_f(self,x_coord):
        return self.axes.c2p(x_coord, self.func(x_coord))
    def get_dot_from_x_coord(self,x_coord,**kwargs):
        return Dot(
            self.get_f(x_coord),
            radius=self.dot_radius,
            **kwargs
        ).set_color(YELLOW)
    def get_dot_updater(self, start, end):
        def updater(mob,alpha):
            x = interpolate(start, end, alpha)
            coord = self.get_f(x)
            mob.move_to(coord)
        return updater

    def get_line_updater(self,d1,d2,buff=3,**kwargs):
        def updater(mob):
            mob.become(
                self.get_line_across_points(d1,d2,buff)
            )
        return updater
    def move_dot(self,dot,start,end,*args,**kwargs):
        self.play(
            UpdateFromAlphaFunc(
                dot, self.get_dot_updater(start,end),
                *args,
                **kwargs
            )
        )
    def get_derivative_updater(self, dot, length=1):
        def updater(mob):
            derivative = Line(
                dot.get_center(),
                self.get_dot_from_x_coord(
                    self.axes.p2c(dot.get_center())[0] + 0.0001
                ).get_center()
            )
            derivative.set_length(length)
            derivative.move_to(dot)
            derivative.move_to(derivative.points[-1]).add_tip(tip_length=.3).set_color(YELLOW)
            mob.become(derivative)
        return updater

class manifold(Scene):
    def construct(self):
        surface = SVGMobject("oneforms/gamma.svg", stroke_width=0)
        surface[0].set_color(BLUE)
        path = SVGMobject("oneforms/gamma.svg", fill_opacity=0)
        path[-1].set_color(RED)
        gamma = TexMobject("\\gamma", stroke_width=0).scale(.5).shift(.25*UP).set_color(RED)

        self.play(  GrowFromCenter(surface[0]))
        self.wait()
        self.play(  ShowCreation(path[-1]),FadeIn(gamma))
        self.wait()
        self.play(  *[FadeOut(mob)for mob in self.mobjects])

class diagram(Scene):
    def construct(self):
        m = TexMobject("M").shift(1.5*UP,2.5*LEFT)
        r = TexMobject("\\mathbb{R}").shift(1.5*UP,2.5*RIGHT)
        tm = TexMobject("TM").shift(1.5*DOWN)

        mtor = DashedLine((-2,1.5,0),(2,1.5,0), stroke_width=2).add_tip(tip_length=.3)
        mtotm = Line(m,tm,stroke_width=2,buff=.25).add_tip(tip_length=.3).set_color(BLUE)
        tmtor = Line(tm,r,stroke_width=2,buff=.25).add_tip(tip_length=.3)
        ghost = TexMobject("s").move_to(tmtor)
        mtocovector = Line(m,ghost,stroke_width=2,buff=.25).add_tip(tip_length=.3).set_color(BLUE)

        gamma = TexMobject("\gamma").scale(.75).move_to(mtotm).shift(.5*LEFT).set_color(RED)
        covector = TexMobject("v^\\ast\\in T^\\ast M").scale(.75).move_to(tmtor).shift(1.12*RIGHT)
        oneforms = TextMobject("1-forms").move_to(mtocovector).scale(.5).shift(.3*UP).rotate(-19*DEGREES)
        omega = TexMobject("\\omega").move_to(mtocovector).scale(.75).shift(.3*UP).rotate(-19*DEGREES).set_color(YELLOW)

        self.play(  *[FadeIn(mob)for mob in [m,r,mtor]])
        self.wait()

        f = TexMobject("``f\" ").scale(.75).next_to(mtor,direction=UP,buff=MED_SMALL_BUFF)
        self.play(FadeIn(f))
        self.wait()
        self.play(  FadeOut(f))
        self.wait()

        self.play(  FadeIn(tm))
        self.wait()
        self.play(  ShowCreation(mtotm))
        self.play(  FadeIn(gamma))
        self.wait()

        self.play(  ShowCreation(tmtor))
        self.play(  FadeIn(covector))
        self.wait()
        
        self.play(  ShowCreation(mtocovector))
        self.play(  FadeIn(oneforms))
        self.wait()
        self.play(  ReplacementTransform(oneforms,omega))
        self.wait()

        """
        self.add(m,r,tm,    mtor, mtotm,tmtor,mtocovector,  gamma,covector,oneforms)
        self.play(  ReplacementTransform(oneforms,omega))
        """

        v1 = VGroup(*self.mobjects)
        self.play(  Transform(v1,v1.copy().shift(1*DOWN)))
        self.wait()

        integral = TexMobject("\\int_C \\vec{F}\\cdot d\\vec{r}").scale(.75).shift(2*UP)

        self.play(  FadeIn(integral))
        self.wait()
        self.play(  Transform(integral,integral.copy().shift(1.5*LEFT)))
        arr = DashedLine(integral,(1.5,2.15,0),buff=.25).add_tip(tip_length=.2)
        self.play(  ShowCreation(arr))
        newintegral = TexMobject("\\int","_\\gamma", "\\omega").scale(.75).move_to((1.5,2,0)).shift(.2*RIGHT)
        newintegral[1].set_color(RED)
        newintegral[-1].set_color(YELLOW)
        self.play(   FadeIn(newintegral))
        self.wait()
        self.play(  *[FadeOut(mob)for mob in self.mobjects])
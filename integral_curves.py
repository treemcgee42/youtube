# Date: 2/16/21
# Purpose: integral curves subsection Lee 13
# Notes:

from manimlib.imports import *


class ex1(GraphScene):
    CONFIG = {
        "x_min" : -4,
        "x_max" : 4,
        "y_min" : -4,
        "y_max" : 4,
        "x_tick_frequency" : 4,
        "y_tick_frequency" : 4,
        "graph_origin" : np.array((-2, 0, 0))
    }
    def construct(self):
        vf_eq = TexMobject(r"""
            x\dfrac{\partial}{\partial x} + y\dfrac{\partial}{\partial y}
        """).scale(.75).to_edge(RIGHT, buff=1.25).to_edge(UP, buff=1)

        self.setup_axes(animate=True)
        self.play(
            FadeIn(vf_eq)
        )

        vf_func = lambda p: np.array([
            p[0],
            p[1],
            0
        ])
        vf = VectorField(
            vf_func,
            x_max = 4.5,
            x_min = -4.5,
            y_max = 3,
            y_min = -3,
            opacity = .5
        ).move_to(self.graph_origin)

        ic_1 = self.get_graph(
            lambda x : x,
            color = PINK,
            x_min = 0,
            x_max = 4
        )

        ic_2 = self.get_graph(
            lambda x : 3*x,
            color = BLUE,
            x_min = -1.3,
            x_max = 0
        )

        self.play(
            *[GrowFromCenter(vec) for vec in vf]
        )
        self.wait(2)

        ode = TextMobject(r"""
            \begin{align*}
                x'(t)=& x(t) \\
                    y'(t)=& y(t)
            \end{align*}
        """).scale(.75).next_to(vf_eq, direction=DOWN, buff=1.5)

        ode_sol = TexMobject(r"""
            (ae^t, be^t)
        """).scale(.75).next_to(ode, direction=DOWN, buff=1.5)
        
        self.cycle(
            [ode, ode_sol],
            out=False
        )

        self.play(
            ShowCreation(ic_1)
        )
        self.play(
            ShowCreation(ic_2)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

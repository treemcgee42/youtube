from manimlib.imports import *
from NumberCreature.NumberCreature import *

class title(Scene):
    def construct(self):
        dforms = TextMobject("Differential Forms")\
                .shift(.5*UP)
        p1 = TextMobject("Part 1: Tangent and Cotangent Spaces")\
                .scale(.75)\
                .next_to(dforms, direction=DOWN, buff=MED_SMALL_BUFF)

        self.wait()
        self.play(  Write(dforms,run_time=3))
        self.wait()
        self.play(  FadeIn(p1, run_time=3))
        self.wait(2)
        #self.play(  *[FadeOut(mob)for mob in self.mobjects])

class letsstart(Scene):
    def construct(self):
        space = TextMobject("Space: $\\mathbb{R }^n$")\
                    .scale(.75)\
                    .to_edge(LEFT,buff=MED_LARGE_BUFF).to_edge(UP,buff=MED_LARGE_BUFF)

        ptex = TexMobject("p","\\in\\mathbb{R }^n")
        ptex[0].set_color(PURPLE)

        tspace = TexMobject("T","_p","\\mathbb{R }^n \\coloneqq \\aa (", "p",",","v",")\\mid",\
                    "v", "\\in \\mathbb{R }^n \\bb")
        tspace[1].set_color(PURPLE)
        tspace[3].set_color(PURPLE)
        tspace[5].set_color(BLUE)
        tspace[-2].set_color(BLUE)

        tident = TexMobject("(","p",",","v",")\\mapsto","v")\
                    .shift(1*DOWN)
        tident[1].set_color(PURPLE)
        tident[3].set_color(BLUE)
        tident[-1].set_color(BLUE)

        a1text = TextMobject("point").next_to(tident[3],buff=2, direction=DOWN)
        a1 = Arrow(DOWN,UP)\
                .next_to(a1text,direction=UP, buff=SMALL_BUFF)
        a2text = TextMobject("vector").next_to(tident[-1],buff=2,direction=RIGHT)
        a2 = Arrow(RIGHT,LEFT)\
                .next_to(a2text,direction=LEFT,buff=SMALL_BUFF)
        a3text = TextMobject("vector space").next_to(tspace[1],buff=2,direction=UP)
        a3 = Arrow(UP,DOWN)\
                .next_to(a3text,direction=DOWN,buff=SMALL_BUFF)

        self.wait()
        self.play(   FadeIn(space))
        self.wait()
        self.play(  FadeIn(ptex))
        self.wait(3)
        self.play(  Transform(ptex,ptex.copy().shift(1*UP)), ShowCreation(tspace))
        self.wait(2)
        self.play(  ShowCreation(tident))
        self.wait()
        self.play(  *[GrowArrow(arrow)for arrow in [a1,a2,a3]],\
                    *[FadeIn(label)for label in [a1text,a2text,a3text]])
        self.wait(3)
        
        tc = tident.copy()

        self.add(tc)
        self.play(  *[FadeOut(mob)for mob in self.mobjects[:-1]],\
                    Transform(tc,tident.copy().to_edge(UP,buff=LARGE_BUFF)))

        Ale = Alex().scale(.65)
        Ale[4].set_color(GREEN)

        self.wait()
        self.play(  FadeIn(Ale))
        self.wait()
        self.play(  Blink(Ale))
        self.wait(2)
        self.play(  Blink(Ale))
        self.wait(2)

        whatpis = TextMobject("$p$", " is a ``basepoint''")\
                    .to_edge(DOWN,buff=LARGE_BUFF)
        whatpis[0].set_color(PURPLE)

        self.play(  Write(whatpis), Blink(Ale))
        self.wait(2)
        self.play(  Blink(Ale))
        self.wait(2)
        self.play(  Blink(Ale))
        self.wait(2)
        self.play(  *[FadeOut(mob)for mob in self.mobjects])
        self.wait()

class basederivative(Scene):
    def construct(self):
        basedef = TextMobject("``Basepoint'' definition of a derivative")\
                    .scale(.75)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)
        
        self.wait()
        self.play(  Write(basedef))
        self.wait(3)

        letu = TextMobject("$U$", " is an open subset of $\\mathbb{R }^n$",align="")\
                .to_edge(LEFT,buff=MED_SMALL_BUFF)\
                .shift(1.5*UP)\
                .scale(.75)
        letu[0].set_color(YELLOW)

        function = TexMobject("f",":","U","\\rightarrow\\mathbb{R }^m",align="")\
                    .next_to(letu,direction=DOWN,buff=LARGE_BUFF)\
                    .scale(.75)
        function[0].set_color(ORANGE)
        function[2].set_color(YELLOW)

        inc1 = TexMobject("\\in C^1",align="")\
                .next_to(function,direction=DOWN,buff=SMALL_BUFF)\
                .scale(.75)

        bigd = TexMobject("D","f","(","p","):\\mathbb{R }^n\\rightarrow\\mathbb{R}^m")\
                .next_to(inc1,direction=DOWN,buff=LARGE_BUFF)\
                .scale(.75)
        bigd[1].set_color(ORANGE)
        bigd[3].set_color(PURPLE)

        jacsmall = TexMobject("\\left[ \\dfrac{\\partial f_i}{\\partial x_j} (p) \\right]")\
                    .next_to(bigd,buff=SMALL_BUFF, direction=DOWN)\
                    .scale(.75) 

        self.play(  ShowCreation(letu))
        self.wait()
        self.play(  ShowCreation(function))
        self.play(  ShowCreation(inc1))
        self.wait(3)
        self.play(  ShowCreation(bigd))
        self.play(  GrowFromCenter(jacsmall))
        self.wait()

        div = Line((0,-2.5,0), (0,2.5,0), stroke_width=1)\
                .shift(.5*DOWN)

        self.play(  ShowCreation(div))

        jacbig = TexMobject("\\begin{bmatrix} \\frac{\\partial f_0}{\\partial x_1} & \\frac{\\partial f_0}{\\partial x_1} & \\cdots\
                    \\\[.35cm] \\frac{\\partial f_1}{\\partial x_0} & \\frac{\\partial f_1}{\\partial x_1} & \\cdots\
                    \\\ \\vdots & \\vdots & \\ddots \\end{bmatrix}")\
                    .to_edge(RIGHT,buff=1.75)\
                    .shift(.5*DOWN)

        self.play(  GrowFromCenter(jacbig))
        self.wait(3)
        self.play(  FadeOut(jacbig))
        self.wait(2)

        qis = TexMobject("q", "=","f","(","p",")")\
                .scale(.75)\
                .shift(3.5*RIGHT,1.5*UP)
        qis[0].set_color(GREEN)
        qis[2].set_color(ORANGE)
        qis[-2].set_color(PURPLE)

        self.play(  ShowCreation(qis))
        self.wait()

        newd = TexMobject("d","f","_p",":T","_p","\\mathbb{R }^n\\rightarrow T","_q","\\mathbb{ R}^m")\
                    .next_to(qis,direction=DOWN,buff=LARGE_BUFF)\
                    .scale(.75)
        newd.set_color_by_tex("f",ORANGE)
        newd.set_color_by_tex("p",PURPLE)
        newd.set_color_by_tex("q",GREEN)
        newddef = TexMobject("\\coloneqq (","q",",D","f","(","p",")","v",")")\
                    .next_to(newd,direction=DOWN,buff=SMALL_BUFF)\
                    .scale(.75)
        newddef.set_color_by_tex("f",ORANGE)
        newddef.set_color_by_tex("p",PURPLE)
        newddef.set_color_by_tex("v",BLUE)
        newddef[1].set_color(GREEN)

        self.play(  ShowCreation(newd))
        self.wait()
        self.play(  ShowCreation(newddef))
        self.wait(3)
        self.play(  *[FadeOut(mob)for mob in self.mobjects])

class seenbefore(Scene):
    def construct(self):
        vf = TextMobject("Vector Field:")\
                .to_edge(UP,buff=LARGE_BUFF)
        assigns = TextMobject("assigns ","$v$","$\\in T_p\\mathbb{R }^3$ ",\
                    "to each ", "$p$","$\\in\\mathbb{R }^3$")\
                    .next_to(vf,buff=1, direction=DOWN)\
                    .scale(.75)
        assigns.set_color_by_tex("v", BLUE)
        assigns[-2].set_color(PURPLE)

        self.wait(2)
        self.play(  ShowCreation(vf))
        self.wait()
        self.play(  ShowCreation(assigns))
        self.wait(2)

        Ale = Alex().scale(.75).shift(1*DOWN)
        Ale[4].set_color(GREEN)

        self.play(  GrowFromCenter(Ale))
        self.wait(2)
        self.play(  Blink(Ale))
        self.wait(2)
        self.play(  *[FadeOut(mob)for mob in self.mobjects])

class cotangent(Scene):
    def construct(self):
        cot = TextMobject("Cotangent Space $T^\\ast_p\\mathbb{R }^n=(T_p\\mathbb{R})^\\ast$:")\
                .to_edge(UP,buff=LARGE_BUFF)
        whatitis = TextMobject("the dual of the tangent space, i.e. $\\operatorname{Hom}\
                    (T_p\\mathbb{R }^n,\mathbb{R})$")\
                    .scale(.75)\
                    .next_to(cot,buff=MED_LARGE_BUFF, direction=DOWN)

        self.wait()
        self.play(  ShowCreation(cot))
        self.wait(2)
        self.play(  ShowCreation(whatitis))
        self.wait(2)

        manifold = TextMobject("manifold ","$M$")\
                    .shift(3*LEFT)
        manifold[-1].set_color(BLUE)
        field = TextMobject("field ","$F$")\
                    .next_to(manifold,buff=MED_LARGE_BUFF,direction=DOWN)
        field[-1].set_color(GREEN)

        self.play(  ShowCreation(manifold), ShowCreation(field))

        ingen = TexMobject("T_{p }^\\ast","M","=\\operatorname{Hom}(T_p","M",",","F",")")\
                .next_to(manifold,buff=1.5)\
                .shift(.25*DOWN)
        ingen.set_color_by_tex("M", BLUE)
        ingen.set_color_by_tex("F", GREEN)

        self.wait(2)
        self.play(  ShowCreation(ingen))
        self.wait(2)
        self.play(  *[FadeOut(mob)for mob in self.mobjects])

class ready(Scene):
    def construct(self):
        Ale = Alex().scale(.75)
        Ale[4].set_color(GREEN)

        self.play(  GrowFromCenter(Ale))
        self.wait(2)
        self.play(  Blink(Ale))
        self.wait(2)
        self.play(  Blink(Ale))
        self.wait(2)
        self.play(  FadeOut(Ale))
        self.wait()













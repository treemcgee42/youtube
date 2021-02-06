from manimlib.imports import *
from NumberCreature.NumberCreature import *

class nothingelse(Scene):
    def construct(self):
        title = TextMobject("Homotopy").set_color(BLUE).to_edge(UP,buff=.5)
        lhomotopy = TextMobject("Left Homotopy").scale(.75).set_color(BLUE_D)
        rhomotopy = TextMobject("Right Homotopy").scale(.75).set_color(BLUE_D)
        lhomdesc = TextMobject("Defined with \\textit{cylinder} objects").scale(.75)
        rhomdesc = TextMobject("Defined with \\textit{path space} objects").scale(.75)

        lhom = VGroup(
            lhomotopy,
            lhomdesc
        ).arrange_submobjects(
            DOWN,
            aligned_edge=LEFT,
            buff=1
        ).shift(4*LEFT)

        rhom = VGroup(
            rhomotopy,
            rhomdesc
        ).arrange_submobjects(
            DOWN,
            aligned_edge=LEFT,
            buff=1
        ).shift(4*RIGHT)

        divider = Line().rotate(90*DEGREES).scale(2).set_color(BLUE)

        self.play(
            Write(title)
        )
        self.wait(2)
        self.play(
            GrowFromCenter(divider)
        )
        self.wait()
        self.play(
            FadeIn(lhom)
        )
        self.wait(2)
        self.play(
            FadeIn(rhom)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

class def122(Scene):
    def construct(self):
        deftitle = TextMobject("\\textsc{Definition 1.22}").scale(.75).to_edge(LEFT,buff=MED_LARGE_BUFF)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)
        
        self.play(
            Write(deftitle)
        )
        self.wait(2)

        # standard interval objects part
        defp1 = TextMobject("The standard ", "interval object", " in Top is the compact connected\
                topological").scale(.75)
        defp1[1].set_color(BLUE)
        defp2 = TextMobject("subspace").scale(.75)
        def1 = VGroup(
            defp1,
            defp2
        ).arrange_submobjects(
            DOWN,
            aligned_edge=LEFT,
            buff=.25
        ).shift(1.5*UP)
        defp3 = TexMobject("I:=[0,1]\hookrightarrow\\mathbb{R}").scale(.75).shift(.5*UP)
        defp4 = TextMobject("equipped with the canonical inclusion of its two endpoints")\
                .scale(.75).next_to(def1,direction=DOWN,buff=1.2).shift(1.3*LEFT)
        defp5 = TexMobject("\\ast\\sqcup\\ast\\overset{(\\delta_0,\\delta_1)}{\\longrightarrow}\
                I\\overset{\\exists!}{\\longrightarrow}\\ast").scale(.75)\
                .next_to(defp3,direction=DOWN,buff=1.5)

        self.play(
            FadeIn(def1)
        )
        self.play(
            FadeIn(defp3)
        )
        self.play(
            FadeIn(defp4)
        )
        self.play(
            FadeIn(defp5)
        )
        self.wait(3)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects[1:-1]]
        )
        self.play(
            Transform(defp5,defp5.copy().shift(3*UP))
        )

        i = Line().scale(1.25).set_color(BLUE_E).rotate(90*DEGREES).shift(1*DOWN)
        pt0 = Dot().move_to(i[-1]).set_color(BLUE).shift(1.2*UP)
        pt1 = Dot().move_to(i[-1]).set_color(BLUE).shift(1.2*DOWN)
        pt0l = pt0.copy().shift(3*LEFT)
        pt1l = pt1.copy().shift(3*LEFT)
        ptr = Dot().move_to(i[-1]).set_color(RED).shift(3*RIGHT)

        diagramfori = VGroup(
            i,
            pt0,
            pt1,
            pt0l,
            pt1l,
            ptr
        )

        self.play(
            FadeIn(diagramfori)
        )
        self.wait(2)

        delta0 = Arrow(pt1l,pt1, stroke_width=3, tip_length=.175).scale(.75)
        delta1 = Arrow(pt0l,pt0, stroke_width=3, tip_length=.175).scale(.75)
        d0 = TexMobject("\\delta_0").scale(.5).next_to(delta0,DOWN,buff=.125)
        d1 = TexMobject("\\delta_1").scale(.5).next_to(delta1,UP,buff=.125)
        uniquearr = Arrow(Dot().move_to(i[-1]),ptr, stroke_width=3, tip_length=.175).scale(.75)

        self.play(
            ShowCreation(delta0),
            ShowCreation(delta1)
        )
        self.play(
            FadeIn(d0),
            FadeIn(d1)
        )
        self.wait()
        self.play(
            ShowCreation(uniquearr)
        )
        self.wait(3)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects[1:]]
        )
        self.wait(2)

        # cylinder object
        c1 = TextMobject("For $X\\in\\operatorname{Top}$, the standard ", "cylinder object", " over $X$\
                is the product topological space", " $X\\times I$",".", alignment="")\
                .scale(.75).shift(2*UP)
        c1[1].set_color(BLUE)
        c1[-2].set_color(BLUE)

        xi = SVGMobject("homotopy/xi.svg").shift(.5*DOWN)
        xi.set_color(RED).set_opacity(.75)
        xi[-1].set_opacity(.25)
        x = xi.copy()[0]
        xlabel = TexMobject("X").scale(.75).next_to(
                    x,
                    direction=DOWN,
                    buff=.25)
        ilabel = TexMobject("I").scale(.75).next_to(
                    xi,
                    direction=LEFT,
                    buff=.3)

        x1 = VGroup(
            x,
            xlabel
        )
        x2 = VGroup(
            xi,
            xlabel.copy(),
            ilabel
        )

        self.play(
            FadeIn(c1)
        )
        self.wait()
        self.play(
            FadeIn(x1)
        )
        self.wait()
        self.play(
            ReplacementTransform(x1,x2)
        )
        self.wait(2)
        self.play(
            FadeOut(x2)
        )
        self.wait(2)

        c2 = TextMobject("It factors the codiagonal:", alignemnt="")\
                .scale(.75).next_to(c1,DOWN,buff=.5).shift(4.4*LEFT)
        c2diag = TexMobject("\\nabla_X:X\\sqcup X\\stackrel{((\\operatorname{id},\\delta_0),\
                    (\\operatorname{id},\\delta_1))}{\\longrightarrow}X\\times I\
                    \\to X").scale(.75).next_to(c2,direction=DOWN,buff=.5).shift(4.5*RIGHT)

        self.play(
            FadeIn(c2)
        )
        self.play(
            FadeIn(c2diag)
        )
        self.wait(2)

        factorcodiagonal = ImageMobject("homotopy/factorcodiagonal.png").scale(1.75).shift(1.5*DOWN)

        self.play(
            FadeOut(c2diag),
            FadeIn(factorcodiagonal)
        )
        self.wait(2)
        self.play(
            FadeOut(factorcodiagonal),
            FadeIn(factorcodiagonal.copy().shift(4*RIGHT,1*UP))
        )

        xtwice = VGroup(
            xi.copy()[0],
            xi.copy()[1]
        ).to_edge(LEFT,buff=.75).shift(1*DOWN)
        xi2 = xi.copy().next_to(xtwice,buff=1.25)
        x3 = xi.copy()[0].next_to(xi2,buff=1.25).shift(.7*DOWN)

        incl1 = TexMobject("\\hookrightarrow").next_to(
                    xi2,
                    direction=LEFT,
                    buff=.4).shift(.7*UP)
        incl2 = incl1.copy().shift(1.4*DOWN)
        inclarrs = VGroup(
            incl1,
            incl2
        )
        projarr = TexMobject("\\to").next_to(
                    xi2,
                    direction=RIGHT,
                    buff=.5
        )

        self.play(
            FadeIn(xtwice)
        )
        self.play(
            FadeIn(xi2)
        )
        self.play(
            FadeIn(x3)
        )
        self.wait()
        self.play(
            FadeIn(inclarrs)
        )
        self.play(
            FadeIn(projarr)
        )
        self.wait(3)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

class def123(Scene):
    def construct(self):
        deftitle = TextMobject("\\textsc{Definition 1.23}").scale(.75).to_edge(LEFT,buff=MED_LARGE_BUFF)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)
        
        self.play(
            Write(deftitle)
        )
        self.wait(2)

        d1 = TextMobject("For $X,Y\\in\\operatorname{Top}$ and $$f,g:X\\to Y,$$ a ","left\
                homotopy", "$$\\eta:f\\Rightarrow_L g$$ is a continuous function\
                $$\\eta:X\\times I\\to Y$$ out of the standard cylinder object over\
                $X$ such that this fits into a commuting diagram of the form", alignment="")\
                .scale(.75)
        d1[1].set_color(BLUE)

        self.play(
            FadeIn(d1)
        )
        self.wait(3)
        self.play(
            FadeOut(d1)
        )

        lhd = ImageMobject("homotopy/lhomdiagram.png").shift(4*LEFT, .5*DOWN).scale(2.5)
        fvlh = SVGMobject("homotopy/fvlh.svg", fill_opacity=0).scale(.75).shift(3*RIGHT,.5*DOWN)
        ffvlh = fvlh.copy()[0]
        gfvlh = fvlh.copy()[1]

        self.play(
            FadeIn(lhd)
        )
        self.wait(2)
        self.play(
            ShowCreation(ffvlh)
        )
        self.wait()
        self.play(
            ReplacementTransform(ffvlh,gfvlh)
        )
        self.wait(2)
        self.play(
            FadeOut(gfvlh)
        )
        self.wait()

        svlh = SVGMobject("homotopy/svlh.svg", fill_opacity=.25)\
                    .shift(3*RIGHT,.5*DOWN).scale(1.5).set_color(RED)
        imf = SVGMobject("homotopy/svlh.svg", fill_opacity=.75)\
                    .shift(3*RIGHT,.5*DOWN).scale(1.5).set_color(WHITE)[0]
        img = SVGMobject("homotopy/svlh.svg", fill_opacity=.75)\
                    .shift(3*RIGHT,.5*DOWN).scale(1.5).set_color(WHITE)[1]
        etafg = svlh[2:]

        self.play(
            FadeIn(imf)
        )
        self.play(
            FadeIn(img)
        )
        self.wait()
        self.play(
            ShowCreation(etafg)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

class ex124(Scene):
    def construct(self):
        extitle = TextMobject("\\textsc{Example 1.24}").scale(.75).to_edge(LEFT,buff=MED_LARGE_BUFF)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)

        self.play(
            Write(extitle)
        )
        self.wait(2)

        diag = ImageMobject("homotopy/ex124diag.png").shift(3*LEFT,.5*DOWN).scale(2)
        pic = SVGMobject("homotopy/ex124pic.svg").shift(3*RIGHT,.5*DOWN).scale(1.5)[:2]
        etaforpic = SVGMobject("homotopy/ex124pic.svg", fill_opacity=0)\
                    .shift(3*RIGHT,.5*DOWN).scale(1.5).set_color(RED)[-1]

        self.play(
            FadeIn(diag)
        )
        self.wait(2)
        self.play(
            FadeIn(pic)
        )
        self.play(
            ShowCreation(etaforpic)
        )
        self.wait(3)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

class ex125(Scene):
    def construct(self):
        extitle = TextMobject("\\textsc{Example 1.25}").scale(.75).to_edge(LEFT,buff=MED_LARGE_BUFF)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)

        self.play(
            Write(extitle)
        )
        self.wait(2)

        diag = ImageMobject("homotopy/ex125diag.png").shift(3*LEFT,.5*DOWN).scale(2)
        pic1 = SVGMobject("homotopy/ex125pic.svg").shift(3*RIGHT, .5*DOWN).scale(1.5)[:-1]
        pic2 = SVGMobject("homotopy/ex125pic.svg", fill_opacity=.25).shift(3*RIGHT, .5*DOWN)\
                .scale(1.5).set_color(RED)[-1]

        self.play(
            FadeIn(diag)
        )
        self.wait(2)
        self.play(
            FadeIn(pic1)
        )
        self.wait()
        self.play(
            Transform(pic1.copy()[0],pic1.copy()[1]),
            ShowCreation(pic2)
        )
        self.wait(2)

        eq = TexMobject("\\eta(x,t):=x(1-t)").scale(.75).set_color(RED)\
                .next_to(pic1,direction=UP,buff=1)

        self.play(
            FadeIn(eq)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

class def126(Scene):
    def construct(self):
        deftitle = TextMobject("\\textsc{Definition 1.26}").scale(.75).to_edge(LEFT,buff=MED_LARGE_BUFF)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)
        
        self.play(
            Write(deftitle)
        )
        self.wait(2)

        d1 = TextMobject("For $X\\in\\operatorname{Top}$, the ","0-th homotopy \\textit{set}",\
                " $\\pi_0(X)$ is the left homotopy equivalence classes of points \
                $x:\\ast\\to X$, i.e. the ","path connected components"," of $X$. This yields a functor\
                $$\\pi_0:\\operatorname{Top}\\to\\operatorname{Set}.$$"\
                ,alignment="").scale(.75).shift(2*UP)
        d1[1].set_color(BLUE)
        d1[-2].set_color(RED)

        self.play(
            Write(d1)
        )
        self.wait(3)

        expi0 = VGroup(
            TexMobject("X\\quad\\quad\\quad \\pi_0(X)"),
            TexMobject("Y\\quad\\quad\\quad \\pi_0(Y)"),
            TexMobject("X\\to Y\\quad\\quad \\pi_0(X)\\to\\pi_0(Y)")
        ).arrange_submobjects(
            DOWN,
            buff=.5
        ).scale(.75).shift(1*DOWN)

        self.play(
            FadeIn(expi0)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects[1:]]
        )

        d2 = TextMobject("For $n\\in\\mathbb{N}$, $n\\geq 1$, the ","$n$th homotopy group",\
                " $\\pi_n(X,x)$ of $X$ at $x$ is the group with:", alignment="").scale(.75)\
                .shift(2*UP)
        d2[1].set_color(BLUE)
        dp1 = TextMobject("- underlying set consisting of left homotopy equivalence classes of maps\
                $\\{I^n\\to X:\\partial I^n\\to x\\}$ where the left homotopies $\\eta$\
                \\textit{are constrained to be constant on the boundary};",alignment="").scale(.75)
        dp2 = TextMobject("- group product operation taking $[\\alpha:I^n\\to X]$ and\
                $[\\beta:I^n\\to X]$ to $[\\alpha\\cdot \\beta]$ with\
                $$\\alpha\\cdot\\beta:I^n\\overset{\\simeq}{\\longrightarrow}\
                I^n\\underset{I^{n-1}}{\\sqcup}I^n\\overset{(\\alpha,\\beta)}{\\longrightarrow}\
                X$$").scale(.75)
        dp1alone = dp1.copy().shift(2*UP)

        dps = VGroup(
            dp1,
            dp2,
        ).arrange_submobjects(
            DOWN,
            aligned_edge=LEFT,
            buff=.5
        ).next_to(d2, direction=DOWN,buff=.5)

        self.play(
            Write(d2)
        )
        self.play(
            FadeIn(dps)
        )
        self.wait(3)
        self.play(
            FadeOut(d2),
            FadeOut(dps),
            FadeIn(dp1alone)
        )
        self.wait()

        i = Line()
        d0 = Dot().move_to(i.get_points()[0])
        d1 = Dot().move_to(i.get_points()[-1])
        ilabel = TexMobject("I").scale(.75).next_to(i,direction=DOWN,buff=.5)

        igp = VGroup(
            i,
            d0,
            d1,
            ilabel
        ).shift(3*LEFT,1*DOWN).set_color(BLUE)

        x = Annulus(fill_opacity=0, stroke_width=2.5).scale(.75)\
                .next_to(igp,buff=2)
        smallx = Dot().move_to(x).shift(1.125*DOWN)
        xlabel = TexMobject("X").scale(.75).next_to(x,direction=DOWN,buff=.5)

        xgp = VGroup(
            x,
            xlabel,
            smallx
        ).shift(.5*UP)

        self.play(
            FadeIn(igp)
        )
        self.play(
            FadeIn(xgp)
        )
        self.wait()

        circ1 = Circle().move_to(smallx).set_color(BLUE).shift(1*UP)\
                .scale(1)
        circ1dot = smallx.copy().set_color(BLUE)
        c1 = VGroup(
            circ1,
            circ1dot
        )
        c2 = c1.copy().scale(.25).rotate(-90*DEGREES)\
                .shift(.95*DOWN,.25*RIGHT).set_color(RED)

        self.play(
            ReplacementTransform(igp.copy()[:-1], c1)
        )
        self.wait()
        self.play(
            ReplacementTransform(igp.copy()[:-1], c2)
        )
        self.wait(3)
        self.play(
            *[FadeOut(mob)for mob in [igp,xgp,c1,c2]]
        )
        self.wait()

        square = Square(fill_opacity=.25).shift(3*LEFT, 1*DOWN).set_color(BLUE)
        sphere = Sphere().shift(3*RIGHT, 1*DOWN)

        self.play(
            FadeIn(square)
        )
        self.play(
            FadeIn(sphere)
        )
        self.wait(2)
        self.play(
            FadeOut(square),
            FadeOut(sphere),
            FadeOut(dp1alone)
        )

        dp2alone = dp2.copy().shift(3*UP)

        self.play(
            FadeIn(dp2alone)
        )
        self.wait()

        i2 = Square(fill_opacity=.25).shift(3*LEFT,1*DOWN)

        i21 = i2.copy().shift(4*RIGHT).set_color(RED)
        i22 = i21.copy().shift(2.03*RIGHT).set_color(BLUE)

        self.play(
            FadeIn(i2)
        )
        self.wait()
        self.play(
            FadeIn(i21),
            FadeIn(i22)
        )
        self.wait(3)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects[1:]]
        )
        self.wait()

        functor = TexMobject("\\pi_{\\bullet\\geq 1}:\\operatorname{Top}^{\\ast /}\\longrightarrow\
                    \\operatorname{Grp}^{\\mathbb{N}_{\\geq 1}}").scale(.75)

        self.play(
            FadeIn(functor)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

class def128(Scene):
    def construct(self):
        deftitle = TextMobject("\\textsc{Definition 1.28}").scale(.75).to_edge(LEFT,buff=MED_LARGE_BUFF)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)
        
        self.play(
            Write(deftitle)
        )
        self.wait(2)

        d1 = TextMobject("A continuous function $f:X\\to Y$ is called a ","homotopy equivalence"," if\
                there exists a continuous function $g:Y\\to X$ and left homotopies $$\\eta_1:f\\circ g\
                \\Rightarrow_L\\operatorname{id}_Y$$ and $$\\eta_2:g\\circ f\\Rightarrow_L\
                \\operatorname{id}_X.$$", alignment="").scale(.75)
        d1[1].set_color(BLUE)

        self.play(
            Write(d1)
        )
        self.wait(3)
        self.play(
            FadeOut(d1)
        )
        self.wait()

        pt1 = TextMobject("(left) homotopy\\qquad\\qquad between functions").scale(.75).shift(.25*UP)
        pt2 = TextMobject("homotopy equivalence\\qquad\\qquad between spaces").scale(.75)\
                .next_to(pt1,direction=DOWN,buff=.5)

        self.play(
            FadeIn(pt1)
        )
        self.wait()
        self.play(
            FadeIn(pt2)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

class ex129(Scene):
    def construct(self):
        extitle = TextMobject("\\textsc{Example 1.29}").scale(.75).to_edge(LEFT,buff=MED_LARGE_BUFF)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)
        
        self.play(
            Write(extitle)
        )
        self.wait(2)

        xi = SVGMobject("homotopy/xi.svg",fill_opacity=.25).set_color(RED).shift(1*LEFT)
        x = xi.copy().next_to(xi,direction=LEFT,buff=2)[0]
        inclarr = TexMobject("\\hookrightarrow").next_to(xi,direction=LEFT,buff=.8).shift(.7*DOWN)
        parr = TexMobject("\\overset{p}{\\swarrow}").next_to(xi,direction=LEFT,buff=.8).shift(.2*UP)

        self.play(
            FadeIn(x)
        )
        self.play(
            FadeIn(xi)
        )
        self.wait()
        self.play(
            FadeIn(inclarr),
            FadeIn(parr)
        )
        self.wait(2)

        forward = TexMobject("X\\overset{(\\operatorname{id},\\delta_0)}{\\longrightarrow}\
                    X\\times I\\overset{p}{\\longrightarrow}X").scale(.75).shift(4*RIGHT,1*UP)
        eta2 = TextMobject("$$\\eta_2:p\\circ(\\operatorname{id},\\delta_0)\\Rightarrow_L\
                \\operatorname{id}_X$$ is trival (constant)!").scale(.75).next_to(forward,\
                direction=DOWN,buff=1)

        defret = TextMobject("``deformation retract''").set_color(BLUE).next_to(inclarr,\
                    direction=DOWN,buff=1.5)

        self.play(
            ShowCreation(forward)
        )
        self.wait()
        self.play(
            FadeIn(eta2)
        )
        self.wait(2)
        self.play(
            Write(defret)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in [defret,eta2,forward]]
        )

        reverse = TexMobject("X\\times I\\overset{p}{\\longrightarrow}\
                    X\\overset{(\\operatorname{id},\\delta_0)}{\\longrightarrow}X\\times I").scale(.75)\
                    .shift(4*RIGHT,1*UP)

        eta1 = TexMobject("\\eta_1:(\\operatorname{id},\\delta_0)\\circ p\\Rightarrow_L\
                    \\operatorname{id}_{X\\times I}").scale(.75).next_to(reverse,direction=DOWN,buff=.5)
        eta1def = TexMobject("\\eta_1(x,t)=x(1-t)").scale(.75).next_to(reverse,direction=DOWN\
                    ,buff=1)

        self.play(
            Write(reverse)
        )
        self.wait()
        self.play(
            FadeIn(eta1)
        )
        self.play(
            FadeIn(eta1def)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

class def130(Scene):
    def construct(self):
        deftitle = TextMobject("\\textsc{Definition 1.30}").scale(.75).to_edge(LEFT,buff=MED_LARGE_BUFF)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)
        
        self.play(
            Write(deftitle)
        )
        self.wait(2)

        d1 = TextMobject("A continuous function $f:X\\to Y$ is called a ", "weak homotopy\
                equivalence", " if its image under all the homotopy group functors is an\
                isomorphism: $$\\pi_0(f):\\pi_0(X)\\overset{\\simeq}{\\longrightarrow}\
                \\pi_0(Y)$$ and for all $x\\in X$ and all $n\\geq 1$ $$\\pi_n(f)\
                :\\pi_n(X,x)\\overset{\\simeq}{\\longrightarrow}\\pi_n(Y,f(x)).$$",alignment="")\
                .scale(.75).shift(0*UP)
        d1[1].set_color(BLUE)

        self.play(
            FadeIn(d1)
        )
        self.wait(3)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

class prop131(Scene):
    def construct(self):
        proptitle = TextMobject("\\textsc{Proposition 1.30}").scale(.75).to_edge(LEFT,buff=MED_LARGE_BUFF)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)
        
        self.play(
            Write(proptitle)
        )
        self.wait(2)

        transition = TextMobject("\\begin{tabular}{ c c }(left) homotopy & between functions\\\\ \
                    homotopy equivalence & between spaces \\\\ \
                    weak homotopy equivalence & between spaces\\end{tabular}").scale(.75)

        self.play(
            FadeIn(transition)
        )
        self.wait(2)
        self.play(
            FadeOut(transition)
        )
        self.wait()

        prop = TextMobject("Every homotopy equivalence is a weak homotopy equivalence.").scale(.75)

        self.play(
            Write(prop)
        )
        self.wait(2)
        self.play(
            FadeOut(prop)
        )
        
        pftitle = TextMobject("Proof:").scale(.75).to_edge(LEFT,buff=.5).shift(2*UP)
        pf1 = TextMobject("For all $X\\in\\operatorname{Top}$, the inclusion maps\
                $$X\\overset{(\\operatorname{id},\\delta_0)}{\\longrightarrow}X\\times I$$\
                are weak homotopy equivalences.", alignment="").scale(.75)
        pf2 = TextMobject("Given a general homotopy equivalence:").scale(.75)

        pf = VGroup(
            pftitle,
            pf1,
            pf2
        ).arrange_submobjects(
            DOWN,
            aligned_edge=LEFT,
            buff=.25
        ).to_edge(LEFT,buff=.5).shift(1*UP)

        self.play(
            FadeIn(pftitle)
        )
        self.wait()
        self.play(
            Write(pf1)
        )
        self.wait(2)
        self.play(
            ReplacementTransform(pf1,pf2.shift(2*UP))
        )
        self.wait()

        diag1 = ImageMobject("homotopy/prop131x.png").to_edge(LEFT,buff=1.5).scale(2).shift(1*DOWN)
        diag2 = ImageMobject("homotopy/prop131y.png").next_to(
            diag1,
            direction=RIGHT,
            buff=1.5
        ).scale(2)

        self.play(
            FadeIn(diag1),
            FadeIn(diag2)
        )
        self.wait(2)

        trivial = TexMobject("\\pi_\\bullet(f)\\circ\\pi_\\bullet(g)\\cong\\pi_\\bullet(\\operatorname{id})\
                    \\cong\\pi_\\bullet(g)\\circ\\pi_\\bullet(f)")\
                .scale(.75).next_to(pf2,buff=.75)

        self.play(
            Write(trivial)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

class rmk132(Scene):
    def construct(self):
        rmktitle = TextMobject("\\textsc{Remark 1.32}").scale(.75).to_edge(LEFT,buff=MED_LARGE_BUFF)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)
        
        self.play(
            Write(rmktitle)
        )
        self.wait(2)

        r1 = TextMobject("The converse is not true in general!").scale(.75)
        r2 = TextMobject("But as we will see:").scale(.75)

        r = VGroup(
            r1,
            r2
        ).arrange_submobjects(
            DOWN,
            aligned_edge=LEFT,
            buff=.5
        ).to_edge(LEFT).shift(1.5*UP)

        pt1 = TextMobject("- The converse holds for ``CW complexes'' (Whitehead's Theorem)").scale(.75)
        pt2 = TextMobject("- Every topological space is weak homotopy equivalent to a \
                CW complex (via CW approximation)", alignment="").scale(.75)

        pts = VGroup(
            pt1,
            pt2
        ).arrange_submobjects(
            DOWN,
            buff=.25,
            aligned_edge=LEFT
        ).shift(1*DOWN)

        self.play(
            FadeIn(r1)
        )
        self.wait()
        self.play(
            FadeIn(r2)
        )
        self.play(
            FadeIn(pts)
        )
        self.wait(2)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

class ex133(Scene):
    def construct(self):
        extitle = TextMobject("\\textsc{Example 1.33}").scale(.75).to_edge(LEFT,buff=MED_LARGE_BUFF)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)
        
        self.play(
            Write(extitle)
        )
        self.wait(2)

        e1 = TextMobject("The projection $X\\times I\\to X$ is a weak homotopy equivalence.\
                Thus we can factor the codiagonal $\\nabla_X$ and consider it as a monomorphism \
                when considering homotopy groups: $$\\nabla_X:X\\sqcup X\\hookrightarrow\
                X\\times I\\overset{\\simeq}{\\longrightarrow}X.$$", alignment="").scale(.75)
        e2 = TextMobject("In fact, we get even better properties than a generic monomorphism: \
                this monomorphism has the ``left lifting property'' against all ``Serre fibrations'' \
                that are weak homotopy equivalences.", alignment="").scale(.75)

        e = VGroup(
            e1,
            e2
        ).arrange_submobjects(
            DOWN,
            aligned_edge=LEFT,
            buff=1
        ).shift(.5*UP)

        self.play(
            FadeIn(e1)
        )
        self.wait(2)
        self.play(
            FadeIn(e2)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

class def134(Scene):
    def construct(self):
        deftitle = TextMobject("\\textsc{Definition 1.34}").scale(.75).to_edge(LEFT,buff=MED_LARGE_BUFF)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)
        
        self.play(
            Write(deftitle)
        )
        self.wait(2)

        d1 = TextMobject("For $X\\in\\operatorname{Top}$, the ","standard topological path space\
                object" " is the mapping space $X^I$.").scale(.75)

        self.play(
            FadeIn(d1)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

class ex135(Scene):
    def construct(self):
        extitle = TextMobject("\\textsc{Example 1.35}").scale(.75).to_edge(LEFT,buff=MED_LARGE_BUFF)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)
        
        self.play(
            Write(extitle)
        )
        self.wait(2)

        e1 = TextMobject("Dually, we can factor the diagonal of $X$ with the path space object:\
                $$\\Delta_X:X\\overset{X^{I\\to\\ast}}{\\longrightarrow}X^I\
                \\overset{X^{\\ast\\sqcup\\ast\\to I}}{\\longrightarrow}X\\times X.$$").scale(.75)
        e2 = TextMobject("This can be very helpful, for example").scale(.75)
        e = VGroup(
            e1,
            e2
        ).arrange_submobjects(
            DOWN,
            aligned_edge=LEFT,
            buff=1
        ).shift(1*UP)

        pt1 = TextMobject("- $X^{I\\to\\ast}$ is a weak homotopy equivalence").scale(.75)
        pt2 = TextMobject("- $X^{\\ast\\sqcup\\ast\\to I}$ is a Serre fibration").scale(.75)
        pts = VGroup(
            pt1,
            pt2
        ).arrange_submobjects(
            DOWN,
            aligned_edge=LEFT,
            buff=.25
        ).next_to(e,direction=DOWN,buff=.25)

        self.play(
            FadeIn(e1)
        )
        self.wait()
        self.play(
            FadeIn(e2)
        )
        self.play(
            FadeIn(pts)
        )
        self.wait(2)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

class def136(Scene):
    def construct(self):
        deftitle = TextMobject("\\textsc{Definition 1.36}").scale(.75).to_edge(LEFT,buff=MED_LARGE_BUFF)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)
        
        self.play(
            Write(deftitle)
        )
        self.wait(2)

        d1 = TextMobject("For continuous functions $f,g:X\\to Y$ between topological spaces \
                $X,Y$, a ","right homotopy"," $f\\Rightarrow_R g$ is a continuous function\
                $$\\eta:X\\to Y^I$$ into the path space object of $Y$ such that the following\
                diagram commutes:", alignment="").scale(.75).shift(1*UP)
        d1[1].set_color(BLUE)

        diag = ImageMobject("homotopy/def136diag.png").scale(1.5).next_to(d1,direction=DOWN,buff=.5)

        self.play(
            FadeIn(d1)
        )
        self.play(
            FadeIn(diag)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )


















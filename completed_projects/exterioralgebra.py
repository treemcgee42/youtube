from manimlib.imports import *
from NumberCreature.NumberCreature import *

class intro(Scene):
    def construct(self):
        oneforms = TextMobject("1-forms")\
                    .scale(.75)\
                    .shift(1*UP)
        vfields = TextMobject("Vector fields")\
                    .scale(.75)\
                    .shift(1*DOWN)
        dl1 = DashedLine(oneforms.get_center(),vfields.get_center())\
                    .scale(.75)

        self.play(  Write(oneforms), Write(vfields))
        self.play(  ShowCreation(dl1))
        self.wait()

        pt = TexMobject("p\\in M")\
                .scale(.75)\
                .shift(4*LEFT)

        l1 = Line(pt.get_right(),oneforms.get_left())\
                .scale(.75)\
                .set_color(GREEN)
        l2 = Line(pt.get_right(),vfields.get_left())\
                .scale(.75)\
                .set_color(BLUE)

        tspace = TexMobject("v\\in T_p\\mathbb{R}^n")\
                    .scale(.75)\
                    .next_to(oneforms,buff=3)
        
        ctspace = TexMobject("\\omega\\in T_p^\\ast\\mathbb{R}^n")\
                    .scale(.75)\
                    .next_to(vfields,buff=3)

        l11 = Line(oneforms.get_right(),tspace.get_left())\
                .scale(.75)\
                .set_color(GREEN)

        l22 = Line(vfields.get_right(),ctspace.get_left())\
                .scale(.75)\
                .set_color(BLUE)

        self.play(  *[Write(mob)for mob in[pt,tspace,ctspace]])
        self.wait()
        self.play(  *[ShowCreation(mob)for mob in [l1,l2]])
        self.play(  *[ShowCreation(mob)for mob in [l11,l22]])
        self.wait(2)

        kforms = TextMobject("$k$-forms")\
                    .scale(.75)\
                    .move_to(oneforms.get_center())
        extalg = TexMobject("\\omega\\in\\Lambda^k(T_p^\\ast\\mathbb{R}^n)")\
                    .scale(.75)\
                    .move_to(tspace.get_center())

        pvfields = TextMobject("$p$-vector fields")\
                    .scale(.75)\
                    .move_to(vfields.get_center())
        extalg2 = TexMobject("\\wedge v_i\\in\\Lambda^k(T_p\\mathbb{R}^n)")\
                    .scale(.75)\
                    .move_to(ctspace.get_center())

        l211 = Line(kforms.get_right(),extalg.get_left())\
                .scale(.75)\
                .set_color(GREEN)
        l222 = Line(vfields.get_right(),extalg2.get_left())\
                .scale(.75)\
                .set_color(BLUE)


        self.play(  Transform(oneforms,kforms),Transform(tspace,extalg),\
                    Transform(l11,l211))
        self.wait(2)
        self.play(  Transform(vfields,pvfields), Transform(ctspace,extalg2),\
                    Transform(l22,l222))
        self.wait(2)
        self.play(  *[FadeOut(mob)for mob in self.mobjects])

class outline(Scene):
    def construct(self):
        toc = TextMobject("\\begin{itemize} \\item Tensors\
                \\item The alternate function\
                \\item The exterior algebra \\end{itemize}")
        self.add(toc)

class basictensors(Scene):
    def construct(self):
        vspace = TextMobject("$V$ is an $n$-dimensional vector space.")\
                    .scale(.75)\
                    .shift(2*UP)
        t = TexMobject("T:V^k\\rightarrow\\mathbb{R}")\
                    .scale(.75)\
                    .next_to(vspace,direction=DOWN,buff=MED_LARGE_BUFF)
        givenby = TextMobject("given by")\
                    .scale(.75)\
                    .next_to(t,direction=DOWN,buff=MED_SMALL_BUFF)
        themap = TexMobject("v\\mapsto T(v_1,\\dots,v_{i-1},v_i,v_{i+1},\\dots,v_k)")\
                    .scale(.75)\
                    .next_to(givenby,direction=DOWN,buff=MED_SMALL_BUFF)
        islinear = TextMobject("is $k$-linear (a $k$-tensor)")\
                    .scale(.75)\
                    .next_to(themap,direction=DOWN,buff=MED_SMALL_BUFF)
        ifits = TextMobject("if it is linear in its $i$th variable for $i=1,\\dots,k$")\
                    .scale(.75)\
                    .next_to(islinear,direction=DOWN,buff=MED_SMALL_BUFF)
        
        lk = TexMobject("L^k(V)\\coloneqq \{\\mbox{the set of all }k\\mbox{-tensors}\}")

        self.add(lk)

class connections(Scene):
    def construct(self):
        t = TexMobject("T:V^k\\rightarrow\\mathbb{R}")\
                    .scale(.75)\
                    .shift(2*UP)
        s = TexMobject("S\\in V^\\ast:V\\rightarrow\\mathbb{R}")\
                    .scale(.75)\
                    .next_to(t,direction=DOWN,buff=MED_SMALL_BUFF)

        fori = TextMobject("For $i=1,\\dots,k$ and $l_i\\in V^\\ast$, we have")\
                    .scale(.75)\
                    .next_to(s,direction=DOWN,buff=LARGE_BUFF)
        tprod = TexMobject("T=l_1\\otimes\\cdots\\otimes l_k\\in L^k(V),")\
                    .scale(.75)\
                    .next_to(fori,direction=DOWN,buff=MED_SMALL_BUFF)
        tprod2 = TexMobject("T(v_1,\\dots,v_k)=l_1(v_1)\\cdots l_k(v_k)")\
                    .scale(.75)\
                    .next_to(tprod,direction=DOWN,buff=MED_SMALL_BUFF)

        self.add(t,s,fori,tprod,tprod2)

class multiindex(Scene):
    def construct(self):
        fora = TextMobject("For a $k$ multi-index $I$,")\
                    .scale(.75)\
                    .shift(2*UP)
        eI = TexMobject("e_I = e_{i_1}\\otimes\\cdots\\otimes e_{i_k}")\
                    .scale(.75)\
                    .next_to(fora,direction=DOWN,buff=MED_SMALL_BUFF)

        basisv = TextMobject("Suppose the $\{e_i\}$ and its dual $\{e^\\ast_i\}$ are bases for $V$ and $V^\\ast$.")\
                    .scale(.75)\
                    .next_to(eI,direction=DOWN,buff=LARGE_BUFF)

        basisofl = TextMobject("The $\{e_I^\\ast\}$ form a basis of $L^k(V)$.")\
                    .scale(.75)\
                    .next_to(basisv,direction=DOWN,buff=MED_SMALL_BUFF)

        self.add(fora,eI, basisv, basisofl)

class sign(Scene):
    def construct(self):
        sig = TexMobject("\\sigma\\in S_k")\
                    .scale(.75)\
                    .shift(1*UP)
        signeq = TexMobject("(-1)^\\sigma=\\prod_{i<j}\\dfrac{x_{\\sigma(i)}-x_{\\sigma(j)}}{x_i-x_j}")\
                    .scale(.75)\
                    .next_to(sig,direction=DOWN,buff=MED_SMALL_BUFF)

        self.add(sig,signeq)










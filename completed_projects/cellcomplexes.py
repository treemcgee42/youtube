from manimlib.imports import *
from NumberCreature.NumberCreature import *

class def137(Scene):
    def construct(self):
        deftitle = TextMobject("\\textsc{Definition 1.37}").scale(.75).to_edge(LEFT,buff=MED_LARGE_BUFF)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)
        
        self.play(
            Write(deftitle)
        )
        self.wait(2)

        d1 = TextMobject("We call the set of canonical boundary inclusion maps of standard\
                $n$-disks $$I_{\\operatorname{Top}}:=\\Big\\{S^{n-1}\\overset{\\iota_n}{\\hookrightarrow}\
                D^n\\Big\\}_{n\\in\\mathbb{N}}\\subset\\operatorname{Mor}(\\operatorname{Top})$$\
                the set of standard ","topological generating cofibrations",".", alignment="")\
                .scale(.75)
        d1[1].set_color(BLUE)

        self.play(
            Write(d1)
        )
        self.wait(3)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

class def138(Scene):
    def construct(self):
        deftitle = TextMobject("\\textsc{Definition 1.38}").scale(.75).to_edge(LEFT,buff=MED_LARGE_BUFF)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)
        
        self.play(
            Write(deftitle)
        )
        self.wait(2)

        d1 = TextMobject("An ","$n$-cell attachment"," is the pushout of a generating\
        cofibration along some continuous function $\phi$:", alignment="").scale(.75).shift(1.5*UP)
        d1[1].set_color(BLUE)
        d1pic = ImageMobject("cellcomplexes/def138no1.png").scale(1.25).next_to(d1,direction=DOWN,buff=.5)

        dn = Circle(stroke_color=YELLOW,fill_color=RED,fill_opacity=.25).scale(.75)\
                .next_to(d1pic,direction=LEFT,buff=2)

        x = VGroup(
            SVGMobject("homotopy/xi.svg",fill_opacity=.25,fill_color=RED,stroke_width=0)[0],
            Line().scale(.25).set_color(YELLOW).shift(.75*DOWN)
        ).next_to(d1pic,buff=1.5)

        self.play(
            FadeIn(d1)
        )
        self.play(
            FadeIn(d1pic)
        )
        self.wait(2)

        self.play(
            FadeIn(dn)
        )
        self.play(
            FadeIn(x)
        )
        self.wait(3)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects[1:]]
        )

        d2 = TextMobject("A ","topological relative cell complex"," is a continuous function\
                $f:X\\to Y$ exhibited by a (possibly infinite) sequence of cell attachments to \
                $X$, i.e. $f$ is a transfinite composition of pushouts of coproducts of \
                generating cofibrations:", alignment="").scale(.75).shift(1.5*UP)
        d2[1].set_color(BLUE)
        d2pic = ImageMobject("cellcomplexes/def138no2.png").scale(1.25)\
                    .next_to(d2,direction=DOWN,buff=.5)

        self.wait()
        self.play(
            FadeIn(d2)
        )
        self.play(
            FadeIn(d2pic)
        )
        self.wait(3)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects[1:]]
        )
        self.wait()

        d3 = TextMobject("A topological space $X$ is a ","cell complex", " if $\\emptyset\\to X$ \
                is a relative cell complex.").scale(.75)
        d3[1].set_color(BLUE)

        self.play(
            FadeIn(d3)
        )
        self.wait(3)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects[1:]]
        )
        self.wait()

        d4p1 = TextMobject("A ", "finite relative cell complex"," is obtained from a finite \
                number of cell attachments.", alignment="").scale(.75)
        d4p1[1].set_color(BLUE)
        d4p2 = TextMobject("A (relative) cell complex is a (relative) ","CW-complex"," if the\
                transfinite composition is countable:", alignment="").scale(.75)
        d4p2[1].set_color(BLUE)

        d4 = VGroup(
            d4p1,
            d4p2
        ).arrange_submobjects(
            DOWN,
            aligned_edge=LEFT,
            buff=.5
        ).shift(1*UP)
        d4pic = ImageMobject("cellcomplexes/def138no3.png").scale(1.25).next_to(d4,direction=DOWN,\
                    buff=.5)

        self.play(
            FadeIn(d4p1)
        )
        self.wait()
        self.play(
            FadeIn(d4p2)
        )
        self.play(
            FadeIn(d4pic)
        )
        self.wait(3)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

class rmk139(Scene):
    def construct(self):
        rmktitle = TextMobject("\\textsc{Remark 1.39}").scale(.75).to_edge(LEFT,buff=MED_LARGE_BUFF)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)
        
        self.play(
            Write(rmktitle)
        )
        self.wait(2)

        r1 = TextMobject("A cell complex precisely refers to a function $f:X\\to Y$ along \
                with the precise pushouts and cell attachments.", alignment="").scale(.75)

        r2 = TextMobject("But it sometimes can refer to a \\textit{space} that admits some \
                (unspecified) cell decomposition, e.g. $S^n$ is a CW-complex.", alignment="")\
                .scale(.75)

        rgp = VGroup(
            r1,
            r2
        ).arrange_submobjects(
            DOWN,
            aligned_edge=LEFT,
            buff=.5
        )

        self.play(
            FadeIn(r1)
        )
        self.wait()
        self.play(
            FadeIn(r2)
        )
        self.wait(3)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

class lemma140(Scene):
    def construct(self):
        lemmatitle = TextMobject("\\textsc{Lemma 1.40}").scale(.75).to_edge(LEFT,buff=MED_LARGE_BUFF)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)
        
        self.play(
            Write(lemmatitle)
        )
        self.wait(2)

        l1 = TextMobject("Every compact subspace of a topological cell complex intersects \
                the interior of a finite number of cells (assuming the axiom \
                of choice and the law of excluded middle).", alignment="").scale(.75)

        self.play(
            FadeIn(l1)
        )
        self.wait(2)
        self.play(
            FadeOut(l1)
        )

        pftitle = TextMobject("Pf:").scale(.75).next_to(lemmatitle,direction=DOWN,buff=.5)\
                    .shift(.75*LEFT)

        self.play(
            FadeIn(pftitle)
        )

        pf1 = TextMobject("Let $Y\\in\\operatorname{Top}$ and $C\\hookrightarrow Y$ compact.\
                \\\\Define $P\\subset Y$ by choosing one point in the interior of the \
                intersection with $C$ of each cell of $Y$ that intersects $C$.", alignment="")\
                .scale(.75).shift(1.5*UP)

        pf2 = TextMobject("Let $c\\in C$. If $c$ is a 0-cell, write $U_c:=\{c\}$. Otherwise \
                write $e_c$ for the (unique) cell of $Y$ containing $c$ in its interior.\
                \\\\There is only one point of $P$ in the interior of $e_c$, so there exists \
                an open neighborhood $c\\in U_c\\subset e_c$ containing no points of $P$ \
                beyond possibly $c$ itself.", alignment="").scale(.75).shift(.5*DOWN)

        self.play(
            FadeIn(pf1)
        )
        self.wait(2)
        self.play(
            FadeIn(pf2)
        )
        self.wait(2)
        self.play(
            FadeOut(pf1),
            FadeOut(pf2)
        )

        pf3 = TextMobject("Let $\\alpha_c$ be the ordinal labelling the stage $Y_{\\alpha_c}$ \
                in the transfinite composition in the cell complex at which the cell $e_c$ \
                appears. Let $\\gamma$ be the ordinal of the full cell complex. Then we can \
                define $$T:=\\Big\\{(\\beta,U)\\mid a_c\\leq\\beta\\leq\\gamma,\\ U\
                \\underset{\\text{open}}{\\subset}Y_\\beta,\\ U\\cap Y_{\\alpha_c}=U_c,\\ \
                U\\cap P\\in\\{\\emptyset,\\{c\\}\\}\\Big\\}$$ with partial ordering via\
                $$(\\beta_1,U_1)<(\\beta_2,U_2)\\quad\\iff\\quad\\beta_1<\\beta_2,\\ U_2\\cap\
                Y_{\\beta_1}=U_1.$$", alignment="").scale(.75)

        self.play(
            FadeIn(pf3)
        )
        self.wait(3)
        self.play(
            FadeOut(pf3)
        )

        pf4 = TextMobject("For a chain $(\\beta_s,U_s)_{s\\in S}$ in $(T,<)$, an upper \
                bound is given by $(\\cup_s\\ \\beta_s,\\cup_s\\ U_s)$. Thus $(T,<)$ \
                contains a maximal element $(\\beta_{\\text{max}},U_{\\text{max}})$ by \
                Zorn's lemma.", alignment="").scale(.75).shift(.5*UP)

        pf5 = TextMobject("It is sufficient to show that $\\beta_{\\text{max}}=\\gamma$. \
                We will argue by contradiction", alignment="").scale(.75)\
                .next_to(pf4,direction=DOWN,buff=.5)

        self.play(
            FadeIn(pf4)
        )
        self.wait(2)
        self.play(
            FadeIn(pf5)
        )
        self.wait(2)
        self.play(
            FadeOut(pf4),
            FadeOut(pf5)
        )
        
        pf6 = TextMobject("Assume $\\beta_{\\text{max}}<\\gamma$. We will construct an element \
                of $T$ larger than $(\\beta_{\\text{max}},U_{\\text{max}})$:", alignment="")\
                .scale(.75)
        pf7 = TextMobject("Consider for each cell $d$ at stage $Y_{\\beta_{\\text{max}}+1}$ \
                its attaching map $h_d:S^{n-1}\\to Y_{\\beta_{\\text{max}}}$ and the \
                corresponding preimage open set $h_d^{-1}(U_{\\text{max}})\\subset S^{n-1}$."\
                ,alignment="").scale(.75)
        pf8 = TextMobject("Enlarge all these preimages to open subsets $D^n$ such that \
                their image $U_d$ back in $X_{\\beta_{\\text{max}}+1}$ doesn't contain $c$.",\
                alignment="").scale(.75)
        pf9 = TextMobject("Then $(\\beta_{\\text{max}},U_{\\text{max}})<(\\beta_{\\text{max}}+1,\
                \\cup_d \\ U_d)$, which is a contradiction. Hence $\\beta_\\text{max}=\\gamma$.\
                $\\blacksquare$", alignment="").scale(.75)

        finalpf = VGroup(
            pf6,
            pf7,
            pf8,
            pf9
        ).arrange_submobjects(
            DOWN,
            aligned_edge=LEFT,
            buff=.5
        ).shift(.5*DOWN)

        self.play(
            FadeIn(pf6)
        )
        self.wait()
        self.play(
            FadeIn(pf7)
        )
        self.wait()
        self.play(
            FadeIn(pf8)
        )
        self.wait()
        self.play(
            FadeIn(pf9)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

class def141(Scene):
    def construct(self):
        deftitle = TextMobject("\\textsc{Definition 1.41}").scale(.75).to_edge(LEFT,buff=MED_LARGE_BUFF)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)
        
        self.play(
            Write(deftitle)
        )
        self.wait(2)

        d1 = TextMobject("For $\\mathcal{C}$ a category and $K\\subset\\operatorname{Mor}\
                (\\mathcal{C})$ a sub-class of its morphisms, a ", "relative $K$-cell \
                complex"," is a transfinite composition of pushouts of coproducts of morphisms \
                in $K$.", alignment="").scale(.75)
        d1[1].set_color(BLUE)

        self.play(
            FadeIn(d1)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

class def142(Scene):
    def construct(self):
        deftitle = TextMobject("\\textsc{Definition 1.42}").scale(.75).to_edge(LEFT,buff=MED_LARGE_BUFF)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)
        
        self.play(
            Write(deftitle)
        )
        self.wait(2)

        d1 = TextMobject("The set of standard ","topological generating acyclic cofibrations"," \
                is the set $$J_{\\operatorname{Top}}:=\\Big\\{ D^n\
                \\overset{(\\operatorname{id},\\delta_0)}{\\hookrightarrow}D^n\\times I\
                \\Big\\}_{n\\in\\mathbb{N}}\\subset\\operatorname{Mor}(\\operatorname{Top}).$$\
                Unlike $I_{\\operatorname{Top}}$, these are weak homotopy equivalences \
                (hence ``acyclic'').", alignment="").scale(.75)
        d1[1].set_color(BLUE)

        self.play(
            FadeIn(d1)
        )
        self.wait(3)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

class lemma143(Scene):
    def construct(self):
        lemmatitle = TextMobject("\\textsc{Lemma 1.43}").scale(.75).to_edge(LEFT,buff=MED_LARGE_BUFF)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)
        
        self.play(
            Write(lemmatitle)
        )
        self.wait(2)

        base = SVGMobject("cellcomplexes/lemma143.svg", stroke_width=0, fill_opacity=.25,\
                fill_color=RED)[0]
        up = SVGMobject("cellcomplexes/lemma143.svg", stroke_width=0, fill_opacity=.5,\
                fill_color=RED)[1]
        top = SVGMobject("cellcomplexes/lemma143.svg", stroke_color=YELLOW, fill_opacity=.25,\
                fill_color=RED)[2]

        diag = VGroup(
            base,
            up,
            top
        )

        l1 = TextMobject("For $X$ a CW-complex, its inclusion $X\\overset{(\\operatorname{id},\
                \\delta_0)}{\\longrightarrow}X\\times I$ into its standard cylinder is a \
                $J_{\\operatorname{Top}}$-relative cell complex.", alignment="").scale(.75)\
                .to_edge(LEFT,buff=.5).shift(2.5*UP)

        self.play(
            FadeIn(l1),
        )
        self.wait(2)

        pftitle = TextMobject("Pf:").scale(.75).to_edge(LEFT,buff=.5).shift(1.5*UP)

        self.play(
            FadeIn(pftitle)
        )
        self.wait()

        pf1 = TextMobject("It suffices to show that we can erect cylinders over all cells \
                using $J_{\\operatorname{Top}}$ morphisms. We prove by induction.", alignment="")\
                .scale(.75)
        pf2 = TextMobject("The cylinder over $D^0$ is $D^1$, so we can erect cylinders \
                over all $0$-cells:", alignment="").scale(.75)

        pf1and2 = VGroup(
            pf1,
            pf2
        ).arrange_submobjects(
            DOWN,
            aligned_edge=LEFT,
            buff=.5
        )
        pic = ImageMobject("cellcomplexes/lemma143.png").next_to(pf2,direction=DOWN).shift(1*RIGHT)

        self.play(
            FadeIn(pf1)
        )
        self.wait(2)
        self.play(
            FadeIn(pf2)
        )
        self.play(
            FadeIn(pic)
        )
        self.wait(2)
        self.play(
            FadeOut(pf1),
            FadeOut(pf2),
            FadeOut(pic)
        )

        pf3 = TextMobject("Assume that the cylinder over all $n$-cells has been erected \
                using attachments from $J_{\\operatorname{Top}}$.", alignment="").scale(.75)
        pf4 = TextMobject("For the $(n+1)$ case, observe that the union of any $(n+1)$-cell \
                $\sigma$ of $X$ with the cylinder over its boundary is homeomorphic to \
                $D^{n+1}$. Hence we can attach along $D^{n+1}\\to D^{n+1}\\times I$ to erect \
                the cylinder over $\sigma$.", alignment="").scale(.75)
        pf3and4 = VGroup(
            pf3,
            pf4
        ).arrange_submobjects(
            DOWN,
            aligned_edge=LEFT,
            buff=.5
        ).shift(.1*DOWN)

        d = diag.copy().next_to(pf4,direction=DOWN,buff=.25)

        self.play(
            FadeIn(pf3)
        )
        self.wait(2)
        self.play(
            FadeIn(pf4)
        )
        self.wait(2)
        self.play(
            ShowCreation(d)
        )
        self.wait(3)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        
class lemma144(Scene):
    def construct(self):
        lemmatitle = TextMobject("\\textsc{Lemma 1.44}").scale(.75).to_edge(LEFT,buff=MED_LARGE_BUFF)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)
        
        self.play(
            Write(lemmatitle)
        )
        self.wait(2)

        l1 = TextMobject("The elements of $J_{\\operatorname{Top}}$ are $I_{\\operatorname{Top}}$-\
            relative cell complexes.", aligned_edge="").scale(.75).to_edge(LEFT,buff=.5)\
            .shift(2.5*UP)

        self.play(
            FadeIn(l1)
        )
        self.wait(2)

        pftitle = TextMobject("Pf:", aligned_edge="").scale(.75).to_edge(LEFT,buff=.5).shift(2*UP)

        self.play(
            FadeIn(pftitle)
        )
        self.wait()

        pf1 = TextMobject("There is a homeomorphism", aligned_edge="").scale(.75)
        pf2 = TextMobject("such that the map on the right is the inclusion of \
                one hemisphere into the boundary $n$-sphere of $D^{n+1}$:", aligned_edge="")\
                .scale(.75)

        pf1and2 = VGroup(
            pf1,
            pf2
        ).arrange_submobjects(
            DOWN,
            aligned_edge=LEFT,
            buff=2
        )
        pic1 = ImageMobject("cellcomplexes/lemma144no1.png").next_to(pf1,direction=DOWN,buff=.1)\
                .shift(3.5*RIGHT).shift(.1*UP)

        self.play(
            FadeIn(pf1and2),
            FadeIn(pic1)
        )

        pic2 = ImageMobject("cellcomplexes/lemma144no2.png").next_to(pf2,direction=DOWN).shift(3*LEFT)
        pic3 = ImageMobject("cellcomplexes/lemma144no3.png").next_to(pic2,buff=3)

        self.play(
            FadeIn(pic2),
            FadeIn(pic3)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

class lemma145(Scene):
    def construct(self):
        lemmatitle = TextMobject("\\textsc{Lemma 1.45}").scale(.75).to_edge(LEFT,buff=MED_LARGE_BUFF)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)
        
        self.play(
            Write(lemmatitle)
        )
        self.wait(2)

        l1 = TextMobject("Every $J_{\\operatorname{Top}}$-relative cell complex is a weak \
                homotopy equivalence.", alignment="").scale(.75).to_edge(LEFT,buff=.5)\
                .shift(2.5*UP)

        self.play(
            FadeIn(l1)
        )
        self.wait(2)

        pftitle = TextMobject("Pf:", alignment="").scale(.75).to_edge(LEFT,buff=.5)\
                    .shift(2*UP)

        self.play(
            FadeIn(pftitle)
        )
        self.wait()

        part1 = TextMobject("1. In the finite-dimensional case, each attachment is a weak \
                    homotopy equivalence.", alignment="").scale(.75)
        part2 = TextMobject("2. Extend this to the non-finite case.", alignment="").scale(.75)
        parts = VGroup(
            part1,
            part2
        ).arrange_submobjects(
            DOWN,
            aligned_edge=LEFT,
            buff=.5
        )

        self.play(
            FadeIn(part1)
        )
        self.wait()
        self.play(
            FadeIn(part2)
        )
        self.wait(2)
        self.play(
            FadeOut(part1),
            FadeOut(part2)
        )
        self.wait()

        pf1 = TextMobject("Let $X\\to\\hat{X}=\\underset{\\to\\beta\\leq\\alpha}{\\lim}X_{\\beta}$ \
                be a $J_{\\operatorname{Top}}$-relative cell complex.", alignment="").scale(.75)
        pf2 = TextMobject("Each stage is a pushout:", alignment="").scale(.75)
        pf1and2 = VGroup(
            pf1,
            pf2
        ).arrange_submobjects(
            DOWN,
            aligned_edge=LEFT,
            buff=.5
        ).shift(.5*UP).to_edge(LEFT,buff=.5)
        pic1 = ImageMobject("cellcomplexes/lemma145no1.png").shift(2*DOWN)

        self.play(
            FadeIn(pf1)
        )
        self.wait()
        self.play(
            FadeIn(pf2)
        )
        self.play(
            FadeIn(pic1)
        )
        self.wait(2)
        self.play(
            FadeOut(pf1),
            FadeOut(pf2),
            FadeOut(pic1)
        )
        pic1a=pic1.copy().shift(1*UP,4*LEFT)
        self.play(
            FadeIn(pic1a)
        )
        self.wait()

        pic2a = ImageMobject("cellcomplexes/lemma145no2.png").shift(2.5*RIGHT, 1*DOWN).scale(1.5)
        pic2b = ImageMobject("cellcomplexes/lemma145no3.png").shift(2.5*RIGHT, 1*DOWN).scale(1.5)
        pic2c = ImageMobject("cellcomplexes/lemma145no4.png").shift(2.5*RIGHT, 1*DOWN).scale(1.5)
        
        self.play(
            FadeIn(pic2a)
        )
        self.wait(2)
        self.play(
            FadeOut(pic2a),
            FadeIn(pic2b)
        )
        self.wait(2)
        self.play(
            FadeOut(pic2b),
            FadeIn(pic2c)
        )
        self.wait(2)
        leftdirection = TexMobject("X_\\beta\\to X_{\\beta+1}\\to X_\\beta\\Rightarrow_L\\text{id}")\
                            .scale(.75)

        self.play(
            FadeOut(pic1a), 
            FadeOut(pic2c)
        )
        self.play(
            FadeIn(leftdirection)
        )
        self.wait(2)
        self.play(
            FadeOut(leftdirection)
        )
        self.wait()

        etani = TexMobject("\\eta_{n_i}:D^{n_i}\\times I\\to D^{n_i}\\times I\\\\ \
                    :\\text{id}\\Rightarrow_L (\\text{id},\\delta_0)\\circ p_{n_i}").scale(.75)\
                    .shift(1*UP)
        self.play(
            FadeIn(etani)
        )
        self.wait(2)

        pic3 = ImageMobject("cellcomplexes/lemma145no5.png").shift(4*LEFT,1.5*DOWN).scale(1.25)

        self.play(
            FadeIn(pic3)
        )
        self.wait()

        pic4 = ImageMobject("cellcomplexes/lemma145no6.png").shift(3*RIGHT,1.5*DOWN).scale(1.25)

        self.play(
            FadeIn(pic4)
        )
        self.wait(2)

        t0 = TextMobject("At $t=0$, ", "$\\eta$","$:X_{\\beta+1}\\overset{\\text{id}}{\\to}X_{\\beta+1}$")\
                .scale(.75).shift(1.5*UP)
        t0[1].set_color(RED)

        self.play(
            FadeOut(etani),
            FadeIn(t0)
        )
        self.wait(2)

        t1 = TextMobject("At $t=1$, ","$\\eta$","$:X_{\\beta+1}\\to X_{\\beta}\\to X_{\\beta+1}$")\
                .scale(.75).next_to(t0,direction=DOWN,buff=.25)
        t1[1].set_color(RED)

        self.play(
            FadeIn(t1)
        )
        self.wait(3)

        concl1 = TextMobject("There exists a left homotopy between $X_\\beta$ and $X_{\\beta+1}$.")\
                    .scale(.75)
        self.play(
            FadeOut(t0), 
            FadeOut(t1),
            FadeOut(pic3),
            FadeOut(pic4)
        )
        self.play(
            FadeIn(concl1)
        )
        self.wait(2)

        cocone = ImageMobject("cellcomplexes/lemma145no7.png").scale(1)

        self.play(
            FadeOut(concl1)
        )
        self.play(
            FadeIn(cocone)
        )
        self.wait(2)

        fin1 = TextMobject("The image of any representative in $\pi_n(\\hat{X})$ is compact, \
                hence is exhibited at some finite stage $X_k$. Thus $\\underset{\\to\\alpha}{\\lim}\
                \\pi_n(X_\\alpha)\\overset{\\simeq}{\\to}\\pi_n(\\hat{X})$. Thus\
                $$\\pi_n(X)\\overset{\\simeq}{\\to}\\pi_n(\\hat{X}).$$").scale(.75).shift(2.25*DOWN)

        self.play(
            FadeIn(fin1)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        


















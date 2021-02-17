from manimlib.imports import *
from NumberCreature.NumberCreature import *

class cattop(Scene):
    def construct(self):
        #   basic information template for a category
        catlabel = TextMobject("Category:").scale(1.25).shift(.5*UP,1.75*LEFT)
        objlabel = TextMobject("Objects:").next_to(catlabel, direction=DOWN,buff=MED_SMALL_BUFF).scale(.75)
        morlabel = TextMobject("Morphisms:").next_to(objlabel, direction=DOWN,buff=SMALL_BUFF).scale(.75)

        #   filling in info wrt Top
        cattop = TextMobject("Top").scale(1.25)\
                    .next_to(catlabel,direction=RIGHT,buff=2).set_color(BLUE)
        objtop = TextMobject("Topological Spaces").next_to(cattop,direction=DOWN,buff=MED_SMALL_BUFF)\
                    .scale(.75).set_color(BLUE)
        mortop = TextMobject("Cont. Functions").next_to(objtop,direction=DOWN,buff=SMALL_BUFF)\
                    .scale(.75).set_color(BLUE)

        #   animating, labels first then info
        self.play(  *[FadeIn(mob) for mob in [catlabel, objlabel, morlabel]])
        self.wait(2)
        self.play(  ShowCreation(cattop))
        self.wait()
        self.play(  ShowCreation(objtop), ShowCreation(mortop))

        #   fading out
        self.wait(3)
        self.play(  *[FadeOut(mob) for mob in self.mobjects])

class def11(Scene):
    def construct(self):
        #   label for definition 1.1, remains constant
        deflabel = TextMobject("\\textsc{Definition 1.1}").scale(.75).to_edge(LEFT,buff=MED_LARGE_BUFF)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)
        self.play(Write(deflabel))
        self.wait(2)

        #   defiinition for a diagram
        diagramis = TextMobject("A ","diagram"," in a category $\\mathcal{C}$ is a").shift(2*UP,2*LEFT).scale(.75)
        diagramis[1].set_color(BLUE)
        casesfordiagdef = TexMobject("\\begin{cases}\\text{- small category }I \\\ \\text{- functor} \\end{cases}")\
                            .scale(.75).next_to(diagramis,direction=RIGHT, buff=MED_LARGE_BUFF)
        functordesc = TextMobject("The functor is of the following type:").scale(.75).shift(.5*UP,2.75*LEFT)
        functex1 = TexMobject("X_\\ast:I\longrightarrow\\mathcal{C}").shift(.75*DOWN)
        functex2 = TexMobject("(i\\overset{\\phi}{\\longrightarrow}j)\\mapsto(X_i\\overset{X(\\phi)}{\\longrightarrow}X_j).")\
                    .next_to(functex1,direction=DOWN,buff=MED_LARGE_BUFF)

        inacat = Line(stroke_width=1.75).next_to(diagramis,direction=DOWN,buff=MED_SMALL_BUFF)\
                    .shift(.55*RIGHT, .15*UP).scale(1.2)

            # examples of what $I$ could be
        tex1wn = TexMobject("X_\\ast:\\mathbb{N}\longrightarrow\\mathcal{C}").shift(.75*DOWN)
        tex1wfset = TexMobject("X_\\ast:\\{1,2,3\\}\longrightarrow\\mathcal{C}").shift(.75*DOWN)
        tex1wemptyset = TexMobject("X_\\ast:\\emptyset\longrightarrow\\mathcal{C}").shift(.75*DOWN)
        functex1orig = functex1.copy()

            # animating
        self.play(FadeIn(diagramis), FadeIn(casesfordiagdef))
        self.wait()
        self.play(ShowCreation(inacat))
        self.wait(2)
        self.play(ShowCreation(functordesc))
        self.play(FadeIn(functex1))
        self.play(FadeIn(functex2))
        self.wait(2)
                # animating examples of what $I$ could be
        self.play(  Transform(functex1,tex1wn))
        self.wait()
        self.play(  Transform(functex1,tex1wfset))
        self.wait()
        self.play(  Transform(functex1,tex1wemptyset))
        self.wait()
        self.play(  Transform(functex1,functex1orig))
        self.wait(2)
        
        self.play(*[FadeOut(mob)for mob in self.mobjects[1:]])

        #   definition for cone
        coneis = TextMobject("A ", "cone", " over this diagram is").shift(2*UP,3*LEFT).scale(.75)
        coneis[1].set_color(BLUE)
        overdiag = Line(stroke_width=1.75).next_to(coneis,direction=DOWN,buff=MED_SMALL_BUFF)\
                    .shift(.15*UP,.4*RIGHT).scale(1.4)

        casesforconedef = TexMobject("\\begin{cases}\\text{- an object }Q \\\ \\text{- morphisms }p_i:Q\\to X_i,& i\\in I \\end{cases}")\
                            .scale(.75).next_to(coneis,direction=RIGHT, buff=MED_LARGE_BUFF)
        stalltriangles = TextMobject("such that all such triangles").next_to(coneis,direction=DOWN,buff=LARGE_BUFF)\
                            .scale(.75).shift(.05*LEFT)
        conetriangle = ImageMobject("uchomotopy/v1cone.png")\
                            .shift(3*RIGHT,0*DOWN)
        commute = TextMobject("commute.").scale(.75).next_to(coneis,direction=DOWN,buff=3)\
                    .shift(1.45*LEFT)

        phiex1 = TexMobject("\\phi:i\\to j").scale(.75).next_to(conetriangle,direction=DOWN,buff=LARGE_BUFF)
        xphiex1 = TexMobject("X(\\phi):X_i\\to X_j").scale(.75).next_to(phiex1,direction=DOWN,buff=MED_SMALL_BUFF)

        psiex1 = TexMobject("\\psi:m\\to n").scale(.75).next_to(conetriangle,direction=DOWN,buff=LARGE_BUFF)
        xpsiex1 = TexMobject("X(\\psi):X_m\\to X_n").scale(.75).next_to(phiex1,direction=DOWN,buff=MED_SMALL_BUFF)
        conetriangle2 = ImageMobject("uchomotopy/v2cone.png")\
                            .shift(3*RIGHT,0*DOWN)

            #   animating
        self.play(FadeIn(coneis))
        self.play(  ShowCreation(casesforconedef))
        self.wait()
        self.play(  ShowCreation(overdiag))
        self.wait()
        self.play(  ShowCreation(stalltriangles))
        self.play(  FadeIn(conetriangle))
        self.play( ShowCreation(commute))
        self.wait(3)

        self.play(FadeIn(phiex1),FadeIn(xphiex1))
        self.wait(2)
        self.play(  Transform(phiex1,psiex1), Transform(xphiex1,xpsiex1))
        self.wait()
        self.play(  FadeOut(conetriangle), FadeIn(conetriangle2))

        self.wait(3)
        self.play(  *[FadeOut(mob)for mob in self.mobjects[1:]])

        #   def for cocone
        coconeis = TextMobject("A ", "cocone", " is dual:").shift(2*UP,3*LEFT).scale(.75)
        coconeis[1].set_color(BLUE)
        coconepic = ImageMobject("uchomotopy/cocone.png")

        self.play(FadeIn(coconeis))
        self.play(FadeIn(coconepic))

        self.wait(3)
        self.play(  *[FadeOut(mob) for mob in self.mobjects[1:]])

        #   def for limit
        limitis = TextMobject("A ", "limit", " over the diagram is the universal cone, denoted ",\
                    "$\\underset{\\leftarrow i\in I}{\\lim}X_i$,").scale(.75).shift(2*UP,1*LEFT)
        limitis[1].set_color(BLUE)
        desclinelimit = Line(stroke_width=1.75).next_to(limitis,direction=DOWN,buff=MED_LARGE_BUFF)\
                        .shift(.6*UP,2.5*LEFT).scale(1.35)
        limitis2 = TextMobject("i.e. every other cone factors through it:").scale(.75)\
                    .next_to(limitis,direction=DOWN,buff=MED_SMALL_BUFF).shift(2*LEFT)

        limitpic = ImageMobject("uchomotopy/limit.png").scale(1.5).shift(1*DOWN)

        self.play(  FadeIn(limitis), ShowCreation(desclinelimit))
        self.wait(2)
        self.play(  FadeIn(limitis2))
        self.wait(2)
        self.play(  FadeIn(limitpic))
        self.wait(4)

        self.play(  *[FadeOut(mob)for mob in self.mobjects[1:]])

        # def for colimit
        colimitis = TextMobject("A ", "colimit", " is dual:").scale(.75).shift(2*UP,3.5*LEFT)
        colimitis[1].set_color(BLUE)

        colimitpic = ImageMobject("uchomotopy/colimit.png").scale(1.5).shift(.5*DOWN)

        self.play(  FadeIn(colimitis))
        self.wait(2)
        self.play(  FadeIn(colimitpic))
        self.wait(4)
        self.play( *[FadeOut(mob)for mob in self.mobjects])
        
class def12(Scene):
    def construct(self):
        #   general variables etc
        deftitle = TextMobject("\\textsc{Definition 1.2}").scale(.75).to_edge(LEFT,buff=MED_LARGE_BUFF)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)
        defintro = TextMobject("For").scale(.75).next_to(deftitle,direction=DOWN,buff=LARGE_BUFF)\
                    .shift(1*RIGHT)
        defintro2 = TexMobject("\\begin{cases} \\{X_i=(S_i,\\tau_i)\\in\\text{Top}\\}_{i\\in I} &\
                        \\text{a set of topological spaces}\\\ S\\in\\text{Set} & \\text{a bare set}\
                        \\end{cases}").scale(.75).next_to(defintro,direction=RIGHT,buff=MED_LARGE_BUFF)
        
        self.play(  Write(deftitle))
        self.wait()
        self.play(  FadeIn(defintro), FadeIn(defintro2))
        self.wait(3)

        #   def initial topology
        defitline1 = TextMobject("For $\\{f_i:S\\to S_i:i\\in I\\}$, the ", "initial topology",\
                        " $\\tau_{\\text{initial}}(\\{f_i\\}_{i\\in I})$ on $S$").scale(.75)\
                        .next_to(deftitle,direction=DOWN,buff=2.5).shift(4.5*RIGHT)
        defitline1[1].set_color(BLUE)
        defitline2 = TextMobject("has the \\textit{minimum} collection of open subsets such that all")\
                        .scale(.75).next_to(defitline1,direction=DOWN,buff=MED_LARGE_BUFF).shift(.7*LEFT)
        defitline3 = TextMobject("$f_i:(S,\\tau_{\\text{initial}}(\\{f_i\\}_{i\\in I}))\\to X_i$",\
                        " are continuous.").scale(.75).next_to(defitline2,direction=DOWN,\
                        buff=MED_LARGE_BUFF).shift(1*LEFT)

        self.play(  FadeIn(defitline1))
        self.wait()
        self.play(  FadeIn(defitline2))
        self.wait()
        self.play(  FadeIn(defitline3))
        self.wait(3)

        inclusionpic0 = SVGMobject("uchomotopy/inclusion.svg", fill_opacity=0, stroke_width=1.75)\
                        .scale(1).shift(2*DOWN, 4*RIGHT)
        inclusionpic1 = SVGMobject("uchomotopy/inclusion.svg", fill_opacity=.5, stroke_width=2,\
                        color=RED)\
                        .scale(1).shift(2*DOWN, 4*RIGHT)

        self.play(  FadeIn(inclusionpic0[0]))
        self.wait(2)
        self.play(  FadeIn(inclusionpic1[1]))
        self.wait(4)
        
        self.play(  *[FadeOut(mob)for mob in self.mobjects[3:]])

        #   def final topology
        deffinline1 = TextMobject("For $\\{f_i:S_i\\to S:i\\in I\\}$, the ", "final topology",\
                        " $\\tau_{\\text{final}}(\\{f_i\\}_{i\\in I})$ on $S$").scale(.75)\
                        .next_to(deftitle,direction=DOWN,buff=2.5).shift(4.1*RIGHT)
        deffinline1[1].set_color(BLUE)
        deffinline2 = TextMobject("has the \\textit{maximum} collection of open subsets such that all")\
                        .scale(.75).next_to(deffinline1,direction=DOWN,buff=MED_LARGE_BUFF).shift(.47*LEFT)
        deffinline3 = TextMobject("$f_i:X_i\\to (S,\\tau_{\\text{final}}(\\{f_i\\}_{i\\in I}))$",\
                        " are continuous.").scale(.75).next_to(deffinline2,direction=DOWN,\
                        buff=MED_LARGE_BUFF).shift(1.15*LEFT)

        epipic0 = SVGMobject("uchomotopy/inclusion.svg", fill_opacity=.5, stroke_width=2)\
                        .scale(1).shift(2*DOWN, 4*RIGHT)[1]
        epipic1 = SVGMobject("uchomotopy/inclusion.svg", fill_opacity=0, stroke_width=1.75,color=RED)\
                        .scale(1).shift(2*DOWN, 4*RIGHT)[0]

        self.play(  FadeIn(deffinline1))
        self.wait()
        self.play(  FadeIn(deffinline2))
        self.wait()
        self.play(  FadeIn(deffinline3))
        self.wait(3)

        self.play(  FadeIn(epipic0))
        self.wait(2)
        self.play(  FadeIn(epipic1))
        self.wait(4)

        self.play( *[FadeOut(mob)for mob in self.mobjects])

class prop15(Scene):
    def construct(self):
        #   general
        proptitle = TextMobject("\\textsc{Proposition 1.5}").scale(.75).to_edge(LEFT,buff=MED_LARGE_BUFF)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)
        propintro = TextMobject("Let $X_\\ast:I\\to\\text{Top}$ be a diagram in Top with components \
                        $X_i=(S_i,\\tau_i)$.").scale(.75).next_to(proptitle,direction=DOWN,\
                        buff=MED_LARGE_BUFF).shift(5*RIGHT)

        #   spoiler
        spoiler = TextMobject("Its limits and colimits exist.").scale(.75).set_color(GREEN)

        #   limit stuff
        limitsetpic = ImageMobject("uchomotopy/limitset.png").shift(3.5*LEFT, .5*DOWN).scale(2)
        limitintop = TexMobject("\\underset{\\leftarrow i\\in I}{\\lim}X_i\
                        \\cong( \\underset{\\leftarrow i\\in I}{\\lim} S_i,\
                        \\tau_{\\text{initial}}(\\{p_i\\}_{i\\in I}))").shift(3*RIGHT, .5*DOWN)\
                        .scale(.75)

        #   colimit stuff
        colimitsetpic = ImageMobject("uchomotopy/colimitset.png").shift(3.5*LEFT, .5*DOWN).scale(2)
        colimitintop = TexMobject("\\underset{\\rightarrow i\\in I}{\\lim}X_i\
                        \\cong( \\underset{\\rightarrow i\\in I}{\\lim} S_i,\
                        \\tau_{\\text{final}}(\\{q_i\\}_{i\\in I}))").shift(3*RIGHT, .5*DOWN)\
                        .scale(.75)

        #   animating
        self.play(Write(proptitle))
        self.wait()
        self.play(FadeIn(propintro))
        self.wait(2)
        self.play(Write(spoiler))
        self.wait(2)
        self.play(  FadeOut(spoiler))
        self.play(  FadeIn(limitsetpic))
        self.wait(2)
        self.play(  FadeIn(limitintop))
        self.wait(3)
        self.play(  FadeOut(limitsetpic), FadeOut(limitintop))
        self.wait()
        self.play(FadeIn(colimitsetpic), FadeIn(colimitintop))
        self.wait(4)
        self.play(  *[FadeOut(mob)for mob in self.mobjects])

class ex16(Scene):
    def construct(self):
        extitle = TextMobject("\\textsc{Example 1.6}").scale(.75).to_edge(LEFT,buff=MED_LARGE_BUFF)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)
        emptydiag = TextMobject("empty diagram $\\emptyset\\to\\text{Top}$").scale(.75)\
                    .next_to(extitle,direction=DOWN,buff=MED_LARGE_BUFF).shift(5.5*RIGHT)

        ex16pic = ImageMobject("uchomotopy/ex16pic.png").shift(3.5*LEFT, .5*DOWN).scale(2)
        limis = TexMobject("\\underset{\\leftarrow i\\in I}{\\lim}X_i\\cong (\\text{pt},\\tau)")\
                .scale(.75).next_to(ex16pic,direction=RIGHT,buff=2)

        #   animation
        self.play(Write(extitle))
        self.wait()
        self.play(  FadeIn(emptydiag))
        self.wait(2)
        self.play(FadeIn(ex16pic))
        self.wait(2)
        self.play(FadeIn(limis))
        self.wait(4)
        self.play(  *[FadeOut(mob)for mob in self.mobjects])

class ex17(Scene):
    def construct(self):
        extitle = TextMobject("\\textsc{Example 1.7}").scale(.75).to_edge(LEFT,buff=MED_LARGE_BUFF)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)
        
        ex17pic = ImageMobject("uchomotopy/ex17pic.png").shift(2.5*LEFT, .5*DOWN).scale(2)
        colimis = TexMobject("\\underset{\\rightarrow i\\in I}{\\lim}X_i\\cong\
                \\underset{i\\in I}{\\sqcup}X_i")\
                .scale(.75).next_to(ex17pic,direction=RIGHT,buff=2)

        self.play(  Write(extitle))
        self.wait(2)
        self.play(  FadeIn(ex17pic))
        self.wait(2)
        self.play(  FadeIn(colimis))
        self.wait(4)
        self.play(  *[FadeOut(mob)for mob in self.mobjects])

class ex110(Scene):
    def construct(self):
        extitle = TextMobject("\\textsc{Example 1.10}").scale(.75).to_edge(LEFT,buff=MED_LARGE_BUFF)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)

        pairedpicspaces = SVGMobject("uchomotopy/eqzer.svg", fill_opacity=.25,\
                            stroke_width=1.75, color=BLUE)[:2].scale(2).shift(2*RIGHT)
        pairedpicelts = SVGMobject("uchomotopy/eqzer.svg", fill_opacity=1,\
                            stroke_width=1.75)[-8:].scale(2).shift(2*RIGHT)
        pairedpicarrgreen = SVGMobject("uchomotopy/eqzer.svg", fill_opacity=0,\
                            stroke_width=1.75, color=GREEN)[2:-12].scale(2).shift(2*RIGHT)
        pairedpicarrred = SVGMobject("uchomotopy/eqzer.svg", fill_opacity=0,\
                            stroke_width=1.75, color=RED)[-12:-8].scale(2).shift(2*RIGHT)

        singlepicspace = SVGMobject("uchomotopy/eqzer2.svg", fill_opacity=.25,\
                            stroke_width=1.75, color=BLUE)[:1].scale(1.9)\
                            .shift(4.5*LEFT)
        singlepicelts1 = SVGMobject("uchomotopy/eqzer2.svg", fill_opacity=1,\
                            stroke_width=1.75)[4].scale(1.9).shift(4.5*LEFT, .7*DOWN)
        singlepicelts2 = SVGMobject("uchomotopy/eqzer2.svg", fill_opacity=1,\
                            stroke_width=1.75)[4].scale(1.9).shift(4.5*LEFT, 1.7*UP)

        #   labels
        x = TexMobject("X").shift(2.9*DOWN, .2*LEFT)
        y = TexMobject("Y").next_to(x,buff=4)

        fgreen = TexMobject("\\overset{f}{\\longrightarrow}").set_color(GREEN)\
                    .next_to(x,buff=1.8).shift(.4*UP)
        gred = TexMobject("\\underset{g}{\\longrightarrow}").set_color(RED)\
                    .next_to(x,buff=1.8).shift(.5*DOWN)

        eqzer = TexMobject("\\operatorname{eq}(f,g)").next_to(x,direction=LEFT,buff=3.3)

        inclarr = TexMobject("\\hookrightarrow").next_to(x,direction=LEFT,buff=1.55)

        #   pic
        eqpic = ImageMobject("uchomotopy/eq.png").scale(2)

        #   animation
        self.play(  Write(extitle))
        self.wait(2)
        self.play(FadeIn(pairedpicspaces), FadeIn(singlepicspace))
        self.play(*[FadeIn(mob)for mob in [x,y,fgreen,gred,eqzer,inclarr]])
        self.wait()
        self.play(FadeIn(pairedpicelts))
        self.wait()
        self.play(  ShowCreation(pairedpicarrgreen))
        self.play(  ShowCreation(pairedpicarrred))
        self.wait(2)
        self.play(  FadeIn(singlepicelts1), FadeIn(singlepicelts2))
        self.wait(3)
        self.play(  *[FadeOut(mob)for mob in self.mobjects[1:]])
        self.wait()
        self.play(  GrowFromCenter(eqpic))
        self.wait(3)

        self.play( *[FadeOut(mob)for mob in self.mobjects])

class ex111(Scene):
    def construct(self):
        extitle = TextMobject("\\textsc{Example 1.11}").scale(.75).to_edge(LEFT,buff=MED_LARGE_BUFF)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)

        twospaces = SVGMobject("uchomotopy/eqzer.svg", fill_opacity=.25,\
                            stroke_width=1.75, color=BLUE)[:2].scale(2).shift(2*LEFT)
        elts = SVGMobject("uchomotopy/eqzer.svg", fill_opacity=1,\
                            stroke_width=1.75)[-8:].scale(2).shift(2*LEFT)
        arrgreen = SVGMobject("uchomotopy/eqzer.svg", fill_opacity=0,\
                            stroke_width=1.75, color=GREEN)[2:-12].scale(2).shift(2*LEFT)
        arrred = SVGMobject("uchomotopy/eqzer.svg", fill_opacity=0,\
                            stroke_width=1.75, color=RED)[-12:-8].scale(2).shift(2*LEFT)
        
        singlepicspace = SVGMobject("uchomotopy/eqzer2.svg", fill_opacity=.25,\
                            stroke_width=1.75, color=BLUE)[:1].scale(1.9)\
                            .shift(4.5*RIGHT)
        singlepicelts1 = SVGMobject("uchomotopy/eqzer2.svg", fill_opacity=1,\
                            stroke_width=1.75)[4].scale(1.9).shift(4.5*RIGHT, .7*DOWN)
        singlepicelts2 = SVGMobject("uchomotopy/eqzer2.svg", fill_opacity=1,\
                            stroke_width=1.75)[4].scale(1.9).shift(4.5*RIGHT, 1.7*UP)
        singlepicelts3 = SVGMobject("uchomotopy/eqzer2.svg", fill_opacity=1,\
                            stroke_width=1.75)[4].scale(1.9).shift(4.5*RIGHT, .5*UP)

        normalarr1 = Arrow().shift(1.15*UP,2.3*RIGHT).scale(2.5)
        normalarr2 = Arrow().shift(1.15*DOWN,2.3*RIGHT).scale(2.5)
        slantarr1 = Arrow().rotate(3*DEGREES).scale(2.5)\
                    .shift(2.3*RIGHT, .2*DOWN)
        slantarr2 = Arrow().rotate(-5*DEGREES).scale(2.5)\
                    .shift(2.3*RIGHT, .3*UP)

        #   labels
        y = TexMobject("Y").shift(2.9*DOWN, .1*RIGHT)
        x = TexMobject("X").next_to(y,direction=LEFT,buff=4)
        fgreen = TexMobject("\\overset{f}{\\longrightarrow}").set_color(GREEN)\
                    .next_to(x,buff=1.8).shift(.4*UP)
        gred = TexMobject("\\underset{g}{\\longrightarrow}").set_color(RED)\
                    .next_to(x,buff=1.8).shift(.5*DOWN)

        coeqzer = TexMobject("\\operatorname{coeq}(f,g)").next_to(y,direction=RIGHT,buff=3.3)

        surjarr = TexMobject("\\twoheadrightarrow").next_to(y,direction=RIGHT,buff=1.55)

        #   pic
        coeqpic = ImageMobject("uchomotopy/coeq.png").scale(2)

        #   animating
        self.play(Write(extitle))
        self.wait(2)
        self.play(  FadeIn(twospaces), FadeIn(x), FadeIn(y))
        self.wait()
        self.play(GrowFromCenter(elts))
        self.play(  ShowCreation(arrgreen), ShowCreation(arrred),\
                ShowCreation(fgreen), ShowCreation(gred))
        self.wait(2)
        self.play(  FadeIn(singlepicspace), FadeIn(coeqzer))
        self.wait()
        self.play(  GrowFromCenter(singlepicelts1), GrowFromCenter(singlepicelts2),\
                GrowFromCenter(singlepicelts3))
        self.play(  *[ShowCreation(mob)for mob in [normalarr1, normalarr2,\
                slantarr1, slantarr2]], ShowCreation(surjarr))
        self.wait(3)
        self.play(  *[FadeOut(mob)for mob in self.mobjects[1:]])
        self.wait()
        self.play(  GrowFromCenter(coeqpic))
        self.wait(3)
        self.play(  *[FadeOut(mob)for mob in self.mobjects])

class ex112(Scene):
    def construct(self):
        extitle = TextMobject("\\textsc{Example 1.12}").scale(.75).to_edge(LEFT,buff=MED_LARGE_BUFF)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)

        bottomspace = SVGMobject("uchomotopy/attaching.svg", stroke_width=1.75,\
                        fill_opacity=.25, color=BLUE)[0].shift(3.25*RIGHT,1.5*DOWN).scale(2)
        topspace = SVGMobject("uchomotopy/attaching.svg", stroke_width=1.75,\
                        fill_opacity=.25, color=BLUE)[1].shift(3.25*RIGHT).scale(2)
        a = SVGMobject("uchomotopy/attaching.svg", stroke_width=1.75,\
                        fill_opacity=.25, color=RED)[2].shift(3.25*RIGHT, .5*DOWN).scale(2)
        a2 = a.copy()
        ainy = a.copy().shift(1.5*DOWN)
        ainx = a.copy().scale(2).shift(1.55*UP)

        pushorig = ImageMobject("uchomotopy/pushorig.png").shift(3.5*LEFT)
        pushfin = ImageMobject("uchomotopy/pushfin.png").shift(3.5*LEFT)
        pushuniversal = ImageMobject("uchomotopy/pushuniversal.png").shift(3.5*LEFT)\
                        .scale(1.5)

        coeq = TexMobject("A\\stackrel{\\longrightarrow}{\\longrightarrow}X\\sqcup Y\\longrightarrow\
                X\\sqcup_A Y").shift(3.5*LEFT)

        self.play(  Write(extitle))
        self.wait(3)
        self.play(  FadeIn(pushorig))
        self.wait(3)
        self.play(  FadeIn(bottomspace), FadeIn(topspace))
        self.wait()
        self.play(  GrowFromCenter(a))
        self.play(  Transform(a, ainy), Transform(a2, ainx))
        self.wait(3)
        self.play(  FadeOut(pushorig), FadeIn(pushfin))
        self.wait()
        self.play(  FadeOut(pushfin), FadeIn(pushuniversal))
        self.wait(3)
        self.play(  FadeOut(pushuniversal))
        self.play(  FadeIn(coeq))
        self.wait(3)
        self.play(  *[FadeOut(mob)for mob in self.mobjects])

class ex113(Scene):
    def construct(self):
        extitle = TextMobject("\\textsc{Example 1.13}").scale(.75).to_edge(LEFT,buff=MED_LARGE_BUFF)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)

        a = Circle(fill_opacity=.25).set_color(RED).shift(2*LEFT, 1.5*UP).scale(.5)
        x = Circle(fill_opacity=.25).set_color(BLUE).next_to(a,direction=DOWN,buff=2)
        y = Dot().set_color(BLUE).next_to(a,buff=4)
        atext = TexMobject("A").next_to(a,direction=LEFT,buff=1)
        xtext = TexMobject("X").next_to(x,direction=LEFT,buff=.5)
        ytext = TexMobject("Y").next_to(y, buff=1)
        a2x = Arrow(a,x)
        a2y = Arrow(a,y)
        ainx = a.copy().shift(3.5*DOWN)
        ainy = Dot().set_color(RED).move_to(y)
        
        po = Circle(fill_opacity=.25).set_color(BLUE).scale(.5).next_to(x,buff=3.05)
        ainpo = Dot().set_color(RED).move_to(po)
        x2po = Arrow(x,po)
        y2po = Arrow(y,po)

        #self.add(   extitle, a, x, y, atext, xtext, ytext, a2x, a2y, ainx, ainy,\
        #            po, ainpo, x2po, y2po)

        #   animating
        self.play(  Write(extitle))
        self.wait()
        self.play(  *[FadeIn(mob)for mob in [a,x,y,atext,xtext,ytext]])
        self.wait()
        self.play(  ShowCreation(a2x), ShowCreation(a2y))
        self.play(  Transform(a.copy(),ainx), Transform(a.copy(),ainy))
        self.wait(2)
        self.play(  ShowCreation(x2po), ShowCreation(y2po))
        self.play(  FadeIn(po), FadeIn(ainpo))
        self.wait(3)
        self.play(  *[FadeOut(mob)for mob in self.mobjects])

class ex114(ThreeDScene):
    def construct(self):
        extitle = TextMobject("\\textsc{Example 1.14}").scale(.75).to_edge(LEFT,buff=MED_LARGE_BUFF)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)

        dn = TexMobject("D^n",":= \\{\\vec{x}\\in\mathbb{R}^n\\mid |\\vec{x}|\\leq 1\\}\\hookrightarrow\
                        \\mathbb{R}^n").scale(.75)
        dn[0].set_color(BLUE)
        dnup = dn.copy().shift(.25*UP)
        snm1 = TexMobject("S^{n-1}",":=\\partial D^n:= \\{\\vec{x}\\in\\mathbb{R}^n\\mid |\\vec{x}|=1\\}\
        \\hookrightarrow \\mathbb{R}^n}").scale(.75).shift(.25*DOWN)
        snm1[0].set_color(RED)

        dnside = dn.copy().to_edge(LEFT,buff=1).shift(.25*UP)
        snm1side = snm1.copy().to_edge(LEFT,buff=1).shift(.25*DOWN)

        d2 = Circle(fill_opacity=.25).set_color(BLUE).shift(4*RIGHT,1.5*UP)
        s1 = Circle(fill_opacity=0).set_color(RED).shift(4*RIGHT,1.5*DOWN)

        self.play(  Write(extitle))
        self.wait()
        self.play(  ShowCreation(dn))
        self.wait()
        self.play(  Transform(dn,dnup))
        self.play(  ShowCreation(snm1))
        self.wait(2)
        self.play(  Transform(dn,dnside), Transform(snm1,snm1side))
        self.wait()
        self.play(  FadeIn(d2))
        self.wait()
        self.play(  FadeIn(s1))
        self.wait(2)
        self.play(  *[FadeOut(mob)for mob in self.mobjects[1:-2]])

        s1diag = s1.copy().move_to([-2.5,1.5,0])
        d2right = d2.copy().next_to(s1diag, buff=3)
        d2below = d2.copy()
        d2belowtemp = d2.copy().next_to(s1diag,direction=DOWN,buff=1.5)

        self.play(  Transform(s1, s1diag), Transform(d2,d2right),\
                    Transform(d2below,d2belowtemp))
        self.wait()
        
        s1down = Arrow(s1,d2below)
        s1right = Arrow(s1,d2right)
        s1ind2down = s1.copy().move_to(d2below)
        s1ind2right = s1.copy().move_to(d2right)

        self.play(  ShowCreation(s1down), ShowCreation(s1right))
        self.play(  Transform(s1.copy(), s1ind2down), Transform(s1.copy(), s1ind2right))
        self.wait(2)

        sp = ParametricSurface(
            lambda u, v: np.array([
                1.5*np.cos(u)*np.cos(v)+2.55,
                1.5*np.cos(u)*np.sin(v),
                1.5*np.sin(u)-2.25
            ]),v_min=0,v_max=TAU,u_min=-PI/2,u_max=PI/2,checkerboard_colors=[BLUE_D, BLUE_E],
            resolution=(15, 32)).scale(.65)
        redeq = ParametricFunction(
                lambda u : np.array([
                1.5*np.cos(u)+2.55,
                1.5*np.sin(u),
                -2.25
            ]),color=RED,t_min=PI,t_max=TAU-.45,
            ).scale(.63)
        ar2po = s1right.copy().scale(.9).shift(3.5*DOWN)
        ad2po = s1down.copy().shift(5*RIGHT)

        self.add_fixed_in_frame_mobjects(*[mob for mob in self.mobjects])
        self.set_camera_orientation(70*DEGREES)
        self.play(  FadeIn(sp), FadeIn(redeq))
        self.add_fixed_in_frame_mobjects(ar2po, ad2po)
        self.play(  ShowCreation(ar2po), ShowCreation(ad2po))
        self.wait(3)
        self.play(  *[FadeOut(mob)for mob in self.mobjects])
        
class transitiontotransfinite(Scene):
    def construct(self):
        goal1 = TextMobject("- Sequences indexed by sets larger than $\\mathbb{N}$").scale(.75)
        goal2 = TextMobject("- ``Infinite compositions'' of morphisms").scale(.75)
        goalgp = VGroup(
            goal1, 
            goal2).arrange_submobjects(
                DOWN,
                aligned_edge=LEFT,
                buff=.5
            )

        self.play(  GrowFromCenter(goalgp))
        self.wait(3)
        self.play(  *[FadeOut(mob)for mob in self.mobjects])

class def115(Scene):
    def construct(self):
        deftitle = TextMobject("\\textsc{Definition 1.15}").scale(.75).to_edge(LEFT,buff=MED_LARGE_BUFF)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)
        
        defp1 = TextMobject("A ", "partial order", " is a set $S$ equipped with a relation $\\leq$ \
                such that $\\forall$ $a,b,c\\in S$").scale(.75).to_edge(LEFT).shift(2*UP)
        defp1[1].set_color(BLUE)

        p1 = TextMobject("- $a\\leq a$").scale(.75)
        p2 = TextMobject("- if $a\\leq b$ and $b\\leq c$, then $a\\leq c$").scale(.75)
        p3 = TextMobject("- if $a\\leq b$ and $b\\leq a$ then $a=b$").scale(.75)

        first3gp = VGroup(
            p1,
            p2,
            p3
        ).arrange_submobjects(
            DOWN,
            aligned_edge=LEFT,
            buff=.5
        )

        threeleq5 = TexMobject("3\\leq 5").scale(1).shift(3*RIGHT,1*UP)

        d1 = Dot().set_color(BLUE_C)
        d2 = Dot().set_color(BLUE_C)
        d3 = Dot().set_color(BLUE_C)
        d4 = Dot().set_color(BLUE_E)
        d5 = Dot().set_color(BLUE_E)

        threedotgp = VGroup(
            d1,
            d2,
            d3
        ).arrange_submobjects(
            DOWN,
            buff=.5
        ).shift(
            2*RIGHT,
            2*DOWN
        )

        fivedotgp = VGroup(
            d4,
            d5,
            d1.copy(),
            d2.copy(),
            d3.copy()
        ).arrange_submobjects(
            DOWN,
            buff=.5
        ).shift(
            4*RIGHT,
            1.35*DOWN
        )

        inclarr = TexMobject("\\hookrightarrow").shift(
            3*RIGHT,
            2*DOWN
        )

        uniquemor1 = TextMobject("$\\exists$ a unique morphism $a\\to b$").scale(.75)
        uniquemor2 = TextMobject("precisely if $a\\leq b$").scale(.75)
        uniquemorgp = VGroup(
            uniquemor1,
            uniquemor2
        ).arrange_submobjects(
            DOWN,
            aligned_edge=LEFT,
            buff=.25
        ).to_edge(LEFT).shift(2.5*DOWN)

        #   animating
        self.play(
            FadeIn(deftitle)
        )
        self.wait(2)
        self.play(
            FadeIn(defp1)
        )
        self.play(
            FadeIn(first3gp)
        )
        self.wait(2)
        self.play(
            Transform(first3gp,first3gp.copy().to_edge(LEFT))
        )
        self.play(
            FadeIn(threeleq5)
        )
        self.wait(2)
        self.play(
            GrowFromCenter(threedotgp),
            GrowFromCenter(fivedotgp)
        )
        self.play(
            FadeIn(inclarr)
        )
        self.wait(2)
        self.play(
            ShowCreation(uniquemorgp)
        )
        self.wait(3)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects[1:]]
        )
        self.wait()
        
        poset = TexMobject("\\{1,2,3,2+3i\\}").shift(2*UP)
        totality1 = TextMobject("- A partial order is a ","total order").scale(.75)
        totality1[-1].set_color(BLUE)
        totality2 = TextMobject("if additionally either $a\\leq b$ or $b\\leq a$.").scale(.75)
        totalitygp = VGroup(
            totality1,
            totality2
        ).arrange_submobjects(
            DOWN,
            aligned_edge=LEFT,
            buff=.25
        )

        self.play(
            GrowFromCenter(poset)
        )
        self.wait(2)
        self.play(
            ShowCreation(totalitygp)
        )
        self.wait()
        self.play(
            *[FadeOut(mob)for mob in self.mobjects[1:]]
        )
        self.wait()

        wellorder1 = TextMobject("- A total order is a ", "well-order", " if additionally")\
                        .scale(.75)
        wellorder1[1].set_color(BLUE)
        wellorder2 = TextMobject("every non-empty subset has a least element.").scale(.75)
        wellordergp = VGroup(
            wellorder1,
            wellorder2
        ).arrange_submobjects(
            DOWN,
            aligned_edge=LEFT,
            buff=.25
        ).shift(.5*UP)

        ordinal = TextMobject("The equivalence class of a well-order is called an ",\
                    "ordinal.").next_to(
                        wellordergp,
                        direction=DOWN,
                        buff=.5).scale(.85)
        ordinal[-1].set_color(BLUE)

        self.play(
            ShowCreation(wellordergp)
        )
        self.wait()
        self.play(
            FadeIn(ordinal)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects[1:]]
        )
        self.wait()

        successor1 = TextMobject("- The ", "successor", " of an ordinal is the class of the well-order")\
                    .scale(.75)
        successor1[1].set_color(BLUE)
        successor2 = TextMobject("with a top element freely adjoined.").scale(.75)
        successorgp = VGroup(
            successor1,
            successor2
        ).arrange_submobjects(
            DOWN,
            aligned_edge=LEFT,
            buff=.25
        ).shift(1*UP)
        lo = TextMobject("- A ", "limit ordinal", " is one that is not a successor.").scale(.75)\
                .shift(
                    .5*DOWN,
                    .9*LEFT
                )
        lo[1].set_color(BLUE)

        self.play(
            FadeIn(successorgp)
        )
        self.wait()
        self.play(
            FadeIn(lo)
        )
        self.wait(3)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

class ex116(Scene):
    def construct(self):
        extitle = TextMobject("\\textsc{Example 1.16}").scale(.75).to_edge(LEFT,buff=MED_LARGE_BUFF)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)

        p1 = TextMobject("- The finite ordinals are labeled by $n\\in\\mathbb{N}$.")\
                .scale(.75)
        p2 = TextMobject("- The first non-empty limit ordinal is $\\omega=[(\\mathbb{N},\\leq)]$.")\
                .scale(.75)
        gp = VGroup(
            p1,
            p2
        ).arrange_submobjects(
            DOWN,
            aligned_edge=LEFT,
            buff=.5
        )

        self.play(
            FadeIn(extitle)
        )
        self.wait(2)
        self.play(
            ShowCreation(gp)
        )
        self.wait(3)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

class def117(Scene):
    def construct(self):
        deftitle = TextMobject("\\textsc{Definition 1.17}").scale(.75).to_edge(LEFT,buff=MED_LARGE_BUFF)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)

        intro = TextMobject("Let $\\mathcal{C}$ be a category, and let $I\\subset\\operatorname{Mor}\
        (\\mathcal{C})$.").scale(.75).to_edge(LEFT).shift(2*UP)

        self.play(
            FadeIn(deftitle)
        )
        self.wait(2)
        self.play(
            FadeIn(intro)
        )
        self.wait()

        seqp11 = TextMobject("For $\\alpha$ an ordinal, an $\\alpha$-indexed ",\
                "transfinite sequence", " of elements in $I$ is a").scale(.75)
        seqp12 = TextMobject("diagram").scale(.75)
        seqp1 = VGroup(
            seqp11,
            seqp12
        ).arrange_submobjects(
            DOWN,
            aligned_edge=LEFT,
            buff=.25
        ).to_edge(LEFT).shift(1*UP)

        diag = TexMobject("X_\\ast:\\alpha\\to\\mathcal{C}").scale(.75)
        st = TextMobject("such that").scale(.75).to_edge(LEFT).shift(.75*DOWN)
        diaggp = VGroup(
            diag,
            st
        )

        self.play(
            ShowCreation(seqp1),
            ShowCreation(diaggp)
        )
        self.wait()
        self.play(
            *[FadeOut(mob)for mob in self.mobjects[1:-1]]
        )
        self.play(
            Transform(diaggp,diaggp.copy().shift(2.5*UP))
        )

        cond1 = TextMobject("- $X_\\ast$ takes all successor morphisms\
                $\\beta\\overset{\\leq}{\\to}\\beta+1$ in $\\alpha$ \
                to elements $X_{\\beta,\\beta+1}\\in I$.").scale(.75)\
                .shift(.5*UP)
        
        self.play(
            FadeIn(cond1)
        )
        self.wait()

        cond2p1 = TextMobject("- $X_\\ast$ is continuous, in that $\\forall$ nonzero limit ordinals\
                    $\\beta<\\alpha$, we have that").scale(.75)
        cond2p2 = TextMobject("$X_\\ast$ restricted to $\\{\\gamma\\mid\\gamma\\leq\\beta\\}$ \
                    is a colimiting cocone for $X_\\ast$ restricted to").scale(.75)
        cond2p3 = TextMobject("$\\{\\gamma\\mid\\gamma<\
                    \\beta\\}$.").scale(.75)
        cond2 = VGroup(
            cond2p1,
            cond2p2,
            cond2p3
        ).arrange_submobjects(
            DOWN,
            aligned_edge=LEFT,
            buff=.25
        ).shift(
            1*DOWN,
            .27*LEFT
        )

        self.play(
            FadeIn(cond2)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects[1:-1]]
        )
        self.play(
            Transform(cond2,cond2.copy().shift(2.5*UP))
        )
        self.wait(2)

        finitecocone = ImageMobject("uchomotopy/finitecocone.png").shift(1.5*DOWN)

        self.play(
            GrowFromCenter(finitecocone)
        )
        self.wait(2)
        
        infinitecocone = ImageMobject("uchomotopy/infinitecocone.png").shift(1.5*DOWN)

        self.play(
            FadeOut(finitecocone),
            FadeIn(infinitecocone)
        )
        self.wait(2)

        infinitecocone2 = ImageMobject("uchomotopy/infinitecocone2.png").shift(1.5*UP)
        transcomp = TextMobject("``Transfinite composition''").next_to(
            infinitecocone2,
            direction=DOWN,
            buff=1
        ).set_color(RED)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects[1:]],
            FadeIn(infinitecocone2)
        )
        self.wait(2)
        self.play(
            ShowCreation(transcomp)
        )
        self.wait(3)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

class expobj(Scene):
    def construct(self):
        xy = TexMobject("X,Y\\in\\operatorname{Top}").scale(.75)\
                .shift(
                    2*UP
                )

        hom = TexMobject("\\operatorname{Hom}_{\\operatorname{Top}}(X,Y)").scale(.75)
        inset = TexMobject("\\in\\operatorname{Set}").scale(.75).shift(2*RIGHT)

        self.play(
            FadeIn(xy)
        )
        self.wait(2)
        self.play(
            ShowCreation(hom)
        )
        self.wait()
        self.play(
            Transform(hom,hom.copy().shift(2*LEFT)),
            FadeIn(inset)
        )
        self.wait(2)

        homs1x = TexMobject("\\operatorname{Hom}_{\\operatorname{Top}}(X,Y)").scale(.75)\
                    .shift(
                        1*DOWN
                    ).set_color(BLUE)
        intop = TexMobject("\\in\\operatorname{Top}").scale(.75).shift(
            2*RIGHT,
            1*DOWN
        ).set_color(BLUE)
        exponential = TextMobject("``exponential objects''").scale(.75).shift(
            2*DOWN
        ).set_color(BLUE)
        self.play(
            ShowCreation(homs1x)
        )
        self.wait()
        self.play(
            Transform(homs1x,homs1x.copy().shift(2*LEFT)),
            FadeIn(intop)
        )
        gp = VGroup(
            hom,
            inset,
            homs1x,
            intop
        )
        self.play(
            Transform(gp,gp.copy().shift(1*UP))
        )
        self.play(
            Write(exponential)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

class def118(Scene):
    def construct(self):
        deftitle = TextMobject("\\textsc{Definition 1.18}").scale(.75).to_edge(LEFT,buff=MED_LARGE_BUFF)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)
                    
        intro = TextMobject("For $X,Y\\in\\operatorname{Top}$, with $Y$ locally compact,",\
                " the ","mapping space"," $X^Y\\in\\operatorname{Top}$ has")\
                .scale(.75)
        intro[-2].set_color(BLUE)
        bullet1 = TextMobject("- underlying set $\\operatorname{Hom}_{\\operatorname{Top}}\
                    (Y,X)$").scale(.75)
        bullet2 = TextMobject("- subbase $\{U^K\}$, where").scale(.75)
        defgp = VGroup(
            intro,
            bullet1,
            bullet2
        ).arrange_submobjects(
            DOWN,
            aligned_edge=LEFT,
            buff=.5
        ).shift(
            1*UP
        )
        
        self.play(
            Write(deftitle)
        )
        self.wait(2)
        self.play(
            FadeIn(defgp)
        )

        uk1 = TextMobject("- $K\\subset Y$ is compact").scale(.75)
        uk2 = TextMobject("- $U\\subset X$ is open").scale(.75)
        uk3 = TextMobject("- $U^K:=$ continuous functions $f$ such that the above commutes")\
                .scale(.75)
        
        defsubgp = VGroup(
            uk1,
            uk2,
            uk3
        ).arrange_submobjects(
            DOWN,
            aligned_edge=LEFT,
            buff=.5
        ).next_to(
            defgp,
            direction=DOWN,
            buff=.5
        )

        self.play(
            FadeIn(defsubgp)
        )

        cotop = ImageMobject("uchomotopy/cotop.png").shift(
            3*RIGHT,
            .5*DOWN
        ).scale(1.25)
        self.play(
            FadeIn(cotop)
        )
        self.wait(3)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

class prop119(Scene):
    def construct(self):
        proptitle = TextMobject("\\textsc{Proposition 1.19}").scale(.75).to_edge(LEFT,buff=MED_LARGE_BUFF)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)

        intro = TextMobject("For $X,Y\\in\\operatorname{Top}$, with $Y$ locally compact,",\
                " $X^Y\\in\\operatorname{Top}$ is an exponential object.")\
                .scale(.75).shift(
                    1.5*UP
                )

        general = TexMobject("\\operatorname{Hom}_{\\operatorname{Top}}(Z\\times Y,X)\
                    \\cong \\operatorname{Hom}_{\\operatorname{Top}}(Z,X^Y)").set_color(BLUE)\
                    .scale(.75)
        particular = TexMobject("\\operatorname{Hom}_{\\operatorname{Top}}(Y,X)\\cong\
                    \\operatorname{Hom}_{\\operatorname{Top}}(1,X^Y)").set_color(BLUE)\
                    .scale(.75)
        gp = VGroup(
            general,
            particular
        ).arrange_submobjects(
            DOWN,
            buff=.5
        )

        self.play(
            Write(proptitle)
        )
        self.wait(2)
        self.play(
            ShowCreation(intro)
        )
        self.wait(2)
        self.play(
            ShowCreation(gp)
        )
        self.wait(3)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

class remark121(Scene):
    def construct(self):
        rmktitle = TextMobject("\\textsc{Remark 1.21}").scale(.75).to_edge(LEFT,buff=MED_LARGE_BUFF)\
                    .to_edge(UP,buff=MED_LARGE_BUFF)

        pt1 = TextMobject("- The assumption that $Y$ is locally compact is necessary.").scale(.75)
        pt2 = TextMobject("- When we need Cartesian closure, we can try to pass to a subcategory.")\
                .scale(.75)

        gp = VGroup(
            pt1,
            pt2
        ).arrange_submobjects(
            DOWN,
            aligned_edge=LEFT,
            buff=.5
        )

        self.play(
            Write(rmktitle)
        )
        self.wait(2)
        self.play(
            FadeIn(gp)
        )




from manimlib.imports import *
from NumberCreature.NumberCreature import *

class title(Scene):
    def construct(self):
        dforms = TextMobject("Differential Forms")\
                .shift(.5*UP)
        p2 = TextMobject("Part 2: Differential 1-Forms")\
                .scale(.75)\
                .next_to(dforms, direction=DOWN, buff=MED_SMALL_BUFF)

        self.wait()
        self.play(  ShowCreation(dforms,run_time=3))
        self.wait(2)
        self.play(  FadeIn(p2,run_time=3))
        self.wait()

        Ale = Alex().scale(.5).shift(3*DOWN)
        Ale[4].set_color(GREEN)

        self.play(  GrowFromCenter(Ale))
        self.wait()
        self.play(  NumberCreatureSays(Ale,"$\\small{dx }$?", bubble_class=ThoughtBubble,\
                                        bubble_kwargs={"height":1.25,"width":1.75}))
        self.wait()
        self.play(  Blink(Ale))
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

class startoff(Scene):
    def construct(self):
        space = TextMobject("Space: $\\mathbb{R}^n$")\
                    .to_edge(UP,buff=1.5)\
                    .to_edge(LEFT,buff=2)\
                    .scale(.75)

        u = TextMobject("$U$"," is an open subset of $\\mathbb{R}^n$")\
                .scale(.75)\
                .next_to(space,buff=MED_LARGE_BUFF, direction=DOWN)
        u[0].set_color(YELLOW)

        p = TexMobject("p","\\in", "U")\
                .next_to(u,buff=SMALL_BUFF, direction=DOWN)\
                .scale(.75)
        p[0].set_color(PURPLE)
        p[-1].set_color(YELLOW)

        tspace = TextMobject("Tangent space: $T_p\\mathbb{R}^n$")\
                    .next_to(p,buff=MED_LARGE_BUFF, direction=DOWN)\
                    .scale(.75)

        cspace = TextMobject("Cotangent space: $T_p^\\ast \\mathbb{R}^n$")\
                    .next_to(tspace,buff=SMALL_BUFF, direction=DOWN)\
                    .scale(.75)

        omg = TexMobject("\\omega","_p","\\in T_p^\\ast \\mathbb{R}^n")\
                .next_to(cspace,buff=MED_LARGE_BUFF, direction=DOWN)\
                .scale(.75)
        omg[0].set_color(BLUE)
        omg[1].set_color(PURPLE)

        self.wait()
        self.play(FadeIn(space))
        self.wait(2)
        self.play(  ShowCreation(u))
        self.play(  ShowCreation(p))
        self.wait(2)
        self.play(  ShowCreation(tspace))
        self.wait()
        self.play(  ShowCreation(cspace))
        self.wait(2)
        self.play(  ShowCreation(omg))
        self.wait()

        div = Line((-1,-3,0),(-1,3,0), stroke_width=1.25)

        self.play(  ShowCreation(div))
        self.wait()

        donef = TextMobject("Differential 1-forms:")\
                    .scale(1)\
                    .next_to(space,buff=4)

        diffdef = TextMobject("a function that maps")\
                    .scale(.75)\
                    .next_to(donef,buff=MED_LARGE_BUFF, direction=DOWN)

        diffdef2 = TexMobject("p","\\mapsto","\\omega","_p")\
                    .scale(.75)\
                    .next_to(diffdef,buff=SMALL_BUFF, direction=DOWN)
        diffdef2[0].set_color(PURPLE)
        diffdef2[-1].set_color(PURPLE)
        diffdef2.set_color_by_tex("\\omega",BLUE)

        self.play(  ShowCreation(donef))
        self.wait()
        self.play(  ShowCreation(diffdef))
        self.play(  ShowCreation(diffdef2))
        self.wait()
        
        Ale = Alex().scale(.5).next_to(diffdef2,buff=1.5,direction=DOWN)
        Ale[4].set_color(GREEN)

        self.play(  GrowFromCenter(Ale))
        self.wait(2)
        self.play(  Blink(Ale))
        self.wait(2)
        self.play(  *[FadeOut(mob)for mob in self.mobjects])
        self.wait()

class pushforwards(Scene):
    def construct(self):
        push = TextMobject("Pushforwards")\
                .to_edge(UP,buff=MED_LARGE_BUFF)
        
        self.wait()
        self.play(  ShowCreation(push))
        self.wait(2)

        elt = TexMobject("X","\\in T_p\\mathbb{R}^n")\
                .scale(.75)\
                .next_to(push,buff=1.5,direction=DOWN)
        elt[0].set_color(RED)

        f = TexMobject("f",":\\mathbb{R}^n\\rightarrow\\mathbb{R}")\
                .scale(.75)\
                .next_to(elt,buff=MED_SMALL_BUFF, direction=DOWN)
        f[0].set_color(BLUE)
        cool = TexMobject("d","f","_p(","X",")=","X","(","f",")")\
                .scale(.75)\
                .next_to(f,buff=LARGE_BUFF, direction=DOWN)
        cool.set_color_by_tex("f",BLUE)
        cool.set_color_by_tex("X",RED)

        self.play(  ShowCreation(elt))
        self.play(  ShowCreation(f))
        self.wait(2)
        self.play(  ShowCreation(cool))
        self.wait(2)
        self.play(  *[FadeOut(mob)for mob in self.mobjects])

class ex1(Scene):
    def construct(self):
        title = TextMobject("Example 1:")\
                    .to_edge(UP,buff=MED_SMALL_BUFF)
        
        self.wait()
        self.play(  FadeIn(title))
        self.wait(2)

        f = TexMobject("f",":U\\rightarrow\\mathbb{R}")\
                .shift(4*LEFT,1.5*UP)
        f[0].set_color(BLUE)
        fin = TexMobject("\\in C^1")\
                .next_to(f,buff=SMALL_BUFF,direction=DOWN)
        p = TexMobject("p","\\in","U")\
                .next_to(fin,buff=MED_LARGE_BUFF,direction=DOWN)
        p[0].set_color(PURPLE)
        q = TexMobject("q","=","f","(","p",")")\
                .next_to(p,buff=SMALL_BUFF,direction=DOWN)
        q.set_color_by_tex("q",GREEN)
        q.set_color_by_tex("p",PURPLE)
        q.set_color_by_tex("f",BLUE)

        self.play(  ShowCreation(f))
        self.play(  ShowCreation(fin))
        self.wait(2)
        self.play(  ShowCreation(p))
        self.play(  ShowCreation(q))
        self.wait()

        div = Line((-1.5,-3,0),(-1.5,3,0),stroke_width=1.25)

        self.play(  ShowCreation(div))
        self.wait()

        dfp = TexMobject("d","f","_p",":T","_p","\\mathbb{R}^n\\rightarrow T","_q","\\mathbb{R}")\
                .next_to(f,buff=3.75)\
                .scale(.75)
        dfp.set_color_by_tex("f",BLUE)
        dfp.set_color_by_tex("p",PURPLE)
        dfp.set_color_by_tex("q",GREEN)

        self.play(  ShowCreation(dfp))
        self.wait(2)

        identi = TexMobject("(q,v)","\\mapsto","v")\
                    .next_to(dfp,buff=SMALL_BUFF,direction=DOWN)\
                    .scale(.75)
        self.play(  ShowCreation(identi))
        self.wait(2)

        canbe = TexMobject("d","f","_p",":T","_p","\\mathbb{R}\\rightarrow\\mathbb{R}")\
                    .next_to(identi,buff=MED_LARGE_BUFF,direction=DOWN)\
                    .scale(.75)
        canbe.set_color_by_tex("f",BLUE)
        canbe.set_color_by_tex("p",PURPLE)

        self.play(  ShowCreation(canbe))
        self.wait()

        canbein = TexMobject("\\in", "T^\\ast","_p","\\mathbb{R}^n")\
                    .next_to(canbe,buff=SMALL_BUFF,direction=DOWN)\
                    .scale(.75)
        canbein[2].set_color(PURPLE)

        self.play(  FadeIn(canbein))
        self.wait(2)

        rev = TextMobject("The assignment")\
                .scale(.75)\
                .next_to(canbein,buff=MED_LARGE_BUFF,direction=DOWN)\
                .shift(.75*LEFT)

        assignment = TexMobject("p","\\mapsto","d","f","_p")\
                        .scale(.75)\
                        .next_to(rev,buff=.25)
        assignment[0].set_color(PURPLE)
        assignment[-1].set_color(PURPLE)
        assignment.set_color_by_tex("f",BLUE)

        self.play(  ShowCreation(rev))
        self.play(  ShowCreation(assignment))

        rev2 = TextMobject("defines the 1-form")\
                .scale(.75)\
                .next_to(rev,buff=SMALL_BUFF,direction=DOWN)\
                .shift(.75*RIGHT)
        
        oneform = TexMobject("df",":","U","\\rightarrow","T^\\ast","_p","\\mathbb{R}^n")\
                    .scale(.75)\
                    .next_to(rev2,buff=SMALL_BUFF+.1,direction=DOWN)
        oneform[0].set_color(RED)
        oneform[-2].set_color(PURPLE)

        self.play(  ShowCreation(rev2))
        self.play(  ShowCreation(oneform[:2]))

        self.play(  Transform(assignment[0].copy(),oneform[2]))
        self.play(  ShowCreation(oneform[3]))
        self.play(  Transform(assignment[2:].copy(),oneform[4:]))
        self.wait(3)

        self.play(  *[FadeOut(mob)for mob in self.mobjects])

class ex2(Scene):
    def construct(self):
        title = TextMobject("Example 2:")\
                    .to_edge(UP,buff=MED_LARGE_BUFF)
    
        self.wait()
        self.play(  FadeIn(title))
        self.wait()

        integral = TexMobject("\int_a^b f(x)\\ dx")\
                    .next_to(title,buff=LARGE_BUFF,direction=DOWN)

        self.play(  ShowCreation(integral))
        self.wait()

        Ale = Alex().scale(.5).shift(2*DOWN)
        Ale[4].set_color(GREEN)

        self.play(  GrowFromCenter(Ale))
        self.wait()

        whatsays = TexMobject("dx","?")
        whatsays[0].set_color(RED)
        self.play(  NumberCreatureSays(Ale,whatsays,bubble_class=ThoughtBubble,\
                    bubble_kwargs={"height":1.5,"width":2}))
        self.wait()
        self.play(  Blink(Ale))
        self.wait(2)
        self.play(  RemovePiCreatureBubble(Ale),*[FadeOut(mob)for mob in [Ale,integral]])
        self.wait()

        exp = TexMobject("(","dx_i",")","\\Big(","\\dfrac{\\partial}{\\partial x_j}","\\Big)_p")\
                .shift(1*UP)
        exp[1].set_color(RED)
        exp[-2].set_color(BLUE)

        self.play(  ShowCreation(exp))
        self.wait()
        
        xiis = TexMobject("x_i(a_1,a_2,\\dots,a_i,\dots,a_n)=a_i")\
                .scale(.75)\
                .next_to(exp,buff=MED_LARGE_BUFF, direction=DOWN)

        self.play(  ShowCreation(xiis))
        self.wait(2)
        self.play(  FadeOut(xiis))
        self.wait()

        exc = exp.copy()

        expcopy = TexMobject("=","(","dx_i",")","\\Big(","\\dfrac{\\partial}{\\partial x_j}","\\Big)_p")\
                .next_to(exp,buff=MED_SMALL_BUFF,direction=DOWN)
        expcopy[2].set_color(RED)
        expcopy[-2].set_color(BLUE)

        self.play(  Transform(exc,expcopy))
        self.add(expcopy)
        self.wait()

        newexp = TexMobject("=","\\dfrac{\\partial}{\\partial x_i}","x_i")\
                    .next_to(exp,buff=MED_LARGE_BUFF,direction=DOWN)

        pforward = TextMobject("(pushforward)").next_to(newexp,buff=LARGE_BUFF)\
                    .scale(.75)

        self.remove(exc)
        self.play(  Transform(expcopy[2].copy(),newexp[-1]), Transform(expcopy[0].copy(),newexp[0]),\
                    Transform(expcopy[-2].copy(),newexp[1]), FadeOut(expcopy))
        self.play(  ShowCreation(pforward))
        self.wait()

        equals1 = TexMobject("=\\begin{cases}0&i\\neq j\\\ 1&i=j\\end{cases}")\
                    .next_to(newexp,buff=MED_SMALL_BUFF,direction=DOWN)

        self.play(  ShowCreation(equals1))
        self.wait()

        kdelta = TexMobject("=\delta^i_j")\
                    .next_to(newexp,buff=MED_LARGE_BUFF,direction=DOWN)

        self.play(  Transform(equals1,kdelta))
        self.wait()
        self.play(  *[FadeOut(mob)for mob in self.mobjects])

class partialpart(Scene):
    def construct(self):
        title = TextMobject("Let's consider $\\dfrac{\\partial}{\\partial x_i}$:")\
                .scale(.75)\
                .to_edge(LEFT,buff=MED_LARGE_BUFF)\
                .to_edge(UP,buff=MED_LARGE_BUFF)

        self.wait()
        self.play(  ShowCreation(title))
        self.wait()

        rnbasis = TexMobject("\\{ e_i\\}=\\{e_0,e_1,\\dots,e_n\\}")\
                    .scale(.75)\
                    .shift(2*LEFT,1*UP)

        self.play(  ShowCreation(rnbasis))
        self.wait()

        rnbasislabel = TextMobject("basis of $\\mathbb{R}^n$")\
                        .scale(.75)\
                        .next_to(rnbasis,direction=DOWN,buff=2)
        ar1 = Arrow(DOWN,UP,length=.75)\
                .next_to(rnbasislabel,direction=UP,buff=SMALL_BUFF)

        self.play(  ShowCreation(rnbasislabel), ShowCreation(ar1))
        self.wait()

        tspacebasis = TexMobject("\\{(p,e_i)\\}")\
                        .scale(.75)\
                        .next_to(rnbasis,buff=2)

        self.play(  ShowCreation(tspacebasis))
        self.wait()

        tspacebasislabel = TextMobject("basis of $T_p\\mathbb{R}^n$")\
                        .scale(.75)\
                        .next_to(tspacebasis,direction=DOWN,buff=2)

        ar2 = Arrow(DOWN,UP,length=.75)\
                .next_to(tspacebasislabel,direction=UP,buff=SMALL_BUFF)

        self.play(  ShowCreation(tspacebasislabel), ShowCreation(ar2))
        self.wait()

        claim = TextMobject("Claim: We can associate the ","$\\{(p,e_i)\\}$"," with ",\
                    "$\\{\\dfrac{\\partial}{\\partial x_i}\\}$.")\
                    .scale(.75)\
                    .shift(1.5*LEFT,1.5*UP)

        self.play(  *[FadeOut(mob)for mob in [ar1,ar2,rnbasis,rnbasislabel,\
                    tspacebasislabel]], ShowCreation(claim[0]), Transform(tspacebasis,claim[1]),\
                    ShowCreation(claim[-2:]) )
        self.wait()

        implic = TextMobject("Implies $\\{\\dfrac{\\partial}{\\partial x_i}\\}$ is a \
                    basis of $T_p\\mathbb{R}^n$")\
                    .scale(.75)\
                    .set_color(GREEN)

        self.play(  GrowFromCenter(implic))
        self.wait()
        self.play(  FadeOut(implic))
        self.wait()

        claimcopy = claim.copy()\
                        .to_edge(LEFT,buff=MED_LARGE_BUFF)\
                        .to_edge(UP,buff=MED_LARGE_BUFF)

        prop = TextMobject("Proposition: $\\phi:T_p\\mathbb{R}^n\\rightarrow \\mathcal{D}_p\\mathbb{R}^n$\
                 is an isomorphism of vector spaces.")\
                 .scale(.75)\
                 .next_to(claimcopy,buff=MED_SMALL_BUFF,direction=DOWN)\
                 .set_color(BLUE)\
                 .shift(1.35*RIGHT)

        self.remove( tspacebasis)
        self.play(  FadeOut(title), Transform(claim,claimcopy))
        self.wait()
        self.play(  ShowCreation(prop))
        self.wait()

        isderivation = TextMobject("set of derivations at $p$")\
                        .scale(.75)\
                        .next_to(prop,buff=2,direction=DOWN)\
                        .shift(.85*LEFT)
        arderivation = Arrow(DOWN,UP)\
                        .next_to(isderivation,direction=UP,buff=SMALL_BUFF)

        self.play(  *[ShowCreation(mob)for mob in [isderivation,arderivation]])
        self.wait()
        self.play(  *[FadeOut(mob)for mob in [isderivation,arderivation]])
        self.wait()

        p = TexMobject("p\\in\\mathbb{R}^n")\
                .to_edge(LEFT,buff=MED_LARGE_BUFF)\
                .shift(.5*UP)\
                .scale(.75)
        v = TexMobject("v\\in T_p\\mathbb{R}^n")\
                .scale(.75)\
                .next_to(p,buff=MED_LARGE_BUFF,direction=DOWN)
        aoft = TexMobject("a(t)=(p_1+tv_1,\dots,p_n+tv_n)")\
                .scale(.75)\
                .next_to(v,buff=MED_LARGE_BUFF,direction=DOWN)\
                .shift(1.5*RIGHT)
        fcinf = TextMobject("$f$ is $C^\\infty$ near $p$")\
                .scale(.75)\
                .next_to(aoft,buff=MED_LARGE_BUFF,direction=DOWN)\
                .shift(1*LEFT)

        self.play(  ShowCreation(p))
        self.wait()
        self.play(  ShowCreation(v))
        self.wait()
        self.play(  ShowCreation(aoft))
        self.wait()
        self.play(  ShowCreation(fcinf))
        self.wait()

        div = Line((-1,-3,0),(-1,1.5,0),stroke_width=1)

        self.play(  ShowCreation(div))
        self.wait()

        limdef = TexMobject("D_v f=\\lim_{t\\rightarrow 0}\\dfrac{f(a(t))-f(v)}{t}")\
                    .scale(.75)\
                    .shift(2.5*RIGHT,1*UP)
        limdefeq1 = TexMobject("=\\sum_{i=1}^n \\dfrac{\\partial f}{\\partial x_i}(p)\
                        \\dfrac{da_i}{dt}(0)")\
                        .scale(.75)\
                        .next_to(limdef,direction=DOWN,buff=MED_SMALL_BUFF)\
                        .shift(1.25*LEFT)

        chainrule = TextMobject("(chain rule)")\
                        .scale(.75)\
                        .next_to(limdefeq1,buff=MED_LARGE_BUFF+.5)\
                        .set_color(GREEN)
        limdefeq2 = TexMobject("=\\sum_{i=1}^n v_i \\dfrac{\\partial f}{\\partial x_i}(p)")\
                        .scale(.75)\
                        .next_to(limdef,direction=DOWN,buff=MED_SMALL_BUFF)

        self.play(  ShowCreation(limdef   ))
        self.wait()
        self.play(  ShowCreation(limdefeq1))
        self.play(  FadeIn(chainrule))
        self.wait()
        self.play(  Transform(limdefeq1,limdefeq2), FadeOut(chainrule))
        self.wait()

        dv = TexMobject("D_v=\\sum_{i=1}^n v_i\\dfrac{\\partial}{\\partial x_i}(p)")\
                .scale(.75)\
                .next_to(limdefeq2,direction=DOWN,buff=MED_SMALL_BUFF)\
                .set_color(YELLOW)

        phimaps = TexMobject("p","\\mapsto","D_v")\
                    .next_to(dv,buff=MED_LARGE_BUFF,direction=DOWN)\
                    .scale(.75)\
                    .set_color(BLUE)

        self.play(  ShowCreation(dv))
        self.wait()
        self.play(  ShowCreation(phimaps))
        self.wait()

        self.play(  Transform(phimaps,phimaps.copy().next_to(prop,direction=DOWN,buff=MED_SMALL_BUFF)\
                    .shift(1.75*LEFT)),\
                    *[FadeOut(mob)for mob in [p,v,aoft,fcinf,div,limdef,limdefeq2,dv,limdefeq1]])
        self.wait()

        confirms = TextMobject("$D_v\\in\\mathcal{D}_p\\mathbb{R}^n$ since \
                        $D_v(fg)=f(D_vg)+(D_vf)g$")
        self.play(  ShowCreation(confirms))
        self.wait()
        self.play(  FadeOut(confirms))
        self.wait()

        # show injectivity

        injectivetitle = TextMobject("Injectivity:")\
                            .scale(.75)\
                            .next_to(prop,buff=LARGE_BUFF,direction=DOWN)\
                            .shift(2*LEFT)

        injp1 = TexMobject("\\mbox{if }","D","v","=","0,")\
                    .scale(.75)\
                    .next_to(injectivetitle,buff=2)

        injp2 = TexMobject("0=D_v(x^j)")\
                    .scale(.75)\
                    .next_to(injp1,buff=MED_SMALL_BUFF,direction=DOWN)

        injp3 = TexMobject("=\\sum_{i=1}^n v^i\\dfrac{\\partial}{\\partial x^i}\\mid_p x^j")\
                    .scale(.75)\
                    .next_to(injp2,buff=MED_SMALL_BUFF,direction=DOWN)

        injp4 = TexMobject("=\\sum_{i=1}^n v^i\\delta_i^j=v^j")\
                    .scale(.75)\
                    .next_to(injp2,buff=MED_SMALL_BUFF,direction=DOWN)


        self.play(  FadeIn(injectivetitle))
        self.wait()
        self.play(  ShowCreation(injp1))
        self.wait()
        self.play(  ShowCreation(injp2))
        self.wait()
        self.play(  ShowCreation(injp3))
        self.wait()
        self.play(  Transform(injp3,injp4))
        self.wait()
        self.play(  *[FadeOut(mob)for mob in [injectivetitle,injp1,injp2,injp3]])
        self.wait()

        # show surjectivity

        surjtitle = TextMobject("Surjectivity:")\
                            .scale(.75)\
                            .next_to(prop,buff=LARGE_BUFF,direction=DOWN)\
                            .shift(4*LEFT)

        ustar = TextMobject("$U\\subset\\mathbb{R}^n$, star-shaped")\
                    .scale(.75)\
                    .to_edge(LEFT,buff= LARGE_BUFF)

        pustar = TexMobject("p\\in U")\
                    .scale(.75)\
                    .next_to(ustar,buff=MED_SMALL_BUFF,direction=DOWN)

        fstar = TexMobject("f:U\\rightarrow\\mathbb{R}^n,\\ C^\\infty")\
                    .scale(.75)\
                    .next_to(pustar,buff=MED_SMALL_BUFF,direction=DOWN)

        csurj = TexMobject("c",":U\\rightarrow\\mathbb{R}^n,\\ c(x)=f(p)")\
                    .scale(.75)\
                    .next_to(fstar,buff=MED_SMALL_BUFF,direction=DOWN)
        csurj[0].set_color(RED)

        cisurj = TexMobject("c^i",":U\\rightarrow\\mathbb{R}^n,\\ c^i(x)=p^i")\
                    .scale(.75)\
                    .next_to(csurj,buff=MED_SMALL_BUFF,direction=DOWN)
        cisurj[0].set_color(ORANGE)

        piisurj = TexMobject("\\pi^i",":U\\rightarrow\\mathbb{R}^n,\\ \\pi^i(x)=x^i")\
                    .scale(.75)\
                    .next_to(cisurj,buff=MED_SMALL_BUFF,direction=DOWN)
        piisurj[0].set_color(GREEN)

        self.play(  FadeIn(surjtitle))
        self.wait()
        self.play(  ShowCreation(ustar))
        self.wait()
        self.play(  ShowCreation(pustar))
        self.wait()
        self.play(  ShowCreation(fstar))
        self.wait()
        self.play(  ShowCreation(csurj))
        self.wait()
        self.play(  ShowCreation(cisurj))
        self.wait()
        self.play(  ShowCreation(piisurj))
        self.wait()

        div2 = Line((-1,-3,0),(-1,1.5,0),stroke_width=1).shift(.25*DOWN)

        self.play(  ShowCreation(div2))
        self.wait()

        foraconst = TextMobject("For a constant function $g$,")\
                        .scale(.75)\
                        .next_to(surjtitle,buff=5)
        cis01 = TexMobject("D(g)=gD(1)")\
                    .scale(.75)\
                    .next_to(foraconst,buff=MED_LARGE_BUFF,direction=DOWN)
        cis02 = TexMobject("D(1)=D(1\cdot 1)=D(1)\cdot 1+1\cdot D(1)=2D(1)")\
                    .scale(.75)\
                    .next_to(cis01,buff=MED_SMALL_BUFF,direction=DOWN)
        cis03 = TexMobject("D(1)=0")\
                    .scale(.75)\
                    .next_to(cis02,buff=MED_SMALL_BUFF,direction=DOWN)
        cis04 = TexMobject("D(g)=0")\
                    .scale(.75)\
                    .next_to(cis03,buff=MED_SMALL_BUFF,direction=DOWN)

        self.play(  ShowCreation(foraconst))
        self.wait()
        self.play(  ShowCreation(cis01))
        self.wait()
        self.play(  ShowCreation(cis02))
        self.wait()
        self.play(  ShowCreation(cis03))
        self.wait()
        self.play(  ShowCreation(cis04))
        self.wait()
        self.play(  *[FadeOut(mob)for mob in [foraconst,cis01,cis02,cis03,cis04]])
        self.wait()

        bytaylor = TextMobject("By Taylor's theorem:")\
                    .scale(.75)\
                    .next_to(surjtitle,buff=5)

        c1 = TexMobject("f=c+\\sum_{i=1}^n(\\pi^i-c^i)\\dfrac{\\partial}{\\partial x_i}")\
                    .scale(.75)\
                    .next_to(bytaylor,buff=MED_LARGE_BUFF,direction=DOWN)

        c2 = TexMobject("Df=Dc+\\sum_{i=1}^n D((\\pi^i -c^i)\\dfrac{\\partial}{\\partial x_i})")\
                    .scale(.75)\
                    .next_to(c1,buff=MED_SMALL_BUFF,direction=DOWN)

        c3 = TexMobject("Df=\\sum_{i=1}^n D(\\pi^i-c^i)(\\dfrac{\\partial}{\\partial x_i}(p))\
                +\\sum_{i=1}^n (\\pi^i(p)-c^i(p))(D(\\dfrac{\\partial}{\\partial x_i}))")\
                    .scale(.5)\
                    .next_to(c2,buff=MED_SMALL_BUFF,direction=DOWN)

        c4 = TexMobject("Df=\\sum_{i=1}^n (D\\pi^i - Dc^i)(\\dfrac{\\partial}{\\partial x_i}(p))")\
                    .scale(.75)\
                    .next_to(c2,buff=MED_SMALL_BUFF,direction=DOWN)

        c5 = TexMobject("Df=\\sum_{i=1}^n D\\pi^i \\dfrac{\\partial}{\\partial x_i}(p)")\
                    .scale(.75)\
                    .next_to(c2,buff=MED_SMALL_BUFF,direction=DOWN)

        self.play(  ShowCreation(bytaylor))
        self.wait()
        self.play(  ShowCreation(c1))
        self.wait()
        self.play(  ShowCreation(c2))
        self.wait()
        self.play(  ShowCreation(c3))
        self.wait()
        self.play(  Transform(c3,c4))
        self.add(c4)
        self.remove(c3)
        self.wait()
        self.play(  Transform(c4,c5))
        self.add(c5)
        self.remove(c4)
        self.wait()
        self.play(  *[FadeOut(mob)for mob in [c1,c2,bytaylor]],\
                    Transform(c5,c5.copy().move_to(bytaylor)))
        self.wait()

        letv = TextMobject("let $v=(Dx^1,\\dots,Dx^n)$")\
                .scale(.75)\
                .next_to(bytaylor,buff=MED_LARGE_BUFF,direction=DOWN)

        finalr = TexMobject("Df=D_vf")\
                    .scale(.75)\
                    .next_to(letv,buff=MED_SMALL_BUFF,direction=DOWN)

        finalr2 = TexMobject("D=D_v")\
                    .scale(.75)\
                    .next_to(letv,buff=MED_SMALL_BUFF,direction=DOWN)

        self.play(  ShowCreation(letv))
        self.wait()
        self.play(  ShowCreation(finalr))
        self.wait()
        self.play(  Transform(finalr,finalr2))
        self.wait()

        self.play(  *[FadeOut(mob)for mob in self.mobjects[1:]])
        self.wait()

        bp1 = TextMobject("basis of $T_p\\mathbb{R}^n$")\
                .scale(.75)\
                .next_to(claimcopy[1],buff=2,direction=DOWN)
        abp1 = Arrow(DOWN,UP)\
                .next_to(bp1,buff=SMALL_BUFF,direction=UP)
        bp2 = TextMobject("basis of $\\mathcal{D}_p\\mathbb{R}^n$")\
                .scale(.75)\
                .next_to(claimcopy[-1],buff=2)
        abp2 = Arrow(RIGHT,LEFT)\
                .next_to(bp2,buff=SMALL_BUFF,direction=LEFT)

        self.play(  *[ShowCreation(mob)for mob in [bp1,abp1,bp2,abp2]])
        self.wait()
        self.play(  *[FadeOut(mob)for mob in self.mobjects])

class dualstuff(Scene):
    def construct(self):

        exp = TexMobject("(","dx_i",")","\\Big(","\\dfrac{\\partial}{\\partial x_j}","\\Big)_p=\delta_j^i")\
                .shift(1*UP)
        exp[1].set_color(RED)
        exp[-2].set_color(BLUE)

        self.play(      ShowCreation(exp))
        self.wait(3)


        exp = TexMobject("(","dx_i",")","\\Big(","\\dfrac{\\partial}{\\partial x_j}","\\Big)_p")\
                .shift(2*UP)
        exp[1].set_color(RED)
        exp[-2].set_color(BLUE)

        self.wait()
        self.play(  ShowCreation(exp))
        self.wait()

        dis1 = TextMobject("$dx_i$"," is biorthogonal to ","$\\dfrac{\\partial}{\\partial x_j}$")\
                .scale(.75)\
                .next_to(exp,buff=LARGE_BUFF,direction=DOWN)
        dis1[0].set_color(RED)
        dis1[-1].set_color(BLUE)

        dis2 = TextMobject("$dx_i$"," is the dual basis of ","$\\dfrac{\\partial}{\\partial x_j}$")\
                .scale(.75)\
                .next_to(exp,buff=LARGE_BUFF,direction=DOWN)
        dis2[0].set_color(RED)
        dis2[-1].set_color(BLUE)

        self.play(  ShowCreation(dis1))
        self.wait()
        self.play(  Transform(dis1,dis2))
        
class dualstuff2(Scene):
    def construct(self):
        partialxi = TexMobject("\\dfrac{\\partial}{\\partial x_i}")\
                .move_to((-2,2,0))\
                .set_color(BLUE)
        partialxitext = TexMobject("T_p\\mathbb{R}^n")\
                .move_to((-2,-2,0))\
                .set_color(BLUE)
        dxi = TexMobject("dx_i")\
                .move_to((2,2,0))\
                .set_color(RED)
        dxitext = TexMobject("T_p^\\ast \\mathbb{R}^n")\
                .move_to((2,-2,0))\
                .set_color(RED)
        l1 = Line((-2,-1.35,0),(-2,1.35,0),stroke_width=1.5)
        b1 = TextMobject("basis").scale(.75)\
                .rotate(PI/2)\
                .next_to(l1,buff=SMALL_BUFF,direction=LEFT)
        l2 = Line(tuple(map(lambda i, j: (i + j), l1.get_points()[0], (4,0,0))),\
                tuple(map(lambda i, j: (i + j), l1.get_points()[-1], (4,0,0))),stroke_width=1.5)
        b2 = TextMobject("basis").scale(.75)\
                .rotate(PI/2)\
                .next_to(l2,buff=SMALL_BUFF,direction=LEFT)
        
        l11 = Line((-1.35,2,0),(1.35,2,0),stroke_width=1.5)
        b11 = TextMobject("dual").scale(.75)\
                .rotate(0)\
                .next_to(l11,buff=SMALL_BUFF,direction=UP)
        l22 = Line(tuple(map(lambda i, j: (i + j), l11.get_points()[0], (0,-4,0))),\
                tuple(map(lambda i, j: (i + j), l11.get_points()[-1], (0,-4,0))),stroke_width=1.5)
        b22 = TextMobject("dual").scale(.75)\
                .rotate(0)\
                .next_to(l22,buff=SMALL_BUFF,direction=UP)
        
        self.wait()
        self.play(  *[ShowCreation(mob)for mob in [partialxitext,partialxi,dxitext,dxi]])
        self.wait()
        self.play(  *[ShowCreation(mob)for mob in [l1,b1,l2,b2]])
        self.wait()
        self.play(  *[ShowCreation(mob)for mob in [l11,b11,b22,l22]])
        self.wait()
        self.play(  *[FadeOut(mob)for mob in self.mobjects])

class intofforms(Scene):
    def construct(self):
        title = TextMobject("Integrations of forms:")\
                    .to_edge(UP,buff=LARGE_BUFF)

        self.wait()
        self.play(  ShowCreation(title))
        self.wait()

        integral = TexMobject("\\int", "f(x)dx")\
                    .shift(0*UP)

        brace1 = Brace(integral[1], DOWN, buff = SMALL_BUFF)
        t1 = brace1.get_text("one-form")

        self.play(  ShowCreation(integral))
        self.wait()
        self.play(  GrowFromCenter(brace1), FadeIn(t1))
        self.wait()

        newintegral = TexMobject("\\int df")
        p2 = TexMobject("=\\int \\sum_{i=1}^n\\dfrac{\\partial}{\\partial x_i} dx_i")\
                .next_to(newintegral,buff=MED_LARGE_BUFF,direction=DOWN)

        self.play(  FadeOut(brace1), FadeOut(t1),\
                    Transform(integral,newintegral))
        self.wait()
        self.play(  ShowCreation(p2))
        self.wait()
        self.play(  *[FadeOut(mob)for mob in self.mobjects])








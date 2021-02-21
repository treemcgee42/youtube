# Date: 2/15/21
# Purpose: first suspension and looping section
# Notes:

from manimlib.imports import *
fn = "sus_and_looping"


class def129(Scene):
    """
    We previously discussed one way we could potentially form reduced suspensions
    and loop spaces. This was the most natural way, but it wasn't obviously
    canonical, and there exist other ways to model the behavior we'd like from
    reduced suspensions and loop spaces.
    """
    def construct(self):
        t = make_title("Definition", 1.29)

        self.title(t)

        d1 = TextMobject(r"""
            \begin{enumerate}
                \item the \textbf{standard suspension} of $X$ is the smash-product-tensoring 
                    $X\wedge S^1$
                \item the \textbf{standard looping} of $X$ is the smash powering 
                    Maps$(S^1, X)_\ast$
            \end{enumerate}
        """).scale(.75)

        self.cycle(
            [d1],
            out=False
        )
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class prop130(Scene):
    """
    Within the model structure on pointed topological spaces, we observed that
    the suspension operation could also be visualized as the following cofiber.
    In the context of sequential spectra, the aforementioned standard suspension
    can be expressed as a cofiber of the canonical inclusion of the wedge product
    into the standard cylinder spectrum.
    Since we are trying to construct a model structure on the category of sequential
    spectra, and in that context suspensions have a deeper meaning. In particular,
    we would like to eventually show that the standard cylinder spectrum is actually
    a cylinder object in the homotopy-theoretic sense. So in particular, we would
    need this inclusion map to be a cofibration.
    In case it is unclear why we have this homeomorphism, just consider this diagram.
    So this is X cross I for a topological space X. Then the cofiber of the inclusion
    amounts to squashing the yellow line, or I plus, to the bottom right point, then
    including X wedge X to the top and bottom red lines, and then squashing those
    to the basepoint in the bottom right. Then we'd obtain something homeomorphic to a
    circle with the white edge, and at each point on that circle we'd have a copy of S^1,
    and the way it is connected makes it clear that this is X wedge S1.
    """
    def construct(self):
        t = make_title("Proposition", "1.30")

        self.title(t)

        p1 = TexMobject(r"""
            X\wedge S^1\simeq\text{cofib}(X\vee X\to X\wedge(I_+))
        """).scale(.75)

        self.cycle(
            [p1]
        )

        cyl = Rectangle(width=2, height=4)
        y_s = 0
        x_cross_sections = []
        
        while y_s <= cyl.height:
            x_cross_sections.append(
                Line(start=cyl.get_vertices()[2] + (0,y_s,0), end=cyl.get_vertices()[3] + (0,y_s,0))\
                .set_color(RED)
            )
            y_s += .5
        iplus = Line(start=cyl.get_vertices()[1], end=cyl.get_vertices()[2])\
            .set_color(YELLOW)

        self.play(
            FadeIn(cyl),
            FadeIn(iplus),
            *[FadeIn(mob) for mob in x_cross_sections]
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class def131(Scene):
    """
    So here's a definition we'll use a little later. The k fold shifted
    spectrum of X is pretty much what you would expect- we move all entries over
    by k. This would make the first k entries empty however, and so we define those
    objects to be points and their structure maps to be 0.
    """
    def construct(self):
        t = make_title("Definition", 1.31)

        self.title(t)

        d1 = TextMobject("The ", "$k$-fold shifted spectrum", " of $X$ is the \
            sequential spectrum $X[k]$ given by", alignment="")\
            .scale(.75).to_title(t)
        d1[1].set_color(BLUE)

        d2 = TextMobject(r"""
            \begin{equation*}
                (X[k])_n:=\begin{cases} X_{n+k} & \text{for }n+k\geq 0 \\
                    \ast & \text{otherwise} \end{cases}
            \end{equation*}
        """).scale(.75)

        d3 = TextMobject(r"""
            \begin{equation*}
                \sigma_n^{X[k]}:=\begin{cases} \sigma_{n+k}^X & \text{for }
                    n+k\geq 0 \\ 0 & \text{otherwise} \end{cases}
            \end{equation*}
        """).scale(.75).next_to(d2, direction=DOWN, buff=.5)

        self.play(
            FadeIn(d1)
        )
        self.play(
            FadeIn(d2)
        )
        self.play(
            FadeIn(d3)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class def132(Scene):
    """
    Ok, so here's one of these alternative models for the suspension and loop spaces.
    These are called that alternative suspension and looping. So the only difference
    is the alternative suspension versus the standard suspension- we are smashing
    on the left instead of the right here. Some authors call this type of 
    suspension a "fake" suspension.
    """
    def construct(self):
        t = make_title("Definition", 1.32)

        self.title(t)

        d1 = TextMobject(r"""
            \begin{enumerate}
                \item the \textbf{alternative suspension} of $X$ is the sequential spectrum 
                    $\Sigma X$ with
                \begin{enumerate}
                    \item $(\Sigma X)_n := S^1\wedge X_n$
                    \item $\sigma_n^{\Sigma X}:= S^1 \wedge (\sigma_n^X)$
                \end{enumerate}
            \end{enumerate}
        """, alignment="").scale(.65).shift(1*UP)

        d2 = TextMobject(r"""
            \begin{enumerate}
                \item[2.] the \textbf{alternative looping} of $X$ is the sequential spectrum 
                    $\Omega X$ with
                \begin{enumerate}
                    \item $(\Omega X)_n := \text{Maps}(S^1, X_n)_\ast$
                    \item $\tilde{\sigma}_n^{\Omega X} := \text{Maps}(S^1, \tilde{\sigma}_n^X)_\ast$
                \end{enumerate}
            \end{enumerate}
        """, alignment="").scale(.65).next_to(d1, direction=DOWN, buff=.5).shift(.25*LEFT)

        self.cycle(
            [d1, d2],
            out=False
        )
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class rmk134(Scene):
    """
    It's not immediately clear that smashing on the right versus the left should make
    a difference on the structure of the spectrum as a whole. So to see this,
    consider a natural isomorphism between the alternative and standard suspension
    functors. This is equivalently a diagram of the following form.
    Well, we might point out that we could cook up this map on the component spaces,
    and thus rearrange the top right to look like the top left.
    But on closer examination, this is not the case. Lets label all our copies of S^1
    to make things clear. Now, if we were to use that map to make the top right
    look like the top left, the left and right morphisms would still be using different
    copies of S^1, and so the diagram wouldn't commute. To rectify this, we'd have to
    flip the copies of S^1 in the top left, but doing this is not okay, in fact
    we can see this by observing that such a morphism would be a pointed map from S^2
    to itself and hence an element of the second homotopy group of S^2, where it
    represents a nontrivial element. We won't go into the details here.
    So while we can't cook up a natural transformation here, we might notice something
    peculiar. That this map, which looks very similar to the previous one, does represent
    a trivial homotopy. We will eventually exploit this. But in general, this sort of
    issue is the motivation for studying symmetric spectra, a different kind of spectra
    which we will hopefully study eventually.
    """
    def construct(self):
        t = make_title("Remark", 1.34)

        self.title(t)

        r1 = tikz("rmk134_r1", r"""
            \begin{tikzcd}
                S^1\wedge S^1\wedge X_n \arrow{d}[left]{S^1\wedge\sigma_n}
                    \arrow{r}[above]{\text{id}_{S^1}\wedge\phi_n} &
                    S^1\wedge X_n\wedge S^1 \arrow{d}[right]{\sigma\wedge S^1} \\
                S^1\wedge X_{n+1} \arrow{r}[below]{\phi_{n+1}} & X_{n+1}\wedge S^1
            \end{tikzcd}
        """, fn).shift(.5*UP)

        r2 = TexMobject(r"""
            S^1\wedge X_n\overset{\simeq}{\to}X_n\wedge S^1
        """).scale(.65).next_to(r1, direction=DOWN, buff=1)

        self.cycle(
            [r1, r2]
        )

        r3 = tikz("rmk134_r3", r"""
            \begin{tikzcd}
                S^1_a\wedge S^1_b\wedge X_n \arrow{d}[left]{S^1_a\wedge\sigma_n}
                    \arrow{r} &
                    S^1_a\wedge X_n\wedge S^1_b \arrow{d}[right]{\sigma\wedge S^1_b} \\
                S^1_a\wedge X_{n+1} \arrow{r} & X_{n+1}\wedge S^1_b
            \end{tikzcd}
        """, fn).shift(.5*UP)

        r4 = TexMobject(r"""
            S^1_a\wedge S^1_b\to S^1_b\wedge S^1_a
        """).scale(.65).next_to(r3, direction=DOWN, buff=1)

        r5 = TexMobject(r"""
            =-1\in\mathbb{Z}=[S^2, S^2]_\ast=\pi_2(S^2)
        """).scale(.65).next_to(r4, direction=DOWN, buff=.25)

        self.cycle(
            [r3, r4, r5]
        )

        r6 = TexMobject(r"""
            S^2_a\wedge S^1_b\to S^1_b\wedge S^2_a
        """).scale(.75)

        self.cycle(
            [r6], 
            out=False
        )
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class prop136_1(Scene):
    def construct(self):
        t = make_title("Proposition", 1.36)

        self.title(t)

        p1 = TextMobject(r"""
            \begin{enumerate}
                \item $(-)[-1]\dashv (-)[1]$
                \item $(-)\wedge S^1\dashv \text{Maps}(S^1, -)_\ast$
                \item $\Sigma\dashv\Omega$
            \end{enumerate}
        """).scale(.75)

        self.cycle(
            [p1]
        )

        p2 = TexMobject(r"""
            (-)[-1]\dashv (-)[1]
        """).scale(.75).to_title(t)

        self.cycle(
            [p2],
            out=False
        )

        p3 = tikz("prop136_1_p3", r"""
            \begin{tikzcd}
                \vdots & \vdots \\
                X_2 \arrow{r}[above]{f_3} & Y_3 \\
                X_1 \arrow{r}[above]{f_2} & Y_2 \\
                X_0 \arrow{r}[above]{f_1} & Y_1 \\
                \ast \arrow{r}[above]{f_0=0} & Y_0
            \end{tikzcd}
        """, fn).shift(1*DOWN).scale(2)

        self.cycle(
            [p3], 
            out=False
        )
        self.play(
            *[FadeOut(mob) for mob in self.mobjects[1:]]
        )

class prop136_2(Scene):
    def construct(self):
        t = make_title("Proposition", 1.36)

        self.add(t)

        p1 = TexMobject(r"""
            (-)\wedge S^1\dashv\text{Maps}(S^1, -)_\ast
        """).scale(.75).to_title(t)

        self.cycle(
            [p1]
        )

class prop136_3(Scene):
    """
    So to show this adjunction for the alternative smash looping, consider
    a homomorphism from the suspension of a spectrum to another spectrum Y.
    We can then show that this is in bijection with maps of this form.
    We observe this in the following way. For example, to show the left and
    bottom maps are in bijection, we observe the following. The morphisms
    on the top and bottom are the classical smash hom adjunction, and the vertical
    maps follow from contravariance considerations. The right and left maps
    exhibit the bijection we are after.
    So then we do the same thing one more time and get something of this form.
    This shows that we have a morphism from X to Omega Y, which shows the bijection
    on hom sets and hence the adjunction we are after.
    """
    def construct(self):
        t = make_title("Proposition", 1.36)

        self.add(t)

        p1 = TexMobject(r"""
            \Sigma\dashv\Omega
        """).scale(.75).to_title(t)

        self.cycle(
            [p1],
            out=False
        )

        p2 = TexMobject(r"""
            f:\Sigma X\to Y
        """).scale(.75).to_edge(DOWN, buff=.5)

        p3 = tikz("prop136_3_p3", r"""
            \begin{tikzcd}
                S^1\wedge S^1\wedge X_n \arrow{r}[above]{S^1\wedge f_n}
                    \arrow{d}[left]{S^1\wedge\sigma_n^X} & S^1\wedge Y_n 
                    \arrow{d}[right]{\sigma_n^Y}\\
                S^1\wedge X_{n+1} \arrow{r}[below]{f_{n+1}} & Y_{n+1}
            \end{tikzcd}
        """, fn).to_edge(LEFT, buff=1)

        p4 = tikz("prop136_3_p4", r"""
            \begin{tikzcd}
                S^1\wedge X_n \arrow{r}[above]{f_n} \arrow{d}[left]{\sigma_n^X}
                    & Y_n \arrow{d}[right]{\tilde{\sigma}_n^Y} \\
                X_{n+1} \arrow{r}[below]{\widetilde{f_{n+1}}} & 
                    \text{Maps}(S^1, Y_{n+1})_\ast
            \end{tikzcd}
        """, fn).to_edge(RIGHT, buff=1)

        self.cycle(
            [p2, p3, p4], out=False
        )
        self.play(
            FadeOut(p4),
            FadeOut(p3)
        )

        p5 = tikz("prop136_3_p5", r"""
            \begin{tikzcd}
                \text{Hom}(S^1\wedge X_{n+1}, S^1\wedge X_{n+1})
                    \arrow{r}[above]{\simeq}
                    \arrow{d}[left]{\text{Hom}(S^1\wedge\sigma_n^X,f_{n+1})}
                    & \text{Hom}(X_{n+1},\text{Maps}(S^1, S^1\wedge X_{n+1})_\ast)
                    \arrow{d}[right]{\text{Hom}(\sigma_n^X,\text{Maps}(S^1,f_{n+1})_\ast)} \\
                \text{Hom}(S^1\wedge S^1\wedge X_n, Y_{n+1})
                    \arrow{r}[above]{\simeq} &
                    \text{Hom}(S^1\wedge X_n,\text{Maps}(S^1,Y_{n+1})_\ast)
            \end{tikzcd}
        """, fn)

        self.cycle(
            [p5]
        )
        self.cycle(
            [p3,p4]
        )

        p6 = tikz("prop136_3_p6", r"""
            \begin{tikzcd}
                X_n
                    \arrow{r}[above]{\widetilde{f_n}}
                    \arrow{d}[left]{\tilde{\sigma}_n}
                    & \text{Maps}(S^1, Y_n)_\ast
                    \arrow{d}[right]{\text{Maps}(S^1,\tilde{\sigma}_n^Y)_\ast} \\
                \text{Maps}(S^1, X_{n+1})_\ast
                    \arrow{r}[below]{\text{Maps}(S^1,\widetilde{f_{n+1}})_\ast}
                    & \text{Maps}(S^1,\text{Maps}(S^1,Y_{n+1})_\ast)_\ast
            \end{tikzcd}
        """, fn)

        p7 = TexMobject(r"""
            \tilde{f}:X\to\Omega Y
        """).scale(.75).next_to(p2, direction=UP, buff=.25)

        self.cycle(
            [p6, p7],
            out=False
        )
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class prop137(Scene):
    """
    So we can finally return to this diagram which we started our series with.
    We've proven all the adjunctions, and it remains only to show that
    the diagram commutes.
    To that end, it suffices to check the suspension case, as the loop case
    follows from the uniqueness of adjoints.
    This is pretty straightforward, and for me the confusion was around why
    we could in some sense commute the smash product terms i.e. S one
    and S n, whereas we couldn't before. I believe this is because we are
    not actually permuting the terms. The way we have written it might suggest
    that, but we are simply exhibiting an isomorphism and rewriting.
    What would make this a permutation of terms goes back to remark 134,
    where we were using the particular order of the smash product in our
    construction of maps out and into them, and we had a whole permuting square.
    So that concludes our section on sequential pre-spectra.
    Next, we will move to the strict model structure on sequential spectra,
    which we have been alluding to so strongly.
    """
    def construct(self):
        t = make_title("Proposition", 1.37)

        self.title(t)

        p1 = tikz("prop137_p1", r"""
            \begin{tikzcd}
                \text{Top}_{\text{cg}}^{\ast /}
                    \arrow[yshift=-.5em]{r}[below]{\Omega}[above]{\dashv}
                    \arrow[xshift=-.5em]{d}[left]{\Sigma^\infty}[right]{\dashv}
                    & \text{Top}_{\text{cg}}^{\ast /}
                    \arrow[yshift=.5em]{l}[above]{\Sigma}
                    \arrow[xshift=-.5em]{d}[left]{\Sigma^\infty}[right]{\dashv} \\
                \text{SeqSpec}(\text{Top}_\text{cg})
                    \arrow[xshift=.5em]{u}[right]{\Omega^\infty}
                    \arrow[yshift=-.5em]{r}[below]{\Omega}[above]{\dashv}
                    & \text{SeqSpec}(\text{Top}_\text{cg})
                    \arrow[yshift=.5em]{l}[above]{\Sigma}
                    \arrow[xshift=.5em]{u}[right]{\Omega^\infty}
            \end{tikzcd}
        """, fn).scale(1.5)

        self.cycle(
            [p1]
        )

        p2 = TexMobject(r"""
            \Sigma^\infty\circ\Sigma\simeq\Sigma\circ\Sigma^\infty
        """).scale(.75).to_edge(UP, buff=1)

        p3 = TextMobject(r"""
            \begin{itemize}
                \item $(\Sigma\Sigma^\infty X)_n=S^1\wedge S^n\wedge X$
                \item $(\Sigma^\infty\Sigma X)_n=S^n\wedge S^1\wedge X$
            \end{itemize}
        """).scale(.75).shift(.5*UP)

        p4 = TexMobject(r"""
            S^1\wedge S^n\wedge X
                \overset{\simeq}{\longrightarrow}
            (S^1)^{\wedge^{n+1}}\wedge X
                \overset{\simeq}{\longrightarrow}
            S^n\wedge S^1\wedge X
        """).scale(.75).next_to(p3, direction=DOWN, buff=1)

        self.cycle(
            [p2, p3, p4], out=False
        )
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

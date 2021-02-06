# Date: 1/28/21
# Purpose: section one of part 1 sequential pre-spectra

from manimlib.imports import *


fn = "preliminaries"


class def11(Scene):
    """
    There are two major equivalent ways to define sequential spectra.
    The traditional component-wise definition is what we cover here,
    and later we will introduce the second definition via topologically
    enriched functors, which will aid us in establishing the stable 
    model structure.
    A sequential prespectrum, which is sometimes just called a sequential
    spectrum or even just a spectrum, is an object consisting of
    component spaces and structure maps. The component spaces are
    n graded, and the structure maps tell us how to move between the
    component spaces. Keep in mind, that the structure maps don't have
    to be homeomorphisms, but they can be, as we will see soon. Due to
    the suspension/loop adjunction, we can equivalently define the
    structure maps as adjunct structure maps.
    So we have a sort of chain complex between the component spaces, in
    such a way as the maps factor through the suspension/hom space.
    Homomorphisms are defined component wise is the most natural way.
    """
    def construct(self):
        title = make_title("Definition", 1.1)

        self.play(
            Write(title)
        )
        self.wait(2)

        thedef = TextMobject("A ", "sequential prespectrum", " is an object with", alignment="")\
                    .scale(.75).next_to(title, direction=DOWN, buff=1).to_edge(LEFT, buff=.5)
        thedef[1].set_color(BLUE)

        self.play(
            FadeIn(thedef)
        )

        thedefp1 = TextMobject(r"""
            \begin{enumerate}
                \item \textit{component spaces} $$X_\bullet =
                    (X_n\in\text{Top}_{\text{cg}}^{\ast /})_{n\in\mathbb{N}}$$
                \item \textit{structure maps} $$\sigma_n:S^1\wedge X_n\to X_{n+1}$$
            \end{enumerate}
        """).scale(.75).shift(2*LEFT)

        self.play(
            FadeIn(thedefp1)
        )
        self.wait(3)

        thedefp2 = TextMobject(r"""
            \begin{enumerate}
                \item \textit{component spaces} $$X_\bullet =
                    (X_n\in\text{Top}_{\text{cg}}^{\ast /})_{n\in\mathbb{N}}$$
                \item \textit{adjunct structure maps} $$\tilde{\sigma}_n:X_n\to
                    \text{Maps}(S^1,X_{n+1})_\ast$$
            \end{enumerate}
        """).scale(.75).shift(2*LEFT)

        self.play(
            ReplacementTransform(thedefp1, thedefp2)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects[1:]]
        )

        def11pic1 = tikz("1", r"""
            \begin{tikzcd}
                \cdots\arrow{d} & X_{n-1}\arrow{d} & X_n\arrow{d} & X_{n+1}\arrow{d} 
                & \cdots\arrow{d} \\
                \cdots\arrow{ur} & \Sigma X_{n-1}\arrow{ur}[rotate=30,xshift=1em]{\sigma_{n-1}} 
                & \Sigma X_n\arrow{ur}[rotate=30,xshift=1em]{\sigma_n} & \Sigma X_{n+1}
                \arrow{ur} & \cdots
            \end{tikzcd}
        """, fn)

        self.play(
            FadeIn(def11pic1)
        )
        self.wait(2)

        def11pic2 = tikz("2", r"""
            \begin{tikzcd}
                \cdots\arrow{dr} & X_{n-1}\arrow{dr}[rotate=-30,xshift=-1em]{\tilde{\sigma}_{n-1}} 
                & X_n\arrow{dr}[rotate=-30,xshift=-1em]{\tilde{\sigma}_{n}} & X_{n+1}\arrow{dr} 
                & \cdots \\
                \cdots\arrow{u} & \Omega X_{n-1}\arrow{u} & \Omega X_n\arrow{u} 
                & \Omega X_{n+1}\arrow{u} & \cdots\arrow{u}
            \end{tikzcd}
        """, fn)

        self.play(
            FadeOut(def11pic1)
        )
        self.play(
            FadeIn(def11pic2)
        )
        self.wait(2)

        hom1 = tikz("hom1", r"""
            \begin{tikzcd}[column sep=large]
                S^1\wedge X_n \arrow{r}[above]{S^1\wedge f_n} 
                    \arrow{d}[right]{\sigma_n^X}&
                    S^1 \wedge Y_n \arrow{d}[right]{\sigma_n^Y} \\
                X_{n+1} \arrow{r}[above]{f_{n+1}} & Y_{n+1}
            \end{tikzcd}
        """, fn).scale(1.25)

        self.play(
            FadeOut(def11pic2)
        )
        self.play(
            FadeIn(hom1)
        )
        self.wait(2)

        hom2 = tikz("hom2", r"""
            \begin{tikzcd}[column sep=huge]
                X_n \arrow{r}[above]{f_n} 
                    \arrow{d}[right]{\tilde{\sigma}_n^X}&
                    Y_n \arrow{d}[right]{\tilde{\sigma}_n^Y} \\
                \cat{Maps}(S^1,X_{n+1})_\ast \arrow{r}[above]{\cat{Maps}(S^1,f_{n+1})_\ast} & 
                    \cat{Maps}(S^1,Y_{n+1})
            \end{tikzcd}
        """, fn).scale(1.25)

        self.play(
            FadeOut(hom1)
        )
        self.play(
            FadeIn(hom2)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class ex13(Scene):
    """
    There is a natural way to create an entire spectrum out of a single
    topological space, you know, compactly generated and pointed.
    It's 0th component is the space X, and we just keep suspending it
    to get the rest of the spaces.
    This is the special case I mentioned before of the structure maps being
    homeomorphisms- this is again just saying that the nth component space
    is literally the nfold suspension.
    Formally, this idea that the entire spectrum is generated by a single space
    means that we have a functor, a quote on quote infinite suspension functor,
    from the category of compactly generated pointed topological spaces to
    The category of sequential spectra on compactly generated topological spaces.
    """
    def construct(self):
        title = make_title("Example", 1.3)

        self.play(
            Write(title)
        )
        self.wait(2)

        theex = TextMobject("For $X\\in\\text{Top}_{\\text{cg}}^{\\ast /}$, its ",\
                "suspension spectrum", " $\Sigma^\infty X$ has")\
                .scale(.75).next_to(title, direction=DOWN, buff=1).to_edge(LEFT, buff=.5)
        theex[1].set_color(BLUE)

        theexparts = TextMobject(r"""
            \begin{itemize}
                \item \textit{component spaces} $$(\Sigma^\infty X)_n:=S^n\wedge X$$
                \item \textit{structure maps} $$S^1\wedge S^n\wedge X
                    \overset{\simeq}{\longrightarrow} S^{n+1}X$$
            \end{itemize}
        """, alignment="").scale(.75).shift(2*LEFT)

        self.play(
            FadeIn(theex)
        )
        self.play(
            FadeIn(theexparts)
        )
        self.wait(2)

        exfunctor = TexMobject(r"""
            \Sigma^\infty:\text{Top}_{\text{cg}}^{\ast /}\to
            \text{SeqSpec}(\text{Top}_{\text{cg}}).
        """).scale(.75).shift(2.5*DOWN).set_color(YELLOW)

        self.play(
            ShowCreation(exfunctor)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class ex14(Scene):
    """
    Of course, we could start with a single point, and we'd simply
    obtain all spheres, the standard sequential sphere spectrum,
    who'se nth component space is the standard n sphere.
    """
    def construct(self):
        title = make_title("Example", 1.4)

        self.play(
            Write(title)
        )
        self.wait(2)

        theex1 = TextMobject("The ", "standard sequential sphere spectrum", \
            " is the suspension spectrum of the point:", alignment="").scale(.75)
        theex1[1].set_color(BLUE)
        theex2 = TexMobject(r"""
            \mathbb{S}_{\text{seq}} := \Sigma^\infty S^0, \\
            (\mathbb{S}_{\text{seq}})_n = S^n.
        """).shift(1*UP).to_edge(LEFT, buff=.5).scale(.75)
        theex = VGroup(
            theex1,
            theex2
        ).arrange_submobjects(
            DOWN,
            buff = .5
        )

        self.play(
            FadeIn(theex)
        )
        self.wait(3)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class ex15(Scene):
    """
    Like I said earlier, not every sequential spectrum is a suspension
    spectrum, i.e. not every spectrum's structure maps are homeomorphisms.
    It's not hard to believe that such spectra exist, but you might be
    wondering if such spectra are useful. 
    A fundamental such example of spectra that is not simply a 
    suspension spectra are the real and complex Thom spectra,
    which is a topic I hope to gt to eventually.
    """
    def construct(self):
        title = make_title("Example", 1.5)

        self.play(
            Write(title)
        )
        self.wait(2)

        theex = TextMobject(r"""
            Not every spectrum is a suspension spectrum. For example, the 
            \textit{Thom} spectra (MO and MU).
        """, alignment="").scale(.75)

        self.play(
            Write(theex)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class def16(Scene):
    """
    We'd like to start upgrading the homotopy theory from the
    category Top to this new category of sequential spectra.
    Let's start by upgrading our notions of smash products
    and mapping spaces.
    They are pretty much defined they way you would expect.
    The analague of the smash product here is called the
    smash tensoring, and on the component spaces it is a 
    component wise smash product. On the structure maps,
    it is the smash product of the original structure
    map with the identity function on K, which makes
    sense in light of how we defined the new component spaces.
    The analogue of the mapping space is called the powering
    of K into X. Its component spaces are the mapping spaces
    with underlying sets maps from K into Xn. Its structure
    maps are defined as you see here. To explain a bit,
    the first map sends points in s1 to the constant map from
    K to that point. Maps from K to Xn are sent to itself,
    the map from K to Xn. This map is the constant identity map,
    which will make an appearance a little bit later.
    Again, these operations give us functors, which you see here.
    """
    def construct(self):
        title = make_title("Definition", 1.6)

        self.play(
            Write(title)
        )
        self.wait(2)

        p1 = TextMobject("1. The ", "smash tensoring", " of $X$ with $K$, denoted $X\\wedge K$, \
            is the sequential spectrum given by", alignment="").scale(.75)
        p1[1].set_color(BLUE)
        p1parts = TextMobject(r"""
            \begin{itemize}
                \item $(X\wedge K)_n := X_n \wedge K$
                \item $\sigma_n^{X\wedge K} := \sigma_n^X \wedge \text{id}_K$.
            \end{itemize}
        """).scale(.75)

        p1gp = VGroup(
            p1,
            p1parts
        ).arrange_submobjects(
            DOWN,
            buff=.5
        ).shift(1*UP)

        p2 = TextMobject("2. The ", "powering", " of $K$ into $X$, denoted \
            $\\text{Maps}(K,X)_\\ast$, is the sequential spectrum with", alignment="").scale(.75)
        p2[1].set_color(BLUE)
        p2parts = TextMobject(r"""
            \begin{itemize}
                \item $(\text{Maps}(K,X)_\ast)_n := \text{Maps}(K,X_n)_\ast$
                \item \tiny{$\sigma_n^{\text{Maps}(K,X)_\ast}:S^1\wedge\text{Maps}(K,X_n)
                    \overset{\text{(const,id)}}{\longrightarrow}\text{Maps}(K,S^1\wedge X_n)_\ast
                    \overset{\text{Maps}(K,\sigma_n)_\ast}{\longrightarrow}\text{Maps}(K,X_{n+1})_\ast$.}
            \end{itemize}
        """).scale(.75)
        p2gp = VGroup(
            p2,
            p2parts
        ).arrange_submobjects(
            DOWN,
            buff=.5
        ).shift(2.25*DOWN)

        self.play(
            FadeIn(p1)
        )
        self.play(
            FadeIn(p1parts)
        )
        self.wait(2)
        self.play(
            FadeIn(p2)
        )
        self.play(
            FadeIn(p2parts)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects[1:]]
        )

        functors = TexMobject(r"""
            (-)\wedge (-):\text{SeqSpec}(\text{Top}_{\text{cg}})
                \times\text{Top}_{\text{cg}}^{\ast /}\to
                \text{SeqSpec}(\text{Top}_{\text{cg}}) \\
            \text{Maps}(-,-)_\ast:(\text{Top}_{\text{cg}}^{\ast /})^{\text{op}}
                \times \text{SeqSpec}(\text{Top}_{\text{cg}}) \to
                \text{SeqSpec}(\text{Top}_{\text{cg}})
        """).scale(.75)

        self.play(
            FadeIn(functors)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class ex17(Scene):
    """
    We've constructed these operations in such a way that certain things
    work out the way we'd expect them to. The smash tensoring of the
    standard sphere spectrum with the toplogical space X is isomorphic
    to the suspension spectrum of X.
    """
    def construct(self):
        title = make_title("Example", 1.7)

        self.play(
            Write(title)
        )
        self.wait(2)

        theex = TexMobject(r"""
            \mathbb{S}_{\text{std}}\wedge X\simeq\Sigma^\infty X
        """).scale(.75)

        self.play(
            FadeIn(theex)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class transtoprop18(Scene):
    """
    Let's return to this diagram from the introduction. This is where we 
    want to be. Before we prove this diagram for model structures on these
    categories, we want to prove it without. The top adjunction is the
    classical smash hom adjunction. We turn right now to the bottom
    adjunction, and afterwards to the vertical ones.
    """
    def construct(self):
        pic = ImageMobject("preliminaries/hospectrapic2.png").scale(1.5)

        self.play(
            FadeIn(pic)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class prop18(Scene):
    """
    So let's get that bottom adjunction, for now not considering if it is
    a Quillen adjunction and just considering the categories without
    a model structure.
    Here's the proof. To show that this is indeed an adjunction, we need to
    show that there is a bijection between the sets of maps f and f
    tilde displayed here. So let's start with a function f.
    This is a homomorphism between spectra, so we have the following 
    commuting square. But by the classical smash hom adjunction in
    Top, this is equivalently, i.e. in bijection with, commuting squares
    of this form. So the bottom map tilde f n+1 is what we want, but
    we also want the top map to have a tilde fn. As it stands,
    this is not what we have, but we can show that this is in bijection with
    maps of the form we want. This comes from the observation that the 
    original top map S^1 wedge fn is the identity in a sense on its S^1
    factor. The S^1 always remained as a wedge factor. So it makes sense
    to try and split of the fn and somehow apply the standard
    smash hom adjunction in such a way that only the fn is changed
    into tilde fn. We can see the idea here, and using the constant identity
    map from earlier, this indeed factors tilde S^1 wedge fn. Thus we have
    a bijection between those maps and maps tilde fn, so we have a bijection
    between commuting squares. This displays the bijection and hence the 
    adjunction we were after.
    """
    def construct(self):
        title = make_title("Proposition", 1.8)

        self.play(
            Write(title)
        )
        self.wait(2)

        theprop = TextMobject(r"""
            For $K\in\text{Top}_{\text{cg}}^{\ast /}$, there is an adjunction
        """).scale(.75).next_to(title, direction=DOWN, buff=1).to_edge(LEFT, buff=.5)
        proppic = tikz("std_seqspec_adj", r"""
            \begin{tikzcd}[column sep=huge]
                \cat{SeqSpec}(\cat{Top}_{\text{cg}}) \arrow[yshift=-.5em]{r}[below]
                    {\cat{Maps}(K,-)_\ast}[above]{\perp} &
                \cat{SeqSpec}(\cat{Top}_{\text{cg}})\arrow[yshift=.5em]{l}[above]
                    {(-)\wedge K}
            \end{tikzcd}
        """, fn).scale(.5)

        self.play(
            FadeIn(theprop)
        )
        self.play(
            FadeIn(proppic)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects[1:]]
        )

        pftitle = TextMobject("Pf:").scale(.75).next_to(title, direction=DOWN, buff=1)\
            .to_edge(LEFT, buff=.5)

        self.play(
            Write(pftitle)
        )
        self.wait(2)

        pf1 = TexMobject(r"""
            \Big\{X\wedge K\overset{f}{\to}Y\Big\}\leftrightarrow
            \Big\{X\overset{\tilde{f}}{\to}\text{Maps}(K,Y)_\ast\Big\}
        """).scale(.75)

        self.play(
            FadeIn(pf1)
        )
        self.wait(2)
        self.play(
            FadeOut(pf1)
        )

        pf2 = tikz("prop18_pfpic1", r"""
            \begin{tikzcd}[column sep=huge, row sep=huge]
                S^1\wedge X_n\wedge K \arrow{r}[above]{S^1\wedge f_n}
                    \arrow{d}[right]{\sigma_n^X\wedge K} & S^1\wedge Y_n
                    \arrow{d}[right]{\sigma_n^Y} \\
                X_{n+1}\wedge K \arrow{r}[above]{f_{n+1}} & Y_{n+1}
            \end{tikzcd}
        """, fn).scale(1.5)

        self.play(
            FadeIn(pf2)
        )

        pf3 = tikz("classical_adjunction", r"""
            \begin{tikzcd}[column sep=huge]
                \cat{Top}_{\text{cg}}^{\ast /} \arrow[yshift=-.5em]{r}[below]
                    {\cat{Maps}(K,-)_\ast}[above]{\perp} &
                \cat{Top}_{\text{cg}}^{\ast /} \arrow[yshift=.5em]{l}[above]
                    {(-)\wedge K}
            \end{tikzcd}
        """, fn).scale(.5).to_edge(DOWN,buff=1)

        self.play(
            FadeIn(pf3)
        )
        self.wait(2)
        self.play(
            FadeOut(pf3)
        )
        self.wait()

        pf4 = tikz("prop18_pfpic2", r"""
            \begin{tikzcd}[column sep=huge, row sep=huge]
                S^1\wedge X_n \arrow{r}[above]{\widetilde{S^1\wedge f_n}}
                    \arrow{d}[right]{\sigma_n^X\wedge K} & 
                    \cat{Maps}(K,S^1\wedge Y_n)_\ast
                    \arrow{d}[right]{\sigma_n^Y} \\
                X_{n+1}\wedge K \arrow{r}[above]{\widetilde{f_{n+1}}} & 
                    \cat{Maps}(K,Y_{n+1})_\ast
            \end{tikzcd}
        """, fn).scale(1.5)

        self.play(
            FadeOut(pf2)
        )
        self.play(
            FadeIn(pf4)
        )
        self.wait(2)
        self.play(
            FadeOut(pf4)
        )

        pf5p1a = tikz("prop18_pfpic3", r"""
            \begin{tikzcd}
                S^1\wedge X_n\wedge K \arrow{r}[above]{S^1\wedge(-)}
                    \arrow{dr}[left, yshift=-.5em]{S^1\wedge f_n} & S^1\wedge X_n\wedge K 
                    \arrow{d}[right]{(-)\wedge f_n}\\
                & S^1\wedge Y_n
            \end{tikzcd}
        """, fn).to_edge(LEFT,buff=1).shift(.5*UP)

        pf5p1b = tikz("prop18_pfpic4", r"""
            \begin{tikzcd}
                S^1\wedge X_n \arrow{r}[above]{S^1\wedge(-)}
                    \arrow{dr}[left, yshift=-.5em]{\widetilde{S^1\wedge f_n}} & S^1\wedge X_n 
                    \arrow{d}[right]{(-)\wedge \tilde{f}_n}\\
                & \cat{Maps}(K,S^1\wedge Y_n)_\ast
            \end{tikzcd}
        """, fn).next_to(pf5p1a,direction=DOWN,buff=1)

        pf5p2a = tikz("prop18_pfpic5", r"""
            \begin{tikzcd}
                X_n\wedge K\arrow{r}[above]{\text{id}}\arrow{dr}[left,yshift=-.5em]
                    {f_n} & X_n\wedge K\arrow{d}[right]{f_n} \\
                & Y_n
            \end{tikzcd}
        """, fn).next_to(pf5p1a,buff=1.5)

        pf5p2b = tikz("prop18_pfpic6", r"""
            \begin{tikzcd}
                X_n\arrow{r}[above]{\text{id}}\arrow{dr}[left,yshift=-.5em]
                    {\tilde{f}_n} & X_n\arrow{d}[right]{\tilde{f}_n} \\
                & \cat{Maps}(K,Y_n)
            \end{tikzcd}
        """, fn).next_to(pf5p2a,direction=DOWN,buff=1)

        self.play(
            FadeIn(pf5p1a)
        )
        self.play(
            FadeIn(pf5p1b)
        )
        self.play(
            FadeIn(pf5p2a)
        )
        self.play(
            FadeIn(pf5p2b)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in [pf5p1a,pf5p1b,pf5p2a,pf5p2b]]
        )

        bij = TexMobject(r"""
            \Big\{S^1\wedge X_n\overset{\widetilde{S^1\wedge f_n}}{\longrightarrow}
                \text{Maps}(K,S^1\wedge Y_n)\Big\} \leftrightarrow
            \Big\{ S^1\wedge X_n\overset{S^1\wedge\tilde{f_n}}{\longrightarrow}
                S^1\wedge\text{Maps}(K,Y_n)\Big\}
        """).scale(.75)

        self.play(
            FadeIn(bij)
        )
        self.wait(2)
        self.play(
            FadeOut(bij)
        )

        self.play(
            FadeIn(pf4)
        )
        self.wait()

        pf6 = tikz("prop18_pfpic7", r"""
            \begin{tikzcd}
                S^1\wedge X_n\arrow{r}[above]{S^1\wedge\tilde{f}_n}
                    \arrow{d}[right]{\sigma_n^X} & S^1\wedge\text{Maps}(K,Y_n)\ast
                    \arrow{d}[right]{\sigma_n^{\text{Maps}(K,Y)_\ast}} \\
                X_{n+1}\arrow{r}[above]{\widetilde{f_{n+1}}} &
                    \text{Maps}(K,Y_{n+1})_\ast
            \end{tikzcd}
        """, fn)

        self.play(
            FadeOut(pf4),
            FadeIn(pf6)
        )
        self.wait(2)
        self.play(
            FadeOut(pf6)
        )
        self.play(
            FadeIn(pf1)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class prop110(Scene):
    """
    Now that we have the bottom adjunction, we turn to the vertical ones.
    To be clear on the notation, applying the infinite loop space 
    to a spectrum X is just picking out the first, or 0th indexed,
    component space.
    Our idea is of course the same, to show a bijection between these
    maps f and tilde f. So f is a map from a suspension spectrum to
    some spectrum Y. Again, we can see this as a set of commuting
    squares. But since we are working with a suspension spectrum, 
    the left vertical map is an isomorphism. What this means is that
    the two horizontal maps are related. Specifically, f n+1 is
    entirely determined by the map fn. So considering all such
    fn, we see that all of them are determined by that initial map
    f0 from X to Y0. But remember, Y0 is just the infinite loop space
    functor applied to Y. Every map f0, and by extension f, corresponds
    to a map f tilde from X to the infinite loop space functor applied
    to Y. This exhibits the bijection we are after, and hence
    the adjunction.
    """
    def construct(self):
        title = make_title("Proposition", "1.10")

        self.play(
            Write(title)
        )
        self.wait(2)

        thegoal = ImageMobject("preliminaries/hospectrapic2.png").scale(1.5)

        self.play(
            FadeIn(thegoal)
        )
        self.wait(2)
        self.play(
            FadeOut(thegoal)
        )
        self.wait()

        theprop = tikz("inf_adjunction", r"""
            \begin{tikzcd}
                (\Sigma^\infty\dashv\Omega^\infty):\cat{SeqSpec}(\cat{Top}_\text{cg})
                \arrow[yshift=-.5em]{r}[below]{\Omega^\infty}[above]{\perp} &
                \cat{Top}_{\text{cg}}^{\ast /}\arrow[yshift=.5em]{l}[above]{\Sigma^\infty}
            \end{tikzcd}
        """, fn).scale(.5)

        self.play(
            FadeIn(theprop)
        )
        self.wait(2)
        self.play(
            FadeOut(theprop)
        )

        pftitle = TextMobject("Pf:").scale(.75).next_to(title,direction=DOWN,buff=1)\
            .to_edge(LEFT,buff=.5)

        self.play(
            Write(pftitle)
        )
        self.wait()

        bij = TexMobject(r"""
            \Big\{\Sigma^\infty X\overset{f}{\to}Y\Big\} \leftrightarrow
            \Big\{X\overset{\tilde{f}}{\to}\Omega^\infty Y\Big\}
        """).scale(.75)

        self.play(
            FadeIn(bij)
        )
        self.wait(2)
        self.play(
            FadeOut(bij)
        )

        pf1 = tikz("prop110_pfpic1", r"""
            \begin{tikzcd}
                S^1\wedge S^nX\arrow{d}[left]{\simeq}\arrow{r}[above]
                    {S^1\wedge f_n} & S^1\wedge Y_n\arrow{d}[right]{\sigma_n^Y} \\
                S^{n+1}\wedge X\arrow{r}[above]{f_{n+1}} & Y_{n+1}
            \end{tikzcd}
        """, fn)

        self.play(
            FadeIn(pf1)
        )
        self.wait(2)

        f0 = TexMobject("f_0:X\\to Y_0").scale(.75).to_edge(DOWN,buff=1.5)
        ftilde = TexMobject("\\tilde{f}:X\\to\\Omega^\\infty Y").scale(.75)\
            .move_to(f0)

        self.play(
            FadeIn(f0)
        )
        self.wait(2)
        self.play(
            Transform(f0,ftilde)
        )
        self.wait(3)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )




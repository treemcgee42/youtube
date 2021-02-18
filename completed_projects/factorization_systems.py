# Date: 2/10/21
# Purpose: projective/injective topics from factorization systems section nLab
# Notes:  uploaded 2/18


from manimlib.imports import *
fn = "factorization_systems"


class def24(Scene):
    """
    Starting off with some preliminary definitions, if a diagram of this form
    admits a lift, then we call that lift an extension.
    On the other hand, if this diagram admits a lift, then we call that a lift.
    So yes, the terminology is inconsistent and can be ambiguous, but it will 
    typically be clear from the situation what we mean.
    If a whole square admits a lift, then we call that a lifting. Again, we
    may just coloquially refer to this as a lift if the context is clear.
    So we've met Injective morphisms before, these are the ones that have the
    right lifting property against all maps in a certain class of morphisms.
    But dually we may talk about projective morphisms, which has the left lifting
    property, meaning it admits a lift for any pr on the right from some certain
    class of morphisms. These are central concepts in weak factorization systems,
    and so I've split up the factorization systems section in the nLab, and will
    focus in particular on these classes of morphisms in this video.
    """
    def construct(self):
        title = make_title("Definition", 2.4)

        self.play(
            Write(title)
        )
        self.wait(2)

        d1 = tikz("def24_d1", r"""
            \begin{tikzcd}
                X \arrow{r}[above]{f} \arrow{d}[left]{p} & Y \\
                B &
            \end{tikzcd}
        """, fn)

        self.cycle(
            [d1],
            out=True
        )

        d2 = tikz("def24_d2", r"""
            \begin{tikzcd}
                X \arrow{r}[above]{f} \arrow{d}[left]{p} & Y \\
                B \arrow{ur}[right,yshift=-.5em]{\tilde{f}}&
            \end{tikzcd}
        """, fn)

        d2_label = TextMobject("``extension''").scale(.75).next_to(d2, direction=DOWN, buff=.5)
        d2_label.set_color(BLUE)

        self.cycle(
            [d2, d2_label],
            out=True
        )

        d3 = tikz("def24_d3", r"""
            \begin{tikzcd}
                & A \arrow{d}[right]{p} \\
                X \arrow{r}[above]{f} & Y
            \end{tikzcd}
        """, fn)

        self.cycle(
            [d3],
            out=True
        )

        d4 = tikz("def24_d4", r"""
            \begin{tikzcd}
                & A \arrow{d}[right]{p} \\
                X \arrow{r}[above]{f} \arrow{ur}[left,yshift=.5em]{\tilde{f}} & Y
            \end{tikzcd}
        """, fn)

        d4_label = TextMobject("``lift''").scale(.75).next_to(d4, direction=DOWN, buff=.5)
        d4_label.set_color(BLUE)

        self.cycle(
            [d4, d4_label],
            out=True
        )

        d5 = tikz("def24_d5", r"""
            \begin{tikzcd}
                X_1 \arrow{d}[left]{p_l} \arrow{r}[above]{f_1} & Y_1
                    \arrow{d}[right]{p_r} \\
                X_2 \arrow{ur} \arrow{r}[above]{f_1} & Y_2
            \end{tikzcd}
        """, fn)

        d5_label = TextMobject("``lifting''").scale(.75).next_to(d5, direction=DOWN, buff=.5)
        d5_label.set_color(BLUE)

        self.cycle(
            [d5, d5_label],
            out=False
        )

        rlp = TextMobject("right lifting property, $\in$Inj").scale(.65).next_to(d5, buff=.5)
        llp = TextMobject("left lifting property, $\in$Proj").scale(.65).next_to(d5, direction=LEFT,\
            buff=.5)

        self.cycle(
            [rlp, llp],
            out=False
        )
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class def25(Scene):
    """
    So we are ready to define weak factorization systems. So its a pair
    of classes of morphisms with certain properties. The way we've written them
    would lead you to believe that these are projective and injective
    morphisms, but more on that in the actual definition.
    So we first require every morphism in C is able to be factored
    as a morphism in the first class followed by a morphism in the second.
    Secondly, the first class must exactly be the class of morphisms with
    the left lifting proeprty against the second class, and vice versa
    the second class must precisely be the one with the right lifting
    property against the first.
    So of course we should be grounding this discussion in what we know
    about topological homotopy theory. So even though we dont know about
    the first property, we do know from the definition of model categories
    that the pair cofibrations comma acyclic fibrations is a weak factorization
    system, which makes sense because we proved that the class of acyclic 
    Serre fibrations is the precisely the one with the right lifting property
    against generating topological cofibrations. Similarly that acyclic
    cofibrations comma Serre fibrations is a weak factorization system
    coincides with our intuition that Serre fibrations are pricisely those
    with the right lifting porperty against acyclic topological generating
    cofibrations.
    """
    def construct(self):
        title = make_title("Definition", 2.5)

        self.play(
            Write(title)
        )
        self.wait(2)

        d1 = TextMobject("A ", "weak factorization system", r"""
             on a category $\mathcal{C}$ is a pair (Proj, Inj) such that
            \begin{enumerate}
                \item Every morphism in $\mathcal{C}$ may be factored:
                    $$f:X\overset{\in\text{Proj}}{\longrightarrow} Z
                        \overset{\in\text{Inj}}{\longrightarrow} Y$$
                \item The classes are closed under having the lifting property 
                    against each other:
                    \begin{itemize}
                        \item Proj is precisely the class with llp against Inj
                        \item Inj is precisely the class with rlp against Proj
                    \end{itemize}
            \end{enumerate}
        """, alignment="").scale(.75)

        self.cycle(
            [d1],
            out=False
        )
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class def26(Scene):
    """
    So here's another way to think about this. First, we define a functorial factorization
    as a functor in the following way. Now this notation can be confusing, so please
    allow me to explain a little. That triangle or simplex notation stands for ordinals,
    so delta 1 is 0 and 1 and delta 2 is 0 and 1 and 2. More specifically, it is all
    morphisms between these elements. So C delta one are morphisms or arrows in C,
    while C delta 2 has objects that are the composition of two morphisms in C. So
    what being a section means is that we can find an intermediary between a morphism
    like so.
    Now, we can relate this back to weak factorization systems by considering the maps
    d0 which takes the composable pair of morphisms to the second morphism and d2 which
    sends the composable pair to the first morphism. If the image of d0 is in the injective
    class of morphisms and the image of d2 is in the projective class, as we've defined them
    in the context of this video, then we would recover the weak factorization system notion,
    and thus cal lthis a functorial weak factorization system.
    Now, the interesting thing is that not every weak factorization system is a functorial
    weak factorization system. But it turns out that most are, in particular those 
    produced by the small object argument which we describe below.
    """
    def construct(self):
        t = make_title("Definition", 2.6)
        self.title(t)

        d1 = TextMobject("For $\\mathcal{C}$ a category, a ", "functorial factorization",\
            " of the morphisms in $\\mathcal{C}$ is a functor $$\\text{fact}:\
            \\mathcal{C}^{\\Delta [1]} \\to \\mathcal{C}^{\\Delta [2]}$$\
            which is a section of the composition functor $d_1:\\mathcal{C}\
            ^{\\Delta [2]}\\to\\mathcal{C}^{\\Delta [1]}$.", alignment="")\
            .scale(.75).next_to(t, direction=DOWN, buff=1).to_edge(LEFT, buff=.5)
        d1[1].set_color(BLUE)

        self.cycle(
            [d1],
            out=False
        )

        d2_1 = TexMobject(r"""
            (a\to c)
        """).scale(.75)

        d2_2 = TexMobject(r"""
            \overset{\text{Fact}}{\longrightarrow}
        """).scale(.75).set_color(RED)
        
        d2_3 = TexMobject(r"""
            (a\to b\to c)
        """).scale(.75)

        d2_4_d1 = TexMobject(r"""
            \overset{d_1}{\longrightarrow}
        """).scale(.75).set_color(RED)

        d2_5_d1 = TexMobject(r"""
            (a\to c)
        """).scale(.75)

        d2_d1 = VGroup(
            d2_1,
            d2_2,
            d2_3,
            d2_4_d1,
            d2_5_d1
        ).arrange_submobjects(
            RIGHT
        ).shift(2*DOWN)

        self.cycle(
            [d2_d1],
            out=False
        )

        d2_4_d0 = TexMobject(r"""
            \overset{d_0}{\longrightarrow}
        """).scale(.75).set_color(RED)

        d2_5_d0 = TexMobject(r"""
            (b\to c)
        """).scale(.75)

        d2_d0 = VGroup(
            d2_1,
            d2_2,
            d2_3,
            d2_4_d0,
            d2_5_d0
        ).arrange_submobjects(
            RIGHT
        ).shift(2*DOWN)

        self.play(
            ReplacementTransform(d2_d1, d2_d0)
        )
        self.wait(2)

        d2_4_d2 = TexMobject(r"""
            \overset{d_2}{\longrightarrow}
        """).scale(.75).set_color(RED)

        d2_5_d2 = TexMobject(r"""
            (a\to b)
        """).scale(.75)

        d2_d2 = VGroup(
            d2_1,
            d2_2,
            d2_3,
            d2_4_d2,
            d2_5_d2
        ).arrange_submobjects(
            RIGHT
        ).shift(2*DOWN)

        self.play(
            ReplacementTransform(d2_d0, d2_d2)
        )
        self.wait(2)

        d3 = TextMobject("functorial weak factorization system")\
            .scale(.75).next_to(d2_d2, direction=UP, buff=0).set_color(BLUE)

        self.play(
            Transform(d2_d2, d2_d2.copy().shift(1.5*UP)),
            FadeIn(d3)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class prop210_1(Scene):
    """
    We now have a series of propositions about the classes of projective and injective
    morphisms. So for notation, we are in a category C, we have K as a class of its morphisms,
    and we say K Proj and K Inj for the subclasses of K projective morphisms and
    K injective morphisms respectively.
    Our first proposition states that both these classes contain the class of isomorphisms
    of C.
    The proof of this is pretty simple. Suppose we have an isomorphism on the left here,
    and we want to show that there is a lift, but this is clear because we have an inverse
    map since it is an isomorphism, so the lift could just be defined as the inverse
    of the isomorphism displayed and then the top horizontal map. The proof of the
    KInj case is just dual, so we don't cover it explicitly.
    """
    def construct(self):
        t = make_title("Proposition", "2.10")

        self.title(t)

        p1 = TextMobject(r"""
            \begin{itemize}
                \item a category $\mathcal{C}$
                \item a class of morphisms $K\subset\text{Mor}(\mathcal{C})$
                \item classes of projective, injective morphisms $K$Proj, $K$Inj
            \end{itemize}
        """).scale(.75)

        self.cycle(
            [p1]
        )

        p2 = TextMobject(r"""
            Both classes contain the class of isomorphisms of $\mathcal{C}$.
        """).scale(.75).to_title(t)

        self.cycle(
            [p2],
            out=False
        )

        p3 = tikz("prop210_1_pf_1", r"""
        \begin{tikzcd}
            A \arrow{r}[above]{f} \arrow{d}[left]{i\in\text{Iso}} & X
                \arrow{d}[right]{p} \\
            B \arrow{r}[below]{g} & Y
        \end{tikzcd}
        """, fn)

        self.cycle(
            [p3],
            out=False
        )
        self.play(
            *[FadeOut(mob) for mob in self.mobjects[1:]]
        )

class prop210_2(Scene):
    """
    The next proposition states that both classes are closed under
    composition. Now, this of course refers to finite composition, but
    it turns that Kproj is also closed under transfinite composition.
    Now lets do KInj first, so lets have two maps of KInj composing
    on the right and a map whose composition is in K on the left.
    So if we draw the top sware with this arrow, which is just the
    composition of the top horizontal and the top
    vertical on the right, then we can see a sort of distorted 
    square on the bottom who has a single Kinj morphism on the right.
    Hence we can lift. Well now if we erase that extra arrow, we
    similarly have a distorted square on the top with a single
    Kinj morphism on the right, so we can lift again, which constitutes a
    lift of the entire square.
    Now, the case for Kproj is dual, and the transfinite composition closure just
    comes from the observation that each lift in the sequence, so like the
    composition of the first 2, first 3, etc, constitutes a cocone, and by the
    universal property there is a universal cocone which constitutes a lift
    over the transfinite composition.
    """
    def construct(self):
        t = make_title("Proposition", "2.10")

        self.add(t)

        p1 = TextMobject(r"""
            Both classes are closed under composition in $\mathcal{C}$. 
            $K$Proj is also closed under transfinite composition.
        """, alignment="").scale(.75).to_title(t)

        self.cycle(
            [p1],
            out=False
        )

        p2 = tikz("prop210_2_pf_1", r"""
        \begin{tikzcd}
            A \arrow{d} \arrow{r} & X \arrow{d}[right]{p_1\in K\text{Inj}} \\
            - \arrow{d}[left]{i\in K} & - \arrow{d}[right]{p_2\in K\text{Inj}} \\
            B \arrow{r} & Y
        \end{tikzcd}
        """, fn).shift(1*DOWN).scale(1.5)

        self.cycle(
            [p2]
        )

        p3 = tikz("prop210_2_p3", r"""
        \begin{tikzcd}
            A \arrow{d} \arrow{dr} \arrow{r} & X \arrow{d}[right]{p_1\in K\text{Inj}} \\
            - \arrow{d}[left]{i\in K} & - \arrow{d}[right]{p_2\in K\text{Inj}} \\
            B \arrow[dashed]{ur} \arrow{r} & Y
        \end{tikzcd}
        """, fn).shift(1*DOWN).scale(1.5)

        self.cycle(
            [p3]
        )

        p4 = tikz("prop210_2_p4", r"""
        \begin{tikzcd}
            A \arrow{d} \arrow{r} & X \arrow{d}[right]{p_1\in K\text{Inj}} \\
            - \arrow{d}[left]{i\in K} & - \arrow{d}[right]{p_2\in K\text{Inj}} \\
            B \arrow{ur} \arrow[dashed]{uur} \arrow{r} & Y
        \end{tikzcd}
        """, fn).shift(1*DOWN).scale(1.5)

        self.cycle(
            [p4]
        )

        p5 = tikz("prop210_2_p5", r"""
        \begin{tikzcd}
            A \arrow{r} \arrow{d}[left]{p_1\in K\text{Proj}} & X \arrow{d} \\
            - \arrow{d}[left]{p_2\in K\text{Proj}} & - \arrow{d}[right]{i\in K} \\
            B \arrow[dashed]{uur} \arrow{r} & Y
        \end{tikzcd}
        """, fn).shift(1*DOWN).scale(1.5)

        self.cycle(
            [p5],
            out=False
        )

        self.play(
            *[FadeOut(mob) for mob in self.mobjects[1:]]
        )

class prop210_3(Scene):
    """
    We now want to show that both classes are closed under retracts. We'll 
    prove the statement for KProj, and the other case is just dual.
    So forming retracts means making this diagram, and we want to show
    that the induced map j is also in K proj. That is, we want to show that
    it has the left lifting property against maps in K. So lets get a map
    in K. We can attach it to the of the diagram since retracts are the
    identity on A. Now we want to show that we can lift to a map from 
    B to X, either one, since they are the same. Well, we can lift from
    D to X by the assumption that i is in KProj, and then just
    precompose with the map from B to D to get a lift from B to X.
    """
    def construct(self):
        t = make_title("Proposition", "2.10")

        self.add(t)

        p1 = TextMobject(r"""
            $K$Proj and $K$Inj are closed under forming retracts.
        """).scale(.75).to_title(t)

        p2 = tikz("prop210_3_p2", r"""
            \begin{tikzcd}
                \text{id}_A: 
                    & A 
                    \arrow{r}\arrow{d}[right]{j}
                    & C
                    \arrow{r}\arrow{d}[right]{i\in K\text{Proj}}
                    & A
                    \arrow{d}[right]{j} \\
                \text{id}_B:
                    & B 
                    \arrow{r}
                    & D
                    \arrow{r}
                    & B
            \end{tikzcd}
        """, fn).shift(.5*DOWN, 1*LEFT)

        self.cycle(
            [p1, p2],
            out=False
        )

        p3 = tikz("prop210_3_p3", r"""
            \begin{tikzcd}
                \text{id}_A: 
                    & A 
                    \arrow{r}\arrow{d}[right]{j}
                    & C
                    \arrow{r}\arrow{d}[right]{i\in K\text{Proj}}
                    & A
                    \arrow{d}[right]{j} \arrow{r}
                    & X
                    \arrow{d}[right]{f\in K} \\
                \text{id}_B:
                    & B 
                    \arrow{r}
                    & D
                    \arrow{r}
                    & B
                    \arrow{r}
                    & Y
            \end{tikzcd}
        """, fn).shift(.5*DOWN, 1*LEFT)

        self.play(
            FadeOut(p2), 
            FadeIn(p3)
        )
        self.wait(2)

        p4 = tikz("prop210_3_p4", r"""
            \begin{tikzcd}
                \text{id}_A: 
                    & A 
                    \arrow{r}\arrow{d}[right]{j}
                    & C
                    \arrow{r}\arrow{d}[right]{i\in K\text{Proj}}
                    & A
                    \arrow{r}
                    & X
                    \arrow{d}[right]{f\in K} \\
                \text{id}_B:
                    & B 
                    \arrow{r}
                    & D
                    \arrow{r}\arrow[dashed]{urr}
                    & B
                    \arrow{r}
                    & Y
            \end{tikzcd}
        """, fn).shift(.5*DOWN, 1*LEFT)

        self.play(
            FadeOut(p3),
            FadeIn(p4)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects[1:]]
        )

class prop210_4(Scene):
    """
    Now we want to show that these classes are closed under pushout
    and pullback. There's a lot of duality here, and the methods are analagous,
    so we will only show this for KInj and pullbacks. Again, the other three
    cases are dual. 
    So let p be in K Inj, and we want to show that the map on the left
    from the pullback is in K inj as well. Well like before, we need to show
    it lifts against maps in K, so add that to our diagram. Now we need
    a map from B to the pullback.
    Well by assumption that p is in KInj, we have a map from B to X.
    And realize that this actually forms a diagram, i.e. consider if
    we just rearranged it where B was in the location where the pullback is.
    So the pull back is of course universal, so there exists a unique map from
    B to the pullback. But we have to be careful, we can't say that this map
    commutes with the entire diagram. We only have this diagram.
    Thus our problem reduces to proving this triangle commutes. So that the
    top map equals the vertal and diagonal map composed.
    Again, we argue
    by the universal property of pullbacks in the following way:
    So the pullback is determined by the maps p and f. Well, we have two diagrams
    and i've highlighted what makes them quote on quote pull back diagrams
    in red. The universal property then says that the map from A to the pullback in 
    this case is unique. In the other diagram, we get that the vertical compose
    diagonal map is also unique. Well, then they must be equivalent, and we are done.
    """
    def construct(self):
        t = make_title("Proposition", "2.10")

        self.add(t)

        p1 = TextMobject(r"""
            $K$Proj and $K$Inj are closed under pushout and pullback.
        """).scale(.75).to_title(t)

        p2 = tikz("prop210_4_p2", r"""
            \begin{tikzcd}
                Z \times_f X
                    \arrow{r}\arrow{d}[left]{f^\ast p}
                    & X
                    \arrow{d}[right]{p\in K\text{Inj}} \\
                Z
                    \arrow{r}[above]{f}
                    & Y
            \end{tikzcd}
        """, fn).shift(.5*DOWN)

        self.cycle(
            [p1, p2],
            out=False
        )

        p3 = tikz("prop210_4_p3", r"""
            \begin{tikzcd}
                A
                    \arrow{r}\arrow{d}[left]{i\in K}
                    & Z \times_f X
                    \arrow{r}\arrow{d}[left]{f^\ast p}
                    & X
                    \arrow{d}[right]{p\in K\text{Inj}} \\
                B
                    \arrow{r}[above]{g}
                    & Z
                    \arrow{r}[above]{f}
                    & Y
            \end{tikzcd}
        """, fn).shift(.5*DOWN)

        self.fade_replace(
            p2,
            p3
        )

        p4 = tikz("prop210_4_p4", r"""
            \begin{tikzcd}
                A
                    \arrow{r}\arrow{d}[left]{i\in K}
                    & Z \times_f X
                    \arrow{r}\arrow{d}[left]{f^\ast p}
                    & X
                    \arrow{d}[right]{p\in K\text{Inj}} \\
                B
                    \arrow{r}[above]{g}\arrow[dashed]{urr}
                    & Z
                    \arrow{r}[above]{f}
                    & Y
            \end{tikzcd}
        """, fn).shift(.5*DOWN)

        self.fade_replace(
            p3,
            p4
        )

        p5 = tikz("prop210_4_p5", r"""
            \begin{tikzcd}
                & Z \times_f X
                    \arrow{r}\arrow{d}[left]{f^\ast p}
                    & X
                    \arrow{d}[right]{p\in K\text{Inj}} \\
                B
                    \arrow{r}[above]{g}\arrow[dashed]{ur}[left,yshift=.5em]{\hat{g}}
                    & Z
                    \arrow{r}[above]{f}
                    & Y
            \end{tikzcd}
        """, fn).shift(.5*DOWN)

        self.fade_replace(
            p4,
            p5
        )

        p6 = tikz("prop210_4_p6", r"""
            \begin{tikzcd}
                A
                    \arrow{r}\arrow{d}[left]{i\in K}
                    & Z\times_f X \\
                B
                    \arrow{ur}[right,yshift=-.5em]{\hat{g}}
            \end{tikzcd}
        """, fn).shift(.5*DOWN)

        self.fade_replace(
            p5, p6
        )

        p7 = tikz("prop210_4_p7", r"""
            \begin{tikzcd}
                A
                    \arrow[red]{r}\arrow[red]{d}[left]{i\in K}
                    & Z \times_f X
                    \arrow[red]{r}\arrow{d}[left]{f^\ast p}
                    & X
                    \arrow{d}[right]{p\in K\text{Inj}} \\
                B
                    \arrow[red]{r}[above]{g}
                    & Z
                    \arrow{r}[above]{f}
                    & Y
            \end{tikzcd}
        """, fn).shift(.5*DOWN)

        self.fade_replace(
            p6, p7
        )

        p8 = tikz("prop210_4_p8", r"""
            \begin{tikzcd}
                A
                    \arrow[red]{d}[left]{i\in K}
                    & Z \times_f X
                    \arrow[red]{r}\arrow{d}[left]{f^\ast p}
                    & X
                    \arrow{d}[right]{p\in K\text{Inj}} \\
                B
                    \arrow[red]{r}[above]{g}\arrow[red]{ur}
                    & Z
                    \arrow{r}[above]{f}
                    & Y
            \end{tikzcd}
        """, fn).shift(.5*DOWN)

        self.fade_replace(
            p7, p8
        )

        p9 = TexMobject(r"""
            (A\to B\to Z\times_f X)\cong (A\to Z\times_f X)
        """).scale(.75).next_to(p8, direction=DOWN, buff=1)

        self.cycle(
            [p9],
            out=False
        )
        self.play(
            *[FadeOut(mob) for mob in self.mobjects[1:]]
        )

class prop210_5(Scene):
    """
    Finally, we want to show that both classes are closed under products
    and coproducts. Again, we prove one out of the four cases, in particular that
    KProj is closed under coproducts.
    We will use the universal property of coproducts a lot. First of all, observing
    that the coproduct of maps is the induced map on the coproduct of the spaces.
    We want to show this is in KProj, so of course we set up our diagram. Then
    we observe that this is just the set of these diagrams, for which we can
    construct a lift by assumption. So then this induces a lift on the coproduct
    diagram, and we are done.
    """
    def construct(self):
        t = make_title("Proposition", "2.10")

        self.add(t)

        p1 = TextMobject(r"""
            $K$Proj and $K$Inj are closed under products and coproducts.
        """).scale(.75).to_title(t)

        p2 = TexMobject(r"""
            \{A_s\overset{i_s}{\longrightarrow}B_s\in K\text{Proj}\}_{s\in S}
        """).scale(.75).shift(.5*DOWN)

        self.cycle(
            [p1, p2],
            out=False
        )

        p3 = TexMobject(r"""
            \big( \underset{s\in S}{\sqcup}A_s \overset{(i_s)_{s\in S}}{\longrightarrow}
            \underset{s\in S}{\sqcup}B_s\big)\in K\text{Proj}
        """).scale(.75).shift(.5*DOWN)

        self.play(
            ReplacementTransform(p2, p3)
        )
        self.wait(2)

        p4 = tikz("prop210_5_p4", r"""
            \begin{tikzcd}
                \underset{s\in S}{\sqcup}A_s
                    \arrow{r}\arrow{d}[left]{(i_s)_{s\in S}}
                    & X
                    \arrow{d}[right]{f\in K} \\
                \underset{s\in S}{\sqcup}B_s
                    \arrow{r}
                    & Y
            \end{tikzcd}
        """, fn).shift(.5*DOWN)

        self.fade_replace(
            p3, p4
        )

        p5 = tikz("prop210_5_p5", r"""
            $
            \left\{
            \begin{tikzcd}
                A_s
                    \arrow{r}\arrow{d}[left]{i_s\in K\text{Proj}}
                    & X
                    \arrow{d}[right]{f\in K} \\
                B_s
                    \arrow{r}
                    & Y
            \end{tikzcd}
            \right\}_{s\in S}
            $
        """, fn).shift(.5*DOWN)

        self.fade_replace(
            p4, p5
        )

        p6 = tikz("prop210_5_p6", r"""
            $
            \left\{
            \begin{tikzcd}
                A_s
                    \arrow{r}\arrow{d}[left]{i_s\in K\text{Proj}}
                    & X
                    \arrow{d}[right]{f\in K} \\
                B_s
                    \arrow{r}\arrow[dashed]{ur}[left, yshift=.5em]{\ell_s}
                    & Y
            \end{tikzcd}
            \right\}_{s\in S}
            $
        """, fn).shift(.5*DOWN)

        self.fade_replace(
            p5, p6
        )

        p7 = tikz("prop210_5_p7", r"""
            \begin{tikzcd}[column sep=huge]
                \underset{s\in S}{\sqcup}A_s
                    \arrow{r}\arrow{d}[left]{(i_s)_{s\in S}}
                    & X
                    \arrow{d}[right]{f\in K} \\
                \underset{s\in S}{\sqcup}B_s
                    \arrow{r}\arrow[dashed]{ur}[left,yshift=.5em]{(\ell_s)_{s\in S}}
                    & Y
            \end{tikzcd}
        """, fn).shift(.5*DOWN)

        self.fade_replace(
            p6, p7
        )
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

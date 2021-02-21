# Date: 2/21/21
# Purpose: derived functors section nLab
# Notes:

from manimlib.imports import *
fn = "derived_functors"


class def239(Scene):
    """
    Given two categories withh weak equivalences, a functor between them that sends weak 
    equivalences to weak equivalences is called a homotopical functor. So in some sense
    it is preserving some extra structure with regards to weak equivalences.
    """
    def construct(self):
        t = make_title("Definition", 2.39)
        self.title(t)

        d1 = TextMobject(r"""
            For $\mathcal{C}$ and $\mathcal{D}$ two categories with weak equivalences, 
            then a functor $F:\mathcal{C}\to\mathcal{D}$ is called a homotopical functor 
            if it sends weak equivalences to weak equivalences.
        """, alignment="").scale(.75).to_title(t)

        self.cycle(
            [d1],
            out=False
        )
        self.clear()

class def240(Scene):
    """
    Now consider the corresponding homotopy categories of these categories. So the functor
    F followed by the localization functor on D is a functor from C to the homotopy category of 
    D and it sends weak equivalences to isomorphisms. Thus there exists a functor from
    the homotopy category of C to the homotopy category of D by the universal property,
    and this is unique again up to unique isomorphism.
    We call this induced map the derived functor or total functor of F.
    """
    def construct(self):
        t = make_title("Definition", "2.40")
        self.title(t)

        d1 = TextMobject(r"""
            Given a homotopical functor $F:\mathcal{C}\to\mathcal{D}$ between categories 
            with weak equivalences whose homotopy categories Ho$(\mathcal{C})$ and 
            Ho$(\mathcal{D})$ exist, then its 
        """, "derived functor", " ", r"""
            is the functor Ho$(F)$ between these homotopy categories which is induced uniquely, 
            up to unique isomorphism, by their universal property:
        """, alignment="").scale(.75).to_title(t)
        d1[1].set_color(BLUE)

        d2 = tikz("def_240_d2", r"""
            \begin{tikzcd}
                \mathcal{C}
                    \arrow{r}[above]{F}\arrow{d}[left]{\gamma_\mathcal{C}}
                    & \mathcal{D}
                    \arrow{d}[right]{\gamma_\mathcal{D}} \\
                \text{Ho}(\mathcal{C})
                    \arrow{r}[below]{\text{Ho}(F)}
                    & \text{Ho}(\mathcal{D})
            \end{tikzcd}
        """, fn).next_to(d1, direction=DOWN, buff=.25)

        self.cycle(
            [d1, d2],
            out=False,
            successive=False
        )
        self.clear()

class rmk241(Scene):
    """
    So remember how we said that the localizations of the subcatgories of fibrant, cofibrant,
    and fibrant cofibrant objects were all isomorphic to the original homotopy category?
    Here's an instance of where that is useful: many of the functors we will study are not
    homotopical generally, but become so when restricted to C_f or C_c.
    """
    def construct(self):
        t = make_title("Definition", 2.41)
        self.title(t)

        r1 = TextMobject(r"""
            Many functors of interest become homotopical only after restriction to 
            the full subcategories $\mathcal{C}_f$ of fibrant objects or $\mathcal{C}_c$ 
            of cofibrant objects.
        """, alignment="").scale(.75)

        self.cycle(
            [r1],
            out=False
        )
        self.clear()

class def242(Scene):
    """
    So to make this a little more explicit, consider a functor F that when restricted
    to the full subcategory of fibrant objects becomes a derived functor. Then we
    call the resulting induced derived functor the right derived functor of F, RF.
    Dually, if the restriction to cofibrant objects makes it a homotopical functor,
    then we call the induced derived functor the left derived functor of F, LF.
    """
    def construct(self):
        t = make_title("Definition", 2.42)
        self.title(t)

        d1 = TextMobject(r"""
            Consider a functor $F:\mathcal{C}\to\mathcal{D}$ out of a model category into 
            a category with weak equivalences.
        """, alignment="").scale(.75).to_title(t)

        d2 = TextMobject(r"""
            1. If the restriction of $F$ to $\mathcal{C}_f$ becomes a homotopical 
            functor, then the derived functor of the restriction is the 
        """, "right derived functor", " $\\mathbb{R}F$:", alignment="")\
            .scale(.75).next_to(d1, direction=DOWN, buff=1)
        d2[1].set_color(BLUE)

        d3 = tikz("def242_d3", r"""
            \begin{tikzcd}
                & \mathcal{C}_f
                    \arrow{r}[above]{i}\arrow{d}[left]{\gamma_{\mathcal{C}_f}}
                    & \mathcal{C}
                    \arrow{r}[above]{F}
                    & \mathcal{D}
                    \arrow{d}[right]{\gamma_\mathcal{D}} \\
                \mathbb{R}F:
                    & \mathcal{C}_f[W^{-1}]
                    \arrow{r}[above]{\simeq}
                    & \text{Ho}(\mathcal{C})
                    \arrow{r}[below]{\text{Ho}(F)}
                    & \text{Ho}(\mathcal{D})
            \end{tikzcd}
        """, fn).next_to(d2, direction=DOWN, buff=.25)

        self.cycle(
            [d1],
            out=False
        )
        self.cycle(
            [d2, d3],
            out=False,
            successive=False
        )

        d4 = TextMobject(r"""
            2. If the restriction of $F$ to $\mathcal{C}_c$ becomes a homotopical 
            functor, then the derived functor of the restriction is the 
        """, "left derived functor", " $\\mathbb{L}F$:", alignment="")\
            .scale(.75).next_to(d1, direction=DOWN, buff=1)
        d4[1].set_color(BLUE)

        d5 = tikz("def242_d5", r"""
            \begin{tikzcd}
                & \mathcal{C}_c
                    \arrow{r}[above]{i}\arrow{d}[left]{\gamma_{\mathcal{C}_c}}
                    & \mathcal{C}
                    \arrow{r}[above]{F}
                    & \mathcal{D}
                    \arrow{d}[right]{\gamma_\mathcal{D}} \\
                \mathbb{R}F:
                    & \mathcal{C}_c[W^{-1}]
                    \arrow{r}[above]{\simeq}
                    & \text{Ho}(\mathcal{C})
                    \arrow{r}[below]{\text{Ho}(F)}
                    & \text{Ho}(\mathcal{D})
            \end{tikzcd}
        """, fn).next_to(d2, direction=DOWN, buff=.25)

        self.play(
            FadeOut(d2),
            FadeOut(d3),
            FadeIn(d4),
            FadeIn(d5)
        )
        self.wait(2)
        self.clear()

class prop243(Scene):
    """
    Now you might not expect this to be useful unless somehow it is easier to ascertain
    that a functor out of the full subcategory of fibrant or cofibrant objects is homotopical.
    This turns out to be the case, and this is called Ken Brown's lemma.
    So suppose C is a model category and D is a category with weak equivalences. Then a functor
    out of Cf is homotopical if it sends acyclic fibrations to weak equivalences.
    Dually, a functor out of Cc is a homotopical functor if it sends acyclic cofibrations
    to weak equivalences.
    We will prove this, but one of our steps will use what is called the factorization lemma,
    and that statement and proof is something we will cover later. We will prove for Cf and
    the other case is dual.
    So suppose that acyclic fibrations are sent to weak equivalences. Now pick a random
    weak equivalence in Cf, and we want to show that it is sent to a weak equivalence.
    Consider the folowing diagram for choice of path space object. So p0 and p1 on the 
    bottom are acyclic fibrations following from the factorization of the diagonal.
    f is a weak equivalence by assumption. the top left vertical morphism is a weak
    equivalence due to the factorization lemma- the composite vertical morphism factors
    f through a weak equivalence, and since if is a weak equivalence then p1 f is as well.
    We can apply F to this diagram. All the acyclic fibrations are sent to weak
    equivalences. The factorization lemma says the vertical composite is a fibration,
    and since both are weak equivalences it is an acyclic fibration. Then we just apply
    two-out-of-three a couple times to see that F of f is a weak equivalence.
    """
    def construct(self):
        t = make_title("Proposition", 2.43)
        self.title(t)

        p1 = TextMobject(r"""
            Let $\mathcal{C}$ be a model category and $\mathcal{D}$ be a 
            category with weak equivalences.
        """, alignment="").scale(.75).to_title(t)

        p2 = TextMobject(r"""
            \begin{enumerate}
                \item a functor $$ F:\mathcal{C}_f\longrightarrow\mathcal{D} $$
                    is a homotopical functor if it sends acyclic fibrations to 
                    weak equivalences.
                \item a functor $$ F:\mathcal{C}_c\longrightarrow\mathcal{D} $$
                    is a homotopical functor if it sends acyclic cofibrations to 
                    weak equivalences.
            \end{enumerate}
        """).scale(.75).next_to(p1, direction=DOWN, buff=.75).to_edge(LEFT, buff=.5)

        self.cycle(
            [p1, p2]
        )

        p3 = tikz("prop243_p3", r"""
            \begin{tikzcd}
                \text{Path}(f)
                    \arrow{r}[below]{\in W\cap\text{Fib}}\arrow{d}[left]{p_1^\ast f\in W}
                    & X
                    \arrow{d}[right]{f\in W} \\
                \text{Path}(Y)
                    \arrow{r}[above]{p_1}[below]{\in W\cap\text{Fib}}[above,yshift=1em]{(\text{pb})}
                        \arrow{d}[left]{p_0\in W\cap\text{Fib}}
                    & Y \\
                Y
            \end{tikzcd}
        """, fn).scale(1.5)

        self.cycle(
            [p3],
            out=False
        )

        p4 = tikz("prop243_p4", r"""
            \begin{tikzcd}
                F(\text{Path}(f))
                    \arrow{r}[below]{\in W}\arrow{d}[left]{F(p_1^\ast f)}
                    & F(X)
                    \arrow{d}[right]{F(f)} \\
                F(\text{Path}(Y))
                    \arrow{r}[above]{F(p_1)}[below]{\in W}
                        \arrow{d}[left]{F(p_0)}
                    & F(Y) \\
                F(Y)
            \end{tikzcd}
        """, fn).scale(1.5)

        self.fade_replace(
            p3, p4
        )
        self.clear()

class cor244(Scene):
    """
    If both C and D are model categories, we don't even need to consider all of D.
    It follows from what we've just discussed that the left derived functor 
    exists as long as the functor F preserves cofibrant objects and acyclic cofibrations
    between them.
    Dually, if F preserves fibrant objects and acyclic fibrations between them, then its
    right derived functor exists.
    """
    def construct(self):
        t = make_title("Corollary", 2.44)
        self.title(t)

        c1 = TextMobject(r"""
            Let $F:\mathcal{C}\to\mathcal{D}$ be a functor between model categories.
        """, alignment="").scale(.75).to_title(t)

        self.cycle(
            [c1],
            out=False
        )

        c2 = TextMobject(r"""
            1. If $F$ preserves cofibrant objects and acyclic cofibrations between them, 
            then its left derived functor exists:
        """, alignment="").scale(.75).next_to(c1, direction=DOWN, buff=.75).to_edge(LEFT, buff=.5)

        c3 = tikz("cor244_c3", r"""
            \begin{tikzcd}
                \mathcal{C}_c
                    \arrow{r}[above]{F}\arrow{d}[left]{\gamma_\mathcal{C}}
                    & \mathcal{D}_c
                    \arrow{d}[right]{\gamma_\mathcal{D}} \\
                \text{Ho}(\mathcal{C})
                    \arrow{r}[above]{\mathbb{L}F}
                    & \text{Ho}(\mathcal{D})
            \end{tikzcd}
        """, fn).next_to(c2, direction=DOWN, buff=.5)

        self.cycle(
            [c2, c3],
            out=False,
            successive=False
        )

        c4 = TextMobject(r"""
            2. If $F$ preserves fibrant objects and acyclic fibrations between them, 
            then its right derived functor exists:
        """, alignment="").scale(.75).next_to(c1, direction=DOWN, buff=.75).to_edge(LEFT, buff=.5)

        c5 = tikz("cor244_c3", r"""
            \begin{tikzcd}
                \mathcal{C}_f
                    \arrow{r}[above]{F}\arrow{d}[left]{\gamma_\mathcal{C}}
                    & \mathcal{D}_f
                    \arrow{d}[right]{\gamma_\mathcal{D}} \\
                \text{Ho}(\mathcal{C})
                    \arrow{r}[above]{\mathbb{R}F}
                    & \text{Ho}(\mathcal{D})
            \end{tikzcd}
        """, fn).next_to(c2, direction=DOWN, buff=.5)

        self.play(
            FadeOut(c2),
            FadeOut(c3),
            FadeIn(c4),
            FadeIn(c5)
        )
        self.wait(2)
        self.clear()

class prop245(Scene):
    """
    We now these derived functors under the hood send weak equivalences to weak equivalences.
    But what does it do to objects? Well, if F preserves fibrant objects and weak equivalences
    between them, then the total right derived functor, sends an object X in C to the
    cofibrant replacement of F of the fibrant replacement of X, i.e. QF(PX).
    Dually, if F preserves cofibrant objects and weak equivalences between them, then the
    total left derived functor sends X to PF(QX).
    We will prove the first statement, the other is just dual.
    Let gamma C be the map from C to the homotopy category of C, and likewise gamma D.
    We can consider RF(X) as gamma D of F(gamma C), as this will give us a map from Ho C
    to Ho D.
    By assumption, F is a homotopical functor on fibrant objects. The map from QP(X) to
    P(X), well first of all they are both fibrant objects. Second by construction the
    map is an acyclic fibration, so under F which is a homotopical functor the map
    F(QPX) to F(PX) is a weak equivalence, and so it is sent to an isomorphism under
    gamma D. Well than using what we said before, we can have this isomorphism with RF(X).
    Also we assumed F preserved fibrant objects, so F(PX) is fibrant, and so gamma D acts
    on it by only cofibrant replaceemnt, i.e. gamma D (FP(X)) is QF(PX), and we are done.
    """
    def construct(self):
        t = make_title("Proposition", 2.45)
        self.title(t)

        p1 = TextMobject(r"""
            Let $F:\mathcal{C}\to\mathcal{D}$ be a functor between two model categories.
        """, alignment="").scale(.75).to_title(t)

        self.cycle(
            [p1],
            out=False
        )

        p2 = TextMobject(r"""
            1. If $F$ preserves fibrant objects and weak equivalences between them, 
            then $\mathbb{R}F(X)\simeq Q(F(PX))$ for
        """, alignment="").scale(.75).next_to(p1, direction=DOWN, buff=1).to_edge(LEFT, buff=.5)

        p3 = tikz("prop245_p3", r"""
            \begin{tikzcd}
                \mathcal{C}_f
                    \arrow{r}[above]{F}\arrow{d}[left]{\gamma_{\mathcal{C}_f}}
                    & \mathcal{D}
                    \arrow{d}[right]{\gamma_\mathcal{D}} \\
                \text{Ho}(\mathcal{C})
                    \arrow{r}[below]{\mathbb{R}F}
                    & \text{Ho}(\mathcal{D})
            \end{tikzcd}
        """, fn).next_to(p2, direction=DOWN, buff=.5)

        self.cycle(
            [p2, p3],
            successive=False
        )

        p4 = TextMobject(r"""
            2. If $F$ preserves cofibrant objects and weak equivalences between them, 
            then $\mathbb{L}F(X)\simeq P(F(QX))$ for
        """, alignment="").scale(.75).next_to(p1, direction=DOWN, buff=1).to_edge(LEFT, buff=.5)

        p5 = tikz("prop245_p3", r"""
            \begin{tikzcd}
                \mathcal{C}_c
                    \arrow{r}[above]{F}\arrow{d}[left]{\gamma_{\mathcal{C}_c}}
                    & \mathcal{D}
                    \arrow{d}[right]{\gamma_\mathcal{D}} \\
                \text{Ho}(\mathcal{C})
                    \arrow{r}[below]{\mathbb{L}F}
                    & \text{Ho}(\mathcal{D})
            \end{tikzcd}
        """, fn).next_to(p2, direction=DOWN, buff=.5)

        self.cycle(
            [p4, p5],
            out=False,
            successive=False
        )
        self.play(
            FadeOut(p1),
            FadeOut(p4),
            FadeOut(p5)
        )

        p6 = TextMobject(r"""
            \begin{align*}
                \mathbb{R}F(X)\simeq & \gamma_D(F(\gamma_\mathcal{C})) \\
                \simeq & \gamma_\mathcal{D}F(Q(P(X)))
            \end{align*}
        """).scale(.75).shift(1*UP)

        p7 = TexMobject(r"""
            F(Q(P(X)))\to F(P(X))
        """).scale(.75).next_to(p6, direction=DOWN, buff=1)

        p8 = TexMobject(r"""
            \mathbb{R}F(X)\simeq\gamma_\mathcal{D}(F(P(X)))
        """).scale(.75).next_to(p7, direction=DOWN, buff=1)

        self.cycle(
            [p6, p7, p8],
            out=False,
            successive=False
        )
        self.clear()

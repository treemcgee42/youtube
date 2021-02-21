# Date: 2/18/21
# Purpose: cor 2.11 - end w. fact. section nLab
# Notes: recorded 2/21

from manimlib.imports import *
fn = "retract_factorizations"


class cor211(Scene):
    """
    So from the proposition that we ended on last time, a pretty immediate
    consequence is that every K injective morphism has the right lifting property
    against all K relative cell complexes and their retracts. Because in particular
    we showed that this class was closed under coproducts and forming retracts and
    the projective morphisms are closed under transfinite colimits.
    I believe we used this result in one of our earlier results, so its nice to have it now.
    """
    def construct(self):
        t = make_title("Corollary", 2.11)

        self.title(t)

        c1 = TextMobject(r"""
            Every $K$-injective morphism has the right lifting property against 
            all $K$-relative cell complexes and their retracts.
        """, alignment="").scale(.75).to_title(t)

        self.cycle(
            [c1],
            out=False
        )
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class lemma213(Scene):
    """
    So being closed under retracts is a pretty cool thing. This lemma says that
    for any category, its class of isomorphisms is closed under retracts.
    Well this is pretty simple, we have our retract diagram, and suppose that f
    is an isomorphism. We want to show that g is an isomorphism, but we can
    just reverse the isomorphism to get this.
    """
    def construct(self):
        t = make_title("Lemma", 2.13)

        self.title(t)

        l1 = TextMobject(r"""
            In every category $\mathcal{C}$ the class of isomorphisms is 
            preserved under retracts.
        """).scale(.75).to_title(t)

        self.cycle(
            [l1],
            out=False
        )

        l2 = tikz("lemma213", r"""
            \begin{tikzcd}
                \text{id}_A:
                    & A
                    \arrow{r}\arrow{d}[right]{g}
                    & X
                    \arrow{r}\arrow{d}[right]{f}
                    & A
                    \arrow{d}[right]{g} \\
                \text{id}_B:
                    & B
                    \arrow{r}
                    & Y
                    \arrow{r}
                    & B
            \end{tikzcd}    
        """, fn).shift(.5*DOWN, 1*LEFT)

        l3 = tikz("lemma213", r"""
            \begin{tikzcd}
                \text{id}_A:
                    & A
                    \arrow{r}\arrow{d}[right]{g}
                    & X
                    \arrow[red]{r}
                    & A
                    \arrow{d}[right]{g} \\
                \text{id}_B:
                    & B
                    \arrow[red]{r}
                    & Y
                    \arrow{r}\arrow[red]{u}[right]{f^{-1}}
                    & B
            \end{tikzcd}    
        """, fn).shift(.5*DOWN, 1*LEFT)

        self.cycle(
            [l2],
            out=False
        )
        self.fade_replace(
            l2, l3
        )
        self.clear()

class prop214(Scene):
    """
    So how far can we run with this idea? We'd like to say something about weak 
    equivalences being closed under forming retracts. This isn't true for all
    categories with weak equivalences however, but it is true for model categories.
    So again, let's start with a retract, and assume that that middle morphism
    w is a weak equivalence. We want to show that f is also a weak equivalence.
    Ok, first let's consider the case that f is a fibration.
    Well, we are in a model category, and so cofibrations comma acyclic fibrations
    are a weak factorization system, so let's factor w as such, i.e. a cofibration
    followed by an acyclic fibration. But since w is a weak equivalence, which are
    closed under two out of three, the cofibration through which it factors is in
    particular a weak equivalence, i.e. an acyclic cofibration.
    Well why did we do that? Well ideally we would like to get this resulting diagram
    commute. We'd have this diagram without the top middle acyclic cofibration, but
    we wouldn't necessarily have the middle morphisms. Well, we'd have that first
    middle morphism s, which is the top horizontal followed by the middle top morphism.
    But we would have the second middle morphism t. The only reason we have it now
    is because f is a fibration and hence has the right lifting property against
    acyclic cofibrations. So t is a lift, and that's why we have that this entire
    diagram commutes.
    Well, then look at the bottom two rows. This exhibits f as a retract of an acyclic
    fibration, and we showed last video that these are closed under retracts, so f is
    an acyclic fibration, hence in particular a weak equivalence, and we are done with
    the case that f is a fibration.
    For the general case, we can factor f as an acyclic cofibration followed by a fibration,
    like so. Now, let's do a pushout in the top left. We showed last video that
    acyclic cofibrations, which are projective morphisms, are closed under pushouts, and hence
    this middle vertical top map is an acyclic cofibration.
    Well remember that we have a map X to Y, and so we have a square A X B Y that is a pushout
    diagram, hence we have a unique map from X' to Y by the universal property of pushouts.
    This map, by two out of three, is a weak equivalence.
    Our last missing map from X prime to A comes from a lift by virtue of the map from X to 
    X' being a projective morphism wrt to fibrations, so the square here is X A' X' and B.
    Well by what we just showed, since this exhibits a fibration as a retract of a weak
    equivalence this means that the bottom left morphism is an acyclic fibration, and
    hence the entire left composite morphism is a weak equivalence and we are done.
    """
    def construct(self):
        t = make_title("Proposition", 2.14)

        self.title(t)

        p1 = TextMobject(r"""
            Given a model category, then its class of weak equivalences is closed 
            under forming retracts.
        """, alignment="").scale(.75).to_title(t)

        self.cycle(
            [p1],
            out=False
        )

        p2 = tikz("prop214_p2", r"""
        \begin{tikzcd}
            \text{id}:
                & A
                \arrow{r}\arrow{d}[left]{f}
                & X
                \arrow{r}\arrow{d}[right]{w}
                & A
                \arrow{d}[right]{f} \\
            \text{id}:
                & B
                \arrow{r}
                & Y
                \arrow{r}
                & B
        \end{tikzcd}
        """, fn).shift(.5*DOWN, 1*LEFT)

        self.cycle(
            [p2],
            out=False
        )

        p3 = tikz("prop214_p3", r"""
            \begin{tikzcd}
                X
                    \arrow{rr}[above]{w}\arrow{dr}[left,yshift=-.5em]{\text{Cof}}
                    &
                    & Y \\
                & X'
                    \arrow{ur}[right,yshift=-.5em]{W\cap\text{Fib}}
            \end{tikzcd}
        """, fn).shift(.5*DOWN)

        self.fade_replace(
            p2, p3
        )

        p4 = tikz("prop214_p4", r"""
        \begin{tikzcd}
            \text{id}:
                & A
                \arrow{r}\arrow{d}[left]{\text{id}}
                & X
                \arrow{r}\arrow{d}[right]{W\cap\text{Cof}}
                & A
                \arrow{d}[right]{\text{id}} \\
            \text{id}:
                & A
                \arrow{r}[above]{s}\arrow{d}[left]{f\in\text{Fib}}
                & X'
                \arrow{d}[right]{W\cap\text{Fib}}\arrow{r}[above]{t}
                & A'
                \arrow{d}[right]{f\in\text{Fib}} \\
            \text{id}:
                & B
                \arrow{r}
                & Y
                \arrow{r}
                & B
        \end{tikzcd}
        """, fn).shift(1*DOWN, .5*LEFT).scale(1.5)

        self.fade_replace(
            p3, p4
        )
        self.play(
            FadeOut(p4)
        )

        p5 = tikz("prop214", r"""
            \begin{tikzcd}
                A
                    \arrow{r}\arrow{d}[left]{W\cap\text{Cof}}
                    & X
                    \arrow{r}\arrow{dd}[right]{W}
                    & A
                    \arrow{d}[right]{W\cap\text{Cof}} \\
                A'
                    \arrow{d}[left]{\text{Fib}}
                    &
                    & A'
                    \arrow{d}[right]{\text{Fib}} \\
                B
                    \arrow{r}
                    & Y
                    \arrow{r}
                    & B
            \end{tikzcd}
        """, fn).shift(1*DOWN).scale(1.5)

        self.cycle(
            [p5],
            out=False
        )

        p6 = tikz("prop214_p6", r"""
            \begin{tikzcd}
                A
                    \arrow{r}\arrow{d}[left]{W\cap\text{Cof}}
                    & X
                    \arrow{r}\arrow{d}[right]{W\cap\text{Cof}}
                    & A
                    \arrow{d}[right]{W\cap\text{Cof}} \\
                A'
                    \arrow{d}[left]{\text{Fib}}\arrow{r}
                    & X'
                    & A'
                    \arrow{d}[right]{\text{Fib}} \\
                B
                    \arrow{r}
                    & Y
                    \arrow{r}
                    & B
            \end{tikzcd}
        """, fn).shift(1*DOWN).scale(1.5)

        self.fade_replace(
            p5, p6
        )

        p7 = tikz("prop214_p7", r"""
            \begin{tikzcd}
                A
                    \arrow{r}\arrow{d}[left]{W\cap\text{Cof}}
                    & X
                    \arrow{r}\arrow{d}[right]{W\cap\text{Cof}}
                    & A
                    \arrow{d}[right]{W\cap\text{Cof}} \\
                A'
                    \arrow{d}[left]{\text{Fib}}\arrow{r}
                    & X'
                    \arrow{d}[right]{W}
                    & A'
                    \arrow{d}[right]{\text{Fib}} \\
                B
                    \arrow{r}
                    & Y
                    \arrow{r}
                    & B
            \end{tikzcd}
        """, fn).shift(1*DOWN).scale(1.5)

        self.fade_replace(
            p6, p7
        )

        p8 = tikz("prop214_p8", r"""
            \begin{tikzcd}
                A
                    \arrow{r}\arrow{d}[left]{W\cap\text{Cof}}
                    & X
                    \arrow{r}\arrow{d}[right]{W\cap\text{Cof}}
                    & A
                    \arrow{d}[right]{W\cap\text{Cof}} \\
                A'
                    \arrow{d}[left]{\text{Fib}}\arrow{r}
                    & X'
                    \arrow{d}[right]{W}\arrow{r}
                    & A'
                    \arrow{d}[right]{\text{Fib}} \\
                B
                    \arrow{r}
                    & Y
                    \arrow{r}
                    & B
            \end{tikzcd}
        """, fn).shift(1*DOWN).scale(1.5)

        self.fade_replace(
            p7, p8
        )
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class lemma215(Scene):
    """
    Our next lemma is sometimes referred to as the retract argument. So if we have a
    composite morphism, and the entire map f has the left lifting property against
    the second map p, then f is a retract of the first map i. Dually, if f has the
    right lifting property against the first map i then f is a retract of the second
    map p. We will prove number two, and the other case is dual.
    So let's right our composition in this way, so the liftings become clear. So by 
    assumption f has the right lifting property against p so there is a lift g from
    Y to A. We can again rearrange this, and then observe that since i compose p
    is f we can complete the diagram in the collowing way, which exhibits f as a retract
    of i as desired.
    """
    def construct(self):
        t = make_title("Lemma", 2.15)

        self.title(t)

        l1 = TexMobject(r"""
            f: X
                \overset{i}{\longrightarrow}
            A
                \overset{p}{\longrightarrow}
            Y
        """).scale(.75).shift(1*UP)

        l2 = TextMobject(r"""
            \begin{enumerate}
                \item If $f$ has the left lifting property against $p$, 
                    then $f$ is a retract of $i$
                \item If $f$ has the right lifting property against $i$, then 
                    $f$ is a retract of $p$.
            \end{enumerate}
        """).scale(.75).next_to(l1, direction=DOWN, buff=.5)

        self.cycle(
            [l1, l2],
            successive=False
        )

        l3 = tikz("lemma215_l3", r"""
            \begin{tikzcd}
                X
                    \arrow{r}[above]{i}\arrow{d}[left]{f}
                    & A
                    \arrow{d}[right]{p} \\
                Y
                    \arrow{r}[above]{=}
                    & Y
            \end{tikzcd}
        """, fn)

        self.cycle(
            [l3],
            out=False
        )

        l4 = tikz("lemma215_l4", r"""
            \begin{tikzcd}
                X
                    \arrow{r}[above]{i}\arrow{d}[left]{f}
                    & A
                    \arrow{d}[right]{p} \\
                Y
                    \arrow{r}[above]{=}\arrow[dashed]{ur}[right,yshift=-.5em]{g}
                    & Y
            \end{tikzcd}
        """, fn)

        self.fade_replace(
            l3, l4
        )

        l5 = tikz("lemma215_l5", r"""
            \begin{tikzcd}
                & X
                    \arrow{r}[above]{=}\arrow{d}[left]{f}
                    & X
                    \arrow{d}[left]{i} \\
                \text{id}_Y: & Y
                    \arrow{r}[below]{g}
                    & A
                    \arrow{r}[below]{p}
                    & Y
            \end{tikzcd}
        """, fn).shift(1*LEFT)

        self.fade_replace(
            l4, l5
        )

        l6 = tikz("lemma215_l6", r"""
            \begin{tikzcd}
                \text{id}_X: & X
                    \arrow{r}[above]{=}\arrow{d}[left]{f}
                    & X
                    \arrow{d}[left]{i}\arrow{r}[above]{=}
                    & X
                    \arrow{d}[left]{f} \\
                \text{id}_Y: & Y
                    \arrow{r}[below]{g}
                    & A
                    \arrow{r}[below]{p}
                    & Y
            \end{tikzcd}
        """, fn).shift(1*LEFT)

        self.fade_replace(
            l5, l6
        )
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class soa(Scene):
    """
    So for the last part of this discusion, we want to talk about what is called the small
    object argument. So, given some category, when can we factor a morphism
    as a C relative complex followed by a C injective morphism, where C is a subclass of 
    morphisms?
    Well, let's try to. Lets consider all possible ways we can attach C cells to X.
    A way to think of this "all possible" ways is to consider the set of all commuting
    squares of this form. So dom and cod are just standins for the domain and codomain, which
    aren't specified. Again, all possible squares. Well ok, we want to factor the right morphism
    as a C relative complex followed by an injective morphism. Well, lets pushout, and we get
    this X_1 which is by definition a relative cell complex. Great, and now we can by the universal
    property construct a map from X1 to Y. In fact, we can rearrange it like this, so that
    lifting properties become more apparant. Well have we achieved our goal of factoring
    the f as a relative cell complex followed by an injective morphism? Well we certainly have
    that the top right morphism is a relative cell complex, but is the bottom right one an 
    injective morphism? So that would mean it lifts morphisms in C. Well, in order for that
    diagonal map to be a lift, there needs to be a morphism accross the middle, making a square.
    So can't we just define that to be the composite of the top horizontal and top right morphism?
    Sure, we can! But remember, injective morphisms admit lifts for all possible commuting squares,
    and our new commuting square we defined with the composite does not cover all such maps
    from dom c to X1 that commute, it only covers those maps which factor through X to X1.
    So we can think of the failure of the bottom right morphism being an injective morphism
    as being measured by the map X to X1.
    Well, this is a pretty large error, it's intuitively 50 % of the entire map f! So how can
    we do better?
    Well take the map we want to study, X1 to Y, and repeat the same process. Well now
    X1 to X2 is a relative cell complex, and relative cell complex compose to relative cell complexes,
    so a map from X to X1 to X2 is a relative cell complex. We'd still like for this final map
    X2 to Y to be an injective morphism, and its failure to be one is this time measured
    by the map from X1 to X2. Inuitively, this error is a 25% of f, which is way better
    than our previous 50% error!
    The idea of the small object is making precise how far we can run with this process, of
    course the hope being that eventually we can achieve 0% error from being an injective
    morphism and have a factorization of f as a relative cell complex followed by an injective
    morphism.
    """
    def construct(self):
        d1 = TexMobject(r"""
            f: X
                \overset{\in C\text{cell}}{\longrightarrow}
            \hat{X}
                \overset{\in C\text{Inj}}{\longrightarrow}
            Y
        """).scale(.75)

        self.cycle(
            [d1],
            out=False
        )

        d2 = tikz("soa_d2", r"""
            $(C/f):= \left\{
            \begin{tikzcd}
                \text{dom}(c)
                    \arrow{r}\arrow{d}[left]{c\in C}
                    & X
                    \arrow{d}[right]{f} \\
                \text{cod}(c)
                    \arrow{r}
                    & Y
            \end{tikzcd}
            \right\}$
        """, fn)

        self.fade_replace(
            d1, d2
        )

        d3 = tikz("soa_d3", r"""
            \begin{tikzcd}
                \coprod_{c\in (C/f)} \text{dom}(c)
                    \arrow{r}\arrow{d}[left]{\coprod_{c\in (C/f)}c}
                    & X
                    \arrow{d} \\
                \coprod_{c\in (C/f)}\text{cod}(c)
                    \arrow{r}
                    & X_1
            \end{tikzcd}
        """, fn)

        self.fade_replace(
            d2, d3
        )

        d4 = tikz("soa_d4", r"""
            \begin{tikzcd}
                \coprod_{c\in (C/f)} \text{dom}(c)
                    \arrow{r}\arrow{d}[left]{\text{id}}
                    & X
                    \arrow{d} \\
                \coprod_{c\in (C/f)} \text{dom}(c)
                    \arrow{d}[left]{\coprod_{c\in (C/f)}c}
                    & X_1
                    \arrow{d} \\
                \coprod_{c\in (C/f)}\text{cod}(c)
                    \arrow{r}\arrow{ur}
                    & Y
            \end{tikzcd}
        """, fn).scale(1.5)

        self.fade_replace(
            d3, d4
        )

        d5 = tikz("soa_d5", r"""
            \begin{tikzcd}
                \coprod_{c\in (C/f)} \text{dom}(c)
                    \arrow{r}\arrow{d}[left]{\text{id}}
                    & X_1
                    \arrow{d} \\
                \coprod_{c\in (C/f)} \text{dom}(c)
                    \arrow{d}[left]{\coprod_{c\in (C/f)}c}
                    & X_2
                    \arrow{d} \\
                \coprod_{c\in (C/f)}\text{cod}(c)
                    \arrow{r}\arrow{ur}
                    & Y
            \end{tikzcd}
        """, fn).scale(1.5)

        self.fade_replace(
            d4, d5
        )
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class def216(Scene):
    """
    So a small object is what will enable us to achieve the intuitive 0% error. Here's
    a simple version that suffices for our purposes:
    We say that a category has small domains if there is an ordinal alpha such that
    for every c in the subclass of morphisms and every C relative cell complex given by
    a transfinite composition, every morphism from domain c to X hat factors through X beta
    to X hat of for order beta less than alpha. So back to our previous example, this would
    give us that since every morphism from domain c to X1 for example factors through
    X to X1, so we don't lose any generality by definining that middle morphism from domain c
    to X1 as the composition.
    """
    def construct(self):
        t = make_title("Definition", 2.16)

        self.title(t)

        d1 = TextMobject(r"""
            For $\mathcal{C}$ a category and $C\subset\text{Mor}(\mathcal{C})$ a subset 
            of its morphisms, we say that these morphisms have 
        """, "small domains", " ", r"""
            if there is an ordinal $\alpha$ such that for every $c\in C$ and for 
            every $C$-relative cell complex given by a transfinite composition
            $$ f:\to X_1\to X_2\to\cdots\to X_{\beta}\to\cdots\to \hat{X}$$
            every morphism $\text{dom}(c)\to \hat{X}$ factors through a stage 
            $X_\beta\to\hat{X}$ of order $\beta<\alpha$:
        """, alignment="").scale(.75).to_title(t)
        d1[1].set_color(BLUE)

        d2 = tikz("def216_d2", r"""
            \begin{tikzcd}
                & X_\beta
                    \arrow{d} \\
                \text{dom}(c)
                    \arrow{ur}\arrow{r}
                    & \hat{X}
            \end{tikzcd}
        """, fn).next_to(d1, direction=DOWN, buff=.25)

        self.cycle(
            [d1, d2], 
            out=False,
            successive=False
        )
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class prop217(Scene):
    """
    So with this requirement, our previous discussion proves that we can factor
    any morphism as a C relative cell complex followed by a 
    C injective morphism. What is this locally small category condition? It
    is saying that we can consider each of its hom sets as actual sets, so 
    basically that our chosen class of morphisms is small enough for things to
    work out like we want them to from a set theoretic perspective.
    """
    def construct(self):
        t = make_title("Proposition", 2.17)

        self.title(t)

        p1 = TextMobject(r"""
            Let $\mathcal{C}$ be a locally small category with all small colimits. 
            If a set $C\subset\text{Mor}(\mathcal{C})$ has small domains, then every 
            morphism $f:X\to Y$ in $\mathcal{C}$ factors as
            $$ F:X\overset{\in C\text{cell}}{\longrightarrow}
            \hat{X}\overset{\in C\text{Inj}}{\longrightarrow} Y.$$
        """, alignment="").scale(.75).to_title(t)

        self.cycle(
            [p1],
            out=False
        )
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

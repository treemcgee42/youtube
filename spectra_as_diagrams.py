# Date: 2/27/21
# Purpose: as topological diagrams section on nLab 1.1
# Notes:

from manimlib.imports import *
fn = "spectra_as_diagrams"


class def122(Scene):
    """
    So the whole notion of topologically enriched functors gives us a really nice way to 
    extend in a sense the model structure from Top cg, in this case to spectra. The idea 
    that makes this applicable here is that sequential spectra happen to be equivalent to 
    a category of topologically enriched functors, which already carries a projective model 
    structure on it. But we're getting ahead of ourselves. Let's start here. So here's a 
    topologically enriched subcategory. Its a subcategory of the enriched category pointed
    top cg over itself, and its objects are the standard n spheres, identified as the smash
    product of the standard circle. Intuitively, this is encoding the sequential part of 
    sequential spectra, as wel will see. Its hom spaces are as follows, and its composition
    is defined as you expect. This gives us a category of topologically enriched functors 
    on standard spheres with values in pointed top cg.
    """
    def construct(self):
        t = make_title("Definition", 1.22)
        self.title(t)

        d1 = TextMobject(r"""
            Write $$\iota: StdSpheres\longrightarrow Top_{cg}^{\ast /}$$ for the non-full 
            topologically enriched subcategory where:
            \begin{itemize}
                \item objects are the standard $n$-spheres $S^n$, for $n\in\mathbb{N}$, 
                    identified as the smash product powers $S^n:=(S^1)^{\wedge^n}$ of the 
                    standard circle
                \item hom-spaces are
                    \[
                        StdSpheres(S^n,S^{k+n}):=
                        \begin{cases}
                            \ast & for \ k<0 \\
                            S^k & otherwise
                        \end{cases}
                    \]
            \end{itemize}
        """, alignment="").scale(.75)

        self.cycle(
            [d1],
            out=False
        )

        d2 = TextMobject(r"""
            \begin{itemize}
                \item composition is induced from composition in $Top_{cg}^{\ast /}$ by 
                    regarding the hom-space $S^k$ above as its image in $Maps(S^n,S^{k+n})_\ast$ 
                    under the adjunct
                    $$ S^k\longrightarrow Maps(S^n, S^{k+n})_\ast $$
                    of the canonical isomorphism
                    $$S^k\wedge S^n\overset{\simeq}{\longrightarrow}S^{k+n}.$$
            \end{itemize}
            This induces the category
            $$[StdSpheres, Top_{cg}^{\ast /}]$$
            of topologically enriched functors on $StdSpheres$ with values in $Top_{cg}^{\ast /}$.
        """, alignment="").scale(.75).to_edge(DOWN)

        self.fade_replace(
            d1, d2
        )
        self.clear()

class prop123(Scene):
    """
    So this is the punchline I was alluding to- there is an equivalence of categories
    from the category of topologically enriched functors to the category of topological
    sequential spectra. So it sends an enriched functor X to the nth component space of
    a sequential spectrum. This sequential spectrum has structure maps like this.
    So this is a pretty amazing result, and I want to admit that it took me a couple weeks
    to understand why this was the case.
    Ok, first lets consider equivalence on classes of objects, and then we will show the 
    equivalence on morphisms. The idea is given by this diagram. The idea is, a functor already
    fixes our component spaces, i.e. it is a choice of space for each Sn. It is also a chocie
    of morphisms between pairs of component spaces. The only ambiguity is that spectra only
    remember maps between consectuive component spaces, i.e. structure maps. So theoretically,
    we could have two functors that even though the send morphisms between consecutive spheres
    to the same thing, they don't send morphisms between nonconsecutive spheres to the same thing,
    so it could be that even though they aren't the same functor, they are sent to the same 
    spectrum, which would obviously break bijectivity. But as this diagram shows, maps between
    nonconsecutive spheres, i.e. the bottom row, completely fix maps between consecutive spheres.
    So we have a bijection between classes of objects, so now let's see about morphisms.
    We want to show there is a bijection between natural transformations of functors on 
    Standard spheres corresponds to a unique homomorphism between their corresponding spectra,
    and vice versa for a bijection.
    So a natural transformation between two functors X and Y on standard spheres is one
    such that for each s in S1, which is the hom space between Sn and Sn+1, the
    square here commutes. So a choice s in S1 is a choice of map from Sn to Sn+1. So the
    left vertical map for example is a map from S1 smash X sn to maps from X sn to X sn+1
    to X sn+1. By the smash hom adjunction, this factors like this. This exhibits a 
    homomorphism of sequential spectra. Conversely, a homomorphism of sequential spectra is
    given like this, and we run the argument backwards to get a natural transformation between
    functors on standard spheres. And we are done showing the bijection.
    """
    def construct(self):
        t = make_title("Proposition", 1.23)
        self.title(t)

        p1 = TextMobject(r"""
            There is an equivalence of categories
            $$ (-)^{seq}:[StdSpheres, Top_{cg}^{\ast /}]\overset{\simeq}{\longrightarrow}
            SeqSpec(Top_{cg})$$
            which is given on objects by sending $X\in [StdSpheres, Top_{cg}^{\ast /}]$ to 
            the sequential prespectrum $X^{seq}$ with components
            $$ X_n^{seq}:=X(S^n)$$
            and with structure maps
            $$\dfrac{S^1\wedge X_n^{seq}\overset{\sigma_n}{\longrightarrow}X_{n+1}^{seq}}
            {S^1\longrightarrow Maps(X_n^{seq}, X_{n+1}^{seq})_\ast}.$$
        """, alignment="").scale(.75).to_edge(DOWN)

        self.cycle(
            [p1]
        )

        p2 = tikz("prop123_p2", r"""
            \begin{tikzcd}
                S^1\wedge S^1
                    \arrow{d}[left]{\simeq}\arrow{r}[above]{=}
                    & StdSpheres(S^n,S^{n+1})\wedge StdSpheres(S^{n+1}, S^{n+2})
                    \arrow{d}[left]{\simeq}[right]{\circ} \\
                S^2
                    \arrow{r}[above]{=}
                    & StdSpheres(S^n, S^{n+2})
            \end{tikzcd}
        """, fn)

        self.cycle(
            [p2]
        )

        p3 = tikz("prop123_p3", r"""
            \begin{tikzcd}
                X(S^n)
                    \arrow{r}[above]{f_n}\arrow{d}[left]{X_{S^n,S^{n+1}}(s)}
                    & Y(X^n)
                    \arrow{d}[right]{Y_{S^n, S^{n+1}}(s)} \\
                X(S^{n+1})
                    \arrow{r}[below]{f_{n+1}}
                    & Y(S^{n+1})
            \end{tikzcd}
        """, fn).shift(3*LEFT)

        p4 = tikz("prop123_p4", r"""
            \begin{tikzcd}
                X(S^n)
                    \arrow{r}[above]{f_n}\arrow{d}[left]{(s, id)}
                    & Y(S^n)
                    \arrow{d}[right]{(s, id)} \\
                S^1\wedge X(S^n)
                    \arrow{r}[below]{id\times f_n}\arrow{d}[left]{\sigma_n^X}
                    & S^1\wedge Y(S^n)
                    \arrow{d}[right]{\sigma_n^Y} \\
                X(S^{n+1})
                    \arrow{r}[below]{f_{n+1}}
                    & Y(S^{n+1})
            \end{tikzcd}
        """, fn).scale(1.5).shift(3*RIGHT)

        self.cycle(
            [p3, p4], 
            out=False
        )
        self.clear()

class remark124(Scene):
    """
    So earlier in this series when we defined tensorings and powerings of sequential spectra,
    you may have wondered why we used that language, which comes from the concepts of tensorings
    and powerings in the context of topologically enriched functors. And the reason is that the
    definitions above are indeed the general notion in the category of functors on standard spheres,
    now that we've shown the equivalence of categories.
    """
    def construct(self):
        t = make_title("Remark", 1.24)
        self.title(t)

        self.clear()

class prop125(Scene):
    """
    Now that we've established this equivalence of categories, we immediately get a bunch
    of things. This first of which is that we now have that the category of sequential 
    spectra has all limits and colimits, and that they are computed objectwise.
    """
    def construct(self):
        t = make_title("Proposition", 1.25)
        self.title(t)

        p1 = TextMobject(r"""
            The category $SeqSpec(Top_{cg})$ of sequential spectra has all limits and colimits, 
            and they are computed objectwise: given
            $$ X_\bullet:I\longrightarrow SeqSpec(Top_{cg})$$
            a diagram of sequential spectra, then:
            \begin{enumerate}
                \item its colimiting spectrum has component spaces the colimit of the 
                    component spaces formed in $Top_{cg}$:
                    $$ (\underset{\longrightarrow i}{\lim}X(i))_n\simeq
                    \underset{\longrightarrow i}{\lim}X(i)_n $$
                \item its limiting spectrum has component spaces the limit of the component 
                    spaces formed in $Top_{cg}$:
                    $$ (\underset{\longleftarrow i}{\lim}X(i))_n\simeq
                    \underset{\longleftarrow i}{\lim}X(i)_n $$
            \end{enumerate}
        """, alignment="").scale(.65).to_edge(DOWN)

        self.cycle(
            [p1],
            out=False
        )

        p2 = TextMobject(r"""
            \begin{enumerate}
                \item the colimiting spectrum has structure maps given by
                    $$ S^1\wedge (\underset{\longrightarrow i}{\lim}X(i)_n)
                    \simeq \underset{\longrightarrow i}{\lim}(S^1\wedge X(i)_n)
                    \overset{\underset{\longrightarrow i}{\lim}\sigma_n^{X(i)}}{\longrightarrow}
                    \underset{\longrightarrow i}{\lim}X(i)_{n+1} $$
                \item the limiting spectrum has adjunct structure maps given by
                    $$ 
                    \underset{\longleftarrow i}{\lim}X(i)_n
                        \overset{\underset{\longleftarrow i}{\lim}\tilde{\sigma}^{X(i)}}
                        {\longrightarrow}
                    \underset{\longleftarrow i}{\lim}Maps(S^1, X(i)_n)_\ast
                        \simeq
                    Maps(S^1, \underset{\longleftarrow i}{\lim}X(i)_n)_\ast
                    $$
            \end{enumerate}
        """, alignment="").scale(.75)

        self.fade_replace(
            p1, p2
        )
        self.clear()

class ex126(Scene):
    """
    The initial and terminal object in the category of sequential
    spectra agree, and they are given by the spectrum constant on a point.
    """
    def construct(self):
        t = make_title("Example", 1.26)
        self.title(t)

        e1 = TextMobject(r"""
            The initial object and terminal object in $SeqSpec(Top_{cg})$ agree and are 
            both given by the spectum constant on the point, which is also the suspension 
            spectrum $\Sigma^\infty \ast$. We will denote this spectrum $\ast$ or $0$ (
            since it is hence a zero object):
            \begin{gather*}
                \ast_n = \ast \\
                S^1\wedge \ast_n\simeq \ast \overset{\simeq}{\to}\ast
            \end{gather*}
        """, alignment="").scale(.75)

        self.cycle(
            [e1],
            out=False
        )
        self.clear()

class ex127(Scene):
    """
    Proposition 125 also tells us how to compute the coproduct of spectra; it is the component
    wise wedge sum and structure maps given as follows.
    """
    def construct(self):
        t = make_title("Example", 1.27)
        self.title(t)

        e1 = TextMobject(r"""
            The coproduct of spectra $X,Y\in SeqSpec(Top_{cg})$, called the
        """, " wedge sum of spectra ", r"""
            $$X\vee Y:= X\sqcup Y$$
            is componentwise the wedge sum of pointed topological spaces
            $$(X\vee Y)_n= X_n\vee Y_n$$
            with structure maps
            $$
            \sigma_n^{X\vee Y}: S^1\wedge (X\vee Y)
                \simeq
            S^1\wedge X\vee S^1\wedge Y
                \overset{(\sigma_n^X,\sigma_n^Y)}{\longrightarrow}
            X_{n+1}\vee Y_{n+1}.
            $$
        """, alignment="").scale(.75)
        e1[1].set_color(BLUE)

        self.cycle(
            [e1],
            out=False
        )
        self.clear()

class ex128(Scene):
    """
    Another important example that will become useful with regards to homotopy as you might
    imagine is what is called the standard cylinder object. It is the smash tensoring of the
    spectrum with the standard interval with a freely adjoined basepoint. Indeed, this factors
    the codiagonal as we'd expect from a standard cylinder object.
    """
    def construct(self):
        t = make_title("Example", 1.28)
        self.title(t)

        e1 = TextMobject(r"""
            For $X\in SeqSpec(Top_{cg})$, its
        """, " standard cylinder spectrum ", r"""
            is the smash tensoring $X\wedge (I_+)$. It has component spaces the 
            standard reduced cylinders
            $$ (X\wedge (I_+))_n = X_n\wedge I_+.$$
            The factoring
            $$\nabla_{S^0}:S^0\vee S^0\longrightarrow I_+\longrightarrow S^0$$
            of the codiagonal gives a factoring of the codiagonal of $X$ through the 
            standard cylinder spectrum
            $$
            \nabla_X:X\vee X
                \overset{X\wedge (S^0\vee S^0\to I_+)}{\longrightarrow}
            X\wedge (I_+)
                \overset{X\wedge (I_+\to S^0)}{\longrightarrow}
            X
            $$
        """, alignment="").scale(.75)
        e1[1].set_color(BLUE)

        self.cycle(
            [e1],
            out=False
        )
        self.clear()

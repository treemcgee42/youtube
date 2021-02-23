# Date: 2/22/21
# Purpose: prelude section 3 nLab
# Notes:

from manimlib.imports import *
fn = "model_top"


class def31(Scene):
    """
    So first of all lets see the model structure on Top itself. Its morphisms
    are of course continuous functions. We claim that the model structure is as follows:
    weak equivalences are weak homotopy equivalences, fibrations are Serre fibrations,
    and cofibrations are retracts of relative cell complexes. We will write these
    as follows, and call them classical. Once we prove this, we will be able to easily
    have these related model structures, the model structure on pointed topological
    spaces, the model structure on compactly generated and compactly generated pointed
    topological spaces, and even the model structures on some topologically enriched 
    functors.
    """
    def construct(self):
        t = make_title("Definition", 3.1)
        self.title(t)

        d1 = TextMobject(r"""
            Say that a continuous function, hence a morphism in Top, is
            \begin{itemize}
                \item a \textbf{classical weak equivalence} if it is a weak homotopy 
                    equivalence
                \item a \textbf{classical fibration} if it is a Serre fibration
                \item a \textbf{classical cofibration} if it is a retract of a relative 
                    cell complex
            \end{itemize}
            Write
            $$ W_\text{cl}, \ \text{Fib}_\text{cl}, \ \text{Cof}_\text{cl} \
                \subset \ \text{Mor}(\text{Top}) $$
            for these classes of morphisms, respectively.
        """, alignment="").scale(.75)

        self.cycle(
            [d1],
            out=False
        )
        self.clear()

class prop32(Scene):
    """
    The first thing we want to show is that the classical weak equivalences, i.e. weak
    homotopy equivalences, satisfy two out of three. But isomorphisms obviously do, in
    particular those of homotopy groups, so this follows immediately.
    """
    def construct(self):
        t = make_title("Proposition", 3.2)
        self.title(t)

        p1 = TextMobject(r"""
            The classical weak equivalences satisfy two-out-of-three.
        """, alignment="").scale(.75)

        self.cycle(
            [p1],
            out=False
        )
        self.clear()

class lemma33(Scene):
    """
    Moving on to the factorization axioms, lets check that every morphism in Top
    factors as a classical cofibration followed by an acyclic classical fibration.
    Recall our technical lemma, that the image of a compact set into a relative cell
    complex is completely attained at some finite stage. Well this shows that I top,
    the topological generating cofibrations which are the inclusion of the n-1 sphere
    into the n disk, have small domains, so f has a small domain as well.
    Using the small object argument, we can therefore factor f as an I top relative
    cell complex followed by an Itop injective morphism. Well we showed that 
    I top injective morphisms are precisely acyclic Serre fibrations, so we have a 
    factorization as a classical cofibration followed by a classical acycic fibration
    and we are done.
    """
    def construct(self):
        t = make_title("Lemma", 3.3)
        self.title(t)

        l1 = TextMobject(r"""
            Every morphism $fX\to Y$ in Top factors as a classical cofibration followed 
            by an acyclic classical fibration:
            $$ f: X\overset{\in\text{Cof}_\text{cl}}{\longrightarrow}
            \hat{X}\overset{W_\text{cl}\cap\text{Fib}_\text{cl}}{\longrightarrow} Y$$
        """, alignment="").scale(.75).to_title(t)

        l2 = TexMobject(r"""
            f:X\overset{\in\text{Cof}_\text{cl}}{\longrightarrow}\hat{X}
            \overset{\in I_\text{Top}\text{Inj}}{\longrightarrow} Y
        """).scale(.75).shift(2*DOWN)

        self.cycle(
            [l1, l2],
            out=False
        )
        self.clear()

class lemma34(Scene):
    """
    Dually, let's show we can factor any morphism as a classical acyclic cofibration
    followed by a classical fibration. Using the same technical lemma, and since n disks
    are compact, we have that f has again small domains. So we can factor this as a 
    Jtop relative cell complex followed by a Jtop injective morphism. So Jtop was our
    classical topological generating cofibrations if you recall. Well then we showed
    that Jtop injective morphisms were Serre fibrations. Finally, we recall that Jtop
    cell complexes are I top relative cell complexes, and weak homotopy equivalences, so
    we do have a classical acyclic cofibration followed by a classical fibration.
    """
    def construct(self):
        t = make_title("Lemma", 3.4)
        self.title(t)

        l1 = TextMobject(r"""
            Every morphism $fX\to Y$ in Top factors as a acyclic classical cofibration followed 
            by an classical fibration:
            $$ f: X\overset{\in W_\text{cl}\cap\text{Cof}_\text{cl}}{\longrightarrow}
            \hat{X}\overset{\text{Fib}_\text{cl}}{\longrightarrow} Y$$
        """, alignment="").scale(.75).to_title(t)

        l2 = TexMobject(r"""
            f:X\overset{\in J_\text{Top}\text{Cell}}{\longrightarrow}\hat{X}
            \overset{\in J_\text{Top}\text{Inj}}{\longrightarrow} Y
        """).scale(.75).shift(2*DOWN)

        self.cycle(
            [l1, l2],
            out=False
        )
        self.clear()

class lemma35(Scene):
    """
    Here's another factorization related result, if we have this commuting square,
    then we get a lift as soon as one of the two is also a classical weak equivalence.
    So one direction is something we already showed, acyclic fibrations are precisely
    those that lift against generating cofibrations, and we showed in earlier corrolary
    211 that hence it lifts against all of its retracts. So what if we have a classical
    weak equivalence on the left? Well we talked just showed that we can factor it
    as a Jtop relative cell complex followed by a fibration i.e. a j top injective
    morphism. Again, Jtop relative cell complex are weak equivalences, so since the
    entire map is by assumption a weak equivalence we have that the second map is an
    acyclic classical fibration by two out of three. Hence it lifts against the overall
    map g which is in particular a cofibration by what we just showed. Another way to phrase
    it is that g has the right lifting property against the second map, and so by the
    retract argument this gives g as a retract of the first morphism, i.e. a retract of a
    jtop relative cell complex. Well, by definition f which is a serre fibration lifts
    against jtop, and hence against its retracts, and we are done.
    """
    def construct(self):
        t = make_title("Lemma", 3.5)
        self.title(t)

        l1 = TextMobject(r"""
            Every commuting square in Top with the left morphism a classical cofibration 
            and the right morphism a fibration admits a lift as soon as one of the two 
            is also a classical weak equivalence:
        """, alignment="").scale(.75).to_title(t)

        l2 = tikz("lemma35_l2", r"""
            \begin{tikzcd}
                {}
                    \arrow{r}\arrow{d}[left]{g\in\text{Cof}_\text{cl}}
                    & {}
                    \arrow{d}[right]{f\in\text{Fib}_\text{cl}} \\
                {}
                    \arrow{r}
                    & {}
            \end{tikzcd}
        """, fn).shift(.5*DOWN)

        self.cycle(
            [l1, l2],
            out=False,
            successive=False
        )

        l3 = TexMobject(r"""
            g:\overset{\in J_\text{Top}\text{Cell}}{\longrightarrow}\quad
            \overset{\in\text{Fib}_\text{cl}}{\longrightarrow}
        """).scale(.75).shift(2.5*DOWN)

        self.cycle(
            [l3],
            out=False
        )
        self.clear()

class prop36(Scene):
    """
    So this should make the final factorization axiom easier to prove,
    that we have that these pairs are weak factorization systems. We already
    showed that they satisfy the lifting properties, but its not clear that
    every map that lifts is contained in these pairs. We did already show
    way back that this is the case for classical fibrations, by definition,
    and for classical acyclic fibrations. So it remains to check for classical
    cofibrations and acyclic cofibrations, i.e. are these pricesly the classes
    with the right lifting property against classicaly acyclic fibrations and
    classical fibrations respectively.
    So let f be a map with the right lifting property against classical fibrations,
    i.e. an itop injective projective morphism. It suffices to show that
    f is a retract of a relative cell complex, as then it would be a cofibration.
    So we can apply the small object argument to factor f as an Itop relative
    cell complex followed by an i top injective morphism. Well then f by assumption
    is in itop inj proj so has the right lifting property against the second map,
    so by the retract argument is a retract of the first, i.e. a retract of an itop
    relative cell complex, so it is a classical cofibration as desired.
    Finally, consider the case for acyclic cofibrations. So pick an f in Jtop
    inj proj. Small object argument tells us that its a retract of a Jtop cell complex
    using the process we did just now. But we showed in the last two lemmas that a
    Jtop cell complex is an Itop cell complex and a weak homotopy equivalence.
    A retract of a Jtop cell complex is thus a retract of an itop cell complex 
    ie a cofibration and also a retract of a weak homotopy equivalence, i.e. still
    a weak homotopy equivalence. Hence f is an acyclic cofibration and we are done.
    """
    def construct(self):
        t = make_title("Proposition", 3.6)
        self.title(t)

        p1 = TextMobject(r"""
            The systems $(\text{Cof}_\text{cl},W_\text{cl}\cap\text{Fib}_\text{cl})$ 
            and $(W_\text{cl}\cap\text{Cof}_\text{cl},\text{Fib}_\text{cl})$ are 
            weak factorizations systems.
        """, alignment="").scale(.75).shift(1.5*UP)

        p2 = TexMobject(r"""
            f:X
                \overset{I_\text{Top}\text{Cell}}{\longrightarrow}\hat{Y}
                \overset{\in I_\text{Top}\text{Inj}}{\longrightarrow} Y
        """).scale(.75).shift(1*DOWN)

        self.cycle(
            [p1, p2],
            out=False
        )
        self.clear()

class thm37(Scene):
    """
    So all of that work gives us this classical model structure on topological
    spaces, or the Serre-Quillen model structure. Nice properties here include
    that every object is fibrant, and the cofibrant objects are retracts of cell
    complexes.
    """
    def construct(self):
        t = make_title("Theorem", 3.7)
        self.title(t)

        t1 = TextMobject(r"""
            The classes of morphisms in $\text{Mor}(\text{Top})$
            \begin{itemize}
                \item $W_\text{cl}$ -weak homotopy equivalences
                \item $\text{Fib}_\text{cl}$ -Serre fibrations
                \item $\text{Cof}_\text{cl}$ -retracts of relative cell complexes
            \end{itemize}
            define a model category structure, $\text{Top}_\text{Quillen}$, the 
        """, "classical model structure on topological spaces", " or ",\
        "Serre-Quillen model structure", ".", alignment="").scale(.75)
        t1[1].set_color(BLUE)
        t1[-2].set_color(BLUE)

        self.cycle(
            [t1]
        )

        t2 = TextMobject(r"""
            In particular
            \begin{enumerate}
                \item every object in $\text{Top}_\text{Quillen}$ is fibrant
                \item the cofibrant objects in $\text{Top}_\text{Quillen}$ are the 
                retracts of cell complexes
            \end{enumerate}
        """, alignment="").scale(.75)

        self.cycle(
            [t2],
            out=False
        )
        self.clear()

class cor38(Scene):
    """
    So we have the classical whitehead theorem, which is a specialization of the
    whitehead theorem in model categories from before.
    """
    def construct(self):
        t = make_title("Corollary", 3.8)
        self.title(t)

        c1 = TextMobject(r"""
            Every weak homotopy equivalence between topological spaces that are 
            homeomorphic to a retract of a cell complex, in particular to a CW-complex 
            is a homotopy equivalence.
        """, alignment="").scale(.75)

        self.cycle(
            [c1],
            out=False
        )
        self.clear()

class def39(Scene):
    """
    What's the deal with the generating part of generating cofibrations and acyclic
    cofibrations? Well if you observe, because of certain proeprties we proved
    in topoogical homotopy theore, we got the entire model structure just from Itop
    and Jtop. This is a meature of a model category called being cofibrantly
    generated. This means that we have two subsets of morphisms, I and J,
    that both have small domains and such that the cofibrations of the 
    category are precisely the retracts of I relative cell complexes, and the acyclic
    cofibrations are precisely the retracts of J relative cell complexes.
    """
    def construct(self):
        t = make_title("Definition", 3.9)
        self.title(t)

        d1 = TextMobject(r"""
            A model category $\mathcal{C}$ is called 
        """, "cofibrantly generated", " ", r"""
            if there exists two subsets
            $$ I, J\subset\text{Mor}(\mathcal{C})$$
            of its class of morphisms, such that
            \begin{enumerate}
                \item $I$ and $J$ have small domains
                \item the (acyclic) cofibrations of $\mathcal{C}$ are precisely the retracts 
                    of $I$-relative cell complexes ($J$-relative cell complexes)
            \end{enumerate}
        """, alignment="").scale(.75)
        d1[1].set_color(BLUE)

        self.cycle(
            [d1],
            out=False
        )
        self.clear()

class prop310(Scene):
    """
    This means that we can efficiently express all of our classes as just
    injective and projective morphisms, like cofibrations are i injective projective
    morphisms, etc.
    We'll prove the first, which will imply the second, and the third and fourth are
    analagous. So clearly I is atleast a subset of I injective projective
    morphisms and then so too are its retracts. For the converse inclusion, consider 
    a map f in i injective projective. Well, by the small object argument we can 
    factor it as an I relative cell complex followed by an I injective morphism.
    Well then it has the right lifting property against the second morphism in that
    composition and so by the retract argument is a retract of the first, i.e. an I
    relative cell complex and hence a cofibration.
    """
    def construct(self):
        t = make_title("Proposition", "3.10")
        self.title(t)

        p1 = TextMobject(r"""
            For $\mathcal{C}$ a cofibrantly generated model category, then its 
            classes $W$, Fib, Cof of are equivalently expressed as injective or 
            projective morphisms:
            \begin{enumerate}
                \item $\text{Cof}= (I\text{Inj})\text{Proj}$
                \item $W\cap\text{Fib}=I\text{Inj}$
                \item $W\cap\text{Cof} = (J\text{Inj})\text{Proj}$
                \item $\text{Fib} = J\text{Inj}$
            \end{enumerate}
        """, alignment="").scale(.75)

        self.cycle(
            [p1],
            out=False
        )
        self.clear()

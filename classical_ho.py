# Date: 2/23/21
# Purpose: classical homotopy category section nLab
# Notes:

from manimlib.imports import *
fn = "classical_ho"


class def311(Scene):
    """
    Now that we have the classical model structure on topological spaces, we can talk
    about its homotopy category, the Serre-Quillen classical homotopy category, which
    we write as Ho Top.
    """
    def construct(self):
        t = make_title("Definition", 3.11)
        self.title(t)

        d1 = TextMobject("The Serre-Quillen ", "classical homotopy category", " ", r"""
            is the homotopy category of the classical model structure on topological 
            spaces:
            $$\text{Ho}(\text{Top}):=\text{Ho}(\text{Top}_\text{Quillen})$$
        """, alignment="").scale(.75)
        d1[1].set_color(BLUE)

        self.cycle(
            [d1],
            out=False
        )
        self.clear()

class rmk312(Scene):
    """
    So we have this equivalence, coming from in particular the observation that
    every object in Top is a fibrant object and retracts of cell complexes are
    cofibrant. This doesn't lose too much information however, as 
     every topological space is weakly equivalent to a retract of a cell
    complex. CW approximation tells us that there is such a CW complex as well.
    So indeed we can think of this as equivalent to CW complexes modulo homotopy classes.
    The universal property and equivalence between the homotopy category and the 
    localization at weak equivalences gives us a bijection up to natural isomorphism
    between functors out of Top CW which agree on homotopy equivalent maps and functors
    out of all of top which sends weak homotopy equivalences to isomorphisms.
    Indeed, this statement will help us show that the two different axiomatizations of
    generalized Eilenberg Steenrod cohomology theories are equivalent.
    """
    def construct(self):
        t = make_title("Remark", 3.12)
        self.title(t)

        r1 = TextMobject(r"""
        \begin{align*}
            \text{Ho}(\text{Top}_\text{Quillen})\simeq & (\text{Top}_\text{Retract(Cell)})/\sim\\
            \simeq & (\text{Top}_\text{CW})/\sim
        \end{align*}
        """).scale(.75).shift(1.5*UP)

        r2 = TextMobject(r"""
            $$\text{Ho}(\text{Top}_\text{Quillen})\simeq\text{Top}[W_\text{cl}^{-1}]$$
            \begin{enumerate}
                \item functors out of $\text{Top}_\text{CW}$ which agree on homotopy-equivalent 
                    maps
                \item functors out of all of Top which send weak homotopy equivalences to 
                    isomorphisms.
            \end{enumerate}
        """, alignment="").scale(.75).shift(1*DOWN)

        self.cycle(
            [r1, r2],
            out=False
        )
        self.clear()

class prop313(Scene):
    """
    So obviously we'd like our standard topological cylinder X cross I to be a cylinder
    object in the abstract sense, so let's see a sketch of the proof.
    So start with a presentation of X as a CW complex and proceed by induction on
    the cell dimension. So the cylinder object over X0 is a cell complex, so assume
    for n in N that Xn cross I has the structure of a CW complex of dimension n+1.
    We want to show that Xn+1 cross I is a CW complex. So for each Xn+1 cell, attach it twice to
    each end of Xn times I, obtaining a hollow cylinder over each n+1 cell.
    Filling them in with the n+1 sphere gives us the cylinder and completes induction,
    so X times I is a CW complex.
    Indeed this construction gives us that X disjoint union X into X times I is a relative
    cell complex, and clearly X cross I to X is a weak homotopy equivalence.
    """
    def construct(self):
        t = make_title("Proposition", 3.13)
        self.title(t)

        p1 = TexMobject(r"""
            X\sqcup X
                \overset{(i_0,i_1)}{\longrightarrow}
            X\times I
                \longrightarrow
            X
        """).scale(.75)

        self.cycle(
            [p1],
            out=False
        )
        self.clear()

class prop314(Scene):
    """
    Likewise, we'd like a statement for the standard topological path space object.
    Whereas last time we required X to be a CW complex, we now let X be any topological
    space.
    Ok, to see this we first want to show that the first map X to XI is a weak equivalence,
    and the second is a fibration. So lets see that the first map, the constant map on X,
    is a weak equivalence. We can in fact show an even stronger assertion that these two are
    homotopy equivalent. So for that let the inverse up to homotopy be one of the components
    of the second map. Then this composite is equal to the identity. The composite the
    other way around is given by rescaling the paths, so we have a path in the path space
    and we continuously shrink it more and more, which we can do since no two points
    on the path are to coincide.
    So it remains to show that XI to X cross X is a fibration, so we have our lifting 
    diagram, and we want there to be a lift from Dn cross I to XI. Well by the
    cartesian product mapping space adjunction with respect to I (which exists because
    I is in particular compact) we can rewrite this in this way. This was confusing to me, 
    so here's what I think is going on. So the top morphism under the adjunction is Dn cross I
    to X. The reason we have a disjoint union is so our choice of i0 or i1 originally doesn't
    matter. In this square, there is actually a hidden morphism from X to X
    cross X. The bottom map is the restriction of the map from Dn cross I to X cross X.
    So here's the thing, a lift in this diagram would imply that we could backtrack
    the previous square and construct a lift, i.e. a lift here implies a lift in the original
    diagram. Ok, so the information of this square is contained in the morphism out
    of the pushout, and now consider the following diagram, where the top map
    is the morphism out of the pushout. If there was a lift here, by adjunction that would
    be a map from Dn cross I to XI, which is what we were looking for initially, and furthermore
    it would agree with the map out of the pushout, i.e. it would agree with the previous
    commuting square, and hence imply a lift in the original case. The left vertical
    here is a homeomoprhism, and we are done.
    """
    def construct(self):
        t = make_title("Proposition", 3.14)
        self.title(t)

        p1 = TexMobject(r"""
            X\longrightarrow X^I
                \overset{(X^{\delta_0}, X^{\delta_1})}{\longrightarrow}
            X\times X
        """).scale(.75).shift(2*UP)

        p2 = tikz("prop314_p2", r"""
            \begin{tikzcd}
                D^n
                    \arrow{r}\arrow{d}[left]{i_0}
                    & X^I
                    \arrow{d} \\
                D^n\times I
                    \arrow{r}
                    & X\times X
            \end{tikzcd}
        """, fn).to_edge(LEFT, buff=.5).scale(.9)

        p3 = tikz("prop314_p3", r"""
            \begin{tikzcd}
                D^n\times I
                    \arrow{r}\arrow{d}
                    & X
                    \arrow{d} \\
                D^n\times I
                    \arrow{r}
                    & X\times X
            \end{tikzcd}
        """, fn).scale(.9).next_to(p2, direction=DOWN, buff=.5)

        p4 = tikz("prop314_p4", r"""
            \begin{tikzcd}
                D^n\sqcup D^n
                    \arrow{r}\arrow{d}
                    & (D^n\times I)\sqcup (D^n\times I)
                    \arrow{d} \\
                D^n\times I
                    \arrow{r}
                    & X
            \end{tikzcd}
        """, fn).to_edge(RIGHT, buff=1).scale(.9)

        p5 = tikz("prop314_p5", r"""
            \begin{tikzcd}
                D^n\times I\underset{D^n\sqcup D^n}{\sqcup}((D^n\times I)\sqcup(D^n\times I))
                    \arrow{r}\arrow{d}
                    & X
                    \arrow{d} \\
                (D^n\times I)\times I
                    \arrow{r}
                    & \ast
            \end{tikzcd}
        """, fn).scale(.9).next_to(p4, direction=DOWN, buff=.5).shift(1*LEFT)

        self.cycle(
            [p1, p2, p3, p4, p5],
            out=False
        )
        self.clear()

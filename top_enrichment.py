# Date: 2/24/21
# Purpose: topological enrichment section nLab
# Notes:

from manimlib.imports import *
fn = "top_enrichment"


class def355(Scene):
    """
    So given two maps in Top cg, the pushout product is surprisingly well-named:
    it is between two maps, and we write it with a square, and it is the universal
    morphism induced by the following pushout, so the bottom map here.
    """
    def construct(self):
        t = make_title("Definition", 3.55)
        self.title(t)

        d1 = TextMobject(r"""
            Let $i_1:X_1\to Y_1$ and $i_2:X_2\to Y_2$ be morphisms in $\text{Top}_\text{cg}$.
            Their 
        """, "pushout product ", r"""
            \[i_1\Box i_2:= ((id, i_2), (i_1,id))\]
            is the universal morphism in the following diagram:
        """, alignment="").scale(.75).shift(1.75*UP)
        d1[1].set_color(BLUE)

        d2 = tikz("def355_d2", r"""
            \begin{tikzcd}
                &  X_1\times X_2 
                    \arrow{dl}[left,yshift=.5em]{(i_1,id)}\arrow{dr}[right,yshift=.5em]{(id,i_2)}
                    & \\
                Y_1\times X_2
                    \arrow{dr}
                    & (po)
                    & X_1\times Y_2
                    \arrow{dl} \\
                & (Y_1\times X_2)\underset{X_1\times X_2}{\sqcup}(X_1\times Y_2)
                    \arrow{d}[right]{((id,i_2),(i_1,id))}
                    & \\
                & Y_1\times Y_2 &
            \end{tikzcd}
        """, fn).scale(1.5).next_to(d1, direction=DOWN, buff=.5)

        self.cycle(
            [d1, d2],
            out=False,
            successive=False
        )
        self.clear()

class ex356(Scene):
    """
    A simple example is two inclusions. Then the pushout product is the following
    inclusion. So this is a good example, consider the inclusion of a point into
    the interval pushout product with itself. Then by the above formula the pushout
    product is 0 cross the interval which is 0 union the interval again included into
    I cross I which is a square. But since we pushed out, the single points on each
    copy of the interval are identified, and hence this can be thought of as the
    inclusion of two adjacent edges of a square into the square.
    """
    def construct(self):
        t = make_title("Example", 3.56)
        self.title(t)

        e1 = TextMobject(r"""
            If $i_1:X_1\hookrightarrow Y_1$ and $i_2:X_2\hookrightarrow Y_2$ are inclusions, 
            then their pushout product $i_1\Box i_2$ is the inclusion
            \[
            (X_1\times Y_2\cup Y_1\times X_2)\hookrightarrow Y_1\times Y_2.
            \]
            For instance
            \[
                (\{0\}\hookrightarrow I)\Box (\{0\}\hookrightarrow I)
            \]
            is the inclusion of two adjacent edges of a square into the square.
        """, alignment="").scale(.75)

        self.cycle(
            [e1],
            out=False
        )
        self.clear()

class ex357(Scene):
    """
    Here's another example. The pushout product with an initial morphism is the
    ordinary Cartesian product functor. And we see this from this diagram.
    """
    def construct(self):
        t = make_title("Example", 3.57)
        self.title(t)

        e1 = TextMobject(r"""
            The pushout product with an initial morphism is just the ordinary 
            Cartesian product functor
            \[ 
            (\emptyset\to X)\Box (-)\simeq X\times (-),
            \] i.e.
            \[
            (\emptyset \to X)\Box (A\overset{f}{\to})\simeq (X\times A
            \overset{X\times f}{\longrightarrow}X\times B).
            \]
        """, alignment="").scale(.75)

        e2 = tikz("ex357_e2", r"""
            \begin{tikzcd}
                &  \emptyset\times A
                    \arrow{dl}\arrow{dr}[right,yshift=.5em]{\simeq}
                    & \\
                X\times A
                    \arrow{dr}[left,yshift=-.5em]{\simeq}
                    & (po)
                    & \emptyset\times B
                    \arrow{dl} \\
                & X\times A
                    \arrow{d}[right]{((id,f),\exists !)}
                    & \\
                & X\times B &
            \end{tikzcd}
        """, fn).scale(2)

        self.cycle(
            [e1]
        )
        self.cycle(
            [e2],
            out=False
        )
        self.clear()

class ex358(Scene):
    """
    Here's a really powerful example. This reveals a nice algebraic structure in the
    cofibrations with respect to pushout products. Just be careful that we don't say 
    anything about two generating acyclic cofibrations, just the pushout product of a
    generating cofibration with an acyclic generating cofibration. Let's prove this.
    Lets consider n disks as interval cubes and n-1 spheres as the boundaries of those
    cubes. Ok, first notice these two things, drawn pictorally.
    The first one, well lets think about it.
    Both inclusions are S0 to D1, so be a previous example, our domain should be
    S0 times D1 union S0 union D1. S0 is the boundary of the interval, hence two disjoint
    points, hence s0 times D1 is two copies of the interval, and we see that the
    codomain is then a square. Similarly, for i1 pushout product j0, our domain
    is S0 cross D1 union D0 cross D1, so we have two lines union one and we get something
    homeomorphic to a square. This can be generalized easily, so look to the nLab for
    that, but I won't cover it here now that we have the intuition.
    """
    def construct(self):
        t = make_title("Example", 3.58)
        self.title(t)

        e1 = TexMobject(r"""
            I_{Top}:\{S^{n-1}\overset{i_n}{\hookrightarrow}D^n\}
            \quad and \quad
            J_{Top}:\{D^n\overset{j_n}{\hookrightarrow}D^n\times I\}
        """).scale(.75)

        e2 = TexMobject(r"""
            i_{n_1}\Box i_{n_2}\simeq i_{n_1+n_2} \\
            i_{n_1}\Box j_{n_2}\simeq j_{n_1+n_2}
        """).scale(.75)

        e_1_to_2 = VGroup(
            e1, e2
        ).arrange_submobjects(
            DOWN,
            buff=1
        )

        self.cycle(
            [e_1_to_2]
        )

        e3 = TexMobject(r"""
            i_1\Box i_1: ( \ = \ \cup \ \mid \ \mid \ )\hookrightarrow\Box \\
            i_1\Box j_0: ( \ = \ \cup \ \mid \ )\hookrightarrow\Box
        """).scale(.75)

        self.cycle(
            [e3],
            out=False
        )
        self.clear()

class def359(Scene):
    """
    So the definition of a pullback powering is almost asking to be dualized, and that is
    what we do now. So given again two morphisms in Top cg, their pullback powering
    is the universal map induced by the following pullback:
    """
    def construct(self):
        t = make_title("Definition", 3.59)
        self.title(t)

        d1 = TextMobject(r"""
            Let $i:A\to B$ and $p:X\to Y$ be two morphisms in $Top_{cg}$. Their 
        """, "pullback powering ", r"""
            is
            \[
            p^{\Box i}:=(p^B,X^i)
            \]
            being the universal morphism in 
        """, alignment="").scale(.75).shift(2*UP)
        d1[1].set_color(BLUE)

        d2 = tikz("def359_d2", r"""
            \begin{tikzcd}
                & X^B
                    \arrow{d}[right]{(p^B,X^i)}
                    & \\
                & Y^B\underset{Y^A}{\times}X^A
                    \arrow{dl}\arrow{dr}
                    & \\
                Y^B
                    \arrow{dr}[left,yshift=-.5em]{Y^i}
                    & (pb)
                    & X^A
                    \arrow{dl}[right,yshift=-.5em]{p^A} \\
                & Y^A &
            \end{tikzcd}
        """, fn).scale(2).next_to(d1, direction=DOWN, buff=.5)

        self.cycle(
            [d1, d2],
            out=False,
            successive=False
        )
        self.clear()

class prop360(Scene):
    """
    So we have these homotopy theoretic properties. Given three morphisms in 
    Top cg, then their pushout product of i1 and i2 has the left lifting property 
    against p if and only if i1 has the LLP hgainst the pullback powering of p and
    i2 and equivalently if i2 has the LLP against the pullback powering of i1. So these
    statements are all equivalent. Let's prove this. The proof was really instructive for me in
    understaning how we can break apart commuting squares and construct other squares that
    contain the same information. I imagine that it will be a useful technique in the
    future. First of all, if we can show that these are in natural bijection, then
    we are done. We will do this using the product hom adjunction in the following way.
    So let's start with the first square, and obtain the second. Ok, so we want to think about
    the information contained in this square, and break up the product or pullback in the bottom
    right. So we definitely need to have the information of commutativity, so that's these 
    first two squares. The last one comes from the observation that the pullback in question
    is the pullback over the diagram XA, YB to YA by definition. So we also have
    the information in the original square that that bottom map commutes with that diagram
    component wise, and that's how we get the third square.
    For the next set of squares we apply the product hom adjunction. And finally, we 
    want to backage all of this information into a single square. Well take the second square,
    It has a pushout and hence a unique map from the pushout to X which agrees with
    f tilde and g2 tilde, so we've captured the information in those maps. No
    if in the second square we could just as well have replaced X with P cross B, as the
    first and third squares demonstrate commutativeity is preserved. Well, then the map
    induces from the pushout is by definition the pushout product of i1 and i2, so we've captured
    the information from those two maps. Finally, we complete the square using information
    contained in the third square, and we get the diagram in question. It contains exactly the
    same information of the original square, so we have a bijection and we are done.
    """
    def construct(self):
        t = make_title("Proposition", "3.60")
        self.title(t)

        p1 = TextMobject(r"""
            Let $i_1, i_2, p$ be three morphisms in $Top_{cg}$. Then for their 
            pushout-products and pullback-powerings the following lifting properties 
            are equivalent:
            \begin{align*}
                i_1\Box i_2 \quad & has \ LLP \ against \quad p \\
                \iff i_1 \quad & has \ LLP \ against \quad p^{\Box i_2} \\
                \iff i_2 \quad & has \ LLP \ against \quad p^{\Box i_1}
            \end{align*}
        """, alignment="").scale(.75)

        self.cycle(
            [p1]
        )

        p2 = tikz("prop360_p2", r"""
            \begin{tikzcd}
                Q
                    \arrow{r}[above]{f}\arrow{d}[left]{i_1}
                    & X^B
                    \arrow{d}[right]{p^{\Box i_2}} \\
                P
                    \arrow{r}[below]{(g_1,g_2)}
                    & Y^B\underset{Y^A}{\times}X^A
            \end{tikzcd}
        """, fn).shift(2*LEFT)

        p3 = TexMobject("\\leftrightarrow")

        p4 = tikz("prop360_p3", r"""
            \begin{tikzcd}
                Q\times B\underset{Q\times A}{\sqcup}P\times A
                    \arrow{r}[above]{(\tilde{f}, \tilde{g}_2)}\arrow{d}[left]{i_1\Box i_2}
                    & X
                    \arrow{d}[right]{p} \\
                P\times B
                    \arrow{r}[below]{\tilde{g}_1}
                    & Y
            \end{tikzcd}
        """, fn).shift(2*RIGHT)

        self.cycle(
            [p2, p3, p4],
            successive=False
        )

        p2.shift(2.5*LEFT,1.5*UP)

        p5 = tikz("prop360_p5", r"""
            \begin{tikzcd}
                & X^B
                    \arrow{d}
                    & \\
                & Y^B\underset{Y^A}{\times}X^A
                    \arrow{dl}\arrow{dr}
                    & \\
                Y^B
                    \arrow{dr}
                    & (pb)
                    & X^A
                    \arrow{dl} \\
                & Y^A &
            \end{tikzcd}
        """, fn).shift(3*RIGHT).scale(1.5)

        self.cycle(
            [p2, p5],
            successive=False
        )
        
        p6 = ImageMobject("top_enrichment/lots_o_squares.tiff").scale(2.5)

        self.cycle(
            [p6],
            out=False
        )
        self.clear()

class prop361(Scene):
    """
    So this makes showing this next proposition a lot easier. The pushout product of to
    classical cofibrations is a classical cofibration, and is moreover acyclic if
    one of them is acyclic to begin with.
    So to see this first point, we should earlier that the pushout product of things
    in i top is again in itop, which imiplies the first line. The second
    comes from the previous proposition. The third comes by closure of lifting
    properties under retracts. The fourth is the proevious proposition again.
    The fifth is the previous proposition again. The sixth is again closure under
    retracts of lifting properties, and the last line is the previous proposition again.
    So the pushout product of classical cofibrations as the left lifting property
    against acyclic fibrations, hence itself must be a classical cofibration by
    definition.
    The second proposition is analagous, and uses the initial observation that
    the pushout of a thing in itop and a thing in jtop is in jtop from the previous
    proposition.
    """
    def construct(self):
        t = make_title("Proposition", 3.61)
        self.title(t)

        p1 = TextMobject(r"""
            The pushout-product in $Top_{cg}$ of two classical cofibrations is a 
            classical cofibration:
            \[
            Cof_{cl}\Box Cof_{cl}\subset Cof_{cl}.
            \]
            If one of them is acyclic, then so is the pushout-product:
            \[
            Cof_{cl}\Box (W_{cl}\cap Cof_{cl})\subset W_{cl}\cap Cof_{cl}.
            \]
        """, alignment="").scale(.75)

        self.cycle(
            [p1]
        )

        p2 = TexMobject(r"""
            I_{Top}\Box I_{Top}\subset I_{Top}
        """).scale(.75).shift(2*UP)

        p3 = TextMobject(r"""
            \begin{align*}
                I_{Top}\Box I_{Top} \quad & has \ LLP \ against \quad
                    W_{cl}\cap Fib_{cl} \\
                \iff \quad I_{Top} \quad & has \ LLP \ against \quad
                    (W_{cl}\cap Fib_{cl})^{\Box I_{Top}} \\
                \Rightarrow \quad Cof_{cl} \quad & has \ LLP \ against \quad
                    (W_{cl}\cap Fib_{cl})^{\Box I_{Top}} \\
                \iff \quad I_{Top}\Box Cof_{cl} \quad & has \ LLP \ against \quad
                    W_{cl}\cap Fib_{cl} \\
                \iff \quad I_{Top} \quad & has \ LLP \ against \quad
                    (W_{cl}\cap Fib_{cl})^{Cof_{cl}} \\
                \Rightarrow \quad Cof_{cl} \quad & has \ LLP \ against \quad
                    (W_{cl}\cap Fib_{cl})^{Cof_{cl}} \\
                \iff \quad Cof_{cl}\Box Cof_{cl} \quad & has \ LLP \ against \quad
                    W_{cl}\cap Fib_{cl}
            \end{align*}
        """).scale(.75).next_to(p2, direction=DOWN, buff=1)

        self.cycle(
            [p2, p3],
            out=False,
            successive=False
        )
        self.clear()

class rmk362(Scene):
    """
    Technically speaking, the closure of the homotopy properties in the previous
    proposition exhibits Top cg Quillen as a monoidal model category with respect
    to the Cartesian product on Topcg, and an enriched model category over itself.
    """
    def construct(self):
        t = make_title("Remark", 3.62)
        self.title(t)

        r1 = TextMobject(r"""
            The model category $(Top_{cg})_{Quillen}$ is
            \begin{enumerate}
                \item a monoidal model category with respect to the Cartesian product 
                    on $Top_{cg}$
                \item an enriched model category over itself
            \end{enumerate}
        """, alignment="").scale(.75)

        self.cycle(
            [r1],
            out=False
        )
        self.clear()

class prop363(Scene):
    """
    What that jargon entails generally, what we have just discussed up to now is the 
    following. Preserving cofibrations and lifting properties should evoke something
    from before- a Quillen adjunction. Indeed, we have shown that in Topcg Quillen
    we have the key property that the product hom adjunction is not just an adjunction,
    but in fact a Quillen adjunction, for X cofibrant. And we see this in the following way.
    Remember that on morphisms, the cartesian product is given by the pushout product
    with the initial morphism. Well by assumption X is cofibrant, so if we input a 
    cofibration, then we will have the pushout product of cofibrations which we showed
    just now is a cofibration, hence the left adjoint is a left quillen functor, and we
    are done.
    """
    def construct(self):
        t = make_title("Proposition", 3.63)
        self.title(t)

        p1 = TextMobject(r"""
            For $X\in (Top_{cg})_{Quillen}$ cofibrant (a retract of a cell complex) 
            then the product-hom-adjunction for $Y$ is a Quillen adjunction:
            \[
            (Top_{cg})_{Quillen}
            \underoverset
                {\underset{(-)^X}{\longrightarrow}}
                {\overset{X \times (-)}{\longleftarrow}}
                {\bot}
            (Top_{cg})_{Quillen}
            \]
        """, alignment="").scale(.75).shift(1*UP)

        p2 = TexMobject(r"""
            X\times (-)\simeq (\emptyset\to X)\Box (-)
        """).scale(.75).shift(2*DOWN)

        self.cycle(
            [p1, p2],
            out=False
        )
        self.clear()

class prop364(Scene):
    """
    And again, in the spirit of linearizing Top cg, we can in fact extend this to 
    pointed compactly generated topological spaces. We again require that X is cofibrant,
    but recall our previous remark that this means it has a non-degenrate basepoint.
    So to see this we need to redefine the pushout product to the smash pushout product,
    which is just defined in the same manner but with replacing cartesian products
    with smash products and mapping spaces with pointed mapping spaces. Similarly we redefine
    the smash pullback powering.
    So Topcg pointed is also cofibrantly generated, using this left adjoint which adjoins
    a basepoint. And recall a property we showed that allowed us to pull it out in a sense
    of a product, and then the reset is immediate.
    """
    def construct(self):
        t = make_title("Proposition", 3.64)
        self.title(t)

        p1 = TextMobject(r"""
            For $X\in(Top_{cg}^{\ast /})_{Quillen}$ cofibrant, then the pointed 
            product-hom-adjunction is a Quillen adjunction:
            \[
            (Top^{\ast/}_{cg})_{Quillen}
            \underoverset
                {\underset{Maps(X,-)_\ast}{\longrightarrow}}
                {\overset{X \wedge (-)}{\longleftarrow}}
                {\bot}
            (Top^{\ast/}_{cg})_{Quillen}
            \]
        """, alignment="").scale(.75).shift(1*UP)

        p2 = TexMobject(r"""
            (i_{n_1})_+\Box_\wedge (i_{n_2})_+ \simeq (i_{n_1+n_2})_+ \\
            (i_{n_1})_+ \wedge_\wedge (i_{n_2})_+ \simeq (i_{n_1+n_2})_+
        """).scale(.75).shift(2*DOWN)

        self.cycle(
            [p1, p2],
            out=False
        )
        self.clear()

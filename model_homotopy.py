# Date: 2/19/21
# Purpose: homotopy subsection of abstract homotopy nLab section
# Notes:

from manimlib.imports import *
fn = "model_homotopy"


class def218(Scene):
    """
    So if you recall from our work with topological homotopy theory, the keys to defining
    right and left homotopy were path space objects and cylinder objects respectively.
    So let's define these things in the abstact setting of model categories. Again, these
    are characterized via diagonals and codiagonals.
    So a path space object is a factorization of the diagonal, i.e. the map from X to
    X cross X, as a weak equivalence followed by a fibration.
    Dually, a cylinder object is a factorization of the codiagonal, i.e. the map from
    X disjoint union X to X as a cofibration followed by a weak equivalence.
    """
    def construct(self):
        t = make_title("Definition", 2.18)

        self.title(t)

        d1 = TextMobject(r"""
            \begin{itemize}
                \item a \textit{path space object} $\text{Path}(X)$ is a factorization of the 
                    diagonal as
                    $$ \Delta_X: X \underoverset{\in W}{i}{\longrightarrow}
                    \text{Path}(X) \underoverset{\in\text{Fib}}{(p_0,p_1)}{\longrightarrow} 
                    X\times X $$
                \item A \textit{cylinder object} $\text{Cyl}(X)$ is a factorization of the 
                    codiagonal as
                    $$ \nabla_X: X \sqcup X \underoverset{\in \text{Cof}}{(i_0,i_1)}{\longrightarrow} 
                    \text{Cyl}(X) \underoverset{\in W}{p}{\longrightarrow} X $$
            \end{itemize}
        """, alignment="").scale(.75).shift(.5*LEFT)

        self.cycle(
            [d1],
            out=False
        )

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class rmk219(Scene):
    """
    Well you might recall the weak factorizations of a model category. In particular,
    that we can do even better than the factorization we just described. We can
    factor the diagonal as an acyclic cofibration followed by a fibration,
    not just a weak equivalence followed by a fibration, and dually we can factor
    the codiagonal as a cofibration followed by an acyclic fibration.
    Some people call these Very good path space and cylinder objects. In fact, some authors
    dont require the fibration cofibration parts of our definition, they just require
    that a path space object factor the diagonal as a weak equivalence followed by something,
    and dually a cylinder object factors the codiagonal as something followed by a weak
    equivalence. Nonetheless, we take the approach from definition 218 before.
    """
    def construct(self):
        t = make_title("Remark", 2.18)

        self.title(t)

        r1 = TexMobject(r"""
            \Delta_X: X \underset{\in W}{\longrightarrow}
                    \text{Path}(X) \underset{\in W\cap\text{Fib}}{\longrightarrow} 
                    X\times X \\
            \nabla_X: X \sqcup X \underset{\in W\cap\text{Cof}}{\longrightarrow} 
                    \text{Cyl}(X) \underset{\in W}{\longrightarrow} X 
        """).scale(.75).shift(.5*LEFT)

        self.cycle(
            [r1],
            out=False
        )
        self.clear()

class fibrant_cofibrant(Scene):
    """
    So here's a useful definition that the nLab doesn't include explicitly, but
    I've included it for completeness. An object X is said to be fibrant if and
    only if the map from X to the terminal object is a fibration, and is dually
    said to be cofibrant if the map from the initial object to X is a cofibration.
    """
    def construct(self):
        d1 = TexMobject(r"""
            (X \text{ fibrant}) \quad\iff\quad (X\overset{\text{Fib}}{\longrightarrow}1) \\
            (X \text{ cofibrant}) \quad\iff\quad (0\overset{\in\text{Cof}}{\longrightarrow} X)
        """).scale(.75)

        self.cycle(
            [d1]
        )

class lemma220(Scene):
    """
    So we can always find SOME cylinder object for X an object of the category that
    factors as an acyclic cofibration followed by a weak equivalence, and dually some
    path space object that is a weak equivalence followed by an acyclic fibration.
    But it turns out that we can have a stronger statment with some added conditions.
    If X if cofibrant, then EVERY cylinder object factors the codiagonal as an map
    followed by a weak equivalence, where each component map is seperately
    an acyclic cofibration. Dually if X is fibrant then every
    pathspace object factors the diagonal as a weak equivalence followed by a map
    whose components are each an acyclic fibration.
    To see this, we prove the path space case, and the other is just dual.
    Well, each component map is a map from X to Path X, and by definition it has
    a right inverse, which is a weak equivalence, and so the entire map is a weak equivalence
    in particular, and so by two out three it follows that each component map is a weak
    equivalence. To see that it is a fibration, consider this diagram.
    Since X is fibrant, the right morphism is a fibration, and since these are closed
    under pullbacks it follows that the right and top morphisms are fibrations as well.
    Well then each component map is a map from the path space object to X cross X to X,
    hence the composite of a fibration (which is by definition) followed by another fibration,
    which we just showed. Hence it is itself a fibration, and we are done.
    """
    def construct(self):
        t = make_title("Lemma", "2.20")

        self.title(t)

        l1 = TextMobject(r"""
            Let $C$ be a model category.
            \begin{itemize}
                \item If $X\in\mathcal{C}$ is cofibrant, then for every cylinder object 
                $\text{Cyl}(X)$, not only is $(i_0, i_1):X\sqcup X\to X$ a cofibration, 
                but each $$i_0, i_1:X\longrightarrow\text{Cyl}(X)$$ is an acyclic 
                cofibration seperately.
                \item If $X\in\mathcal{C}$ is fibrant, then for every path space object 
                $\text{Path}(X)$ of $X$, not only is $(p_0,p_1):\text{Path}(X)\to X\times X$ 
                a fibration, but each $$ p_0, p_1:\text{Path}(X)\longrightarrow X$$ is an 
                acyclic fibration seperately.
            \end{itemize}
        """, alignment="").scale(.7)

        l2 = TexMobject(r"""
            X\sqcup X\to\text{Path}(X)\to X
        """).scale(.75)

        l3 = tikz("lemma220_l3", r"""
            \begin{tikzcd}
                X\times X
                    \arrow{r}\arrow{d}
                    & X
                    \arrow{d} \\
                X
                    \arrow{r}[above,yshift=1em]{(\text{pb})}
                    & \ast
            \end{tikzcd}
        """, fn)

        self.cycle(
            [l1]
        )

        self.cycle(
            [l2],
            out=False
        )
        self.fade_replace(
            l2, l3
        )
        self.clear()

class ex221(Scene):
    """
    So it turns out that path space objects are not very unique. Just consider the
    standard topological path space object, which is the mapping space out of 
    the interval of length 1. We can construct a new path space object
    out of two copies of this, and end up with the mapping space out of the interval
    of length 2 instead of 1. We can generalize this idea and obtain a path space
    object from any other two path space objects by forming what is called the fiber
    product under the assumption that X is fibrant.
    It is the pullback in this middle square here. The middle left morphism
    is an fibration since the middle right is and they are closed under pullbacks.
    The top left morphism is a weak equivalence and we see this in 
    the following way. The maps in red are weak equivalences on the level of component
    maps. So I'm not saying X and X times X are weakly homotopy equivalent, but the
    component map from X to X is. But from this the top left morphism is a weak
    equivalence by two out of three.
    """
    def construct(self):
        t = make_title("Example", 2.21)

        self.title(t)

        e1 = tikz("ex221_e1", r"""
            \begin{tikzcd}
                X
                    \arrow{r}[above]{\Delta_X}\arrow{d}
                    & X\times X
                    \arrow{d} \\
                \text{Path}_1(X)\underset{X}{\times}\text{Path}_2(X)
                    \arrow{r}\arrow{d}[left]{\in\text{Fib}}
                    & \text{Path}_1(X)\times\text{Path}_2(X)
                    \arrow{d}[right]{\in\text{Fib}} \\
                X\times X\times X
                    \arrow{r}[above]{(\text{id},\Delta_X,\text{id})}[above,yshift=1em]
                    {(\text{pb})}\arrow{d}[right]{(\text{pr}_1,\text{pr}_3)\in\text{Fib}}
                    & X\times X\times X\times X
                    \arrow{d}[right]{(p_1, p_4)} \\
                X\times X
                    \arrow{r}[above]{=}
                    & X\times X
            \end{tikzcd}
        """, fn).scale(2)

        self.cycle(
            [e1],
            out=False
        )
        self.clear()

class def222(Scene):
    """
    So that was just an example. Returning to definitions, left and right homotopies
    are defined as they were in the topological case, with cylinder objects and path
    space objects respectively. But of course, in the abstract setting of a model
    category we use the abstract definitions of these objects.
    """
    def construct(self):
        t = make_title("Definition", 2.22)

        self.title(t)

        d1 = TextMobject(r"""
            Let $f,g:X\to Y$ be two parallel morphisms in a model category.
        """, alignment="").scale(.75).to_title(t)

        d2 = TextMobject(r"""
            \begin{itemize}
                \item a \textit{left homotopy} $\eta:f\Rightarrow_L g$ is a morphism such 
                that the following diagram commutes:
            \end{itemize}
        """).scale(.75).shift(.5*UP)

        d3 = tikz("def222_d3", r"""
            \begin{tikzcd}
                X
                    \arrow{r}\arrow{dr}[right,yshift=-.5em]{f}
                    & \text{Cyl}(X)
                    \arrow{d}[right]{\eta}
                    & X
                    \arrow{l}\arrow{dl}[right,yshift=-.5em]{g} \\
                & Y
            \end{tikzcd}
        """, fn).next_to(d2, direction=DOWN, buff=.25)

        self.cycle(
            [d1],
            out=False
        )

        self.cycle(
            [d2, d3],
            successive=False
        )

        d4 = TextMobject(r"""
            \begin{itemize}
                \item a \textit{right homotopy} $\eta:f\Rightarrow_R g$ is a morphism such 
                that the following diagram commutes:
            \end{itemize}
        """).scale(.75).shift(.5*UP)

        d5 = tikz("def222_d5", r"""
            \begin{tikzcd}
                & X
                    \arrow{dl}[left,yshift=.5em]{f}\arrow{d}[right]{\eta}
                    \arrow{dr}[right,yshift=.5em]{g}
                    & \\
                Y
                    & \text{Path}(Y)
                    \arrow{l}\arrow{r}
                    & Y
            \end{tikzcd}
        """, fn).next_to(d2, direction=DOWN, buff=.25)

        self.cycle(
            [d4, d5],
            successive=False,
            out=False
        )
        self.clear()

class lemma223(Scene):
    """
    Now we have a pretty cool proposition that I mentioned before when covering left and right
    homotopies in the topological setting. First, we have this lemma from which that proposition
    will easily follow.
    So let f and g ber parrellel morphism from X to Y. So if X is cofibrant, then
    each left homotopy corresponds to a right homotopy with respect to any chosen
    path space object, and if Y is fibrant the dually for each right homotopy there is a
    left homotopy with respect to any chosen cylinder object.
    So in particular if X is cofibrant and Y is fibrant, we can just keep applying this
    lemma and get that every left homotopy is exhibited by every cylinder object, and
    dually that every right homotopy is exhibited by every path space object.
    We will prove the first case where X is cofibrant and the other is again just dual.
    So we have this commuting diagram. The top map is the composite of X to Y and Y
    to the Path space via inclusion. The only other ambiguous map is maybe
    the bottom one. It is the map from cyl x to x to y on one of the Ys, and
    the assumed left homotopy on the other Y. So by assumption X is cofibrant, and
    so the left vertical morphism is an acyclic cofibration. Since the right on is a 
    fibration, we have a lift from Cyl X to Path Y. And just rearranging this gives
    us a right homotopy with respect to Path Y.
    """
    def construct(self):
        t = make_title("Lemma", 2.23)

        self.title(t)

        l1 = TextMobject(r"""
            \begin{enumerate}
                \item Let $X$ be cofibrant. If there is a left homotopy $f\Rightarrow_L g$ 
                then there is also a right homotopy $f\Rightarrow_R g$ with respect to 
                any chosen path space object.
                \item Let $Y$ be fibrant. If there is a right homotopy $f\Rightarrow_R g$ 
                then there is also a left homotopy $f\Rightarrow_L g$ with respect to any chosen 
                cylinder object.
            \end{enumerate}
        """).scale(.75)

        self.cycle(
            [l1]
        )

        l2 = tikz("lemma223_l2", r"""
            \begin{tikzcd}
                X
                    \arrow{r}[above]{i\circ f}\arrow{d}[left]{i_0\in W\cap\text{Cof}}
                    & \text{Path}(Y)
                    \arrow{d}[right]{p_0,p_1\in\text{Fib}} \\
                \text{Cyl}(X)
                    \arrow{ur}[left,yshift=.5em]{h}\arrow{r}[below]{(f\circ p,\eta)}
                    & Y\times Y
            \end{tikzcd}
        """, fn)

        self.cycle(
            [l2],
            out=False
        )

        l3 = tikz("lemma223_l3", r"""
            \begin{tikzcd}
                & & Y \\
                X
                    \arrow{r}[above]{i_1}
                    & \text{Cyl(X)}
                    \arrow{r}[above]{h}\arrow{ur}[left,yshift=.5em]{f\circ p}
                        \arrow{dr}[left,yshift=-.5em]{\eta}
                    & \text{Path}(Y)
                    \arrow{u}[right]{p_0}\arrow{d}[right]{p_1} \\
                & & Y
            \end{tikzcd}
        """, fn).scale(1.5)

        self.fade_replace(
            l2, l3
        )
        self.clear()

class prop224(Scene):
    """
    So here's perhaps the punchline you remember. If X is cofibrant and Y is fibrant,
    again in a model category, then the relations of left homotopy and right homotopy coincide,
    and both are equivalence relations.
    So if you've taken an introductory algebraic topology class, you might wonder why we
    never heard of a distinction between left and right homotopy. Well, in the
    classical model structure on topological spaces, every object is fibrant, and CW
    complexes are cofibrant, so for most of the cases we encounter in an introductory course
    we have CW complexes and the notions of left and right homotopy coincide. I think that's
    pretty cool.
    """
    def construct(self):
        t = make_title("Proposition", 2.24)
        
        self.title(t)

        p1 = TextMobject(r"""
            For $X$ cofibrant and $Y$ fibrant, the relations of left homotopy and right 
            homotopy on the hom set $\text{Hom}(X,Y)$ coincide and are both equivalence 
            relations.
        """, alignment="").scale(.75)

        self.cycle(
            [p1],
            out=False
        )
        self.clear()

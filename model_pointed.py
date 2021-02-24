# Date: 2/22/21
# Purpose: model structure on pointed spaces section nLab
# Notes:

from manimlib.imports import *
fn = "model_pointed"


class def315(Scene):
    """
    We want to pass and specialize to pointed spaces, which are objects equipped with 
    a basepoint. This is the first step to stable homotopy theory. A nice thing we get
    from this, as we will see, is a canonical non-cartesian tensor product (assuming
    the original category had cartesian products). This will be the smash product. But
    to begin with, a slice category of a category is the one whose objects are morphisms
    into some object X in the original category, and whose morphisms are commuting
    triangles.
    Dually, the coslice category has objects morphisms out of X and morphisms again
    are commuting triangles. Obviouslly there are canonical forgetful functors to the
    original category.
    """
    def construct(self):
        t = make_title("Definition", 3.15)
        self.title(t)

        d1 = TextMobject(r"""
            Let $\mathcal{C}$ be a category and let $X\in\mathcal{C}$ be an object.
        """, alignment="").scale(.75).to_title(t)

        d2 = TextMobject(r"""
            The slice category $\mathcal{C}_{/X}$ is the category whose
            \begin{itemize}
                \item objects are morphisms $A\to X$ in $\mathcal{C}$
                \item morphisms are commuting triangles:
                    \begin{equation*}
                    \begin{matrix}
                        A & & \to & & B \\
                        & \searrow & & \swarrow & \\
                        & & X & &
                    \end{matrix}
                    \end{equation*}
            \end{itemize}
        """, alignment="").scale(.75).to_edge(LEFT).shift(.5*DOWN)

        self.cycle(
            [d1, d2],
            out=False
        )

        d3 = TextMobject(r"""
            The coslice category $\mathcal{C}^{X/}$ is the category whose
            \begin{itemize}
                \item objects are morphisms $X\to A$ in $\mathcal{C}$
                \item morphisms are commuting triangles:
                    \begin{equation*}
                    \begin{matrix}
                        & & X & & \\
                        & \swarrow & & \searrow & \\
                        A & & \to & & B
                    \end{matrix}
                    \end{equation*}
            \end{itemize}
        """, alignment="").scale(.75).to_edge(LEFT).shift(.5*DOWN)

        self.fade_replace(
            d2, d3
        )
        self.clear()

class def316(Scene):
    """
    What we want to focus on is this. For a category with a terminal object, the
    category of pointed objected is the coslice category at this object, i.e. it
    has objects morphisms out of the terminal object and morphisms are commuting triangles,
    so intuitively this is saying a morphism from X to Y sends the basepoint of X to the
    basepoint of Y.
    """
    def construct(self):
        t = make_title("Definition", 3.16)
        self.title(t)

        d1 = TextMobject(r"""
            For $\mathcal{C}$ a category with terminal object $\ast$, the 
        """, "category of pointed objects", " has", r"""
            \begin{itemize}
                \item objects are morphisms (pointed objects) $\ast\overset{x}{\to}X$
                \item morphisms are commuting triangles
                \begin{equation*}
                \begin{matrix}
                    & & \ast & & \\
                    & {}^x \swarrow & & \searrow {}^y & \\
                    X & & \overset{f}{\longrightarrow} & & Y
                \end{matrix}
                \end{equation*}
            \end{itemize}
        """, alignment="").scale(.75)

        self.cycle(
            [d1],
            out=False
        )
        self.clear()

class rmk317(Scene):
    """
    One thing we get is what is called a zero object. This comes from the observation
    that in a category of pointed objects, the terminal object and initial object coincide:
    this is given by the object the terminal object mapping into itself. Indeed, if
    you look back at the triangle that shows morphisms, then there is a unique map out of 
    this zero object into any other sending the terminal object to the basepoint in the
    other object, and obviously there is a unique map into it as it is a terminal object.
    """
    def construct(self):
        t = make_title("Remark", 3.17)
        self.title(t)

        r1 = TexMobject(r"""
            0:X\overset{\exists !}{\longrightarrow} 0 \overset{\exists !}{\longrightarrow} Y
        """).scale(.75)

        self.cycle(
            [r1],
            out=False
        )
        self.clear()

class def318(Scene):
    """
    So given a category with terminal object and finit colimits, then the forgetful functor
    from its category of pointed objects has a left adjoint given by forming the disjoint
    union or coproduct with a base point. So intuitively the forgetful functor forgets the
    choice of basepoint on the space, and its adjunct chooses a basepoint back.
    """
    def construct(self):
        t = make_title("Definition", 3.18)
        self.title(t)

        d1 = TexMobject(r"""
            \mathcal{C}^{\ast/}
            \underoverset
            {\underset{U}{\longrightarrow}}
            {\overset{(-)_+}{\longleftarrow}}
            {\bot}
            \mathcal{C}
        """).scale(.75)

        self.cycle(
            [d1],
            out=False
        )
        self.clear()

class prop319(Scene):
    """
    So here's a proposition we won't prove directly but hopefully it makes intuitive sense. So
    if a category has all limits and colimits, then so does its category of pointed objects.
    Specifically, the limits are the limits of the underlying diagrams in C with the basepoint
    of the limit object induced by the universal property in C, and dually the colimits
    are the colimits in C with the basepoint adjoined. That it is adjoined means its not actually
    given by the coproduct in C, which we will see in the next example.
    """
    def construct(self):
        t = make_title("Proposition", 3.19)
        self.title(t)

        p1 = TextMobject(r"""
            Let $\mathcal{C}$ be a category with all limits and colimits. Then so does 
            the category of pointed objects. Moreover,
            \begin{enumerate}
                \item the limits are the limits of the underlying diagrams in $\mathcal{C}$, 
                    with the base point of the limit induced by its universal property in 
                    $\mathcal{C}$
                \item the colimits are the limits in $\mathcal{C}$ of the diagrams with the 
                    basepoint adjoined
            \end{enumerate}
        """, alignment="").scale(.75)

        self.cycle(
            [p1],
            out=False
        )
        self.clear()

class ex320(Scene):
    """
    Here are a couple examples. So given two pointed objects, then their product is
    as you'd expect, just X cross Y and the basepoint is x comma y. The coproduct
    is the pushout of this diagram. And we call this the wedge sum. So I like to 
    think this as attaching two spaces by gluing them together at their basepoints.
    """
    def construct(self):
        t = make_title("Example", "3.20")
        self.title(t)

        e1 = TextMobject(r"""
            Given two pointed objects $(X, x)$ and $(Y, y)$, then
            \begin{enumerate}
                \item their product in $\mathcal{C}^{\ast /}$ is $(X\times Y, (x,y))$
                \item their coproduct is called the \textbf{wedge sum}:
            \end{enumerate}
        """, alignment="").scale(.75).shift(1*UP)

        e2 = tikz("ex320_e2", r"""
            \begin{tikzcd}
                \ast
                    \arrow{r}[above]{x}\arrow{d}[left]{y}
                    & X
                    \arrow{d} \\
                Y
                    \arrow{r}[above,yshift=1em]{\text{(po)}}
                    & X\vee Y
            \end{tikzcd}
        """, fn).next_to(e1, direction=DOWN, buff=.5)

        self.cycle(
            [e1, e2],
            out=False,
            successive=False
        )
        self.clear()

class ex321(Scene):
    """
    Another example is that for a CW complex, then the quotient for n a natural number
    of its n skeleton by its n-1 skeleton is the wedge sum of n spheres, one for each
    n cell of X. So like just consider even the cube or solid sphere D3. Its 2 skeleton
    is the boundary S2. Its one skeleton doesn't exist, so we have that the quotient
    is just S2. Well indeed this is just one copy of S2.
    """
    def construct(self):
        t = make_title("Example", 3.21)
        self.title(t)

        e1 = TextMobject(r"""
            For $X$ a CW-complex, $n\in\mathbb{N}$, then
            $$ X^n / X^{n-1} \simeq \underset{i\in I_n}{\vee}S^n$$
        """, alignment="").scale(.75).to_edge(LEFT, buff=.5)

        self.cycle(
            [e1],
            out=False
        )
        self.clear()

class def322(Scene):
    """
    Now we arrive at the non cartesian tensor product, i.e. the smash product.
    Its a functor given by the following pushout. We can even get this nice formula.
    """
    def construct(self):
        t = make_title("Definition", 3.22)
        self.title(t)

        d1 = tikz("def322_d1", r"""
            \begin{tikzcd}
                X\sqcup Y
                    \arrow{r}[above]{(\text{id}_X,y),(x,\text{id}_Y)}\arrow{d}
                    & X\times Y
                    \arrow{d} \\
                \ast
                    \arrow{r}
                    & X\wedge Y
            \end{tikzcd}
        """, fn)

        d2 = TexMobject(r"""
            X\wedge Y = \dfrac{X\times Y}{X\vee Y}
        """).scale(.75).next_to(d1, direction=DOWN, buff=.5)

        self.cycle(
            [d1, d2],
            out=False,
            successive=False
        )
        self.clear()

class rmk323(Scene):
    """
    So we can't really hope for this to be commutative, but ideally it would be associate!
    But let's look at what that would entail. In general, this is not associative. In particular,
    the failure here is that crossing with some space does not preserve quotients, so like
    on the left numerator the quotient cross Z isnt the same as X cross Y cross Z quotiented.
    Not necessarily, so the smash product in Top is not generally associative, but it turns
    out that the smash product in compactly generated topological spaces is.
    """
    def construct(self):
        t = make_title("Remark", 3.23)
        self.title(t)

        r1 = TexMobject(r"""
            \dfrac{
                \frac{X\times Y}{X\vee Y}\times Z
            }{
                \frac{X\times Y}{X\vee Y}\vee Z
            }
        """).scale(.75)

        r2 = TexMobject(r"""
            \dfrac{
                X\times\frac{Y\times Z}{Y\vee Z}
            }{
                X\vee \frac{Y\times Z}{Y\vee Z}
            }
        """).scale(.75)

        r_1_and_2 = VGroup(
            r1, r2
        ).arrange_submobjects(
            RIGHT,
            buff=1
        )

        self.cycle(
            [r_1_and_2],
            out=False
        )
        self.clear()

class ex324(Scene):
    """
    So recall that adjunct functor to the forgetful one that adjoined a basepoint
    to a space. Then we have these nice properties. The first one is pretty
    straightforward: this is the colimit of this diagram. The second to me was
    more striking, but not too hard to see. The second line might be not so immediate
    to see, but this is distribution, so X cross Y disjoint union X cross point which
    is just X disjoint union Y cross point which is just Y disjoint union point cross
    point which is just point.
    """
    def construct(self):
        t = make_title("Example", 3.24)
        self.title(t)

        e1 = TextMobject(r"""
            For $X,Y\in\text{Top}$ with $X_+,Y_+\in\text{Top}^{\ast /}$. Then
            \begin{itemize}
                \item $X_+\vee Y_+\simeq (X\sqcup Y)_+$
                \item $X_+ \wedge Y_+\simeq (X\times Y)_+$
            \end{itemize}
        """, alignment="").scale(.75).to_title(t)

        e2 = TextMobject(r"""
            \begin{align*}
                X_+\wedge Y_+ \simeq & 
                    \dfrac{(X\sqcup\ast)\times(X\sqcup\ast)}
                    {(X\sqcup\ast)\vee(Y\sqcup\ast)} \\ \simeq &
                    \dfrac{X\times Y\sqcup X\sqcup Y\sqcup\ast}
                    {X\sqcup Y\sqcup\ast} \\ \simeq &
                    X\times Y\sqcup\ast
            \end{align*}
        """).scale(.75).shift(1.5*DOWN)

        self.cycle(
            [e1, e2],
            out=False
        )
        self.clear()

class ex325(Scene):
    """
    So here's a pretty important construction. Take the standard cylinder object in Top
    and disjoint union a basepoint. So again, this point is just floating somewhere in
    space it isn't attached to I. We had the cartesian product in Top and could form the
    cylinder object X cross I. In the pointed category, we can form the reduced cylinder,
    i.e. the wedge product of X with I plus. So think about what this means. Its the cartesian
    product of X with I disjoint union a point modulo X wedge that. So the top becomes
    X cross I disjoint union X and the bottom is I disjoint union X, since we attach along base
    points. Well, then the copies of X that are floating in the numerator and demoniator vanish,
    and we are left with X cross I modulo I, and the only way to make this canonical
    is to perform this identification over the basepoint x0 of X. So all in all we form
    the cylinder object then identify the interval over the basepoint.
    In general we use the word reduced to mean the pointed analog of something. We'll see 
    this again for reduced suspensions.
    But a cool thing is that just how there was a canonical injection in Top from the coproduct
    to the cylinder object, so too is there one from the wedge sum, the analog for coproducts in
    this pointed setting, to the reduced cylinder.
    """
    def construct(self):
        t = make_title("Example", 3.25)
        self.title(t)

        e1 = TexMobject(r"""
            I_+\in\text{Top}^{\ast /}
        """).scale(.75)

        e2 = TexMobject(r"""
            X\wedge(I_+) = (X\times I)/(\{x_0\}\times I)
        """).scale(.75)

        e3 = TexMobject(r"""
            X\vee X\longrightarrow X\wedge (I_+)
        """).scale(.75)

        e_1_to_3 = VGroup(
            e1, e2, e3
        ).arrange_submobjects(
            DOWN,
            buff=1
        )

        self.cycle(
            [e1, e2, e3],
            out=False
        )
        self.clear()

class ex326(Scene):
    """
    Let's talk about pointed mapping spaces. They are defined as you might expect, they
    are the subset of maps from Y to X that send the basepoint of Y to the basepoint of
    X. The quote on quote basepoint of the mapping space is the map constant on the
    basepoint of X, i.e. sends everything in Y to the baespoint of X. Well this allows
    us to define the standard topological pointed path space object, which is the pointed
    mapping space from I plus to X. We have the analagous bijection. Is this an adjunction?
    """
    def construct(self):
        t = make_title("Example", 3.26)
        self.title(t)

        e1 = TexMobject(r"""
            \text{Maps}((Y,y), (X,x))_\ast\hookrightarrow (X^Y, \text{const}_x)
        """).scale(.75).shift(1*UP)

        e2 = TexMobject(r"""
            \text{Hom}_{\text{Top}^{\ast /}}
                ((Z,z)\wedge (Y,y), (X,x)) \simeq
            \text{Hom}_{\text{Top}^{\ast /}}
                ((Z,z),\text{Maps}((Y,y),(X,x))_\ast)
        """).scale(.75).shift(1*DOWN)

        self.cycle(
            [e1, e2],
            out=False
        )
        self.clear()

class ex327(Scene):
    """
    Here's some new definitions. It's listed as an example in the nLab however.
    But the fiber or kernel of a map f from X to Y in the pointed category is the 
    following pullback in C:
    Dually, the cofiber or cokernel is the following pushout in C.
    """
    def construct(self):
        t = make_title("Example", 3.27)
        self.title(t)

        e1 = TextMobject(r"""
            Given a morphism $f:X\to Y$ in a pointed category with finite limits 
            and colimits,
            \begin{enumerate}
                \item its \textbf{fiber} or \textbf{kernel} is the pullback
                \begin{equation*}
                \begin{matrix}
                    \text{fib}(f) & \longrightarrow & X \\
                    \downarrow & (\text{pb}) & \downarrow {}^f \\
                    \ast & \longrightarrow & Y
                \end{matrix}
                \end{equation*}
                \item its \textbf{cofiber} or \textbf{cokernel} is the pushout
                \begin{equation*}
                \begin{matrix}
                    X & \overset{f}{\longrightarrow} & Y \\
                    \downarrow & (\text{po}) & \downarrow \\
                    \ast & \longrightarrow & \text{cofib}(f)
                \end{matrix}
                \end{equation*}
            \end{enumerate}
        """, alignment="").scale(.7)

        self.cycle(
            [e1],
            out=False
        )
        self.clear()

class prop329(Scene):
    """
    So we have the following proposition, that, I don't know about you, I was really
    really hoping was the case. If C is a model category, then both the slic and
    coslice category carry model structures themselves. Their weak equivalences,
    fibrations, and cofibrations are precisely thouse whose imaeg under the forgetful functor
    to C are. So for example a map in the coslice category is a fibration if and only if
    it is in C.
    In particular we have a model category on pointed objects, as well as a pointed
    homotopy category.
    """
    def construct(self):
        t = make_title("Proposition", 3.29)
        self.title(t)

        self.clear()

class def331(Scene):
    """
    So in particular we have the classical model structure on pointed topological
    spaces, as well as its homotopy category, the classical pointed homotopy category.
    """
    def construct(self):
        t = make_title("Definition", 3.31)
        self.title(t)

        d1 = TexMobject(r"""
            \text{Ho}(\text{Top}^{\ast /}):=\text{Ho}(\text{Top}_\text{Quillen}^{\ast /})
        """).scale(.75)

        self.cycle(
            [d1],
            out=False
        )
        self.clear()

class rmk332(Scene):
    """
    So let's think about fibrant and cofibrant objects in the pointed category. So
    the fibrant objects are the same, but when we take cofibrant objects, the map we
    require to be a cofibration is the composite inclusion of the basepoint and
    the map from the space to the terminal object, so actually cofibrant objects
    in the pointed category are those for which the baespoint inclusion is a cofibration
    as well as the map from the space to the terminal object, as then the composite is a
    cofibration as desired. So in particular cofibrant pointed topological spaces
    are cofibrant topological spaces. We say for such spaces that their basepoints
    are non degenerate.
    """
    def construct(self):
        t = make_title("Remark", 3.32)
        self.title(t)

        r1 = TextMobject(r"""
            ``non-degenerate basepoints''
        """).scale(.75)

        self.cycle(
            [r1],
            out=False
        )
        self.clear()

class def333(Scene):
    """
    Since Top was cofibrantly generated, we might hope that the pointed topological
    spaces category is as well. So here's how we'd define the
    generating cofibrations and acyclic cofibrations, they are defined pretty much in
    the way you expect.
    """
    def construct(self):
        t = make_title("Definition", 3.33)
        self.title(t)

        d1 = TexMobject(r"""
            I_{\text{Top}^{\ast /}} = \left\{ S^{n-1}_+ \overset{(\iota_n)_+}
                {\longrightarrow}D^n_+ \right\} \subset\text{Mor}(\text{Top}^{\ast /})
        """).scale(.75)

        d2 = TexMobject(r"""
            J_{\text{Top}^{\ast /}} = \left\{ D^n_+ \overset{(\text{id},\delta_0)_+}
                {\longrightarrow}(D^n\times I)_+ \right\} \subset\text{Mor}(\text{Top}^{\ast /})
        """).scale(.75)

        d_1_and_2 = VGroup(
            d1, d2
        ).arrange_submobjects(
            DOWN,
            buff=1
        )

        self.cycle(
            [d_1_and_2],
            out=False
        )
        self.clear()

class thm334(Scene):
    """
    And indeed, these exhibit the classical model structure on pointed topological
    spaces as a cofibrantly generated model category.
    The argument runs analagously as it did for Top, and intuitively this is because
    we freely adjoined a basepoint rather than making it attached to any of the spaces.
    nLab leaves out the details of the proof, so I will here as well, but as always I'm
    happy to revisit.
    """
    def construct(self):
        t = make_title("Theorem", 3.34)
        self.title(t)

        t1 = TextMobject(r"""
            The sets $I_{\text{Top}^{\ast /}}$ and $J_{\text{Top}^{\ast /}}$ exhibit the 
            classical model structure on pointed topological spaces as a cofibrantly 
            generated model category.
        """, alignment="").scale(.75)

        self.cycle(
            [t1],
            out=False
        )
        self.clear()

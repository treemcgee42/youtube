# Date: 2/16/21
# Purpose: first section nLab complex oriented cohomology
# Notes:

from manimlib.imports import *
fn = "reduced_cohomology"


class def11(Scene):
    """
    Our goal in this series to is to develop generalized cohomology with an eye
    towards complex oriented cohomology. We follow the nLab.
    So again, we are concerened with generalized, not necessarily standard,
    cohomology here. Ok, here is the traditional definition of a reduced cohomology
    theory. We will give several and eventually show they are equivalent.
    So a reduced cohomology theory is first of all a functor from the
    opposite category of pointed topological spaces to Z graded abelian
    groups. So this is just the notion that if you have a chain complex
    and are moving from left to right, then on the level of cohomology
    you are moving right to left.
    Secondly, we require there to be a degree one natural isomorphism, called
    the suspension isomorphism. So this needs to have certain properties, but
    I want to just point out that this is already hinting that spectra will show
    up somewhere.
    But ok, here are the properties we require. If two maps are homotopic and
    base point preserving, then their induced maps on the cohomology groups are
    equal. Basically making sure we don't see diferrences between maps of the
    same homotopy type.
    Our second condition is exactness. So lets saw you have an inclusion of A into X.
    Then Cone i is the induced mapping cone, i.e. the reduced cylinder over A disjoint
    union X modulo the image of A. So then there is an induced map from X into this
    mapping cone, and we are requireing that this sequence here is exact on the level
    of cohomology groups.
    """
    def construct(self):
        t = make_title("Definition", 1.1)

        self.title(t)

        d1 = TextMobject("A ", "reduced cohomology theory", " is")\
            .scale(.75).to_title(t)
        d1[1].set_color(BLUE)

        d2 = TextMobject(r"""
            \begin{enumerate}
                \item a functor 
                    \begin{gather*}
                        \tilde{E}^\bullet:(\text{Top}_\text{CW}^{\ast /})^\text{op}
                            \to \text{Ab}^\mathbb{Z} \\
                        \tilde{E}:(X\overset{f}{\longrightarrow} Y)\mapsto
                            (\tilde{E}^\bullet(Y)\overset{f^\ast}{\longrightarrow}
                            \tilde{E}^\bullet(X))
                    \end{gather*}
                \item a natural isomorphism, called the \textbf{suspension isomorphism}:
                    $$\sigma_E:\tilde{E}^\bullet(-)\overset{\simeq}{\longrightarrow}
                    \tilde{E}^{\bullet + 1}(\Sigma -)$$
            \end{enumerate}
        """).scale(.75).shift(1*LEFT, .5*DOWN)

        self.cycle(
            [d1, d2],
            out=False,
            successive=False
        )

        d3 = TextMobject(r"""
            \begin{enumerate}
                \item \textit{(homotopy invariance)} For $f_1,f_2:X\to Y$ such that 
                    $f_1\simeq f_2$, then $f_1^\ast = f_2^\ast$.
                \item \textit{(exactness)} For $i:A\hookrightarrow X$ and $j:X\to\text{Cone}(i)$,
                    $$\tilde{E}^\bullet(\text{Cone}(i))\overset{j^\ast}{\longrightarrow}
                    \tilde{E}^\bullet(X)\overset{i^\ast}{\longrightarrow}\tilde{E}^\bullet(A)$$
            \end{enumerate}
        """).scale(.75).shift(.5*DOWN)

        self.play(
            ReplacementTransform(d2, d3)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class def12(Scene):
    """
    So our homotopy invariance condition leads us to this next definition, which
    is much more succinct:
    This time, we define a reduced generalized cohomology theory as a functor
    from the opposite category of the pointed classical homotopy category.
    So supposedly this encodes the homotopy invariance condition without losing too
    much information.
    And again, we have the suspension isomorphisms, but this time we rephrase
    the exactness condition as taking homotopy cofiber sequences to exact
    sequences. Again, we'll later show these are equivalent definitions.
    """
    def construct(self):
        t = make_title("Definition", 1.2)

        self.title(t)

        d1 = TextMobject("A ", "reduced generalized cohomology theory", " is")\
            .scale(.75).to_title(t)
        d1[1].set_color(BLUE)

        d2 = TextMobject(r"""
        \begin{enumerate}
            \item A functor
                $$ \tilde{E}^\bullet:\text{Ho}(\text{Top}^{\ast /})^\text{op}
                \longrightarrow\text{Ab}^\mathbb{Z} $$
            \item Natural isomorphisms, called \textbf{suspension isomorphisms},
                $$ \sigma:\tilde{E}^{\bullet+1}(\Sigma -)\overset{\simeq}{\longrightarrow}
                \tilde{E}^\bullet(-) $$
                such that
                \begin{enumerate}
                    \item \textit{(exactness)} it takes homotopy cofiber sequences to 
                        exact sequences
                \end{enumerate}
        \end{enumerate}
        """).scale(.75).shift(.5*DOWN).to_edge(LEFT, buff=.5)

        self.cycle(
            [d1, d2],
            out=False,
            successive=False
        )
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class def13(Scene):
    """
    Another really similar definition, but our functor is just from the opposite
    category of pointed spaces, not the homotopy category, but we require that
    weak equivalences are sent to isomorphisms.
    """
    def construct(self):
        t = make_title("Definition", 1.3)

        self.title(t)

        d1 = TextMobject("A ", "reduced generalized cohomology theory", " is")\
            .scale(.75).to_title(t)
        d1[1].set_color(BLUE)

        d2 = TextMobject(r"""
        \begin{enumerate}
            \item A functor
                $$ \tilde{E}^\bullet:(\text{Top}^{\ast /})^\text{op}
                \longrightarrow\text{Ab}^\mathbb{Z} $$
                \begin{enumerate}
                    \item \textit{(WHE)} it takes weak homotopy equivalences to 
                        isomorphisms
                \end{enumerate}
            \item Natural isomorphisms, called \textbf{suspension isomorphisms},
                $$ \sigma:\tilde{E}^{\bullet+1}(\Sigma -)\overset{\simeq}{\longrightarrow}
                \tilde{E}^\bullet(-) $$
                such that
                \begin{enumerate}
                    \item \textit{(exactness)} it takes homotopy cofiber sequences 
                        in $\text{Ho}(\text{Top}^{\ast /})^\text{op}$ to 
                        exact sequences
                \end{enumerate}
        \end{enumerate}
        """).scale(.65).shift(.75*DOWN).to_edge(LEFT, buff=1.25)

        self.cycle(
            [d1, d2],
            out=False,
            successive=False
        )
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class prop14_12(Scene):
    """
    To see that the first and second conditions are the same, let's first consider
    the homotopy invariance condition. So the only ambiguity is that maybe requiring
    homotopy invariance for just CW complexes is weaker than working in the homotopy
    category of pointed topological spaces. Because CW complexes are in that category,
    but there might be more. But this is resolved by CW approximation, which says
    that for any other space in the homotopy category in particular we can find a CW
    complex with the same homotopy type. So neither definition's statement regarding
    homotopy invariance is stronger.
    We also need to show that the conditions on the exact sequences are the same.
    So here is the homotopy cofiber sequence. What we have to notice is that for
    CW complexes, the mapping cone is a model for the homotopy cofiber. We then 
    recall the suspension isomorphism, so on the level
    of cohomology groups the suspension X suspension why just become degree one higher
    cohomology groups of X and Y, and so we can see that the two exactness requirements
    are equivalent.
    """
    def construct(self):
        t = make_title("Proposition", 1.4)

        self.title(t)

        p1 = TextMobject(r"""
            \begin{itemize}
                \item CW approximation $\Rightarrow$ homotopy invariance
            \end{itemize}
        """).scale(.75).to_title(t)

        p2 = TexMobject(r"""
            X\overset{f}{\longrightarrow}Y\longrightarrow\text{hocofib}(f)\longrightarrow
            \Sigma X\overset{\overline{\Sigma}}{\longrightarrow}\Sigma Y\longrightarrow\cdots
        """).scale(.75).shift(.5*DOWN)

        self.cycle(
            [p1, p2]
        )

class prop14_23(Scene):
    """
    Now let's see how the second and third definitions are equivalent. The first observation
    is that the homotopy category is indeed the localization of its underlying category
    at the weak equivlences. So we can see that definitions two and three share the same
    homotopy invariance conditions. We then recall the universal property of the aforementioned
    localization at the weak equivalences. It states that any functo from the underlying
    category to some other category, in this case Z graded abelian groups, that
    sends weak equivalences to isomorphisms (which cohomology does) factors through the
    localization at the weak equivalences. This shows what we want.
    All this in fact suggests that we could, if we wanted to, consider generalized cohomology
    in terms of any abstract homotopy theory, instead of the particular pointed topological
    spaces we consider here. That's all definition 1.5 says, so we won't go over it 
    explicitly here.
    """
    def construct(self):
        t = make_title("Proposition", 1.4)

        self.add(t)

        p1 = tikz("prop14_23_p1", r"""
            \begin{tikzcd}
                \text{Top}^\text{op}
                    \arrow{r}[above]{F}
                    \arrow{d}[left]{\gamma_{\text{Top}}}
                    & \text{Ab}^\mathbb{Z} \\
                \text{Ho}(\text{Top})^\text{op}\simeq(\text{Top}_\text{CW})/\sim
                    \arrow{ur}[right,yshift=-.5em]{\tilde{F}}
            \end{tikzcd}
        """, fn)

        self.cycle(
            [p1], 
            out=False
        )
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class def16(Scene):
    """
    So given a generlized cohomology theory, we can say that it is in addition
    additive if for pointed CW complexes we can pull out their wedge product in
    the following way, i.e. this morphism is an isomorphism. This is nice since
    it is often useful for calculations to pull out what happens inside the functor
    to make computations tractable.
    We have a few more definitions. So we've been talking about generalized cohomology
    theories, but we say that a cohomology theory is in particular ordinary
    if its value on the 0 sphere is 0 for any degree higher than 0. We say that
    its value on the 0 sphere is concentrated in degree 0. If its not ordinary,
    we can use the word generalized or to be precise we could call it an 
    extraordinary cohomolgy theory.
    So we have two cohomology theories, what does it mean to move between them?
    Well a homomorphism between reduced cohomology theories is a natural transformation
    that is compatible with the suspension isomorphisms as you see here.
    """
    def construct(self):
        t = make_title("Definition", 1.6)

        self.title(t)

        d1 = TextMobject("We say $\\tilde{E}^\\bullet$ is ", "additive", " if")\
            .scale(.75).to_title(t)
        d1[1].set_color(BLUE)

        d2 = TextMobject(r"""
            \begin{itemize}
                \item \textit{(wedge axiom)} For $\{X_i\}_{i\in I}$ any 
                    set of pointed CW-complexes,
                    $$ \tilde{E}^\bullet(\vee_{i\in I}X_i)\overset{\simeq}{\longrightarrow}
                    \prod_{i\in I}\tilde{E}^\bullet (X_i). $$
            \end{itemize}
        """).scale(.75).shift(.5*DOWN,1*LEFT)

        self.cycle(
            [d1, d2]
        )
        
        d3 = TextMobject("We say $\\tilde{E}^\\bullet$ is ", "ordinary", " if")\
            .scale(.75).to_title(t)

        d4 = TextMobject(r"""
            \begin{itemize}
                \item \textit{(Dimension)} $\tilde{E}^{\bullet\neq 0}(S^0)\simeq 0$.
            \end{itemize}
        """).scale(.75).shift(.5*DOWN,1*LEFT)

        self.cycle(
            [d3, d4]
        )

        d5 = TextMobject(r"""
            A homomorphism $\eta:\tilde{E}^\bullet\to\tilde{F}^\bullet$ is a compatible 
            natural transformation:
        """).scale(.75).to_title(t)

        d6 = tikz("def16_d6", r"""
            \begin{tikzcd}
                \tilde{E}^\bullet(X)
                    \arrow{r}[above]{\eta_X}\arrow{d}[left]{\sigma_E}
                    & \tilde{F}^\bullet(X)
                    \arrow{d}[right]{\sigma_F} \\
                \tilde{E}^{\bullet+1}(\Sigma X)
                    \arrow{r}[above]{\eta_{\Sigma X}}
                    & \tilde{F}^{\bullet+1}(\Sigma X)
            \end{tikzcd}
        """, fn).shift(.5*DOWN)

        self.cycle(
            [d5, d6],
            out=False
        )
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class def17(Scene):
    """
    So lets look at the homotopy cofiber sequence, recalling that one of
    our axioms is that the cohomology functor sends this to exact sequences.
    We then recall that there is a suspension isomorphism relating
    the cohomology group of X to the one degree higher cohomology group
    of the suspension of X. So what we want to do is to take that long exact
    sequence so that it only has underlying spaces X and Y and Z.
    The cohomology functor is contravariant, so we have a map from the
    cohomology group of the suspension of X to the cohomology group of Z.
    We can extend this to a map from the one degree lower cohomology group
    of X in the following way, and we call this the connecting homomorphism.
    """
    def construct(self):
        t = make_title("Definition", 1.7)

        self.title(t)

        d1 = TexMobject(r"""
            X
                \overset{f}{\longrightarrow}
            Y
                \overset{g}{\longrightarrow}
            Z
                \overset{\text{coker}(g)}{\longrightarrow}
            \Sigma X
        """).scale(.75)

        self.cycle(
            [d1]
        )

        d2 = TextMobject("A ", "connecting homomorphism", " is the composite")\
            .scale(.75).to_title(t)
        d2[1].set_color(BLUE)

        d3 = TexMobject(r"""
            \partial:\tilde{E}^\bullet(X)
                \overset{\sigma}{\longrightarrow}
            \tilde{E}^{\bullet+1}(\Sigma X)
                \overset{\text{coker}(g)^\ast}{\longrightarrow}
            \tilde{E}^{\bullet+1}(Z)
        """).scale(.75).shift(.5*DOWN)

        self.cycle(
            [d2, d3],
            out=False,
            successive=False
        )
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class prop18(Scene):
    """
    And of course, the point of all this is that this sequence is now exact.
    This is due to the composite was the suspension isomorphism, key word 
    is isomorphism, followed by a map that already fit into a long exact sequence.
    """
    def construct(self):
        t = make_title("Proposition", 1.8)

        self.title(t)

        p1 = TextMobject("The following sequence is exact:")\
            .scale(.75).to_title(t)

        p2 = TexMobject(r"""
            \cdots
                \overset{\partial}{\longrightarrow}
            \tilde{E}^\bullet(Z)
                \longrightarrow
            \tilde{E}^\bullet(Y)
                \longrightarrow
            \tilde{E}^\bullet(X)
                \overset{\partial}{\longrightarrow}
            \tilde{E}^{\bullet+1}(Z)
                \longrightarrow
            \cdots
        """).scale(.75).shift(.5*DOWN)

        self.cycle(
            [p1, p2],
            out=False,
            successive=False
        )
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

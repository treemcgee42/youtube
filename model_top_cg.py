# Date: 2/23/21
# Purpose: model structure of compactly gend spaces nLab
# Notse:

from manimlib.imports import *
fn = "model_top_cg"


class intro(Scene):
    """
    So a theme that we've been returning to time and time again is that Top as a 
    category is not cartesian closed, i.e. mapping spaces XY in general don't satisfy
    the exponential property. They only exist when Y is locally compact. So here's
    three reasons why we'd like cartesian closure. Firstly, the smash product becomes
    associative, obviously a really nice thing. Secondly, we can develop a concept
    of topologically enriched functors. For example, in the stable homotopy theory
    we prove many parts of the model structure on sequential spectra by observing that
    they are equivalent as a category to a category of topologically enriched functors.
    Third, there the geometric realization of simplicial sets preserves products.
    So a geometric realizaiton of a simplicial set is making a topological space
    from a simplicial set, and this is very useful for computations.
    So we want a category that is cartesian closed, a sub category of Top. How do we
    think about what this should be? Well by CW approximation, it suffices for the
    purposes of homotopy to consider CW complexes, so we definetly want our category to
    include those. But we do still want all limits and colimits, as well as to have a
    model structure.
    A full subcategory like this, and this is the category of compact generated
    topological spaces that we turn to now.
    """
    def construct(self):
        i1 = TextMobject(r"""
            \begin{enumerate}
                \item the smash product on pointed topological spaces becomes 
                    associative
                \item there is a concept of topologically enriched functors with values 
                    in topological spaces
                \item geometric realization of simplicial sets preserves products
            \end{enumerate}
        """, alignment="").scale(.75)

        self.cycle(
            [i1]
        )

class def335(Scene):
    """
    So for X a topological space, we say that a subset A of X is compactly closed or k-closed
    if for every continuous function out of a compact Hausdorff space K into X, the preimage
    of A is a closed subset of K.
    The purpose of that technical definition is this. A space X is called compactly generated 
    if its closed subsets coincide with the k-closed subsets. We write Top cg for the
    full subcategory of Top of compactly generated topological spaces.
    """
    def construct(self):
        t = make_title("Definition", 3.35)
        self.title(t)

        d1 = TextMobject(r"""
            Let $X$ be a topological space.
        """, alignment="").scale(.75)

        d2 = TextMobject(r"""
            A subset $A\subset X$ is called \textbf{compactly closed} or 
            $k$-\textbf{closed} if for every continuous function $f:K\to X$ 
            out of a compact Hausdorff space $K$, then the preimage $f^{-1}(A)$ 
            is a closed subset of $K$.
        """, alignment="").scale(.75)

        d3 = TextMobject("The space $X$ is called ", "compactly generated", " ", r"""
            if its closed subsets coincide with the $k$-closed subsets. Write
            $$ \text{Top}_\text{cg}\hookrightarrow\text{Top} $$
            for the full subcategory of $\text{Top}$ on the compactly generated 
            topological spaces.
        """, alignment="").scale(.75)
        d3[1].set_color(BLUE)

        d_1_to_3 = VGroup(
            d1, d2, d3
        ).arrange_submobjects(
            DOWN,
            buff=.5
        )

        self.cycle(
            [d_1_to_3],
            out=False
        )
        self.clear()

class def336(Scene):
    """
    So we'd like to have a functor from Top to Top cg. Here's how we are going to do that.
    So you have a space X in Top, that has an underlying set S and a topology or collection 
    of open sets tau. Then our functor k sends it to the topological space with the same
    underlying set, but whose open sets are the collection of all k-open subsets of X with
    respect to tau.
    I want to point out that to me at least its not obvious that this is a topology, but 
    we won't cover this technicality right now.
    """
    def construct(self):
        t = make_title("Definition", 3.36)
        self.title(t)

        d1 = TexMobject(r"""
            \text{Top}\overset{k}{\longrightarrow}\text{Top}_\text{cg}
            \hookrightarrow\text{Top}
        """).scale(.75)

        d2 = TexMobject(r"""
            (S,\tau)\mapsto (S,k\tau)
        """).scale(.75)

        d_1_to_2 = VGroup(
            d1, d2
        ).arrange_submobjects(
            DOWN,
            buff=1
        )

        self.cycle(
            [d_1_to_2],
            out=False
        )
        self.clear()

class lemma337(Scene):
    """
    So it turns out that this functor k behaves really well. First of all,
    for X in top cg and Y in top, continuous functions between them remain
    continuous when Y is passed to k(Y).
    So it suffices to show that given a k-closed subset A in Y then its
    preimage in X is closed. So pick any continuous function phi from a compact
    Hausdorff space K into X. So f compose phi is a map from K to X. Well since
    A is k closed by assumption, f compose phi inverse of A which is phi inveres
    of f inverse of A is a closed subset in K. Hence f inverse A is k closed in X,
    and since X is by assumption compactly generated, f inverse of A is actually closed
    in X.
    """
    def construct(self):
        t = make_title("Lemma", 3.37)
        self.title(t)

        l1 = TextMobject(r"""
            Let $X\in\text{Top}_\text{cg}\hookrightarrow\text{Top}$ and let $Y\in\text{Top}$.
        """, alignment="").scale(.75).to_title(t)

        l2 = TexMobject(r"""
            X\longrightarrow Y
        """).scale(.75).shift(.5*UP)

        l3 = TexMobject(r"""
            X\longrightarrow k(Y)
        """).scale(.75).next_to(l2, direction=DOWN, buff=.5)

        self.cycle(
            [l1, l2, l3],
            out=False,
            successive=False
        )

        l4 = TexMobject(r"""
            (f\circ\phi)^{-1}(A)=\phi^{-1}(f^{-1}(A))\subset K
        """).scale(.75).to_edge(DOWN, buff=1)

        self.cycle(
            [l4],
            out=False
        )
        self.clear()

class cor338(Scene):
    """
    So here's a cool consequence, theres a natural bijection on these hom sets.
    In particular, we actually have the following adjunction. So this particular
    type of adjunction where the right adjunct is the inclusion is what we mean when 
    we call Topcg or whatever category a coreflective subcategory with coreflector k.
    Also observe that k is idempotent.
    Colimits in Top cg exist and are computed as in Top. Limits in Top cg exist,
    and we compute them in Top and apply k to the result.
    """
    def construct(self):
        t = make_title("Corollary", 3.38)
        self.title(t)

        c1 = TexMobject(r"""
            \text{Hom}_\text{Top}(X,Y)\simeq\text{Hom}_{\text{Top}_\text{cg}}(X,k(Y))
        """).scale(.75)

        c2 = TexMobject(r"""
            \text{Top}_\text{cg}
            \underoverset
                {\underset{k}{\longleftarrow}}
                {\hookrightarrow}
                {\bot}
            \text{Top}
        """).scale(.75)

        c3 = TexMobject(r"""
            k(k(X))\simeq k(X)
        """).scale(.75)

        c_1_to_3 = VGroup(
            c1, c2, c3
        ).arrange_submobjects(
            DOWN,
            buff=1
        )

        self.cycle(
            [c1, c2, c3],
            out=False
        )
        self.clear()

class def339(Scene):
    """
    So what are mapping spaces here? As a bit of forewarning, you've probably noticed 
    that we are laying out technical results but ommiting proofs, because our main
    goal is abstract homotopy theory here. The nLab provides references if you're interested,
    but I hope to atleast convey the idea. So for compactly generated mapping spaces,
    we'd like it to coincide with the typical compact open topology in certain
    scenarios, but be modified so we have the exponential property. So here's
    how we will define it. XY is the set of continuous functions from Y to X
    of course, and its subbase is given by elements of the following form. This
    definition agrees with the compact open topology when Y is a compactly generated
    Hausdorff space, but in general it is not the same. By abuse of notation, some
    people say compact-open topology for both of these topologies, even when they don't 
    agree, so we need to be careful.
    """
    def construct(self):
        t = make_title("Definition", 3.39)
        self.title(t)

        d1 = TextMobject(r"""
            For $X,Y\in\text{Top}_\text{cg}$, the 
        """, "compactly generated mapping space", " ", r"""
            $X^Y\in\text{Top}_\text{cg}$ is the compactly generated topological space whose 
            underlying set is the set $C(Y,X)$ of continuous functions $f:Y\to X$, and for 
            which a subbase for its topology has element $U^{\phi(K)}$, for $U\subset X$ any 
            open subset and $\phi:K\to Y$ a continuous functions out of a compact Hausdorff 
            space $K$ given by
            $$ U^{\phi(K)}:= \{f\in C(Y,X)\mid f(\phi(K))\subset U\} $$
        """, alignment="").scale(.75)
        d1[1].set_color(BLUE)

        self.cycle(
            [d1],
            out=False
        )
        self.clear()

class prop341(Scene):
    """
    So this is what we've been wanting to show: Top cg is indeed cartesian
    closed. In other words, we have this adjunction.
    """
    def construct(self):
        t = make_title("Proposition", 3.41)
        self.title(t)

        p1 = TexMobject(r"""
            \text{Top}_\text{cg}
            \underoverset
            {\underset{(-)^X}{\longrightarrow}}
            {\overset{X \times (-)}{\longleftarrow}}
            {\bot}
            \text{Top}_\text{cg}
        """).scale(.75)

        self.cycle(
            [p1],
            out=False
        )
        self.clear()

class cor342(Scene):
    """
    So in pointed spaces the analogy for the cartesian product was the smash product.
    Indeed, if we specialize to pointed compactly generated topological spaces, defining
    pointed mapping spaces in this way, then we have this adjunction as we expect.
    """
    def construct(self):
        t = make_title("Corollary", 3.42)
        self.title(t)

        c1 = TexMobject(r"""
            \text{Maps}(Y,X)_\ast
            :=
            \text{fib}\left(
                X^Y \overset{\text{ev}_y}{\longrightarrow} X
                ,
                x
            \right)
        """).scale(.75)

        c2 = TexMobject(r"""
            \text{Top}_\text{cg}^{\ast/}
            \underoverset
            {\underset{\text{Maps}(Y,-)_\ast}{\longrightarrow}}
            {\overset{Y \wedge (-)}{\longleftarrow}}
            {\bot}
            \text{Top}_\text{cg}^{\ast/}
        """).scale(.75)

        c_1_to_2 = VGroup(
            c1, c2
        ).arrange_submobjects(
            DOWN,
            buff=1
        )

        self.cycle(
            [c1, c2],
            out=False,
            successive=False
        )
        self.clear()

class cor343(Scene):
    """
    So here's a really cool fact. Under the assumptions here, we can
    pull out limits and colimits in the following way. So if the limit
    is in the second also called covariant argument, then it pulls out
    to a limit. This is just a property of being an adjoint. The more interesting
    result is that if there is a colimit in the first or contravariant argument, then
    it pulls out to a limit. Note that these are already established properties of
    Hom sets, we are just trying to show that this property applies to pointed
    compactly generated mapping spaces as well.
    So let's see why this second statement would be true. So compactly generated sets
    are entirely characterized by the continuous functions out of compact Hausdorff
    spaces into them, by definition. Hence it suffices to show that these two things
    are naturally isomorphic for any compact Hausdorff space K. Well by the first statement
    we can apply the smash hom adjunction we just showed to the left. In the second step
    we rearrange the colimit, and in the third we use the property of hom sets that takes
    colimits in its contravariant argument to limits outside. The fourth step applies the
    adjunction again, and we use the property of hom sets again to move the limit back
    inside to to covariant argument, and we are done.
    """
    def construct(self):
        t = make_title("Corollary", 3.43)
        self.title(t)

        c1 = TextMobject(r"""
            For $I$ a small category,
        """, alignment="").scale(.75).to_title(t)

        c2 = TexMobject(r"""
            \text{Maps}(X,\underset{\longleftarrow i}{\lim}Y_i)_\ast \simeq
                \underset{\longleftarrow i}{\lim}\text{Maps}(X,Y_i)_\ast
        """).scale(.75)

        c3 = TexMobject(r"""
            \text{Maps}(\underset{\longrightarrow i}{\lim}X_i, Y)_\ast \simeq
                \underset{\longleftarrow i}{\lim}\text{Maps}(X_i,Y)_\ast
        """).scale(.75).next_to(c2, direction=DOWN, buff=.5)

        self.cycle(
            [c1, c2, c3],
            successive=False
        )

        c4 = TexMobject(r"""
            \text{Hom}_{\text{Top}_\text{cg}^{\ast /}}\left(
            \text{Maps}(\underset{\longrightarrow i}{\lim}X_i, Y)_\ast\right)
            \simeq \text{Hom}_{\text{Top}_\text{cg}^{\ast /}}\left(
                \underset{\longleftarrow i}{\lim}\text{Maps}(X_i,Y)_\ast\right)
        """).scale(.75).shift(2*UP)

        c5 = TextMobject(r"""
            \begin{align*}
                \text{Hom}_{\text{Top}_\text{cg}^{\ast /}}\left(K,\text{Maps}
                (\underset{\longrightarrow i}{\lim}X_i, Y)_\ast\right)
                \simeq &
                \text{Hom}_{\text{Top}_\text{cg}^{\ast /}}\left( K\wedge
                \underset{\longrightarrow i}{\lim}X_i, Y\right) \\
                \simeq &
                \text{Hom}_{\text{Top}_\text{cg}^{\ast /}}\left(
                \underset{\longrightarrow i}{\lim}(K\wedge X_i),Y\right) \\
                \simeq & \underset{\longleftarrow i}{\lim}\left(
                \text{Hom}_{\text{Top}_\text{cg}^{\ast /}}(
                K\wedge X_i, Y)\right) \\
                \simeq & \underset{\longleftarrow i}{\lim}\text{Hom}_{\text{Top}_\text{cg}^{\ast /}}
                (K,\text{Maps}(X_i,Y)_\ast) \\
                \simeq & \text{Hom}_{\text{Top}_\text{cg}^{\ast /}}\left(K,
                \underset{\longleftarrow i}{\lim}\text{Maps}(X_i,Y)_\ast\right)
            \end{align*}
        """).scale(.75).shift(1*DOWN)

        self.cycle(
            [c4, c5],
            out=False
        )
        self.clear()

class prop344(Scene):
    """
    Here's another thing we were aiming for: that the smash product becomes associative.
    The unit or tensor unit is the 0 sphere as you might expect.
    Let's prove this. Well we showed earlier that the cartesian product in this category
    is now left adjoint to the mapping space here, and so it preserves colimits,
    and in particular quotient space projections. Hence we can compute this, and analagously
    the other way.
    """
    def construct(self):
        t = make_title("Proposition", 3.44)
        self.title(t)

        p1 = TextMobject(r"""
            On pointed compactly generated topological spaces, the smash product 
            $$ (-)\wedge (-):\text{Top}_\text{cg}^{\ast /}\times\text{Top}_\text{cg}^{\ast /}
            \longrightarrow \text{Top}_\text{cg}^{\ast /} $$
            is associative and the 0-sphere is a tensor unit for it.
        """, alignment="").scale(.75).shift(.5*LEFT)

        self.cycle(
            [p1]
        )

        p2 = TextMobject(r"""
            \begin{align*}
                (X\wedge Y)\wedge Z) = &
                    \dfrac{
                        \frac{X\times Y}{X\times\{y\}\sqcup\{x\}\times Y}\times Z
                    }{(X\wedge Y)\times\{z\}\sqcup\{[x]=[y]\}\times Z} \\
                \simeq & \dfrac{
                    \frac{X\times Y\times Z}{X\times\{y\}\times Z\sqcup\{x\}\times Y\times Z}
                }{X\times Y\times\{z\}} \\
                    \simeq & \dfrac{X\times Y\times Z}{X\vee Y\vee Z}
            \end{align*}
        """).scale(.75)

        self.cycle(
            [p2],
            out=False
        )
        self.clear()

class rmk345(Scene):
    """
    Technically speaking, this associativity gives us that the category of
    pointed compactly generated topological spaces is a closed symmetric
    monoidal category. So are unpointed compactly generated spaces, but those
    have the added property of being cartesian.
    So you might think that its bad to be not cartesian, but this isn't the case.
    So think about the cartesian product of two vectors spaces versus their tensor
    product. Their tensor product is really the full linearization do the the
    way its elements interact with each other, which is why it's so useful to consider.
    Likewise, pointed Top cg is more linear than top cg, but it actually isn't the
    full linearization. The full linearization of top cg turns out to be structured
    spectra, which we will discuss in our series on spectra.
    """
    def construct(self):
        t = make_title("Remark", 3.45)
        self.title(t)

        r1 = TexMobject(r"""
            (\text{Top}_\text{cg}^{\ast /},\wedge,S^0)
        """).scale(.75)

        r2 = TexMobject(r"""
            (\text{Top}_\text{cg},\times,\ast)
        """).scale(.75)

        r_1_to_2 = VGroup(
            r1, r2
        ).arrange_submobjects(
            DOWN,
            buff=1
        )

        self.cycle(
            [r1, r2],
            out=False
        )
        self.clear()

class ex346(Scene):
    """
    So remember that k was idempotent, meaning k^2 = k. Well, intuitively that means 
    that k applied to something that was already compactly generated doesn't change 
    it, so lets cover a few examples of things that are already compactly generated.
    These include every CW complex, all locally compact topological spaces, all
    first countable topological spaces hence metrizable, discrete, and codiscrete topological
    spaces.
    """
    def construct(self):
        t = make_title("Example", 3.46)
        self.title(t)

        e1 = TextMobject(r"""
            \begin{enumerate}
                \item every CW-complex
                \item all locally compact topological spaces
                \item all first-countable topological spaces
                    \begin{enumerate}
                        \item all metrizable topological spaces
                        \item all discrete topological spaces
                        \item all codiscrete topological spaces
                    \end{enumerate}
            \end{enumerate}
        """).scale(.75)

        self.cycle(
            [e1],
            out=False
        )
        self.clear()

class ex348(Scene):
    """
    So while in general products of compactly generated spaces aren't
    compactly generated themselves, it turns out that the product of a CW complex with
    a compact, or even more generally locally compact CW complex, is indeed compactly
    generated.
    """
    def construct(self):
        t = make_title("Example", 3.48)
        self.title(t)

        e1 = TextMobject(r"""
            The product topological space of a CW-complex with a compact CW-complex, 
            and more generally with a locally compact CW-complex, is compactly generated.
        """, alignment="").scale(.75)

        self.cycle(
            [e1],
            out=False
        )
        self.clear()

class prop349(Scene):
    """
    So more generally, for X a compactly generated space and Y a locally compact
    Hausdorff space, the product X cross Y is compactly generated.
    """
    def construct(self):
        t = make_title("Proposition", 3.49)
        self.title(t)

        p1 = TextMobject(r"""
            For $X$ a compactly generated space and $Y$ a locally compact Hausdorff 
            space, then the product topological space $X\times Y$ is compactly generated.
        """, alignment="").scale(.75)

        self.cycle(
            [p1],
            out=False
        )
        self.clear()

class prop350(Scene):
    """
    And indeed, k(X) to X is a weak homotopy equivalence as we'd hope, and this is
    essentially due to the bijection of continuous functions and their homotopies.
    """
    def construct(self):
        t = make_title("Proposition", "3.50")
        self.title(t)

        p1 = TextMobject(r"""
            For every topological space $X$, the canonical function $k(X)\to X$ is 
            a weak homotopy equivalence.
        """, alignment="").scale(.75)

        self.cycle(
            [p1],
            out=False
        )
        self.clear()

class thm351(Scene):
    """
    And here's the big punchline. The restriction of the model category structure on Top
    quillen to top cg exhibits the model category structure on Top cg, and in fact
    the same sets I top and Jtop that exhibited top quillen as cofibrantly generated
    exhibits Top cg as cofibrantly generated. Finally, the coreflection is also a Quillen
    adjunction.
    So really this is everything we hoped for, we still capture the homotopical essence of Top
    Quillen while gaining a lot of nice properties that Top Quillen didn't have.
    """
    def construct(self):
        t = make_title("Theorem", 3.51)
        self.title(t)

        t1 = TextMobject(r"""
            The restriction of the model category structure on $\text{Top}_\text{Quillen}$ 
            along the inclusion $\text{Top}_\text{cg}\hookrightarrow\text{Top}$ is still a 
            model category structure, and is cofibrantly generated still by $I_\text{Top}$ 
            and $J_\text{Top}$. The coreflection is a Quillen equivalence:
            $$ (\text{Top}_\text{cg})_\text{Quillen}
            \underoverset
            {\underset{k}{\longleftarrow}}
            {\hookrightarrow}
            {\bot}
            \text{Top}_\text{Quillen} $$
        """, alignment="").scale(.75)

        self.cycle(
            [t1],
            out=False
        )
        self.clear()

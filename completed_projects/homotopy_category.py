# Date: 2/20/21
# Purpose: homotopy category section nLab
# Notes: recorded 2/23/21

from manimlib.imports import *
fn = "homotopy_category"


class def225(Scene):
    """
    So we'd like to isolate the homotopy related parts of a model category. Here's
    one such construction. As we will show, this is the one that forces all the
    weak equivalences of the model category to turn into actual isomorphisms.
    So given a model category C, we write Ho C for the category whose objects are
    the objects of C which are both fibrant and cofibrant, and whose morphisms
    are the homotpy classes of morphisms of C (we showed last time that these
    are equivalence classes of morphisms, hence our nomenclature). The composition
    of two classes is the class of the composition of representative. We call Ho C
    the homotopy category of the model category C.
    """
    def construct(self):
        t = make_title("Definition", 2.25)
        self.title(t)

        d1 = TextMobject("Let $C$ be a model category. The ",\
            "homotopy category of the model category", ", $\\text{Ho}(\\mathcal{C})$",\
             " is", r"""
            \begin{itemize}
                \item objects are those objects of $\mathcal{C}$ which are both fibrant 
                    and cofibrant
                \item morphisms are homotopy classes of morphisms of $\mathcal{C}$ with 
                    composition given on representatives by composition in $\mathcal{C}$
            \end{itemize}
        """, alignment="").scale(.75).to_title(t)
        d1[1].set_color(BLUE)

        self.cycle(
            [d1],
            out=False
        )
        self.clear()

class prop226(Scene):
    """
    The only ambiguity that could make the definition above not well defined is our condition
    on composition. Is the composition of homotopy classes really the homotopy class of the 
    composition of any two representatives?
    Well, yes, and to see this let f be the representative of the homotopy class of a map from 
    X to Y. We want to show that given two maps g and h from Y to Z, if they are in then same
    homotopy class, then so is fg and fh. Again, all objects are assumed to be both fibrant 
    and cofibrant. Well, since the notions of right and left homotopy coincide, we can make the
    following diagram to exhibit the homotopy by assumption from g to h. And this exhibits the
    homotopy from fg and fh as well.
    This showed the case of precomposition, but for postcomposition we argue dually, drawing the
    diagram with a left homotopy instead.
    """
    def construct(self):
        t = make_title("Proposition", 2.26)
        self.title(t)

        p1 = TextMobject(r"""
            Composition of morphisms between fibrant-cofibrant objects in $\mathcal{C}$ 
            indeed passes to homotopy classes.
        """, alignment="").scale(.75).to_title(t)

        p2 = tikz("prop226_p2", r"""
        \begin{tikzcd}
            & & Z \\
            X
                \arrow{r}[above]{f}
                & Y
                \arrow{ur}[left,yshift=.5em]{g}\arrow{r}[above]{\eta}\arrow{dr}[left,yshift=-.5em]{h}
                & \text{Path}(Z)
                \arrow{u}[right]{p_1}\arrow{d}[right]{p_0} \\
            & & Z
        \end{tikzcd}
        """, fn).shift(1*DOWN).scale(1.5)

        self.cycle(
            [p1, p2],
            out=False
        )
        self.clear()

class lemma227(Scene):
    """
    So let's get back to what we said earlier, that the homotopy category is the one
    which forces weak equivalence to become isomorphisms. Well what is an isomorphism in
    the homotopy category? So intuitively this would be homotopy equivalences, and we'll show
    this a little later. For now, we have this lemma, which is called the Whitehead theorem
    in model categories. If you recall the topological Whitehead theorem said that a weak
    equivalence between CW complex implied a homotopy equivalence. We mentioned briefly that
    CW complexes are both fibrant and cofibrant, so this lemma is upgrading that result to 
    model categories.
    So how do we see this? Well lets start with a weak equivalence. We can factor it as an
    acyclic cofibration followed by a fibration, but since it is a weak equivalence by two
    out of three we can factor it as an acyclic cofibration followed by an acyclic fibration.
    Well so this middle object Z is a fibrant cofibrant object as well, i.e. pre and postcompose
    with the appropriate fibrations and cofibrations from X and Y. But ok, to show that the entire
    map is a homotopy equivalence, since it factors as an acyclic cofibration followed by an acyclic
    fibration it suffices to show that these maps are homotopy equivalences.
    So we will show that acyclic fibrations between fibrant cofibrant objects are homotopy 
    equivalences, and the case for acyclic cofibrations is just dual. Ok, suppose f from X
    to Y is an acyclic fibration between fibrant cofibrant objects. Then the following diagram
    lifts, and so it has a right inverse. How did we get the lift? Well, because of the map
    on the left, which is a cofibration since Y is by assumption cofibrant. So it remains
    to show that this map is also a left inverse up to left homotopy.
    So pick a cylinder object on X. Well then we have this commuting square. The left
    map is a cofibration since cylinder objects factor the codiagonal as a cofibration
    followed by an acyclic fibration. You might be wondering how on the top we have
    f inverse compose f if we only know that f inverse is a right inverse of f, i.e. that
    f compose f inverse is the identity. Well all we need is commutativity, and the previous
    diagram did give us at least that.
    But anyways, we have this diagram, which if you stare at it for a second reveals
    the desired left homotopy between f inverse compose f and the identity.
    """
    def construct(self):
        t = make_title("Lemma", 2.27)
        self.title(t)

        l1 = TextMobject(r"""
            Let $\mathcal{C}$ be a model category. A weak equivalence between two 
            objects which are both fibrant and cofibrant is a homotopy equivalence.
        """, alignment="").scale(.75).to_title(t)

        l2 = tikz("lemma227_l2", r"""
            \begin{tikzcd}
                0
                    \arrow{r}\arrow{d}[left]{\in\text{Cof}}
                    & X
                    \arrow{d}[right]{f\in\text{Fib}\cap W} \\
                Y
                    \arrow[dashed]{ur}[left,yshift=.5em]{f^{-1}}\arrow{r}[above]{=}
                    & Y
            \end{tikzcd}
        """, fn).shift(1*DOWN)

        self.cycle(
            [l1, l2],
            out=False
        )

        l3 = tikz("lemma227_l3", r"""
            \begin{tikzcd}
                X\sqcup X
                    \arrow{d}[left]{\in\text{Cof}}\arrow{r}[above]{(f^{-1}\circ f,\text{id})}
                    & X
                    \arrow{d}[right]{f\in W\cap\text{Fib}} \\
                \text{Cyl}(X)
                    \arrow{r}[below]{f\circ p}
                    & Y
            \end{tikzcd}
        """, fn).shift(1*DOWN)

        self.fade_replace(
            l2, l3
        )
        self.clear()

class def228(Scene):
    """
    Ok, so this homotopy category wouldn't be super useful if we didn't have a way 
    to move from the original model category to the corresponding homotopy category.
    So let's make a functor between these categories. On the level of objects, here's 
    what it does. So pick an object X in C. Consider the initial morphism. We can
    factor this as a cofibration followed by an acyclic fibration, of course.
    Is X is fibrant, we further require that this second map is the identity on X.
    Intuitively think of how we could just set QX to X. Also consider the terminal
    morphism from X. Again, we can factor this as an acyclic cofibration followed by
    a fibration, and again we require the first map to be the identity on X if X was
    fibrant. Note that the choices of these intermidiary objects are not at canonical-
    they are choices.
    So here's how we actually get an object in the homotopy category. This
    functor sends X to PQX. So apply first process to the inital morphism and get QX,
    then apply the second to this QX and get PQX.
    Ok, what does this functor do to a morphism from X to Y? Well so do what I described,
    obtain QX and QY first. We have this diagram, and since the first morphism is a 
    cofibration and the second is an acyclic fibration by assumption, we have a lift from QX
    to QY. Then we just do this again after forming PQX and PQY.
    """
    def construct(self):
        t = make_title("Definition", 2.28)
        self.title(t)

        d1 = TextMobject(r"""
            Given a model category $\mathcal{C}$, consider a choice for each object 
            $X\in\mathcal{C}$ of
            \begin{itemize} 
                \item a factorization 
                    $\emptyset
                        \underoverset{\in\text{Cof}}{i_X}{\longrightarrow}
                    QX
                        \underoverset{\in W\cap\text{Fib}}{p_X}{\longrightarrow}
                    X$ 
                    of the initial morphism, such that when $X$ is already cofibrant 
                    then $p_X=\text{id}_X$
                \item a factorization 
                    $ X
                        \underoverset{\in W\cap\text{Cof}}{j_X}{\longrightarrow}
                    PX
                        \underoverset{\in\text{Fib}}{q_X}{\longrightarrow}
                    \ast$ 
                    of the initial morphism, such that when $X$ is already fibrant 
                    then $j_X=\text{id}_X$
            \end{itemize}
        """, alignment="").scale(.75).to_title(t)

        self.cycle(
            [d1]
        )

        d2 = TexMobject(r"""
            \gamma_{P,Q}:\mathcal{C}\longrightarrow\text{Ho}(\mathcal{C})
        """).scale(.75).shift(4*LEFT, .5*UP)

        d3 = TexMobject(r"""
            X\mapsto PQX \\
            f\mapsto PQf
        """).scale(.75).next_to(d2, direction=DOWN, buff=.5)
        
        d4 = tikz("def228_d4", r"""
            \begin{tikzcd}
                0
                    \arrow{r}\arrow{d}[left]{i_X}
                    & QY
                    \arrow{d}[right]{p_Y} \\
                QX
                    \arrow{ur}[left,yshift=.5em]{Qf}\arrow{r}[below]{f\circ p_X}
                    & Y
            \end{tikzcd}
        """, fn).shift(3*RIGHT, 1*UP)

        d5 = tikz("def228_d5", r"""
            \begin{tikzcd}
                QX
                    \arrow{d}[left]{j_{QX}}\arrow{r}[above]{j_{QY}\circ Qf}
                    & PQY
                    \arrow{d}[right]{q_{QY}} \\
                PQX
                    \arrow{ur}[left,yshift=.5em]{PQf}\arrow{r}
                    & \ast
            \end{tikzcd}
        """, fn).next_to(d4, direction=DOWN, buff=1)

        self.cycle(
            [d2, d3, d4, d5],
            out=False
        )
        self.clear()

class lemma229(Scene):
    """
    Ok, we definitely need to check that this functor is well defined. It's not
    at all clear that it is.
    So first of all, is PQX even fibrant-cofibrant? Just consider this diagram, and
    it's clear that it is pretty directly from construnction.
    So let's see now if the morphisms are well defined. First consider two lifts from earlier
    from QX to QY given a map f from X to Y. Then we have this diagram, which lifts and
    exhibits a left homotopy between those two lifts. So the top map is these two lifts.
    The other ambiguous one is the bottom map, which is just the map Cyl Qx to QX given
    by the codiagonal map, followed by the map from QX to X from the factorization of the
    initial morphism to X, and finally followed by the map f from X to Y. Well QX and
    QY are cofibrant by assumption, so they are also right homotopic to each other.
    So the postcomposition of both of these maps with the map from QY to PQY are also
    right homotopic by a map, call it kappa. 
    So now apply P to this to get PQX and PQY. Suppose we have two lifts from PQX to PQY.
    Now we have this diagram which admits a lift, so these two maps are homotopic, and so 
    PQf is well defined, i.e. the functor is well defined on morphisms.
    Well does this functor respect composition? We can see this by looking at this
    diagram. You can rearrange this to convince yourself that PQg followed by PQf is a 
    lift in the sense we were talking about when showing morphisms were well defined. 
    Then by that same argument it is homotopic to PQ(g compose f), and we are done.
    """
    def construct(self):
        t = make_title("Lemma", 2.29)
        self.title(t)

        l1 = tikz("lemma229_l1", r"""
            \begin{tikzcd}
                0 
                    \arrow{d}[left]{\in\text{Cof}}\arrow{dr}[right,yshift=.5em]{\in\text{Cof}}
                    & & \\
                QX
                    \arrow{r}[below]{\in W\cap\text{Cof}}\arrow{d}[left]{\in W}
                    & PQX\arrow{r}[below]{\in\text{Fib}}
                    & \ast\\
                X
            \end{tikzcd}
        """, fn).scale(1.5)

        self.cycle(
            [l1],
            out=False
        )

        l2 = tikz("lemma229_l2", r"""
            \begin{tikzcd}[column sep=huge]
                QX\sqcup QX
                    \arrow{d}[left]{\in\text{Cof}}\arrow{r}[above]{((Qf)_1, (Qf)_2)}
                    & QY
                    \arrow{d}[right]{p_Y\in W\cap\text{Fib}} \\
                \text{Cyl}(QX)
                    \arrow{r}[below]{f\circ p_X\circ\sigma_{QX}}
                    & Y
            \end{tikzcd}
        """, fn)

        self.fade_replace(
            l1, l2
        )

        l3 = tikz("lemma229_l3", r"""
            \begin{tikzcd}[column sep=huge]
                QX
                    \arrow{d}[left]{\in W\cap\text{Cof}}\arrow{r}[above]{\kappa}
                    & \text{Path}(PQY)
                    \arrow{d}[right]{\in \text{Fib}} \\
                PQX
                    \arrow{r}[below]{(P(Qf)_1, P(Qf)_2)}
                    & PQY\times PQY
            \end{tikzcd}
        """, fn)

        self.fade_replace(
            l2, l3
        )

        l4 = tikz("lemma229_l4", r"""
            \begin{tikzcd}
                X
                    \arrow{d}[left]{f}
                    & QX
                    \arrow{l}[above]{p_X}\arrow{d}[right]{Qf}\arrow{r}[above]{j_{QX}}
                    & PQX
                    \arrow{d}[right]{PQf} \\
                Y
                    & QY
                    \arrow{l}[below]{p_y}\arrow{r}[below]{j_{QY}}
                    & PQY
            \end{tikzcd}
        """, fn)

        self.fade_replace(
            l3, l4
        )

        l5 = tikz("lemma229_l5", r"""
            \begin{tikzcd}
                X
                    \arrow{d}[left]{f}
                    & QX
                    \arrow{l}[above]{p_X}\arrow{d}[right]{Qf}\arrow{r}[above]{j_{QX}}
                    & PQX
                    \arrow{d}[right]{PQf} \\
                Y
                    \arrow{d}[left]{g}
                    & QY
                    \arrow{l}[below]{p_y}\arrow{r}[below]{j_{QY}}\arrow{d}[right]{Q_g}
                    & PQY
                    \arrow{d}[right]{PQ_g} \\
                Z
                    & QZ
                    \arrow{l}[below]{p_Z}\arrow{r}[below]{j_{QZ}}
                    & PQZ
            \end{tikzcd}
        """, fn).scale(1.5)

        self.fade_replace(
            l4, l5
        )
        self.clear()

class def230(Scene):
    """
    We're finally ready to return to the claim made earlier that the homotopy category
    is the one that forces weak equivalences to become isomorphisms. So here's a definition.
    Given a category with weak equivalences, its localization is another category
    and a functor to this new category from the original that sends weak equivalences to
    isomorphisms, and is universal with this property. So for any other functor to another
    category D that sends weak equivalences to isomorphisms, that new functor will
    factor through gamma up to natural isomorphism. This factorization will be unique up
    up to natural isomorphism. So in particular given two maps f one and f two tilde,
    there is a unique natural isomorphism from f one tilde to f2 tilde.
    So to be careful, its isn't gaurenteed that a localization even exists. Also, the term
    localization can be more general. Like, given a subclass of morphisms K, then a localization
    at K sends morphisms to K to isomorphisms. But for our purposes, we will say localization
    to mean a localization at the weak equivalences.
    """
    def construct(self):
        t = make_title("Definition", "2.30")
        self.title(t)

        d1 = TextMobject("For $\\mathcal{C}$ a category with weak \
            equivalences, its ", "localization", " ", r"""
            at the weak equivalences is, if it exists,
            \begin{enumerate}
                \item a category denoted $\mathcal{C}[W^{-1} ]$
                \item a functor
                    $$\gamma:\mathcal{C}\longrightarrow\mathcal{C}\left[W^{-1}\right]$$
            \end{enumerate}
        """, alignment="").scale(.75).to_title(t)

        d2 = TextMobject(r"""
            \begin{enumerate}
                \item $\gamma$ sends weak equivalences to isomorphisms
                \item $\gamma$ is universal with this property:
                    $$
                    \begin{matrix}
    \mathcal{C} & & \overset{F}{\longrightarrow} & & D \\
    & {}_{\mathllap{\gamma}}\searrow &\Downarrow^{\rho}& \nearrow_{\mathrlap{\tilde F}} \\
    & & \text{Ho}(\mathcal{C})
  \end{matrix}
                    $$
            \end{enumerate}
        """, alignment="").scale(.75).to_edge(LEFT, buff=.5)

        self.cycle(
            [d1],
            out=False
        )

        self.fade_replace(
            d1, d2
        )
        self.clear()

class thm231(Scene):
    """
    So here's the theorem we've been aluding to. For a model category C, the homotopy
    category is indeed that localization of the underlying category with weak equivalences.
    This is exhibited by the functor gamma p q, which is from before, e.g. the one that
    sent objects X to PQX.
    So let's prove this.
    So remember that isomorphisms in the homotopy category are homotopy equivalences.
    We have this diagram from before, and we want to show that the right morphism
    is a homotopy equivalence if f is a weak homotopy equivalence. Well by the Whitehead
    theorem for model categories, it suffices to show that this make is a weak equivalence,
    but this follows by repeated application of two-out-of-three.
    So it remains to show universality. Well let F be any functor that sends weak equivalences to
    isomorphisms. We need to show that it factors in the following way uniquely up to unique
    isomorphism in the sense we just covered. Well remember how we required gamma P Q was the 
    identity on
    fibrant cofibrant objects? So if a factorization F tilde even existed, which we're not
    claiming right now it does, it must send images of maps between fibrant cofibrant objects 
    under gamma to what F sends the map to. 
    But the homotopy category has only fibrant
    cofibrant objects, and hence F is fixed up to unique natural isomorphism on the homotopy
    category. In particular, it sends maps between images in the homotopy category from 
    the original category to what F would have sent PQf to. We use this fact later.
    The only thing left to show in the diagram is that there is a natural isomorphism rho.
    F is a functor, so apply it to the commuting diagram from before. the morphisms,
    which were weak equivalences, are by assumption sent to isomorphisms. So then just
    define rho for the choice of X to be the map from F(X) to F(PQX) on the top, so 
    of course reversing that first morphism from F(X) to F(QX), which we can do since its
    an isomorphism. Hence we have this diagram, which exhibits the desired natural
    isomorphism. Because it is an isomorphism and not just a homomorphism, we are done.
    """
    def construct(self):
        t = make_title("Theorem", 2.31)
        self.title(t)

        t1 = tikz("thm231_t1", r"""
            \begin{tikzcd}
                \mathcal{C}
                    \arrow{d}[left]{\gamma_{P,Q}}\arrow{r}[above]{=}
                    & \mathcal{C}
                    \arrow{d}[right]{\gamma} \\
                \text{Ho}(\mathcal{C})
                    \arrow{r}[above]{\simeq}
                    & \mathcal{C}[W^{-1}]
            \end{tikzcd}
        """, fn)

        self.cycle(
            [t1]
        )

        t2 = tikz("thm231_t2", r"""
            \begin{tikzcd}
                X
                    \arrow{d}[left]{f}
                    & QX
                    \arrow{l}[above]{p_X}[below]{\simeq}\arrow{d}[right]{Qf}
                        \arrow{r}[above]{j_{QX}}[below]{\simeq}
                    & PQX
                    \arrow{d}[right]{PQf} \\
                Y
                    & QY
                    \arrow{l}[above]{\simeq}[below]{p_y}\arrow{r}[above]{\simeq}[below]{j_{QY}}
                    & PQY
            \end{tikzcd}
        """, fn)

        self.cycle(
            [t2],
            out=False
        )

        t3 = TextMobject(r"""
                    $$
                    \begin{matrix}
    \mathcal{C} & & \overset{F}{\longrightarrow} & & D \\
    & {}_{\mathllap{\gamma}}\searrow &\Downarrow^{\rho}& \nearrow_{\mathrlap{\tilde F}} \\
    & & \text{Ho}(\mathcal{C})
  \end{matrix}
                    $$
        """).scale(.75)

        self.fade_replace(
            t2, t3
        )

        t4 = tikz("thm231_t4", r"""
            \begin{tikzcd}
                F(X)
                    \arrow{d}[left]{F(f)}
                    & F(QX)
                    \arrow{d}[right]{F(Qf)}\arrow{l}[above]{F(p_X)}[below]{\text{iso}}
                        \arrow{r}[above]{F(j_{QX})}
                    & F(PQX)
                    \arrow{d}[right]{F(PQf)} \\
                F(Y)
                    & F(QY)
                    \arrow{l}[above]{\text{iso}}[below]{F(p_y)}
                        \arrow{r}[above]{\text{iso}}[below]{F(j_{QY})}
                    & F(PQY)
            \end{tikzcd}
        """, fn)

        self.fade_replace(
            t3, t4
        )

        t5 = tikz("thm231_t5", r"""
            \begin{tikzcd}
                \rho_X: & F(X)
                    \arrow{d}[left]{F(f)}\arrow{r}[above]{F(p_X)^{-1}}[below]{\text{iso}}
                    & F(QX)
                    \arrow{r}[above]{F(j_{QX})}
                    & F(PQX)
                    \arrow{d}[right]{F(PQf)}\arrow{r}[above]{=} 
                    & \tilde{F}(\gamma_{P,Q}(X))
                    \arrow{d}[right]{\tilde{F}(\gamma_{P,Q}(f))}\\
                \rho_Y: & F(Y)
                    \arrow{r}[above]{\text{iso}}[below]{F(p_y)^{-1}}
                    & F(QY)
                    \arrow{r}[above]{\text{iso}}[below]{F(j_{QY})}
                    & F(PQY)
                    \arrow{r}[above]{=}
                    & \tilde{F}(\gamma_{P,Q}(X))
            \end{tikzcd}
        """, fn)

        self.fade_replace(
            t4, t5
        )
        self.clear()

class rmk232(Scene):
    """
    If you've been paying attention, you might have observed that we never resolved that
    forming P and Q was a choice, not canonical. But with what we have just shown, we now
    know that it doesn't really matter, and we can just speak of The functor, gamma, which
    we will call the localization functor, which is unique up to isomorphism.
    This is a cool result of the model category structure.
    """
    def construct(self):
        t = make_title("Remark", 2.32)
        self.title(t)

        r1 = TexMobject(r"""
            \gamma: \mathcal{C}\longrightarrow\text{Ho}(\mathcal{C})
        """).scale(.75)

        self.cycle(
            [r1],
            out=False
        )
        self.clear()

class prop233(Scene):
    """
    In general, the localization of a 
    category fo weak equivalences at its weak equivalences may force more morphisms than 
    just weak equivalences to become isomorphisms.
    """
    def construct(self):
        t = make_title("Proposition", 2.33)
        self.title(t)

        p1 = TextMobject(r"""
            Let $\mathcal{C}$ be a model category and $\gamma:\mathcal{C}\to\text{Ho}
            (\mathcal{C})$ be its localization functor. Then a morphism $f$ in $\mathcal{C}$ 
            is a weak equivalence precisely if $\gamma(f)$ is an isomorphism in 
            $\text{Ho}(\mathcal{C})$.
        """, alignment="").scale(.75).to_title(t)

        self.cycle(
            [p1],
            out=False
        )
        self.clear()

class def234(Scene):
    """
    So when we formed the homotopy category, we had to steps. Restrict to fibrant cofibrant
    objects, and pass from morphisms to homotopy classes of morphisms.
    We can however talk about the full subcategory of fibrant objects, cofibrant objects,
    and fibrant cofibrant objects. These can each be regarded as categories with weak
    equivalences via their weak equivalences inherited from the original model category C.
    """
    def construct(self):
        t = make_title("Definition", 2.34)
        self.title(t)

        d1 = tikz("def234_d1", r"""
        \begin{tikzcd}
            & \mathcal{C}_{fc}
                \arrow{dl}\arrow{dr}
                & \\
            \mathcal{C}_c
                \arrow{dr}
                & & \mathcal{C}_f
                \arrow{dl} \\
            & \mathcal{C}
        \end{tikzcd}
        """, fn).scale(1.5)

        self.cycle(
            [d1],
            out=False
        )
        self.clear()

class rmk235(Scene):
    """
    Well certainly these things inherit more than just the structure of a category with
    weak equivalences, considering they come from a model category. The category of fibrant
    objects is said to have the structure of a fibration category, also called a Brown
    category of fibrant objects, and the category with cofibrant objects is said to have
    the structure of a cofibration category. We will exploit these properties when we talk
    about homotopy fiber sequences. The idea intuitively by calling these fibration
    and cofibration categories is that each subcategory inherits quote on quote half of 
    the factorization axioms of the oveall model category.
    """
    def construct(self):
        t = make_title("Remark", 2.35)
        self.title(t)

        r1 = TextMobject(r"""
            \begin{itemize}
                \item fibration category (Brown-category of fibrant objects)
                \item cofibration category
            \end{itemize}
        """).scale(.75)

        self.cycle(
            [r1],
            out=False
        )
        self.clear()

class cor236(Scene):
    """
    So by our previous theorem, a quick corollary is that the restriction of the
    localization functor to the subcategories of fibrant objects or cofibrant objects
    or fibrant cofibrant objects all exhibit the homotopy category of the original 
    model caegory as the localization of the subcategories at their own respective
    weak equivalences.
    """
    def construct(self):
        t = make_title("Corollary", 2.36)
        self.title(t)

        c1 = TexMobject(r"""
            \text{Ho}(\mathcal{C})
                \simeq
            \mathcal{C}[W^{-1}]
                \simeq
            \mathcal{C}_f[W_f^{-1}]
                \simeq
            \mathcal{C}_c[W_c^{-1}]
                \simeq
            \mathcal{C}_{fc}[W_{fc}^{-1}]
        """).scale(.75)

        self.cycle(
            [c1],
            out=False
        )
        self.clear()

class lemma237(Scene):
    """
    Now, if X is cofibrant and Y is fibrant, then we have this neat result about the
    hom set in the homotopy category of PX and QY- it is in bijection with the
    hom set in the original category modulo weak equivalences.
    So we want to show that this morphism is a bijection, so first break it up and
    factor it as so. Suppose that second map was an isomorphism. Now suppose
    we replaced the middle with X, QY, and suppose the new second map was an
    isomorphism. Then both of these facts combined would suggest that the overall
    map was a bijection in the first place. Ok, so we need to show that these two maps
    are isomorphisms. We prove one, and the other is of course dual.
    To see that this map is surjective, consider that since X is cofibrant there
    is a lift in the following diagram, so any morphism from X to Y corresponds to a
    morphism from X to QY. To see that it is injective, consider the following
    commutative diagram, which exhibits a homotopy of maps from X to QY to Y. Then
    the fact that this diagram lifts suggests that their corresponding maps from X to QY
    were homotopic already, and we are done.
    """
    def construct(self):
        t = make_title("Lemma", 2.37)
        self.title(t)

        l1 = TexMobject(r"""
            \text{Hom}_{\text{Ho}(\mathcal{C})}(PX, QY)
                =\text{Hom}_\mathcal{C}(PX, QY)/\sim
                \overset{\text{Hom}_\mathcal{C}(j_X,p_Y)}{\longrightarrow}
                \text{Hom}_\mathcal{C}(X,Y)/\sim
        """).scale(.75)

        self.cycle(
            [l1],
            out=False
        )

        l2 = TexMobject(r"""
            \text{Hom}_\mathcal{C}(PX, QY)/\sim
                \overset{\text{Hom}_\mathcal{C}(\text{id}_{PX}, p_Y)/\sim}{\longrightarrow}
            \text{Hom}_\mathcal{C}(PX, Y)/\sim
                \overset{\text{Hom}_\mathcal{C}(j_X,\text{id}_Y)/\sim}{\longrightarrow}
            \text{Hom}_\mathcal{C}(X,Y)/\sim
        """).scale(.75)

        self.fade_replace(
            l1, l2
        )

        l3 = TexMobject(r"""
            \text{Hom}_\mathcal{C}(\text{id}_X,p_Y)/\sim \ : \ 
                \text{Hom}_\mathcal{C}(X,QY)/\sim \ 
                \to
                \text{Hom}_\mathcal{C}(X,Y)/\sim \\
            \text{Hom}_\mathcal{C}(j_X,\text{id}_Y)/\sim \ : \ 
                \text{Hom}_\mathcal{C}(PX, Y)/\sim \ \to
                \text{Hom}_\mathcal{C}(X,Y)/\sim
        """).scale(.75)

        self.fade_replace(
            l2, l3
        )

        l4 = tikz("lemma237_l4", r"""
            \begin{tikzcd}
                0
                    \arrow{r}\arrow{d}[left]{\in\text{Cof}}
                    & QY
                    \arrow{d}[right]{p_Y\in W\cap\text{Fib}} \\
                X
                    \arrow{r}[above]{f}
                    & Y
            \end{tikzcd}
        """, fn)

        self.fade_replace(
            l3, l4
        )

        l5 = tikz("lemma237_l5", r"""
            \begin{tikzcd}
                X\sqcup X
                    \arrow{r}[above]{(f,g)}\arrow{d}[left]{\in\text{Cof}}
                    & QY
                    \arrow{d}[right]{p_Y\in W\cap\text{Fib}} \\
                \text{Cyl}(X)
                    \arrow{r}[below]{\eta}
                    & Y
            \end{tikzcd}
        """, fn)

        self.fade_replace(
            l4, l5
        )
        self.clear()

class lemma238(Scene):
    """
    Our last result is this. Every commuting square in the homotopy category is in the image
    of the localization functor. So a priori it is gaurenteed that there is a corresponding
    square in the original category that commutes up to homotopy, so that under the localization
    functor we get an actual commuting square. But the cool thing is, there is actually a
    proper commuting square, i.e. not just up to homotopy, in the original category. However,
    these might not necessarily have the same objects, as we will see. But there will be a
    commuting square corresponding to each commuting square in the homotopy category, i.e.
    a representative.
    So let's prove this. Consider a commuting square in the homotopy category. So like I was
    saying, at the very least we have this diagram, which says that f compose b and a compose
    f prime commute up to homotopy. So the top square suggests we do the pushout to the mapping
    cylinder, and this gives us this factorization via universal properties.
    It is a theorem that the induced map from the codomain to the mapping cylinder is a homotopy
    equivalence, so in the homotopy category, where such maps become isomorphisms, f is given
    by the class for which the map A to cylinder A to cylinder f is a representative, to be
    precise. It also gives us that the map from cylinder f to B prime, is a representative for
    the original map b from Y to B prime. In other words this is a commuting square in the
    original category that represents the original commuting square from the homotopy category.
    """
    def construct(self):
        t = make_title("Lemma", 2.38)
        self.title(t)

        l1 = tikz("lemma_238_l1", r"""
        \begin{tikzcd}
            A
                \arrow{r}[above]{f}\arrow{d}[left]{a}
                & B
                \arrow{d}[right]{b} \\
            A'
                \arrow{r}[below]{f'}
                & B'
        \end{tikzcd} $\in\text{Ho}(\mathcal{C})$
        """, fn)

        self.cycle(
            [l1],
            out=False
        )

        l2 = tikz("lemma_238_l2", r"""
            \begin{tikzcd}
                A
                    \arrow{r}[above]{f}\arrow{d}[left]{i_1}
                    & B
                    \arrow{d}[right]{b} \\
                \text{Cyl}(A)
                    \arrow{r}[below]{\eta}
                    & B' \\
                A
                    \arrow{u}[left]{i_0}\arrow{r}[below]{a}
                    & A'
                    \arrow{u}[right]{f'}
            \end{tikzcd}
        """, fn).scale(1.5)

        self.fade_replace(
            l1, l2
        )

        l3 = tikz("lemma_238_l3", r"""
            \begin{tikzcd}
                A
                    \arrow{r}[above]{f}\arrow{d}[left]{i_1}
                    & B
                    \arrow{d}[right]{\in W} \\
                \text{Cyl}(A)
                    \arrow{r}[above, yshift=1em]{(\text{po})}\arrow{dr}[left,yshift=-.5em]{\eta}
                    & \text{Cyl}(f)
                    \arrow{d} \\
                A
                    \arrow{u}[left]{i_0}\arrow{dr}[left,yshift=-.5em]{a}
                    & B' \\
                & A'
                    \arrow{u}[right]{f'}
            \end{tikzcd}
        """, fn).scale(2)

        self.fade_replace(
            l2, l3
        )

        l4 = tikz("lemma_238_l4", r"""
            \begin{tikzcd}
                A
                    \arrow{r}\arrow{d}[left]{a}
                    & \text{Cyl}(f)
                    \arrow{d} \\
                A'
                    \arrow{r}[below]{f'}
                    & B'
            \end{tikzcd}
        """, fn)

        self.fade_replace(
            l3, l4
        )
        self.clear()

# Date: 2/21/21
# Purpose: quillen adjunctions section nLab
# Notes: recorded 2/27

from manimlib.imports import *
fn = "quillen_adjunctions"


class intro(Scene):
    """
    So it seems that we have a lot of duality between left and right derived functors.
    It would be really awesome if we had an adjunction, which encodes a lot of the assumptions
    from earlier. Let's quickly review basic facts about adjuncts. So they are a pair of
    functors L and R going back and forth from two categories. And we have a natural
    bijection on these hom sets. So not only are these in bijection as sets, but the naturality
    means that given morphisms g from d2 to d1 in D and f from c1 to c2 in C, the following
    is a commutative square. So the vertical maps are the only ones that are potentially
    ambiguous, and these are just the hom functor applied, so take the left side for example.
    the image of a function up to from L d1 to c1 is the map from L d2 to Ld1 to c1 to c2.
    As notation suggests, we call L the left adjoint and R the right adjoint.
    So given a morphisms from the hom sets in bijection L(d) to c, we call the corresponding
    morphism d to R(c) its adjunct, and express it like this.
    We call the map from d to RLd the adjunction unit, and the map LRc to c the adjunction
    counit.
    These are pretty cool, notice that we can obtain all the other morphisms in the hom
    sets in which the lie from them, i.e. factoring through them.
    """
    def construct(self):
        d1 = tikz("intro_d1", r"""
            \begin{tikzcd}
                C \arrow[yshift=-.5em]{r}[below]{R}
                    & D
                    \arrow[yshift=.5em]{l}[above]{L}
            \end{tikzcd}
        """, fn).shift(3.5*LEFT, .5*UP).scale(.5)

        d2 = TexMobject(r"""
            \phi_{d,c}:
                \text{Hom}_\mathcal{C}(L(d),c)
                \overset{\simeq}{\longrightarrow}
                \text{Hom}_\mathcal{D}(d,R(c))
        """).scale(.65).next_to(d1, direction=DOWN, buff=1)

        d3 = tikz("intro_d3", r"""
            \begin{tikzcd}
                \text{Hom}_\mathcal{C}(L(d_1),c_1)
                    \arrow{r}[above]{\phi_{d_1,c_1}}[below]{\simeq}
                        \arrow{d}[left]{f\circ(-)\circ L(g)}
                    & \text{Hom}_\mathcal{D}(d_1, R(c_1))
                    \arrow{d}[right]{R(f)\circ(-)\circ g} \\
                \text{Hom}_\mathcal{C}(L(d_2),c_2)
                    \arrow{r}[above]{\simeq}[below]{\phi_{d_2,c_2}}
                    & \text{Hom}_\mathcal{D}(d_2,R(c_2))
            \end{tikzcd}
        """, fn).shift(3*RIGHT)

        self.cycle(
            [d1, d2, d3]
        )

        d4 = TexMobject(r"""
            \dfrac{L(c)\overset{f}{\longrightarrow}d}
                {c\overset{\tilde{f}}{\longrightarrow} R(d)}
        """).scale(.75).shift(1*UP)

        d5 = TexMobject(r"""
            \widetilde{(Ld\overset{f}{\to}c)}=(d\overset{\eta}{\to}RLd\overset{Rf}{\to}Rc) \\
            \widetilde{(d\overset{g}{\to}Rc)}=(Ld\overset{Lg}{\to}LRc\overset{\eta}{\to}c)
        """).scale(.75).shift(1.5*DOWN)

        self.cycle(
            [d4, d5]
        )

class def246(Scene):
    """
    That was pretty standard, it's time for some upgrades. We'd like to upgrade adjoint
    functors to model categorieis. A Quillen adjunction consisting of left and right
    Quillen functors is one which satisfies the following equivalent conditions:
    L preserves cofibrations and R preserves fibrations, L preserves acyclic
    cofibrations and R preserves acyclic fibrations, L preserves cofibrations and acyclic
    cofibrations, and R preserves fibrations and acyclic fibrations.
    The idea to keep in mind is that we want to associate L with preserving cofibrations,
    and R with preserving fibrations.
    """
    def construct(self):
        t = make_title("Definition", 2.46)
        self.title(t)

        d1 = TextMobject(r"""
            Let $\mathcal{C}$, $\mathcal{D}$ be model categories. A pair of adjoint 
            functors between them
                $$ (L\dashv R) \ : \ \mathcal{C}
                    \underoverset
                    {\underset{R}{\longrightarrow}}
                    {\overset{L}{\longleftarrow}}
                    {}
                    \mathcal{D} $$
            is called a 
        """, "Quillen adjunction", " ", r"""
            if the following equivalent conditions are satisfied:
            \begin{enumerate}
                \item $L$ preserves cofibrations and $R$ preserves fibrations
                \item $L$ preserves cofibrations and $R$ preserves acyclic fibrations
                \item $L$ preserves cofibrations and acyclic cofibrations
                \item $R$ preserves fibrations and acyclic fibrations
            \end{enumerate}
        """, alignment="").scale(.65).to_title(t)
        d1[1].set_color(BLUE)

        self.cycle(
            [d1],
            out=False
        )
        self.clear()

class prop247(Scene):
    """
    So let's check that those conditions are indeed all equivalent.
    Here are two observations, that if true we could deduce all the previous conditions
    from.
    So a left adjoint preserves acyclic cofibrations precisely if its right adjoint
    preserves fibrations. Right, so intuitively say R sends fibrations in C to fibrations
    in D. An acyclic cofibration in D would lift against this image, and somehow that means
    its image in C lifts against the original fibration.
    Dually, a left adjoint preserves cofibrations if its right adjoing preserves acyclic
    fibrations.
    We'll show statement one, and two is again just dual. So let f be an acyclic
    cofibration in D and g a fibration in C. Then for every commutative diagram on the
    left, we have a corresponding commuting diagram on the right. By assumption L
    preserves acyclic cofibrations, so there is a lift from LB to X on the right.
    We then apply the adjunction to get a left on the left from B to RX. Conversely, 
    suppose R preserves fibrations. Then we have a lift on the left, which goes to 
    a lift on the right by the same argument, and we are done.
    """
    def construct(self):
        t = make_title("Proposition", 2.47)
        self.title(t)

        p1 = TextMobject(r"""
            \begin{itemize}
                \item A left adjoint $L$ between model categories preserves acyclic 
                    cofibrations precisely if its right adjoint $R$ preserves fibrations
                \item A left adjoint $L$ between model categories preserves cofibrations 
                    precisely if its right adjoint $R$ preserves acyclic fibrations
            \end{itemize}
        """).scale(.75)

        self.cycle(
            [p1]
        )

        p2 = tikz("prop247_p2", r"""
            \begin{tikzcd}
                A
                    \arrow{r}\arrow{d}[left]{f}
                    & R(X)
                    \arrow{d}[right]{R(g)} \\
                B
                    \arrow{r}
                    & R(Y)
            \end{tikzcd}
        """, fn).shift(2*LEFT)

        p3 = tikz("prop247_p3", r"""
            \begin{tikzcd}
                L(A)
                    \arrow{r}\arrow{d}[left]{L(f)}
                    & X
                    \arrow{d}[right]{g} \\
                L(B)
                    \arrow{r}
                    & Y
            \end{tikzcd}
        """, fn).shift(1*LEFT).next_to(p2, buff=1)

        self.cycle(
            [p2, p3],
            out=False,
            successive=False
        )
        self.clear()

class lemma248(Scene):
    """
    So lets keep seeing if and how Quillen adjunctions preserve model category
    structures. This lemma says that R of a path space object of X in C is a 
    path space object in D for R(X) if X was fibrant to begin with.
    Dually, if X is cofibrant, then its cylinder object is sent to a cylinder object
    for LX under L.
    So we'll prove the second case, the first is dual.
    A neat property of adjoints is that right adjoints preserve limits and left adjoints
    preserve colimits. Hence L of X disjoint union X is LX disjoint union LX. Well
    then we can pull out the codiagonal map like so, observing that L preserves
    cofibrations. 
    Well since X is cofibrant, a map from X to Cyl X is an acyclic cofibration, and
    so LX to L Cyl X is also. Consider then the triangle L Cyl X and LX and another LX,
    and by two out of three we see LCyl X to X is a weak equivalence, and we are done.
    """
    def construct(self):
        t = make_title("Lemma", 2.48)
        self.title(t)

        l1 = TextMobject(r"""
            Let $\mathcal{C} \stackrel{\overset{L}{\longleftarrow}}{\underoverset{R}{\bot}
            {\longrightarrow}} \mathcal{D}$ be a Quillen adjunction.
            \begin{enumerate}
                \item For $X\in\mathcal{C}$ a fibrant object and $\text{Path}(X)$ a 
                path space object, then $R(\text{Path}(X))$ is a path space object for 
                $R(X)$.
                \item For $X\in\mathcal{C}$ a cofibrant object and $\text{Cyl}(X)$ a 
                cylinder object, then $L(\text{Cyl}(X))$ is a cylinder object for $L(X)$.
            \end{enumerate}
        """, alignment="").scale(.75).to_title(t)

        self.cycle(
            [l1]
        )

        l2 = TexMobject(r"""
            L(X\sqcup X\overset{\text{Cof}}{\longrightarrow}\text{Cyl}(X)) =
            (L(X)\sqcup L(X)\overset{\in\text{Cof}}{\longrightarrow}L(\text{Cyl}(X)))
        """).scale(.75).shift(2*UP)

        l3 = tikz("lemma248_l3", r"""
            \begin{tikzcd}
                & L(\text{Cyl}(X))
                    \arrow{dr}
                    & \\
                LX
                    \arrow{ur}\arrow{rr}
                    & & LX
            \end{tikzcd}
        """, fn).next_to(l2, direction=DOWN, buff=1.5)

        self.cycle(
            [l2, l3],
            out=False
        )
        self.clear()

class prop249(Scene):
    """
    And the properties of Quillen adjunction go even deeper. On the level of homotopy 
    categories, the derived functors of a Quillen adjunction are also adjoint functors.
    In the last video, we showed that we could consider hom sets in the homotopy category
    as hom sets in the underlying category, so the adjunction condition is equivalently
    expressed as this.
    But we already have a bijection before modding out by homotopy classes by assumption,
    so it just remains to show that modding out by homotopy classes doesn't change
    anything. Which is to say, we want that if two maps LX to Y were homotopic, then
    their corresponding maps from X to RY are also homotopic, specifically left homotopic.
    Well we just showed that cylinder objects are sent to cylinder objects under L.
    So we can write a left homotopy from f to g in the following way. Well then our
    adjunction gives us a corresponding left homotopy, and we are done.
    """
    def construct(self):
        t = make_title("Proposition", 2.49)
        self.title(t)

        p1 = TextMobject(r"""
            For $\mathcal{C} \underoverset{\underset{R}{\longrightarrow}}
            {\overset{L}{\longleftarrow}}{\bot_{\text{Qu}}}\mathcal{D}$ is a Quillen 
            adjunction, then the corresponding left and right derived functors form a 
            pair of adjoint functors
                $$ \text{Ho}(\mathcal{C})
                \underoverset
                {\underset{\mathbb{R}R}{\longrightarrow}}
                {\overset{\mathbb{L}L}{\longleftarrow}}
                {\bot}
                \text{Ho}(\mathcal{D}) $$
        """, alignment="").scale(.75).to_title(t)

        self.cycle(
            [p1]
        )

        p2 = TexMobject(r"""
            \text{Hom}_\mathcal{C}(LX,Y)/\sim
                \simeq
            \text{Hom}_\mathcal{D}(X,RY)/\sim
        """).scale(.75)

        self.cycle(
            [p2],
            out=False
        )

        p3 = TexMobject(r"""
            (f\Rightarrow_L g) \ : \ LX\to Y
        """).scale(.75)

        p4 = TexMobject(r"""
            \eta:\text{Cyl}(LX) = L\text{Cyl}(X)\to Y
        """).scale(.75)

        p5 = TexMobject(r"""
            (\tilde{f}\Rightarrow_L\tilde{g}):X\to RY
        """).scale(.75)

        p6 = TexMobject(r"""
            \tilde{\eta}:\text{Cyl}(X)\to RX
        """).scale(.75)

        p_3_to_6 = VGroup(
            p3, p4, p5, p6
        ).arrange_submobjects(
            DOWN,
            buff=.5
        )

        self.fade_replace(
            p2, p_3_to_6
        )
        self.clear()

class def250(Scene):
    """
    Quillen adjuncts can also strongly relate two model categories on the level
    of their homotopy categories. We say that there is a Quillen equivalence if
    any of the following equivalent conditions are met:
    First, the right derived functor is an equivalence of categories,
    second if the left derived functor is an equivalence of categories. Third,
    if for every cofibrant object d in D, the derived adjunction unit is a weak 
    equivalence. So the first map in the composition here is the adjunction unit,
    and the second is the fibrant replacement of L(d). We call this composite the
    derived adjunction unit again.
    We also require the dual case,
    that for every fibrant object the following composite is a weak equivalence,
    where the first map is the cofibrant replacement of Rc and the second is the 
    adjunction counit.  We call this composite the derived adjunction counit.
    Our fourth equivalent condition is that for every cofibrant object d in D and
    every fibrant object c in C, a morphism d to R(c) is a weak equivalence if
    and only if its adjunct morphism L(c) to d is.
    """
    def construct(self):
        t = make_title("Definition", "2.50")
        self.title(t)

        d1 = TextMobject(r"""
            For $\mathcal{C}$, $\mathcal{D}$ be two model categories, a Quillen 
            adjunction is called a 
        """, "Quillen equivalence", " ", r"""
            $$ \mathcal{C}
            \underoverset
            {\underset{R}{\longrightarrow}}
            {\overset{L}{\longleftarrow}}
            {\simeq_{\mathrlap{Q}}}
            \mathcal{D} $$
            if the following equivalent conditions hold:
        """, alignment="").scale(.65).to_title(t)
        d1[1].set_color(BLUE)

        self.cycle(
            [d1],
            out=False
        )

        d2 = TextMobject(r"""
            1. The right derived functor of $R$ is an equivalence of categories
            $$ \mathbb{R}R:\text{Ho}(\mathcal{C})\overset{\simeq}{\longrightarrow}
            \text{Ho}(\mathcal{D}) $$
        """).scale(.65).to_edge(DOWN, buff=2)

        self.cycle(
            [d2],
            out=False
        )

        d3 = TextMobject(r"""
            2. The left derived functor of $L$ is an equivalence of categories
            $$ \mathbb{L}L:\text{Ho}(\mathcal{D})\overset{\simeq}{\longrightarrow}
            \text{Ho}(\mathcal{C}) $$
        """).scale(.65).to_edge(DOWN, buff=2)

        self.fade_replace(
            d2, d3
        )

        d4 = TextMobject(r"""
            3. For every cofibrant $d\in\mathcal{D}$, the derived adjunction unit is a weak 
            equivalence:
            $$ d\overset{\eta}{\longrightarrow}R(L(d))\overset{R(j_{L(d)})}{\longrightarrow}
            R(P(L(d))) \quad \in W$$
            and for every fibrant $c\in\mathcal{C}$ the derived adjunction counit is a 
            weak equivalence:
            $$ L(Q(R(c)))\overset{L(p_{R(c)})}{\longrightarrow}L(R(c))
            \overset{\epsilon}{\longrightarrow}c \quad \in W$$
        """, alignment = "").scale(.65).shift(2*DOWN)

        self.fade_replace(
            d3, d4
        )

        d5 = TextMobject(r"""
            4. For every cofibrant $d\in\mathcal{D}$ and every fibrant $c\in\mathcal{C}$, 
            a morphism $d\to R(c)$ is a weak equivalence precisely if its adjunct is:
            $$ \dfrac{d\overset{\in W_\mathcal{D}}{\longrightarrow}R(c)}
            {L(d)\overset{\in W_\mathcal{C}}{\longrightarrow} c} $$
        """, alignment="").scale(.65).shift(2*DOWN)

        self.fade_replace(
            d4, d5
        )
        self.play(
            FadeOut(d5),
            FadeOut(d1)
        )

        d6 = tikz("prop250_d6", r"""
            \begin{tikzcd}
                \mathcal{D}_c
                    \arrow{r}[above]{L}\arrow{d}[left]{\gamma_P}
                    & \mathcal{C}
                    \arrow{d}[right]{\gamma_{P,Q}} \\
                \text{Ho}(\mathcal{D})
                    \arrow{r}[below]{\mathbb{L}L}
                    & \text{Ho}(\mathcal{C})
            \end{tikzcd}
        """, fn).shift(.5*UP)

        d7 = TexMobject(r"""
            (\mathbb{L}L)d\simeq PLPd\simeq PLd \quad \in\text{Ho}(\mathcal{C})
        """).scale(.75).next_to(d6, direction=DOWN, buff=.5)

        self.cycle(
            [d6, d7]
        )

        d8 = TexMobject(r"""
            \text{Hom}_{\text{Ho}(\mathcal{C})}((\mathbb{L}L)Pd, (\mathbb{L}L)Pd)
            \to
            \text{Hom}_{\text{Ho}(\mathcal{C})}(Pd, (\mathbb{R}R)(\mathbb{L}L)Pd)
        """).scale(.75)

        d9 = TexMobject(r"""
            \text{Hom}_{\text{Ho}(\mathcal{C})}(PLd, PLd)
            \overset{\text{Hom}(j_{Ld},\text{id})}{\longrightarrow}
            \text{Hom}_\mathcal{C}(Ld, PLd)/\sim
        """).scale(.75)

        d10 = TexMobject(r"""
            Ld\overset{j_{Ld}}{\longrightarrow}PLd\overset{\text{id}}{\longrightarrow}PLd
        """).scale(.75)

        d11 = TexMobject(r"""
            X\overset{\eta}{\longrightarrow}RLd\overset{R(j_{Ld})}{\longrightarrow}RPLd
        """).scale(.75)

        d_8_to_11 = VGroup(
            d8, d9, d10, d11
        ).arrange_submobjects(
            direction=DOWN,
            buff=.5
        )

        self.cycle(
            [d_8_to_11]
        )

        d12 = TexMobject(r"""
            LX\overset{j_{LX}}{\longrightarrow}PLX
        """).scale(.75)

        d13 = TexMobject(r"""
            X\overset{\eta}{\longrightarrow}RLX\overset{Rj_{LX}}{\longrightarrow}RPLX
        """).scale(.75)

        d_12_to_13 = VGroup(
            d12, d13
        ).arrange_submobjects(
            direction=DOWN,
            buff=.5
        )

        self.cycle(
            [d_12_to_13]
        )

        d14 = tikz("prop250_d14", r"""
            \begin{tikzcd}
                \tilde{f}:
                    & d
                    \arrow{r}[above]{\eta}\arrow{d}[left]{=}
                    & RLd
                    \arrow{r}[above]{Rf}\arrow{d}[right]{Rj_{Ld}}
                    & Rc
                    \arrow{d}[right]{Rj_c} \\
                & d
                    \arrow{r}[below]{\in W}
                    & RPLd
                    \arrow{r}[above]{RPf}
                    & RPc
            \end{tikzcd}
        """, fn).shift(.5*UP, 1*LEFT)

        d15 = TexMobject(r"""
            f:LD\longrightarrow c
        """).scale(.75).next_to(d14, direction=DOWN, buff=.5)

        self.cycle(
            [d14, d15],
            out=False,
            successive=False
        )
        self.clear()

class prop251(Scene):
    """
    So we definitely need to convince ourselves that all these conditions are indeed
    equivalent. 1 and two are easy to see, so lets see how these are equivalent to 3.
    So a pair of adjoint functors is an equivalence of categories if and only if
    the adjunction unit and counit are natural isomoprhisms. Hence it suffices to show
    that the adjunction unit and counit represent adjunction units and counits in
    the homotopy category. So we will construct an adjunction counit, and show
    that it is represented by a derived adjunction counit.
    We show that this is the case for the adjunction unit, and the other is dual.
    So again, we want to show that the derived adjunction unit is an adjunction
    unit in the homotopy category. So let d be in D_c, and consider the follwoing 
    commuting diagram from previous videos. 
    So then I claim this shows these three things are isomorphic in the homotopy
    category. So the first and third follow just by commutativity. The middle
    one is the third but with a fibrant replacement do to Pd applied once more.
    Why is this isomorphic? Well be assumption d is cofibrant, hence the map
    d to Pd is an acyclic fibration, and left Quillen functors preserve those, so d
    to Pd is a weak equivalence hence an isomorphism in the homotopy category.
    Ok, we have an element in the homotopy category of D, so no we want to consider
    its adjunction unit and show that it is represented by a derived adjunction unit.
    Well by definition its adjunction unit is the image of the identity under this
    adjunction isomorphism. Well, LLPd is by what we just talked about PLPd which we showed
    is just PLd. And on the right we have our equivalent homset in regular C. So
    the adjunction unit is equivalently the image of the identity in this, so again
    this is after the hom functor, so it is a map from Ld to PLd to Pld to Pld again,
    or just simply Ld to PLd to Pld. Indeed, this is equivalently by adjunct properties
    this composite, which is is a derived adjunction unit.
    Now we need to show that 3 and 4 are equivalent. To see that four implies 3,
    consider the weak equivalence LX to PLX, so again this is a weak equivalence by
    property of fibrant replacements. Then its LR adjunct is the following composite,
    which by assumption on 4 is a weak equivalence as well, But this is a derived unit,
    and since it is a weak equivalence satisfies 3. Dually we can show this for counits.
    Finally lets see that 3 implies 4. So suppose Ld to c is a weak equivalence, where
    d is cofibrant and c is fibrant. We want to show that its adjunct is a weak equivalence
    as well. Well, it fits into this commuting diagram. Notice that the bottom left is
    the composite derived adjunction unit, and we assumed by 3 that these were weak equivalences.
    Well, f is a weak equivalence, so Pf is by assumption. Well R preserves acyclic fibrations,
    and since c is fibrant, we can use Ken browns lemma to conclude that R preserves
    weak equivalences so RPf and RjY are weak equivalecnes, so by two out of three
    the top composite adjunct is a weak equivalence as well.
    """

class prop252(Scene):
    """
    Our last result is thankfully a bit of a simplification. So given a Quillen adjunction,
    suppose R creates weak equivalences, by which we mean a morphism f in C is a weak 
    equivalence precisely if Rf is. Well, then we have a Quillen equivalence if and only
    if for all cofibrant objects d in D the adjunction unit (not derived) is a weak
    equivalence.
    So let's prove this. Well we just said that we have a Quillen equivalence if and only
    if for every cofibrant object the derived adjunction unit is a weak equivalence,
    and for every fibrant object the derived adjunction counit is a weak equivalence.
    Well the derived adjunction unit had its first map as the map we are assuming in the
    proposition is a weak equivalence, and R preserves the second weak equivalence
    by assumption.
    Hence by two out of three we are done, conversely as well.
    So we only need to show this second conditions is true if and only if eta was 
    a weak equivalence. Well by assumption on R the composite in 2 is a weak
    equivalence if and only if it is after applying R. If we precompose with this
    map, by what we just showed with regards to the first condition this first map
    is a weak equivalence, so by two out of three the entire composite is a weak
    equivalence if and only if the composite from before without the precomposition was.
    Well by the properties of adjuncts, look at the composite from condition 2 and
    notice this is its adjunt. The bottom map is a weak equivalence because of
    properties of the cofibrant replacement. So assuming we have a Quillen equivalence, then
    the top map becomes a weak equivalence. Conversely, if we assumed the proposition then
    the above map is by assumption a weak equivalence, and this implies the property that
    tells us we have a Quillen equivalence, I believe it was property 4.
    """
    def construct(self):
        t = make_title("Proposition", 2.52)
        self.title(t)

        p1 = TextMobject(r"""
            If in a Quillen adjunction $(L\dashv R)$ the right adjoint $R$ 
            ``creates weak equivalences'' then it is a Quillen equivalence precisely 
            if for all cofibrant $d\in\mathcal{D}$ the plain adjunction unit 
            is a weak equivalence:
            $$ d\overset{\eta}{\longrightarrow} R(L(d))\quad\in W $$
        """, alignment="").scale(.75)

        self.cycle(
            [p1]
        )

        p2 = TextMobject(r"""
            \begin{enumerate}
                \item for every cofibrant $d\in\mathcal{D}$ the derived adjunction unit 
                    is a weak equivalence:
                    $$ d\overset{\eta}{\longrightarrow}R(L(d))
                    \overset{R(j_{L(d)})}{\longrightarrow} R(P(L(d)))\quad\in W $$
                \item for every fibrant $c\in\mathcal{C}$, the derived adjunction counit 
                    is a weak equivalence:
                    $$ L(Q(R(c)))\overset{L(p_{R(c)})}{\longrightarrow}
                    L(R(c))\overset{\epsilon}{\longrightarrow} c\quad\in W $$
            \end{enumerate}
        """, alignment="").scale(.75)

        self.cycle(
            [p2]
        )

        p3 = TexMobject(r"""
            R(L(Q(R(c))))\overset{R(L(p_{R(c)}))}{\longrightarrow}
            R(L(R(c)))\overset{R(\epsilon)}{\longrightarrow} R(c)
        """).scale(.75)

        p4 = TexMobject(r"""
            Q(R(c))
                \overset{\eta_{Q(R(c))}}{\longrightarrow}
            R(L(Q(R(c))))
                \overset{R(L(p_{R(c)}))}{\longrightarrow}
            R(L(R(c)))
                \overset{R(\epsilon)}{\longrightarrow}
            R(c)
        """).scale(.75)

        p5 = TexMobject(r"""
            \dfrac{
                L(Q(R(c)))\overset{L(p_{R(c)})}{\longrightarrow}
                L(R(c))\overset{\epsilon}{\longrightarrow}c
            }{
                Q(R(c))\overset{p_{R(c)}}{\longrightarrow} R(c)
            }
        """).scale(.75)

        p_3_to_5 = VGroup(
            p3, p4, p5
        ).arrange_submobjects(
            DOWN,
            buff=.5
        )

        self.cycle(
            [p_3_to_5],
            out=False
        )
        self.clear()

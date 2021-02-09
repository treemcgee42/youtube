# Date: 2/6/21
# Purpose: "Fibrations" section in nLab intro to htpy theory
# Notes: Last updated 2/9/21


from manimlib.imports import *
fn = "fibrations"


class def146(Scene):
    """
    Lifting properties are going to be extremely important in our
    future work, and so I want to start right off the bat by defining them,
    and I'll try to build in intuition as we go. It's just good in my
    opinion to know the general definition first. So yeah, we have a mategory
    and a class of morphisms C in that category. Then we have a map p
    which implicitly also contains the information about the spaces
    E, its domain, and B, its codomain. p is said to have the right
    lifting property against morphisms in C if every commuting square
    admits a lift in the following way, so this diagram commutes. We will
    equivalently, and more often say that p is a C-injective morphism.
    So there's a little bit to be careful about here. A lift needs to exist
    only if a commuting square exists.
    """
    def construct(self):
        title = make_title("Definition", 1.46)

        self.play(
            Write(title)
        )
        self.wait(2)

        thedef = TextMobject("Let $c\\in C\\subset\\text{Mor}(\\mathcal{C})$. \
            A morphism $p:E\\to B$ in $\\mathcal{C}$ has the ", "right lifting property",\
            " against morphisms in $C$ if every commuting diagram", alignment="")\
            .scale(.75).next_to(title, direction=DOWN, buff=1).to_edge(LEFT, buff=.5)
        thedef[1].set_color(BLUE)

        thedef2 = TextMobject("has a lift $h$:", alignment="").scale(.75)
        thedef3 = TextMobject("We also say $P$ is a ", "$C$-injective morphism",".",\
            alignment="").scale(.75)
        thedef3[1].set_color(BLUE)

        thedeftext = VGroup(
            thedef,
            thedef2,
            thedef3
        ).arrange_submobjects(
            DOWN,
            buff=2,
            aligned_edge = LEFT
        )

        commuting_1 = tikz("std_commuting_square", r"""
            \begin{tikzcd}
                X \arrow{d}[left]{c}\arrow{r} & E \arrow{d}[right]{p} \\
                Y \arrow{r} & B
            \end{tikzcd}
        """, fn).scale(.75).shift(.85*UP)

        commuting_2 = tikz("std_lift_square", r"""
            \begin{tikzcd}
                X \arrow{d}[left]{c}\arrow{r} & E \arrow{d}[right]{p} \\
                Y\arrow[dashed]{ur}[left,yshift=.5em]{h} \arrow{r} & B
            \end{tikzcd}
        """, fn).scale(.75).shift(1.25*DOWN)

        self.play(
            FadeIn(thedeftext),
            FadeIn(commuting_1),
            FadeIn(commuting_2)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class some_intuition(Scene):
    """
    Let's try to see how this can be useful with regards to homotopy.
    Suppose we are trying to understand the nth homotopy group of a
    topological space B. This is the set of homotopy equivalence classes of 
    maps from S^n to B. But this might be quite untractable, or hard
    to calculate. What if we could study just a part of the entire
    set of homotopy equivalence classes? Well we could find a space E
    and a map from E to B such that the following diagram commutes.
    But since we are interested in homotopy equivalence of maps, we
    should probably require that if maps from S^n to B are homotopic,
    then so are their lifts. Then, in a sense, we have a situation 
    where the amount pi_n of E differs from pi_n of B is measured
    by the map from E to B.
    We can also rearrange this idea into a way that lets us see the
    connection to the right lifting property from before. This general
    pattern where the bottom left object is the standard cylinder object
    of the top left object is called the homotopy lifting property.
    In the case where we replace S^n with some random topological space
    X we say that the map from E to B is a Hurewicz fibration.
    The other notable case is when we replace S^n with D^n. That is what
    we turn to now.
    """
    def construct(self):
        pi_n = TexMobject("\\pi_n(B)").scale(.75)

        self.play(
            FadeIn(pi_n)
        )
        self.wait(2)

        sn_to_b = TexMobject("S^n\\longrightarrow B").scale(.75)

        self.play(
            ReplacementTransform(pi_n, sn_to_b)
        )
        self.wait(2)

        commuting_1 = tikz("sn_to_b", r"""
            \begin{tikzcd}
                & E \arrow{d}[right]{\pi} \\
                S^n\arrow{ur}[left,yshift=.5em]{\tilde{f}} \arrow{r}[below]{f} & X
            \end{tikzcd}
        """, fn)

        self.play(
            FadeOut(sn_to_b),
            FadeIn(commuting_1)
        )
        self.wait(2)

        commuting_2 = tikz("sn_to_b_htpy", r"""
            \begin{tikzcd}
                & E \arrow{d}[right]{\pi} \\
                S^n \arrow{ur}[left,yshift=.5em]{\tilde{f}\Rightarrow \tilde{g}} 
                    \arrow{r}[below]{f\Rightarrow g} & X
            \end{tikzcd}
        """, fn)

        self.play(
            FadeOut(commuting_1),
            FadeIn(commuting_2)
        )
        self.wait(2)
        self.play(
            FadeOut(commuting_2)
        )

        sn_ex = tikz("sn_ez_square", r"""
            \begin{tikzcd}
                S^n \arrow{d} \arrow{r} & E \arrow{d} \\
                S^n\times I \arrow{r} \arrow[dashed]{ur} & B
            \end{tikzcd}
        """, fn)

        self.play(
            FadeIn(sn_ex)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class def147(Scene):
    """
    So yeah, a Serre fibration is a J top injective morphisms, i.e. a map
    that has the right lifting property against the class of generating acyclic
    cofibrations.
    """
    def construct(self):
        title = make_title("Definition", 1.47)

        self.play(
            Write(title)
        )
        self.wait(2)

        thedef = TextMobject("A ", "Serre fibration", " is a $J_{\\text{Top}}$-injective \
            morphism: it has the right lifting property against all topological \
            generating acyclic cofibrations, e.g.", alignment="")\
            .scale(.75).next_to(title, direction=DOWN, buff=1).to_edge(LEFT, buff=.5)
        thedef[1].set_color(BLUE)

        thedefpic = tikz("serre_fibration_square", r"""
        \begin{tikzcd}
            D^n \arrow{d}[left]{(\text{id},\delta_0)} \arrow{r}
                & E \arrow{d}[right]{p} \\
            D^n\times I \arrow[dashed]{ur}[left,yshift=.5em]{\exists h} \arrow{r}
                & B
        \end{tikzcd}
        """, fn).shift(1*DOWN, .5*LEFT)

        self.play(
            FadeIn(thedef)
        )
        self.play(
            FadeIn(thedefpic)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class rmk149(Scene):
    """
    Remember that we are trying to generalize topological homotopy theory.
    What we will show eventually is that the specific shape of Dn and Dn times I
    don't matter with respect to the properties of Serre fibrations. What
    really matters is that these maps that Serre fibrations lift against are
    relative cell complexes and weak homotopy equivalences, which I think
    is pretty neat. Again, we will cover that later once we've developed abstract
    homotopy theory.
    """
    def construct(self):
        title = make_title("Remark", 1.49)

        self.play(
            Write(title)
        )
        self.wait(2)

        thermk = TextMobject("What matters for Serre fibrations is actually just \
            that the morphisms it has the right lifting property \
            against are relative cell complexes and weak homotopy equivalences.", alignment="")\
            .scale(.75).next_to(title, direction=DOWN, buff=2).to_edge(LEFT, buff=.5)

        self.play(
            FadeIn(thermk)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class prop150(Scene):
    """
    So going back to our goal of generality, many of the statements we are
    going to give in the rest of this video have analagous in a more general setting.
    Presently, we defer the proof of this statement to the next video or the video
    after that where we will prove it in generality.
    But in this case, it says that a Serre fibration not only has the right lifting
    property against Jtop, which is the definition, but also against all retracts
    of Jtop relative cell complexes, which is a pretty considerable extension,
    and it's really neat that it works out like that in my opinion.
    """
    def construct(self):
        title = make_title("Proposition", "1.50")

        self.play(
            Write(title)
        )
        self.wait(2)

        theprop = TextMobject(r"""
            A Serre fibration has the right lifting property against 
            all retracts of $J_{\text{Top}}$-relative cell complexes.
        """, alignment="").scale(.75).next_to(title, direction=DOWN, buff=2).to_edge(LEFT, buff=.5)

        self.play(
            FadeIn(theprop)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class prop151(Scene):
    """
    Here's cool proposition that we are ready to prove. We'll actually
    return to this and prove a more general version of this later, but for now,
    suppose f is a Serre fibration and y is any point in y. Then we can consider
    the fiber of y, which we will call Fy, as a subset of X, and hence we have the
    following fiber inclusion. This proposition states that on the level of homotopy groups,
    the induced sequence is exact.
    So let's prove this. That the sequence is exact just means that the kernel of the
    second map is the image of the first. So immediately we see that one direction is clear.
    Suppose you are a sphere (hence a representative of an equivalence class of the homotopy
    group) in Fy. Well by definition you are mapped to a single point, y, under f asterik,
    since you are in the fiber over the single point y, i.e. in Fy. So what we are left to
    show is that this is the ENTIRE kernel, i.e. that every sphere in X that maps trivially
    into Y is homotopic to a sphere entirely in Fy.
    So to get formal, let alpha be something in the kernel, so it is a map from a
    sphere to X. Our goal is to show that alpha is homotopic to something in the image
    of the inclusion, so it is homotopic to a sphere that is sent entirely to the single point
    Y.
    As far as proof technicques go, one of our assumptions was that f was a Serre fibration,
    so we better arrange our diagram in a way that lets us exploit this fact. So we can think of
    alpha, or indeed any map from the sphere, as fitting into this diagram. So what we are doing
    is sort of packaging the information of f compose alpha into some map kappa.
    So by assumption alpha composed with f is trivial, and hence it, and by analogy kappa,
    is left homotopic to the constant map sending everything to the single point y. That's
    what it means to be trivial.
    Well again, as soon as you hear homotopy you should think of what that means for the diagram.
    In this case, it means that our square becomse something like this. We can rewrite this diagram
    in this way so we can exploit some patterns.
    In particular, consider the top two squares. Again, we'd like to exploit the fact that f
    is a Serre fibration, but as of right now we can construct any lifts because
    the left morphism in the square is not a generating acyclic cofibration. But recall that 
    previous proposition that said Serre fibrations also lift against J Top relative cell
    complexes. Well recall that the inclusion of a CW complex, such as a sphere, into its 
    cylinder object is a Jtop relative cell complex. So your should be thinking, how can
    we squeeze in a S n-1 times I into this top part?
    Well the 2 top right morphisms are f and id, and id is sort of redundant. So what if
    we deleted that middle row containing Dn kappa and Y? We could then replace the Dn
    with S n-1 times I and rearrange the top two squares in the following way.
    Great! Now we can use the fact that f is a Serre fibration and obtain a lift eta tilde.
    What is this a homotopy between? Well it is between the top map alpha and some other
    map alpha prime. We can image alpha as living on the top of the cylinder s n-1 times I
    and alpha prime living on the bottom of that cylinder.
    So I just want to reaffirm that this is what we want. We wanted to say something about all
    maps homotopic to an element alpha in the kernel. In particular, we wanted to say that
    alpha was homotopic to a map that is trivial, i.e. sends everything to a single point.
    This such a map lives in the image, and would show that the kernel and image are isomorphic.
    So lets show that this map alpha prime could be the constant map.
    We can again piece together all of our information that we have accumulated into the
    following diagram, which finally exhibits what we want: since the outer square commutes,
    and alpha prime is the top two morphisms. 
    Looking back at what we did, we used the fact that kappa was homotopic to the 
    constant map to construct a homotopy eta, and then showed that we could lift
    in a suitable way against eta.
    """
    def construct(self):
        title = make_title("Proposition", 1.51)

        self.play(
            Write(title)
        )
        self.wait(2)

        theprop = TextMobject(r"""
            For a Serre fibration $f:X\to Y$ and a point $y:\ast\to Y$, consider
            $$F_y:=f^{-1}(y)\overset{\iota}{\hookrightarrow} X\overset{f}{\to} Y.$$
            Then for any $(x:\ast\to X)\in F_y\subset X$, the following sequence is exact:
            $$\pi_\bullet(F_y,x)\overset{\iota_\ast}{\longrightarrow}
            \pi_\bullet(X,x)\overset{f_\ast}{\longrightarrow}\pi_\bullet(Y,y).$$
        """, alignment="").scale(.75).to_edge(LEFT, buff=.5)

        self.play(
            FadeIn(theprop)
        )
        self.wait(2)
        self.play(
            FadeOut(theprop)
        )

        pftitle = TextMobject("Pf:").scale(.75).next_to(title, direction=DOWN, buff=1)\
            .to_edge(LEFT, buff=.5)
        the_sequence = TexMobject(r"""
            \pi_\bullet(F_y,x)\overset{\iota_\ast}{\longrightarrow}
            \pi_\bullet(X,x)\overset{f_\ast}{\longrightarrow}\pi_\bullet(Y,y)
        """).scale(.75).to_edge(UP, buff=1)

        self.play(
            Write(pftitle),
            FadeIn(the_sequence)
        )
        self.wait(2)

        to_prove = TexMobject(r"""
            \text{ker}(f_\ast)\simeq\text{im}(\iota_\ast)
        """).scale(.75)

        self.play(
            FadeIn(to_prove)
        )
        self.wait(2)

        supset_true = TexMobject(r"""
            \text{ker}(f_\ast)\supseteq\text{im}(\iota_\ast)
        """).scale(.75)

        self.play(
            ReplacementTransform(to_prove, supset_true)
        )
        self.wait(2)
        self.play(
            FadeOut(supset_true)
        )
        self.wait(2)

        p1 = TextMobject(r"""
            Let $([\alpha]\in\pi_\bullet (X,x))\in\text{ker}(f_\ast)$.
        """, alignment="").scale(.75).next_to(pftitle, direction=DOWN, buff=.5)\
            .to_edge(LEFT, buff=.5)

        self.play(
            FadeIn(p1)
        )
        self.wait(2)

        p2 = tikz("p2_prop151_pf", r"""
            \begin{tikzcd}
                S^{n-1} \arrow{d} \arrow{r}[above]{\alpha} & 
                    X \arrow{d}[right]{f} \\
                D^n \arrow{r}[above]{\kappa} & Y
            \end{tikzcd}
        """, fn)

        self.play(
            FadeIn(p2)
        )
        self.wait(2)

        p3 = TexMobject(r"""
            \eta:\kappa\Rightarrow\text{const}_y
        """).scale(.75).next_to(p2, direction=DOWN, buff=.5)

        self.play(
            FadeIn(p3)
        )
        self.wait(2)
        self.play(
            FadeOut(p1), 
            FadeOut(p2),
            FadeOut(p3)
        )

        p4 = tikz("p4_prop151_pf", r"""
            \begin{tikzcd}
                S^{n-1} \arrow{d}[left]{\iota_n} \arrow{r}[above]{\alpha} 
                    & X \arrow{dd}[right]{f} \\
                D^n \arrow{dr}[right, yshift=.5em]{\kappa} 
                    \arrow{d}[left]{(\text{id},\delta_1)} & \\
                D^n\times I \arrow{r}[above]{\eta} & Y \\
                D^n \arrow{u}[left]{(\text{id},\delta_0)} 
                    \arrow{ur}[right,yshift=-.5em]{\text{const}_y} &
            \end{tikzcd}
        """, fn).scale(1.5).shift(1*DOWN)

        self.play(
            FadeIn(p4)
        )
        self.wait(2)
        self.play(
            FadeOut(p4)
        )

        p5 = tikz("p5_prop151_pf", r"""
            \begin{tikzcd}
                & S^{n-1} \arrow{d}[left]{\iota_n} \arrow{r}[above]{\alpha}
                    & X \arrow{d}[right]{f} \\
                & D^n \arrow{d}[right]{(\text{id},\delta_1)} \arrow{r}[above]{\kappa}
                    & Y \arrow{d}[right]{\text{id}} \\
                D^n \arrow{r}[above]{(\text{id},\delta_0)} \arrow{d} & D^n\times I
                    \arrow{r}[above]{\eta} & Y \arrow{d} \\
                \ast \arrow{rr}[above]{y} & & Y
            \end{tikzcd}
        """, fn).scale(2).shift(1*DOWN)

        self.play(
            FadeIn(p5)
        )
        self.wait(2)
        self.play(
            FadeOut(p5)
        )

        p6 = tikz("p6_prop151_pf", r"""
            \begin{tikzcd}
                S^{n-1} \arrow{rr}[above]{\alpha} \arrow{d}[left]{(\text{id},\delta_1)}
                    & & X \arrow{d}[right]{f} \\
                S^{n-1}\times I \arrow{r}[above]{(\iota_n,\text{id})} & D^n\times I
                    \arrow{r}[above]{\eta} & Y
            \end{tikzcd}
        """, fn)
        self.play(
            FadeIn(p6)
        )
        self.wait(2)

        p7 = TexMobject(r"""
            \tilde{\eta}:\alpha\Rightarrow \alpha'
        """).scale(.75).next_to(p6, direction=DOWN, buff=1)

        self.play(
            FadeIn(p7)
        )
        self.wait(2)
        self.play(
            FadeOut(p6),
            FadeOut(p7)
        )

        p8 = tikz("p8_prop151_pf", r"""
            \begin{tikzcd}
                \alpha': & S^{n-1} \arrow{d}[right]{\iota_n} \arrow{r}[above]{(\text{id},\delta_0)}
                    & S^{n-1}\times I \arrow{d}[right]{(\iota_n,\text{id})}
                    \arrow{r}[above]{\tilde{\eta}} & X \arrow{d}[right]{f} \\
                & D^n \arrow{d} \arrow{r}[above]{(\text{id},\delta_0)} & 
                    D^n\times I \arrow{r}[above]{\eta} & Y \arrow{d} \\
                & \ast \arrow{rr}[above]{y} & & Y
            \end{tikzcd}
        """, fn).scale(2).shift(1*DOWN)

        self.play(
            FadeIn(p8)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class lemma152(Scene):
    """
    Here's our last lemma for this section, and fair warning, this is
    a bit of a larger effort to prove.
    The lemma comes from something you might have been wondering: like sure,
    Serre fibrations lift against generating acyclic cofibrations, but what about
    just regular generating cofibrations? It turns our that the maps
    that lift against I top, the generating cofibrations, are precisely the
    acyclic cofibrations, i.e. Serre fibrations that are also weak homotopy
    equivalences. So we have this nifty sort of duality, were acyclic Serre
    fibrations are those maps that lift against regular generating cofibrations,
    and regular Serre fibrations are those that lift against acyclic generating
    cofibrations.
    """
    def construct(self):
        title = make_title("Lemma", 1.52)

        self.play(
            Write(title)
        )
        self.wait(2)

        thelemma = TextMobject(r"""
            The set of ($I_\text{Top}=\{S^{n-1}\hookrightarrow D^n\}$)-injective morphisms \
            is equivalently the set of acyclic Serre fibrations.
        """, alignment="").scale(.75).to_edge(LEFT, buff=.5)

        self.play(
            FadeIn(thelemma)
        )
        self.wait(2)
        self.play(
            FadeOut(thelemma)
        )
        
        theduality = TextMobject(r"""
            \begin{tabular}{l l}
                generating cofibrations & acyclic generating cofibrations \\
                acyclic Serre fibrations & Serre fibrations
            \end{tabular}
        """).scale(.75)

        self.play(
            FadeIn(theduality)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects[1:]]
        )

class lemma152_forward_pf(Scene):
    """
    So the forward direction is not so bad to prove. So we are starting
    with an Itop injective morphism, and we want to show that it is
    first of all a weak homotopy equivelence, and secondly that it is
    a Serre fibration, which will show that it is an acyclic Serre fibration.
    So by assumption there exists a lift. To show the weak homotopy equivalence
    we want to show that all homotopy groups/sets are isomorphic.
    You might see why this should be true, because in the top left we have
    maps out of Sn, which defines the homotopy group.
    But ok, when n is 0, the dn is D0 which is just a point, and
    its boundary, or s -1, is just the empty set. Well the bottom map, which
    is a map with domain a single point, just defines a point in x, and if
    every such map lifts, then we automatically get that the map p is surjective,
    since we can always lift to a point in X hat that maps to x under p.
    In n = 1, we see that two points being connected in X means that there is a map
    from D^1, which is isomorphic to I, with each point as the endpoint of its image.
    Well that I connects them in a sense, and again we can lift that whole map to X hat,
    so we get a connected component in X hat corresponding to the connected component
    in X. So p is injective on the level of connected homotopy groups, and this
    paired with the aforementioned surjectivity shows that p is an isomorphism
    on the level of the 0th homotopy group.
    So for n greater than or equal to 1, suppose you were a trivial element in the
    nth homotopy group of X. Since you are a map from Sn to X and you are trivial,
    that means you can be factored through D n+1 via a map that sends its
    boundary to a trivial thing in X. This makes sense becuase a map from
    D n+1 is contractable and hence trivial, so if you could be factored through it
    you had to be trivial in the first place. Well, then there is a lifting from 
    D n+1 to X hat, which again tells us that this map from Sn to D n+1 up to X hat,
    which is equivalently the top map, is trivial. What does this tell us?
    On the level of the nth homotopy group, if you were trivial in pi n of X, 
    the your preimage under p was trivial in pi n of X hat, which means the kernel
    of p is trivial, and hence p in injective on the level of nth homotopy
    groups. It remains only to show that p is surjective.
    To see this, consider an element of pi n of X. Well, another way of saying that
    other than as a map from Sn is as a map from Dn that sends the boundary to a single
    point, in other words this diagram here. Well there is a lift by assumption,
    so there is a corresponding representative of that element in pi n of X in 
    pi n of X hat, and we are done with showing that p is a weak homotopy equivalence.
    To show that it is a Serre fibration is not that hard: we recall the previous
    fact from last video that every element of Jtop in an I top relative cell complex.
    Something we will prove in the next few videos is that by closure this implies that
    I top injective morphisms lift against I top relative cell complexes, so in this case
    they lift against in particular elements of Jtop, which shows that it is a Serre fibration.
    """
    def construct(self):
        title = make_title("Lemma", 1.52)

        self.add(
            title
        )

        the_statement_1 = TextMobject(r"""
            $I_\text{Top}$-injective morphisms are weak homotopy equivalences.
        """, alignment="").scale(.75).to_edge(UP, buff=1.25)

        self.play(
            FadeIn(the_statement_1)
        )
        self.wait(2)

        lifting_property = tikz("lemma152_lifting_property", r"""
            \begin{tikzcd}
                S^{n-1} \arrow{d}[left]{\iota_n} \arrow{r} & \hat{X} \arrow{d}[right]{p} \\
                D^n \arrow[dashed]{ur}[left,yshift=.5em]{\exists} \arrow{r} & X
            \end{tikzcd}
        """, fn)

        self.play(
            FadeIn(lifting_property)
        )
        self.wait()

        pi_0 = TexMobject("\\pi_0:").scale(.75).to_edge(LEFT, buff=.5)

        self.play(
            FadeOut(lifting_property)
        )
        self.play(
            FadeIn(pi_0)
        )
        self.wait(2)

        n_0 = tikz("lemma152_pf_n_0", r"""
            \begin{tikzcd}
                S^{-1}\cong\emptyset \arrow{d} \arrow{r} & \hat{X} \arrow{d}[right]{p} \\
                D^0\cong\ast \arrow{r}[below]{x} \arrow[dashed]{ur} & X
            \end{tikzcd}
        """, fn)

        self.play(
            FadeIn(n_0)
        )
        self.wait(2)
        self.play(
            FadeOut(n_0)
        )

        n_1 = tikz("lemma152_pf_n_1", r"""
            \begin{tikzcd}
                S^{0}\cong\ast\sqcup\ast \arrow{d} \arrow{r} & \hat{X} \arrow{d}[right]{p} \\
                D^1\cong I \arrow{r} \arrow[dashed]{ur} & X
            \end{tikzcd}
        """, fn)

        self.play(
            FadeIn(n_1)
        )
        self.wait(2)
        self.play(
            FadeOut(pi_0),
            FadeOut(n_1)
        )

        pi_geq1 = TexMobject("\\pi_{n\geq 1}:").scale(.75).to_edge(LEFT, buff=.5)

        self.play(
            FadeIn(pi_geq1)
        )
        self.wait(2)

        n_n = tikz("lemma152_pf_n_n", r"""
            \begin{tikzcd}
                S^{n} \arrow{d} \arrow{r} & \hat{X} \arrow{d}[right]{p} \\
                D^{n+1} \arrow{r} \arrow[dashed]{ur} & X
            \end{tikzcd}
        """, fn)

        self.play(
            FadeIn(n_n)
        )
        self.wait(2)
        self.play(
            FadeOut(n_n)
        )

        a_surj = tikz("lemma152_pf_a_surj", r"""
            \begin{tikzcd}
                S^{n-1} \arrow{d} \arrow{r} & \ast \arrow{d} \arrow{r} 
                    & \hat{X} \arrow{d}[right]{p} \\
                D^n \arrow{r} & X \arrow{r}[above]{=} & X
            \end{tikzcd}
        """, fn)

        self.play(
            FadeIn(a_surj)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in [pi_geq1, a_surj, the_statement_1]]
        )

        the_statement_2 = TextMobject(r"""
            $I_\text{Top}$-injective morphisms are Serre fibrations
        """).scale(.75).to_edge(UP, buff=1.25)

        self.play(
            FadeIn(the_statement_2)
        )
        self.wait(2)

        statement_2_prop = TextMobject(r"""
            Every element of $J_\text{Top}$ is an $(I_\text{Top})$ relative cell complex.
        """).scale(.75)

        self.play(
            FadeIn(statement_2_prop)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        
class lemma152_reverse_pf(Scene):
    """
    As a bit of forewarning, the proof of the reverse direction,
    which we turn to know, is a significantly greater effort than the
    forward direction. If you follow along, however, I think you will
    find it to be very elegant and insightful. I'll do my best
    to make sense of it.
    So our assumption here is that we are starting with an acyclic
    Serre fibration f. We need to show that this lifts against the set
    of generating cofibrations. These are the inclusions of the boundary 
    into the n sphere. Like above, the fact that f is acyclic and hence
    a weak homotopy equivalence means that f is surjective, and so there
    exists a lift in the n=0 case, and in the n=1 case, which is again
    just formulating that connected components are images of connected
    components. Again, this is from the proof of the forward direction.
    The interesting things happen for n greater than or equal to 2.
    We want to show that we can construct lifts for commuting squares of this
    form. Since alpha compose f factors through a map kappa from the n
    disk, this shows that the image of alpha under f is trivial in the
    n-1 homotopy group of Y at little y. So little y and litte x are just
    the image of a chosen basepoint in S n-1.
    Well since f is an isomorphism on the level of homotopy groups, alpha
    itself is trivial in the n-1 homotopy group of X at little x.
    So since it's trivial, we can do the same thing and observe that alpha
    being trivial is equivalent to the existence of a map kappa prime
    such that this upper triangle commutes. So far so good, but the real
    issue, and our focus for the remainder of the proof, is that the bottom
    triangle doesn't necessarily commute. Our goal will be to show that we can
    find a map rho prime interchangeable with kappa prime such that both the 
    upper and lower triangles commute.
    A little bit of rearranging gives us this commuting square. Now
    you look at this square, and realize that you actually know the pushout
    of the square, it's an elementary example we covered- its the n sphere.
    Hence we can use the universal property of pushouts to obtain a unique
    map kappa comma f compose with kappa prime. So as a bit of warning on the
    notation, the mapps kappa and f compose kappa prime in the square
    are actually from dn to y, but we right it in this way to express
    the universal property succinctly. Also, this pair paranthesis notation
    for the map from Sn to Y has components which reflect the fact that it is 
    induced via the universal property of pushouts with respect to the maps
    or cocone with maps kappa and f compose with kappa prime.
    Well ok, this is nice, we have that this unique map is by definition a
    representative of the nth homotopy group of Y at y. Well again, since f
    is an isomorphism on the level of homotopy groups, this corresponds to the
    image of the equivalence class of some map rho from Sn to X.
    Immediately we observe that this is the bottom triangle from the original
    square. We had that the top triangle commuted, and wanted to show the bottom
    one did too. But that one had the diagonal map as kappa prime. So we want
    to re write rho with that in mind.
    So again, we remember that Sn is a pushout. But to do anything with that,
    we need two maps from Dn to X over which we can use the universal property
    to obtain some unique map out of Sn.
    So we can imagine that one of these maps carries the information of kappa 
    prime, and the other of kappa. kappa prime is actually a map from Dn to X
    so we can use that. Regular kappa isn't however, so we can just use a placeholder,
    rho prime, to keep track of this information.
    This exhibits the map rho is of the form rho prime comma kappa prime. Ok,
    so we have something of this form. Why did we do this? Well the idea is that
    rho prime is the suitable substitute for kappa prime, when the bottom map is
    just kappa.
    Well here's something cool about this new pushout map defined here: 
    it is in fact trivial. So for the first line we recall that kappa prime was
    defined to be such that f compose kappa prime was kappa,
    so in the first line the first summand is just that substitution and the second
    is a trivial element, i.e. in the class from kappa to itself. For the second line,
    we just factor out f from the first summand. For the third line, 
    we observe that f of rho prime kappa prime from the second line was just
    kappa comma f compose kappa prime from the commuting bottom triangle we just
    saw. And from this it is clear that this is 0.
    Well ok, so because we can just include sn into the standard interval
    object of dn, we already had a homotopy from kappa to 
    f compose rho prime, which we can call phi. So phi is just the extension
    of that previous map f compose rho prime comma kappa to the cylinder
    object over Dn. 
    Well phi is that map on the boundary of the cylinder object,
    so what does that mean? It means that the map is constant on the boundary of
    Dn. Why? Well consider each Dn to be a hemisphere of Sn, so they are
    attached along their boundaries to form Sn. Then since the map out of Sn
    is trivial and can be mapped to a single point, this means we could
    squash the hemispheres together, as this is also trivial homotopy type.
    If it was a circle, this would amount to having opposite points on the circle
    and holding them still and deforming the lines so that they are identified.
    But ok, phi is constant on the boundary. Why is this important?
    Well consider the situation we have, i.e. what phi is saying.
    It's saying right now that tihs diagram sort of commutes, almost
    commutes. I.e. it seems to commute up to homotopy, but we want it to
    literally commute.
    But what does phi actually tell us? Since it is constant on the
    boundary, it can be considered as a map out of s n-1
    union dn times i attached along the cylinder sn-1 times i.
    Intuitively, this means that each moment of the homotopy, which is a
    cross section of dn times I, the boundary is unchanged, which
    is just saying that the map is fixed on the boundary. But wow,
    this is just asking to be put into a pushout diagram. But what maps
    are we doing the pushout over? Well certainly it contains the information
    of phi, but remember that we had that commuting square, and we
    wanted the image of phi to agree with alpha compose f. We want
    everything to commute, after all, and alpha really is the only thing
    we haven't accounted for yet. We'll see this in a bit
    So previously our diagram with phi didn't reflect the fact that it fixed
    the boundary, and this new map just reflects that fact.
    But what's the nice thing about this attaching space? It's 
    homeomorphic to Dn times I again! So we can rewrite the homotopy
    phi between kappa and rho prime compose f with this new map
    f compose alpha comma phi. And finally, finally we can use the observation
    that f is a Serre fibration to demonstrate the following lift.
    And looking back at our square, this is precisely showing that kappa
    is rho prime compose with f by commutative, which shows the bottom triangle
    commutes as desired.
    Furthermore, the fact that alpha is in that middle map ensures that
    the entire square commutes.
    So hopefully you found that proof to be pretty neat. For now, that's
    all I have. We've in fact finished the first section of the nLab,
    topological homotopy theory. Starting next time, we get into the real
    substance of the theory, abstract homotopy.
    """
    def construct(self):
        title = make_title("Lemma", 1.52)

        self.add(
            title
        )

        n_0_and_1 = TexMobject("n=0,1:").scale(.75).to_edge(LEFT, buff=.5)
        self.play(
            FadeIn(n_0_and_1)
        )
        self.wait(2)

        n_0 = tikz("lemma152_reverse_pf_1", r"""
            \begin{tikzcd}
                \emptyset \arrow{d} \arrow{r} & X \arrow{d}[right]{f} \\
                \ast \arrow{r} \arrow[dashed]{ur} & Y
            \end{tikzcd}
        """, fn)

        self.play(
            FadeIn(n_0)
        )
        self.wait(2)
        self.play(
            FadeOut(n_0)
        )

        n_1 = tikz("lemma152_reverse_pf_2", r"""
            \begin{tikzcd}
                \ast\sqcup\ast \arrow{d} \arrow{r} & X \arrow{d}[right]{f} \\
                I \arrow{r} \arrow[dashed]{ur} & Y
            \end{tikzcd}
        """, fn)

        self.play(
            FadeIn(n_1)
        )
        self.wait(2)
        self.play(
            FadeOut(n_1)
        )

        n_geq_2 = TexMobject("n\\geq 2:").scale(.75).to_edge(LEFT, buff=.5)

        self.play(
            ReplacementTransform(n_0_and_1, n_geq_2)
        )
        self.wait(2)

        p1 = tikz("lemma152_reverse_pf_ngeq2_1", r"""
            \begin{tikzcd}
                S^{n-1} \arrow{r}[above]{\alpha} \arrow{d}[left]{\iota_n}
                    & X \arrow{d}[right]{f} \\
                D^n \arrow{r}[above]{\kappa} & Y
            \end{tikzcd}
        """, fn)

        self.play(
            FadeIn(p1)
        )
        self.wait(2)

        p2 = TexMobject(r"""
            f_\ast [\alpha] = 0\in\pi_{n-1}(Y,y)
        """).scale(.75).next_to(p1, direction=DOWN, buff=.5)

        self.play(
            FadeIn(p2)
        )

        p3 = TexMobject(r"""
            [\alpha] = 0\in\pi_{n-1}(X,x)
        """).scale(.75).next_to(p2, direction=DOWN, buff=.25)

        self.play(
            FadeIn(p3)
        )
        self.wait(2)
        self.play(
            FadeOut(p2),
            FadeOut(p3),
            FadeOut(p1)
        )
        self.play(
            FadeIn(p1.shift(2*LEFT))
        )

        p4 = tikz("lemma152_reverse_pf_ngeq2_2", r"""
            \begin{tikzcd}
                S^{n-1} \arrow{r}[above]{\alpha} \arrow{d}[left]{\iota_n} & X \\
                D^n \arrow{ur}[right, yshift=-.5em]{\kappa '}
            \end{tikzcd}
        """, fn).shift(2*RIGHT)

        self.play(
            FadeIn(p4)
        )
        self.wait(2)
        self.play(
            FadeOut(p4), 
            FadeOut(p1)
        )

        p5 = tikz("lemma152_reverse_pf_ngeq2_3", r"""
            \begin{tikzcd}
                S^{n-1} \arrow{r}[above]{\iota_n} \arrow{d}[left]{\iota_n} & 
                    D^n \arrow{d}[right]{f\circ\kappa '} \\
                D^n \arrow{r}[below]{\kappa} & Y
            \end{tikzcd}
        """, fn)

        self.play(
            FadeIn(p5)
        )
        self.wait(2)
        self.play(
            FadeOut(p5)
        )

        p6 = tikz("lemma152_reverse_pf_ngeq2_4", r"""
            \begin{tikzcd}
                S^{n-1} \arrow{r}[above]{\iota_n} \arrow{d}[left]{\iota_n} & 
                    D^n \arrow{d}[right]{f\circ\kappa '} & \\
                D^n \arrow{r}[below]{\kappa}[above,yshift=.5em]{(\text{po})} & S^n 
                    \arrow{dr}[right,yshift=.5em]{(\kappa,f\circ\kappa ')}& \\
                & & Y
            \end{tikzcd}
        """, fn).scale(1.5)

        self.play(
            FadeIn(p6)
        )
        self.wait(2)

        p7 = TexMobject(r"""
            [(\kappa,f\circ\kappa ')]\in\pi_n(Y,y)
        """).scale(.75).next_to(p6, direction=DOWN, buff=.5)

        self.play(
            FadeIn(p7)
        )
        self.wait(2)

        p8 = TexMobject(r"""
            f_\ast[\rho]=[(\kappa,f\circ\kappa ')]
        """).scale(.75).next_to(p7, direction=DOWN, buff=.25)

        self.play(
            FadeIn(p8)
        )
        self.wait(2)
        self.play(
            FadeOut(p6),
            FadeOut(p7), 
            FadeOut(p8)
        )

        p9 = tikz("lemma152_reverse_pf_ngeq2_9", r"""
            \begin{tikzcd}
                & X \arrow{d}[right]{f} \\
                S^n \arrow{ur}[left,yshift=.5em]{\rho}[right,yshift=-.5em]{\Downarrow}
                    \arrow{r}[below]{(\kappa,f\circ\kappa ')} & Y
            \end{tikzcd}
        """, fn)

        self.play(
            FadeIn(p9)
        )
        self.wait(2)
        self.play(
            FadeOut(p9)
        )

        p10 = p6 = tikz("lemma152_reverse_pf_ngeq2_10", r"""
            \begin{tikzcd}
                S^{n-1} \arrow{r}[above]{\iota_n} \arrow{d}[left]{\iota_n} & 
                    D^n \arrow{d}[right]{\rho '} & \\
                D^n \arrow{r}[below]{\kappa '}[above,yshift=.5em]{(\text{po})} & S^n 
                    \arrow{dr}[right,yshift=.5em]{(\rho ', \kappa ')}& \\
                & & X
            \end{tikzcd}
        """, fn).scale(1.5)

        self.play(
            FadeIn(p10)
        )
        self.wait(2)
        self.play(
            FadeOut(p10)
        )
        
        p11 = tikz("lemma152_reverse_pf_ngeq2_11", r"""
            \begin{tikzcd}
                & X \arrow{d}[right]{f} \\
                S^n \arrow{ur}[left,yshift=.5em]{(\rho ', \kappa ')}[right,yshift=-.5em]{\Downarrow}
                    \arrow{r}[below]{(\kappa,f\circ\kappa ')} & Y
            \end{tikzcd}
        """, fn)

        self.play(
            FadeIn(p11)
        )
        self.wait(2)
        self.play(
            FadeOut(p11)
        )

        self.play(
            FadeIn(p4.shift(2*LEFT))
        )
        self.wait(2)
        self.play(
            FadeOut(p4)
        )

        p12 = TexMobject(r"""
            S^n\overset{(f\circ\rho ',\kappa)}{\longrightarrow} Y
        """).scale(.75).to_edge(UP, buff=2.5)

        self.play(
            FadeIn(p12)
        )
        self.wait(2)

        p13 = TextMobject(r"""
            \begin{align*}
                [(f\circ\rho ',\kappa)] =& [(f\circ\rho ',f\circ\kappa ')] + 
                    [(f\circ\kappa ',\kappa)] \\
                =& f_\ast[(\rho',\kappa ')] + [(f\circ\kappa ',\kappa)] \\
                =&[(\kappa,f\circ\kappa ')] + [(f\circ\kappa ',\kappa)] \\
                =& 0
            \end{align*}
        """).scale(.75).shift(1*DOWN)

        self.play(
            FadeIn(p13)
        )
        self.wait(2)
        self.play(
            FadeOut(p12),
            FadeOut(p13)
        )

        p14 = tikz("lemma152_reverse_pf_ngeq2_14", r"""
            \begin{tikzcd}
                D^n \arrow{d} \arrow{dr}[right,yshift=.5em]{f\circ\rho '} & \\
                S^n\hookrightarrow D^n\times I \arrow{r}[above]{\phi} & Y \\
                D^n \arrow{u} \arrow{ur}[right,yshift=-.5em]{\kappa}
            \end{tikzcd}
        """, fn).scale(1.5)

        self.play(
            FadeIn(p14)
        )
        self.wait(2)
        self.play(
            FadeOut(p14)
        )

        p15 = tikz("lemma152_reverse_pf_ngeq2_15", r"""
            \begin{tikzcd}
                S^{n-1} \arrow{r}[above]{\alpha} \arrow{d}[left]{\iota_n} 
                    & X \arrow[dashed]{d}[right]{f} \\
                D^n \arrow[dashed]{ur}[left,yshift=.5em]{\rho '}[right,yshift=-.5em]{\Downarrow \phi}
                    \arrow{r}[below]{\kappa} & Y
            \end{tikzcd}
        """, fn)

        self.play(
            FadeIn(p15)
        )
        self.wait(2)
        
        p16 = TexMobject(r"""
            \phi:D^n\times I\to Y
        """).scale(.75).next_to(p15, direction=DOWN, buff=.5)

        self.play(
            FadeIn(p16)
        )
        self.wait(2)

        p17 = tikz("lemma152_reverse_pf_ngeq2_17", r"""
            \begin{tikzcd}
            S^{n-1}\times I \arrow{r} \arrow{d} & S^{n-1} \arrow{d}[right]{f\circ\alpha} & \\
            D^n\times I \arrow{r}[below]{\phi} & S^{n-1}\underset{S^{n-1}\times I}{\sqcup}
                D^n\times I \arrow{dr}[right,yshift=.5em]{(f\circ\alpha,\phi)} & \\
            & & Y
            \end{tikzcd}
        """, fn).scale(1.5)

        self.play(
            FadeOut(p15),
            FadeIn(p17)
        )
        self.wait(2)

        p18 = TexMobject(r"""
            S^{n-1}\underset{S^{n-1}\times I}{\sqcup}
                D^n\times I \overset{(f\circ\alpha,\phi)}{\longrightarrow} Y
        """).scale(.75).move_to(p16)

        self.play(
            ReplacementTransform(p16, p18)
        )
        self.wait(2)
        self.play(
            FadeOut(p18),
            FadeOut(p17)
        )

        p19 = tikz("lemma152_reverse_pf_ngeq2_19", r"""
            \begin{tikzcd}
                D^n \arrow{d} \arrow{r}[above]{\rho '} & X \arrow{d}[right]{f} \\
                S^{n-1}\underset{S^{n-1}\times I}{\sqcup} D^n\times I
                    \arrow{r}[above]{(f\circ\alpha,\phi)} \arrow[dashed]{ur} & Y \\
                D^n \arrow{u} \arrow{ur}[right,yshift=-.5em]{\kappa} &
            \end{tikzcd}
        """, fn).scale(1.5).shift(2.5*LEFT)

        self.play(
            FadeIn(p19)
        )
        self.wait(2)
        
        p20 = tikz("lemma152_reverse_pf_ngeq2_20", r"""
            \begin{tikzcd}
                S^{n-1} \arrow{r}[above]{\alpha} \arrow{d}[left]{\iota_n} 
                    & X \arrow{d}[right]{f} \\
                D^n \arrow{ur}[left,yshift=.5em]{\rho '}
                    \arrow{r}[below]{\kappa} & Y
            \end{tikzcd}
        """, fn).shift(2.5*RIGHT)

        self.play(
            FadeIn(p20)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

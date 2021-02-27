# Date: 2/24/21
# Purpose: model structure on functors nLab
# Notes:

from manimlib.imports import *
fn = "model_top_functors"


class def365(Scene):
    """
    We alluded earlier to developing a model structure on functors enriched in a suitable 
    sense over Top cg, and this is what we turn to now. First some definitions.
    A topologically enriched category is a category enriched over Top cg. It has
    a class of objects, obviously, but its morphisms is where this enrichment over Topcg
    comes into play. So for each a, b objects, the space of morphisms between them
    also called the hom space is a space in Top cg. So this is a sort of generalization of 
    mapping spaces, but note that we aren't assuming anything about morphisms from a to b,
    indeed a and b need not apparantly be topological spaces. We just need to associate
    to each pair a hom space which is a Top cg space. 
    We want this to respect composition in the following sense. And we also want to 
    have an identity morphism on a that makes the composition associative and unital,
    just meaning it is a unit. So the composition was defined out of the cartesian product,
    and I don't know about you but now when I see a cartesian product in Top cg I immediately
    am thinking about specializing to pointed Top cg, which we indeed can do by replacing
    the cartesian product with a smash product and requiring hom spaces to be pointed
    Top cg spaces.
    """
    def construct(self):
        t = make_title("Definition", 3.65)
        self.title(t)

        d1 = TextMobject("A ", "topologically enriched category ", r"""
            $\mathcal{C}$ is a $Top_{cg}$-enriched category, hence:
            \begin{enumerate}
                \item a class of objects $Obj(\mathcal{C})$
                \item for each $a,b\in Obj(\mathcal{C})$ a compactly generated 
                    space $$\mathcal{C}(a,b)\in Top_{cg}$$ called the 
                    \textbf{space of morphisms} or the \textbf{hom-space} between 
                    $a$ and $b$
                \item for each $a,b,c\in Obj(\mathcal{C})$ a continuous function a 
                    composition function
                    $$ \circ_{a,b,c}:\mathcal{C}(a,b)\times\mathcal{C}(b,c)\longrightarrow
                    \mathcal{C}(a,c) $$
                \item for each $a\in Obj(\mathcal{C})$ a point $Id_a\in\mathcal{C}(a,a)$ called 
                    the identity morphism on $a$ such that composition is associative and 
                    unital.
            \end{enumerate}
        """, alignment="").scale(.7).shift(.5*DOWN)

        self.cycle(
            [d1],
            out=False
        )
        self.clear()

class rmk366(Scene):
    """
    So what is so enriched about this category? Well, notice that we didn't really talk
    about homs between objects in the category as sets as we usually do, but instead as
    entire top cg spaces, which is a lot of extra structure and information. So it is
    in this sense enriched. Enriched from what? Well from the category with morphisms
    just the underlying set of the hom spaces.
    """
    def construct(self):
        t = make_title("Remark", 3.66)
        self.title(t)

        r1 = TextMobject(r"""
            The forgetful functor $$U:Top_{cg}\longrightarrow Set$$ yields an ordinary 
            locally small category with $$Hom_\mathcal{C}(a,b)=U(\mathcal{C}(a,b)).$$
        """, alignment="").scale(.75).to_edge(LEFT, buff=.5)

        self.cycle(
            [r1],
            out=False
        )
        self.clear()

class ex367(Scene):
    """
    The most immediate example is Top cg itself, as we saw that the mapping space exists
    always. Composition is given in this way, so if we apply the product mapping space
    adjunction to this composition we get our desired map. And of course we can
    also view pointed top cg as enriched over itself as well.
    """
    def construct(self):
        t = make_title("Example", 3.67)
        self.title(t)

        e1 = TextMobject(r"""
            The category $Top_{cg}$ canonically obtains the structure of a topologically 
            enriched category. Its hom-spaces are $$Top_{cg}(X,Y):=Y^X,$$ its composition
            is given by the adjunct of 
            $$ X\times Y^X\times Z^Y \overset{(ev, id)}{\longrightarrow}Y\times Z^Y 
            \overset{ev}{\longrightarrow} Z.$$
            Similarly with $$Top_{cg}^{\ast /}(X,Y):=Maps(X, Y)_\ast.$$
        """, alignment="").scale(.75)

        self.cycle(
            [e1],
            out=False
        )
        self.clear()

class def368(Scene):
    """
    And now we are ready to talk about topologically enriched functors. So as the name 
    might suggest, it is a functor between two topologically enriched categories in the 
    following sense: objects are send to objects, and the hom space of a and b is
    sent to the hom space of f of a and f of b in the enriched category D. We do require
    that this preserves composition and identity, of course.
    Ok, so what does a homomorphism between enriched functors look like? We get the 
    notion of a Top cg enriched natural transformation. So it's like a normal natural
    transformation with some more structure. So here's how we think of it generally-
    its a family of morphisms eta c such that for any two objects c and d of C
    the following diagram commutes. So here I is the tensor object of the category
    we are enriching over, which in this case is Topcg, whose tensor unit is the point.
    But I like this presentation that nLab gives on their dedicated enriched natural 
    transformation page over the one they give in the material, this just meshes better
    with my intuition of a normal natural transformation.
    The nLab gives this definition explicitly, that there always exist eta c and
    eta d such that these agree. Looking out our previous characterization of an
    enriched natural transformation, this composition makes sense, where here
    it is compressed perhaps at the cost of abuse of notation.
    """
    def construct(self):
        t = make_title("Definition", 3.68)
        self.title(t)

        d1 = TextMobject("A ", "topologically enriched functor ", r"""
            between two topologically enriched categories
            $$ F:\mathcal{C}\longrightarrow\mathcal{D}$$
            is a $Top_{cg}$-enriched functor, hence:
            \begin{enumerate}
                \item a function
                    $$F_0:Obj(\mathcal{C})\longrightarrow Obj(\mathcal{D})$$
                    of objects
                \item for each $a,b\in Obj(\mathcal{C})$ a continuous function
                    $$ F_{a,b}:\mathcal{C}(a,b)\longrightarrow\mathcal{D}(F_0(a), F_0(b))$$
                    of hom-spaces that preserves composition and identity.
            \end{enumerate}
        """, alignment="").scale(.75).to_edge(DOWN, buff=.5)
        d1[1].set_color(BLUE)

        d2 = TextMobject("An" " enriched natural transformation ", r"""
            $\eta:F\to G$ is a family of morphisms in the category $V$ we 
            are enriched over
            $$\eta_c:I\longrightarrow D(F c, G c)$$
            (out of the tensor unit $I$ of $V$) indexed over $Ob(C)$ such that for any 
            two objects $c, d$ of $C$ the following diagram commutes:
        """, alignment="").scale(.75).to_title(t)
        d2[1].set_color(BLUE)

        d3 = tikz("def368_d3", r"""
            \begin{tikzcd}
                C(c,d)
                    \arrow{r}[above]{\cong}\arrow{d}[left]{\cong}
                    & C(c,d)\otimes I
                    \arrow{r}[above]{G_{c,d}\otimes\eta_c}
                    & D(G c,G d)\otimes D(F c,G c)
                    \arrow{d}[right]{\circ_D} \\
                I \otimes C(c,d)
                    \arrow{r}[below]{\eta_d\otimes F_{c,d}}
                    & D(F d, Gd)\otimes D(F c, F d)
                    \arrow{r}[below]{\circ_D}
                    & D(F c, G d)
            \end{tikzcd}
        """, fn).next_to(d2, direction=DOWN, buff=.25)

        self.cycle(
            [d1]
        )
        self.cycle(
            [d2, d3],
            successive=False
        )

        d4 = TextMobject(r"""
            Equivalently, for each $c\in Obj(\mathcal{C})$ a choice of morphism 
            $\eta_c\in\mathcal{D}(F(c),G(c))$ such that for each pair of objects 
            $c, d\in\mathcal{C}$ these two agree:
            \begin{gather*}
                \eta_d\circ F(-):\mathcal{C}(c,d)\longrightarrow\mathcal{D}(F(c),G(d)) \\
                G(-)\circ\eta_c:\mathcal{C}(c,d)\longrightarrow\mathcal{D}(F(c), G(d))
            \end{gather*}
        """, alignment="").scale(.75)

        d5 = TextMobject(r"""
            We write $[\mathcal{C},\mathcal{D}]$ for the resulting category of topologically 
            enriched functors.
        """, alignment="").scale(.75)

        d_4_to_5 = VGroup(
            d4, d5
        ).arrange_submobjects(
            DOWN, buff=2
        )

        self.cycle(
            [d4, d5],
            out=False
        )
        self.clear()

class ex370(Scene):
    """
    So let's have another way to think about topologically enriched functors. So
    okay, it obviously has the impormation of associating a top cg space
    to each object in the enriched category, but here's another way to think of the
    information with regards to morphisms. Since we have the product mapping
    adjunction, the association of the C hom space of a and b to the hom space
    of Fa in Fb in Top cg, which is the mapping space Fb Fa, is equivalently
    a continuous function of this form which respects composition.
    On another not, we can define a functor for each object c in the enriched category,
    which sends an object do to the hom space of c and d. On morphisms,
    like it sends the morphism from d to e to the a morphism from c to d to e
    in the hom space of c and e, basically respecting composition as we've defined
    it so far. We call such a functor a representable functor, in this case specifically 
    a topologically enriched representable functor, and will often use y for it.
    """
    def construct(self):
        t = make_title("Example", 3.70)
        self.title(t)

        e1 = TextMobject(r"""
            A functor $F\in [\mathcal{C},Top_{cg}]$ is equivalently
            \begin{enumerate}
                \item a compactly generated topological space $F_a\in Top_{cg}$ for each 
                    object $a\in Obj(\mathcal{C})$
                \item a continuous function
                    $$ F_a\times\mathcal{C}(a,b)\longrightarrow F_b$$
                    for all pairs of objects $a,b\in Obj(\mathcal{C})$ such that 
                    composition is respected.
            \end{enumerate}
        """, alignment="").scale(.75)

        self.cycle(
            [e1]
        )

        e2 = TextMobject(r"""
            For every object $c\in\mathcal{C}$, there is a topologically enriched
        """, " representable functor", r"""
            , denoted $y(c)$ or $\mathcal{C}(c,-)$, which sends objects to
            $$ y(c)(d)=\mathcal{C}(c,d)\in Top_{cg}$$
            and whose action on morphisms is, under the above indentification, just 
            the composition operation in $\mathcal{C}$.
        """, alignment="").scale(.75)
        e2[1].set_color(BLUE)

        self.cycle(
            [e2],
            out=False
        )
        self.clear()

class prop371(Scene):
    """
    So an awesome feature of topologically enriched functors is that they inheret
    just enough structure from Top cg, which is well structured as we've seen, to
    be general enough for applications but also again retain a lot of good properties.
    So the first example of this is that for C a small topologically enriched category,
    the category of topologically enriched functors has all limits and colimits,
    and we compute them objectiwse like this. So let's see why this is.
    If we just forget the topology, then this is the case in Set of course, which
    has all limits and colimits and so the properties follow from the universal property.
    Well then we've shown that Top cg has limits and colimits as well, so this goes
    back to proposition 1.5 in the first video, that this property persists
    when we add the topology back into the picture. So the idea is that we are
    essentially taking limits and colimits of objects in Top cg.
    """
    def construct(self):
        t = make_title("Proposition", 3.71)
        self.title(t)

        p1 = TextMobject(r"""
            For $\mathcal{C}$ any small topologically enriched category, then the 
            enriched functor category $[\mathcal{C}, Top_{cg}]$ has all limits and colimits, 
            and they are computed objectwise:
            if $$F_\bullet:I\longrightarrow [\mathcal{C},Top_{cg}]$$ is a diagram of functors 
            and $c\in\mathcal{C}$ is any object, then
            $$ (\underset{\longleftarrow i}{\lim}F_i)(c)\simeq \underset{\longleftarrow i}{\lim}
            (F_i(c))\quad\in Top_{cg}$$
            and
            $$(\underset{\longrightarrow i}{\lim}F_i)(c)\simeq \underset{\longrightarrow i}{\lim}
            (F_i(c))\quad\in Top_{cg}$$
        """, alignment="").scale(.75)

        self.cycle(
            [p1],
            out=False
        )
        self.clear()

class def372(Scene):
    """
    We can also construct two new operations. The first is called tensoring.
    So it takes an enriched functor, a top cg spaces, and spits out a top cg
    functor. This resulting functor sends an object c in the enriched category to 
    F(c), which is a top cg space, cross X. Dually, the powering again takes a 
    top cg space X and an enriched functor and spits out an enriched functor.
    The resulting enriched functor sends an object c to the mapping space F(c) X.
    Analagously, we can do the same for pointed top cg with smash products
    and pointed mapping spaces. These are smash tensoring and pointed powerings.
    """
    def construct(self):
        t = make_title("Definition", 3.72)
        self.title(t)

        d1 = TextMobject("The", " tensoring ", r"""
            of $[\mathcal{C}, Top_{cg}]$ over $Top_{cg}$ is a functor
            \begin{gather*}
                (-)\cdot (-):[\mathcal{C},Top_{cg}]\times Top_{cg}\longrightarrow
                    [\mathcal{C},Top_{cg}] \\
                F\cdot X: c\mapsto F(c)\times X
            \end{gather*}
        """, alignment="").scale(.75).to_edge(LEFT, buff=.5)
        d1[1].set_color(BLUE)

        self.cycle(
            [d1],
            out=False
        )

        d2 = TextMobject("The", " powering ", r"""
            of $[\mathcal{C},Top_{cg}]$ over $Top_{cg}$ is a functor
            \begin{gather*}
                (-)^{(-)}:(Top_{cg})^{op}\times [\mathcal{C},Top_{cg}]
                \longrightarrow [\mathcal{C},Top_{cg}] \\
                F^X:c\mapsto F(c)^X
            \end{gather*}
        """, alignment="").scale(.75).to_edge(LEFT, buff=.5)
        d2[1].set_color(BLUE)

        self.fade_replace(
            d1, d2
        )
        self.clear()

class prop373(Scene):
    """
    One of the most important results in category theory is the Yoneda lemma, and
    we can, with enrichement and representable functors, obtain a Top cg enriched
    version of the Yoneda lemma. So there is a stronger version, but here's a simpler
    version that will suffice for our purposes. So yeah,
    we have a bijection from the tensorings of gamma c and X to F and morphisms 
    from X to F(c). So the tensoring lies in the category of enriched functors, while
    the second morphisms are morphisms in Top cg itself. So let's prove this.
    We start with a map from the tensoring of gamma c and X to F, and we want to 
    find a corresponding map from X to Fc. At a point c, this is this map eta c
    from the hom space of c and itself cross X to F(c). Well we required that this
    hom space with itself have an identity morphism, so restrict to that case
    to obtain a map from X to F(c). So this is of course the form we were looking
    for, but we have some more work to do. Because we restricted to c, it is not clear that
    on all the other objects d in the enriched category that this is uniquel defined.
    Well, eta are maps on functors, but which functors first of all? Well from the tensoring
    of a representable functor and X to F. Will the tensoring is the hom space of c
    and something cross X, and F is from C to Topcg. So we have a natural transformation
    square as follows. If you're looking at the nLab, remark 369 is a specialization of the
    case when these are our two functors, not generally, so don't be confused, because
    it really confused me when I saw it.
    But ok, left map followed by the bottom one is by a map from the top left to the
    bottom right, hence an element of that hom space since we are enriched, and since this is
    a hom space in Topcg it is the mapping space as you see here. Now instead of all of the 
    Hom space of c to itself, restrict ourselves to the identity on c. Then we get this
    commuting square associated to any morphism f. Well, then the bottom map is as follows by
    commutativity. The point of restricting like this is that this map is uniquely determined,
    there's no wiggle room in how to determine this. Hence eta d in general, which must agree
    with the restriction to identity, can only be defined in one way, and so we are done in this
    direction, we showed that to each morphism from the tensoring to an enriched functor,
    there is a unique morphism from X to F(c).
    We need to show the converse, and then we will be done. But we do the same method, this
    time starting with a function from X to F(c), then considering this component for each 
    d, restricting to the identity, etc.
    """
    def construct(self):
        t = make_title("Proposition", 3.73)
        self.title(t)

        p1 = TextMobject(r"""
            For $c\in Obj(\mathcal{C})$, $X\in Top_{cg}$, and $F\in [\mathcal{C}, Top_{cg}]$, 
            there is a natural bijection between
            \begin{enumerate}
                \item morphisms $y(c)\cdot X\longrightarrow F$ in $[\mathcal{C}, Top_{cg}]$
                \item morphisms $X\longrightarrow F(c)$ in $Top_{cg}$.
            \end{enumerate}
            In short:
            $$ \dfrac{y(c)\cdot X\longrightarrow{F}}{X\longrightarrow F(c)}$$
        """, alignment="").scale(.75)

        self.cycle(
            [p1]
        )

        p2 = TexMobject(r"""
            \eta_c:\mathcal{C}(c,c)\times X\longrightarrow F(c) \\
            \eta_c(id_c,-):X\longrightarrow F(c)
        """).scale(.75)

        p3 = TexMobject(r"""
            \eta_d:\mathcal{C}(c,d)\times X\longrightarrow F(d)
        """).scale(.75)

        p_2_to_3 = VGroup(
            p2, p3
        ).arrange_submobjects(
            DOWN, buff=2
        )

        self.cycle(
            [p_2_to_3],
            out=False
        )

        p4 = TexMobject(r"""
            F(-)\circ\eta_c:\mathcal{C}(c,d)\longrightarrow F(d)^{\mathcal{C}(c,c)\times X}\\
            \eta_d\circ\mathcal{C}(c,-)\times X:\mathcal{C}(c,d)\longrightarrow 
                F(d)^{\mathcal{C}(c,c)\times X}
        """).scale(.75)

        self.fade_replace(
            p_2_to_3, p4
        )

        p5 = tikz("prop373_p5", r"""
            $f\quad\mapsto\quad$
            \begin{tikzcd}
                \mathcal{C}(c,c)\times X
                    \arrow{r}[above]{\eta_c}\arrow{d}[left]{\mathcal{C}(c,f)}
                    & F(c)
                    \arrow{d}[right]{F(f)} \\
                \mathcal{C}(c,d)\times X
                    \arrow{r}[below]{\eta_d}
                    & F(d)
            \end{tikzcd}
        """, fn).shift(.5*UP)

        self.fade_replace(
            p4, p5
        )

        p6 = tikz("prop373_p6", r"""
            $f\quad\mapsto\quad$
            \begin{tikzcd}
                \{id_c\}\times X
                    \arrow{r}[above]{\eta_c}\arrow{d}[left]{\mathcal{C}(c,f)}
                    & F(c)
                    \arrow{d}[right]{F(f)} \\
                \{f\}\times X
                    \arrow{r}[below]{\eta_d}
                    & F(d)
            \end{tikzcd}
        """, fn).shift(.5*UP)

        self.fade_replace(
            p5, p6
        )
        self.clear()

class def374(Scene):
    """
    It's time to start thinking about how to get a model structure. So we have these classes,
    which are formed by tensoring with topological generating cofibrations and acyclic topological
    generating fibrations over all representable functors. Likewise, in the pointed case we
    just use smash tensoring instead of regular tensoring. As you might expect, these
    are the generating cofibrations and acyclic generating cofibrations that will exhibit
    what is called the projective model structure on topologically enriched functors over C
    as cofibrantly generated.
    """
    def construct(self):
        t = make_title("Definition", 3.74)
        self.title(t)

        d1 = TextMobject(r"""
        \begin{gather*}
            I_{Top}^\mathcal{C}:=\left\{ y(c)\cdot (S^{n-1}\overset{\iota_n}{\longrightarrow}
                D^n) \right\}_{{n \in \mathbb{N},} \atop {c \in Obj(\mathcal{C})}} \\
            J_{Top}^\mathcal{C}:=\left\{ y(c)\cdot (D^n\overset{(id,\delta_0)}{\longrightarrow}
                D^n\times I) \right\}_{{n \in \mathbb{N},} \atop {c \in Obj(\mathcal{C})}}
        \end{gather*}
        """).scale(.75)

        self.cycle(
            [d1],
            out=False
        )

        d2 = TextMobject(r"""
        \begin{gather*}
            I_{Top^{\ast /}}^\mathcal{C}:=\left\{ y(c)\cdot (S^{n-1}\overset{(\iota_n)_+}{\longrightarrow}
                D^n) \right\}_{{n \in \mathbb{N},} \atop {c \in Obj(\mathcal{C})}} \\
            J_{Top^{\ast /}}^\mathcal{C}:=\left\{ y(c)\cdot (D^n\overset{(id,\delta_0)_+}{\longrightarrow}
                D^n\times I) \right\}_{{n \in \mathbb{N},} \atop {c \in Obj(\mathcal{C})}}
        \end{gather*}
        """).scale(.75)

        self.fade_replace(
            d1, d2
        )
        self.clear()

class def375(Scene):
    """
    For classes of morphisms in the model category, these are actually going to be top
    enriched natural transformations, as we are trying to put the model category on 
    topologically enriched functors. SO a projective weak equivalence is one that
    for all choice of object c we have a weak equivalence. This makes sense because eta
    c will be a map between objects in Top cg.
    Projective fibrations likewise are those eta such that each eta c is a Serre fibration,
    and projective cofibrations are retracts of the I top C from before, so the set of 
    tensoring with all representable functors with all generating topological cofibrations
    one by one. We write these in this way, indicated the model structure which we will turn
    to now.
    """
    def construct(self):
        t = make_title("Definition", 3.75)
        self.title(t)

        d1 = TextMobject(r"""
            A natural transformation $\eta:F\to G$ between topologically enriched functors 
            is
            \begin{itemize}
                \item a \textbf{projective weak equivalence} if for all $c\in Obj(\mathcal{C})$ 
                    the component $\eta_c:F(c)\to G(c)$ is a weak homotopy equivalence
                \item a \textbf{projective fibration} if for all $c\in Obj(\mathcal{C})$ the 
                    component $\eta_c:F(c)\to G(c)$ is a Serre fibration
                \item a \textbf{projective cofibration} if it is a retract of an 
                    $I_{Top}^\mathcal{C}$-relative cell complex
            \end{itemize}
            Write
            \begin{gather*}
                [\mathcal{C},(Top_{cg})_{Quillen}]_{proj} \\
                [\mathcal{C},(Top_{cg})_{Quillen}^{\ast /}]_{proj}
            \end{gather*}
        """, alignment="").scale(.75).to_edge(DOWN)

        self.cycle(
            [d1],
            out=False
        )
        self.clear()

class thm376(Scene):
    """
    The theorem of course is that these constitute the projective model structure on enriched
    functors, over Top cg and over pointed Top cg.
    For the proof, we already showed that this has all limits an colimits, so we can focus
    just on the model structure. But the enriched Yoneda lemma tells us that for example
    studying morphisms rom our class of cofibrations, which we defined as a tensoring 
    of representable
    functors with generating topological cofibrations, amounts to studying morphisms
    from topological generating cofibrations. So we can generalize all of our previous
    work is the idea. So for example, studying the right lifting property can be thought
    of as this.
    """
    def construct(self):
        t = make_title("Theorem", 3.76)
        self.title(t)

        t1 = TextMobject(r"""
            These classes of morphisms constitute a model category structure on 
            $[\mathcal{C},Top_{cg}]$ and $[\mathcal{C},Top_{cg}^{\ast /}]$, called the
        """, " projective model structure on enriched functors ", r"""
            $$[\mathcal{C},(Top_{cg})_{Quillen}]_{proj}$$ and
            $$[\mathcal{C},(Top_{cg})_{Quillen}^{\ast /}]_{proj}.$$
            These are cofibrantly generated, with sets of generating (acyclic) 
            cofibrations the sets $I_{Top}^\mathcal{C}$, $J_{Top}^\mathcal{C}$ and 
            $I_{Top^{\ast /}}^\mathcal{C}$, $J_{Top^{\ast /}}^\mathcal{C}$, respectively.
        """, alignment="").scale(.75)
        t1[1].set_color(BLUE)

        self.cycle(
            [t1]
        )

        t2 = tikz("thm376_t2", r"""
        $\left(
            \begin{tikzcd}
                y(c)\cdot S^{n-1}
                    \arrow{r}\arrow{d}[left]{(id\cdot\iota_n)}
                    & F
                    \arrow{d}[right]{r} \\
                y(c)\cdot D^n
                    \arrow{r}
                    & G
            \end{tikzcd}
        \right) \quad\leftrightarrow\quad
        \left(
            \begin{tikzcd}
                S^{n-1}
                    \arrow{r}\arrow{d}
                    & F(c)
                    \arrow{d}[right]{\eta_c} \\
                D^n
                    \arrow{r}
                    & G(c)
            \end{tikzcd}
        \right)$
        """, fn)

        self.cycle(
            [t2],
            out=False
        )
        self.clear()

class ex377(Scene):
    """
    An evident example is the category of enriched functors of pointed top cg from 
    itself. The nuance is important here, though, because above we required that the
    enriched category was small, but pointed top cg isn't, which is a problem in so
    far as we have the failure of all limits and colimits existing.
    We can remedy this by restricting to a full subcategory. One good choise is finite
    CW-complexes. Then we do have a projective model category, which has the name
    strict model structure for excisive functors. This amazingly shows up in spectra, so
    in stable homotopy theory, where this is shown to be Quillen equivalent to a model
    structure for spectra.
    """
    def construct(self):
        t = make_title("Example", 3.77)
        self.title(t)

        e1 = TexMobject(r"""
            [Top_{cg}^{\ast /}, Top_{cg}^{\ast /}]
        """).scale(.75)

        e2 = TexMobject(r"""
            Top_{cg, fin}^{\ast /}\hookrightarrow Top_{cg}^{\ast /}
        """).scale(.75)

        e3 = TexMobject(r"""
            [Top_{cg, fin}^{\ast /}, Top_{cg}^{\ast /}]_{proj}
        """).scale(.75)

        e_1_to_3 = VGroup(
            e1, 
            e2, 
            e3
        ).arrange_submobjects(
            DOWN,
            buff=1
        )

        self.cycle(
            [e1, e2, e3],
            out=False
        )
        self.clear()

class ex377_outro(Scene):
    """
    It might not seem like it, but this projective model structure allows us to generalize 
    a lot of concepts to a homotopy-theoretic version. So the excisive functors from before
    can be used to generalized differential calculus to the Goodwillie calculus, which is a 
    homotopy theoretic version. Similarly, we can obtain what are called homotopy colimits.
    So here's a way to think about the property of having colimits and limits. So let C
    be a category, I be a small category which we use to quote on quote index the limits. Then
    we can consider the functor category from I to C, so all functors from I to C. This amounts
    to squares as objects, and morphisms between squares i.e. natural transformations as
    morphisms. We call these objects I shaped diagrams. Well, we can canonically associate
    to each object in see the square or diagram that is just constant on c. So on the right
    of the square is something that sends c to itself. Ok, the purpose of this way the 
    following.
    Think about the property of having colimits. This amounts to a universal cocone of shape I,
    which can be thought of as an elemnt in the functor category I C. The morphisms from the
    colimit object in C to objects in the diagram is equivalently thought of, by univesality,
    as the maps between cocones, i.e. we have the following adjunction precisely
    when C has all colimits of shape I. DUally with limits.
    """
    def construct(self):
        d1 = TextMobject(r"""
            \begin{enumerate}
                \item precisely when $\mathcal{C}$ has all colimits of shape $I$, then the functor 
                    $const_I$ has a left adjoint functor, which is the operation of forming 
                    these colimits:
                    $$ [I,\mathcal{C}]
                    \underoverset
                    {\underset{const_I}{\longleftarrow}}
                    {\overset{\underset{\longrightarrow}{\lim}_I}{\longrightarrow}}
                    {\bot}
                    \mathcal{C} $$
                \item precisely when $\mathcal{C}$ has all limits of shape $I$, then the 
                    functor $const_I$ has a right adjoint functor, which is the operation 
                    of forming these limits.
                    $$ [I,\mathcal{C}]
                    \underoverset
                    {\underset{\underset{\longleftarrow}{\lim}_I}{\longrightarrow}}
                    {\overset{const_I}{\longleftarrow}}
                    {\bot}
                    \mathcal{C} $$
            \end{enumerate}
        """, alignment="").scale(.75)

        self.cycle(
            [d1],
            out=False
        )
        self.clear()

class prop378(Scene):
    """
    The ideas was that I was small, and now you might see why enriched functors come
    into play. It turns out that those adjunctions above can be upgraded to Quillen
    adjunctions in the case of Top cg and pointed top cg. To see this, just think
    of a fibration in Top cg. The contant map in the adjunctions sends it to the
    I-shaped diagram constant on the fibration. What were fibrations in the projective
    model structure? Well they were natural transformations that for each object was
    a Serre fibration. Well, consider a morphism between two I shaped diagrams, one
    being the one constant on the fibration. Well then if we pick some point in I,
    the diagram is still constant objectwise and hence preserves the fibration. Likewise
    for acyclic fibrations.
    """
    def construct(self):
        t = make_title("Proposition", 3.78)
        self.title(t)

        p1 = TextMobject(r"""
            Let $I$ be a small topologically enriched category. Then the 
            $(\underset{\longrightarrow I}{\lim}\dashv const_I)$-adjunction is a Quillen 
            adjunction:
            \begin{gather*}
                [I,(Top_{cg})_{Quillen}]_{proj}
                \underoverset
                {\underset{const_I}{\longleftarrow}}
                {\overset{\underset{\longrightarrow}{\lim}_I}{\longrightarrow}}
                {\bot}
                (Top_{cg})_{Quillen} \\
                [I,(Top^{\ast/}_{cg})_{Quillen}]_{proj}
                \underoverset
                {\underset{const}{\longleftarrow}}
                {\overset{\underset{\longrightarrow}{\lim}}{\longrightarrow}}
                {\bot}
                (Top^{\ast/}_{cg})_{Quillen}
            \end{gather*}
        """, alignment="").scale(.75)

        self.cycle(
            [p1],
            out=False
        )
        self.clear()

class def379(Scene):
    """
    The point is that Quillen adjunctions give us a way to upgrade things to the 
    homotopy category. A homotopy colimit is the left derived functor of the colimit
    functor from before.
    """
    def construct(self):
        t = make_title("Definition", 3.79)
        self.title(t)

        d1 = TextMobject("The left derived functor of the colimit functor is the",\
            " homotopy colimit ", r"""
            $$hocolim_I:=\mathbb{L}\underset{\longrightarrow I}{\lim}:
            Ho([I,Top])\longrightarrow Ho(Top)$$
            and
            $$ hocolim_I:=\mathbb{L}\underset{\longrightarrow I}{\lim}:
            Ho([I,Top^{\ast /}])\longrightarrow Ho(Top^{\ast /}).$$
        """, alignment="").scale(.75)
        d1[1].set_color(BLUE)

        self.cycle(
            [d1],
            out=False
        )
        self.clear()

class rmk380(Scene):
    """
    We don't exactly know how to form colimits in this functor category, but since every object
    in Top cg is fibrant, every object of the Functor category is projectively fibrant,
    meaning that it is fibrant with respect to the projective model structure. Hence it suffices
    to just take the ordinary colimit of any projectively cofibrant replacement.
    """
    def construct(self):
        t = make_title("Remark", "3.80")
        self.title(t)

        self.clear()

class ex381(Scene):
    """
    So of course the archetypical example of this is when we take I to be the poset of
    natural numbers. So let's think of a functor from this to Top cg. Well that amounts
    to a sequence of topological spaces. Now observe the following. Observe this sequence
    is projectively cofibrant, so intuitively think of the initial object above this diagram and
    making a cone, so a map from it to each object in the sequence. What does that mean?
    Well by definition it means that each of those maps are cofibrantions in Top cg ( we get
    this reduced definition since the natural numbers have the discrete topology, so the
    tensoring is really simple). Well that would imply then that all the horizontal maps are
    cofibrations as well. Equivalently, if we didn't start with the assumption that the 
    sequence is cofibrant, then if all the horizontal maps were cofibrations and the first
    object was X_0, commutativity would again imply that the entire sequence is cofibrant.
    So those two conditions are pricesly, i.e. if and only if, what makes a sequence here 
    cofibrant.
    """
    def construct(self):
        t = make_title("Example", 3.81)
        self.title(t)

        e1 = TexMobject(r"""
            \mathbb{N}^\leq = \{0\to 1\to 2\to 3\to \cdots \}
        """).scale(.75)

        e2 = TexMobject(r"""
            X_\bullet:\mathbb{N}^\leq\longrightarrow Top_{cg}
        """).scale(.75)

        e_1_to_2 = VGroup(
            e1, e2
        ).arrange_submobjects(
            DOWN, 
            buff=1
        )

        self.cycle(
            [e_1_to_2],
            out=False
        )

        e3 = TextMobject(r"""
            $$X_0\overset{f_0}{\longrightarrow}X_1\overset{f_1}{\longrightarrow}X_2
            \overset{f_2}{\longrightarrow}X_3\longrightarrow\cdots$$
            Those sequences $X_\bullet$ which are cofibrant in the projective model 
            structure are precisely those for which
            \begin{enumerate}
                \item all component morphisms $f_i$ are cofibrations in $(Top_{cg})_{Quillen}$ 
                    or $(Top_{cg}^{\ast /})_{Quillen}$, hence retracts of relative cell complex 
                    inclusions
                \item the object $X_0$, and hence all other objects, are cofibrant, hence are 
                    retracts of cell complexes.
            \end{enumerate}
        """, alignment="").scale(.75)

        self.fade_replace(
            e_1_to_2, e3
        )
        self.clear()

class prop382(Scene):
    """
    So assume for a second that the sequence isn't cofibrant at all. We just have two sequences,
    and suppose we have a projective cofibration between them. Well intuitively imagine we
    stack them, so then all vertical maps between spaces in the sequences are cofibrations.
    So it's not hard to belive that when we form colimits over these diagrams, we in a sense
    also form colimits over these vertical maps and hence obtain a cofibration between
    the colimits in Top cg. Analagously for acyclic cofibrations.
    But now suppose that the sequences were projectively cofibrant, and not only that, instead
    of all the maps between the sequences of spaces being just cofibrations in Top cg, i.e.
    retracts of realative cell complexes, we also require that these are actually plain
    relative cell complex inclusions. So this is a heavy extra requirement on top of these
    sequences being cofibrant. Then we have this proposition, which gives us quite a bit more:
    The colimit not only preserves cofibrations, it also preserves fibrations. Secondly,
    if we have a finite category and then consider a finite I shaped diagram of 
    sequences, then we have this weak homotopy equivalence.
    Here's the idea for the proof. For the first statement, the idea is that fibrations
    lift against relative cell complexes in Top cg, and since the domain and codomain
    of relative cell complexes are compact they appear at a finite stage in the sequence, and so
    the fibration and we have a lift occurs at a finite stage, and it persists to the colimit.
    So this is often the problem as we've seen a couple times, that the obstruction to the
    fibration for example being preserved is that the lift doesn't necessarily occur at a 
    finite stage, so we can't assume it exists overall.
    The second statement also uses the fact that we obtain the images of spheres at a finite
    stage in the colimit, and we have these equivalences for example, and that's the essential
    idea.
    """
    def construct(self):
        t = make_title("Proposition", 3.82)
        self.title(t)

        p1 = TextMobject(r"""
            In the projective model structures on cotowers in topological spaces, 
            $[\mathbb{N}^{\leq},(Top_{cg})_{Quillen}]_{proj}$ and 
            $[\mathbb{N}^{\leq},(Top_{cg}^{\ast /})_{Quillen}]_{proj}$, the following 
            holds:
            \begin{enumerate}
                \item The colimit functor preserves fibrations between sequences of relative 
                    cell complex inclusions
                \item Let $I$ be a finite category, let $D_\bullet(-):I\to 
                    [\mathbb{N}^{\leq},(Top_{cg})_{Quillen}]_{proj}$ be a finite diagram of 
                    sequences of relative cell complexes. Then there is a weak homotopy 
                    equivalence
                    $$\underset{\longrightarrow n}{\lim}\left(\underset{\longleftarrow i}{\lim}
                    D_n(i)\right)\overset{\in W_{cl}}{\longrightarrow}\underset{\longleftarrow i}
                    {\lim}\left( \underset{\longrightarrow n}{\lim}D_n(i)\right)$$
                    from the colimit over the limit sequences to the limit of the colimits 
                    of sequences.
            \end{enumerate}
        """, alignment="").scale(.75).to_edge(DOWN)

        self.cycle(
            [p1]
        )

        p2 = TextMobject(r"""
        \begin{align*}
            Hom\left( S^q,\underset{\longrightarrow n}{\lim}\left(\underset{\longleftarrow i}{\lim}
                D_n(i)\right)\right) \simeq &
                \underset{\longrightarrow n}{\lim}\left(\underset{\longleftarrow i}{\lim}
                Hom(S^q, D_n(i))\right) \\
                \overset{\sim}{\longrightarrow} & \underset{\longleftarrow i}{\lim}
                \left(\underset{\longrightarrow n}{\lim} Hom(S^q, D_n(i))\right) \\
                \simeq & Hom\left(S^q, \underset{\longleftarrow i}{\lim}\left( 
                \underset{\longrightarrow n}{\lim}D_n(i)\right)\right)
        \end{align*}
        """).scale(.75)

        self.cycle(
            [p2],
            out=False
        )
        self.clear()

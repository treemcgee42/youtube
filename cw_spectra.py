# Date: 2/28/21
# Purpose: cw-spectra section 1.1 nLab
# Notes:

from manimlib.imports import *
fn = "cw_spectra"


class def27(Scene):
    """
    So like we mentioned last time, the stable model structure we will be working 
    towards has the same cofibrations as the strict model structure on sequential spectra,
    and so its worthwhile examing cofibrancy properties in the strict structure. Just
    like CW complexes were cofibrant in the classical model structures, we start here with
    cell spectra and CW spectra. So a cell spectrum has component spaces that are cell complexes,
    and the structure maps need to be relative cell complex inclusions. A CW spectrum is a cell
    spectrum that has all component spaces CW complexes.
    """
    def construct(self):
        t = make_title("Definition", 2.7)
        self.title(t)

        d1 = TextMobject(r"""
            A sequential spectrum $X$ is called a
        """, " cell spectrum ", r"""
            if
            \begin{enumerate}
                \item all component spaces $X_n$ are cell complexes
                \item all structure maps $\sigma_n:S^1\wedge X_n\to X_{n+1}$ are relative 
                    cell complex inclusions.
            \end{enumerate}
            A
        """, " CW-spectrum ", r"""
            is a cell spectrum such that all component spaces $X_n$ are CW-complexes.
        """, alignment="").scale(.75)
        d1[1].set_color(BLUE)
        d1[-2].set_color(BLUE)

        self.cycle(
            [d1],
            out=False
        )
        self.clear()

class ex28(Scene):
    """
    An easy way to generate a whole class of these CW spectra is to just take a CW complex, 
    and then consider its suspension spectrum.
    """
    def construct(self):
        t = make_title("Example", 2.8)
        self.title(t)

        e1 = TextMobject(r"""
            The suspension spectrum $\Sigma^\infty X$ for $X\in Top_{cg}^{\ast /}$ a 
            CW-complex is a CW-spectrum.
        """, alignment="").scale(.75)

        self.cycle(
            [e1],
            out=False
        )
        self.clear()

class rmk29(Scene):
    """
    So let's think about what attaching a p cell to a cell spectrum means. So we attach this
    at some stage q, i.e. we attach it at the qth component space. By the nature of our structure
    maps and such, at the q+k stage this cell appears as its k fold suspension, i.e. because
    we suspended it it each time we moved up a component space. So that sounds like a p cell
    attachment is sort of attaching an entire spectrum to the original spectrum. This diagram
    makes it explicit. So everything here is a spectrum, to start with. Let's look at the left.
    The negative q is a functor we discussed earlier, it amounts to setting the first q-1 component
    spaces and structure maps to be trivial, so in a sense we are starting at the qth stage.
    So the inclusion sp-1 to dp pointed is obviously a cofibration, and we covered last time
    that the sigma infinity functor was a Quillen functor, hence in particular preserved cofibrations.
    So the vertical left map is a cofibration. Well, those are preserved under pushouts, so the
    middle vertical is a cofibration too. Then on the right side we can do the cofiber pushout
    of that middle vertical morphism. Intuitively, this kills the first q-1 stages, since
    we attached no cells there, on the qth stage it identifies the boundary of the cell to a point,
    yielding a p sphere, killing everything else, the next stage we have a p+1 sphere, etc.
    Hence the cofiber is this sphere spectrum.
    So in a sense, we started with a p-1 sphere spectrum, shifted q, and ended with a p sphere
    spectrum shifted q. 
    In the stable model structure, cell attachments to CW spectra are, after cofibers, integer
    shifts of the sphere spectrum, so we will have somethigng of this form.
    """
    def construct(self):
        t = make_title("Remark", 2.9)
        self.title(t)

        r1 = tikz("rmk29_r1", r"""
            \begin{tikzcd}
                \Sigma^\infty S^{p-1}_+[-q]
                    \arrow{r}\arrow{d}[left]{\Sigma^\infty(i_p)_+[-q]}
                    & X
                    \arrow{r}\arrow{d}
                    & \ast
                    \arrow{d} \\
                \Sigma^\infty D^p_+[-q]
                    \arrow{r}[above,yshift=1em]{(po)}
                    & \hat{X}
                    \arrow{r}[above,yshift=1em]{(po)}
                    & \Sigma^\infty S^p[-q]
            \end{tikzcd}
        """, fn)

        self.cycle(
            [r1]
        )

        r2 = TexMobject(r"""
            \Sigma^{p-q-1}\mathbb{S}
                \longrightarrow
            X
                \longrightarrow
            \hat{X}
                \longrightarrow
            \Sigma^{p-1}\mathbb{S}
        """).scale(.75)

        self.cycle(
            [r2],
            out=False
        )
        self.clear()

class lemma210(Scene):
    """
    Here's a technical lemma. For kappa a regular cardinal, X a kappa cell spectrum,
    i.e. then X is k small with respect to morphisms of spectra that are degreewise
    relative cell complex inclusions.
    The proof here seems to use a result from a later section. This result says that
    in particular maps out of a cell attachment is equivalently a map out of
    the component space in the lowest nontrivial degree. Since we are trying to prove
    smallness with respect to degreewise relative cell complex inclusions, this says
    it suffices to consider smallness of this lowest degree component space, which we
    already know is small. Hence all these cells on the level of spectra are small.
    The rest of the proof presents another result, but I'm not to sure about the argument,
    so I will revisit it if another section brings some insight into the proof,
    if you understand what is going on there please leave a comment as well.
    """
    def construct(self):
        t = make_title("Lemma", 2.10)
        self.title(t)

        l1 = TextMobject(r"""
            Let $\kappa$ be a regular cardinal and let $X$ be a $\kappa$-cell spectrum, hence 
            a cell spectrum obtained from at most $\kappa$ stable cell attachments. Then $X$ 
            is $\kappa$-small with respect to morphisms of spectra that are degreewise 
            relative cell complex inclusions.
        """, alignment="").scale(.75)

        self.cycle(
            [l1],
            out=False
        )
        self.clear()

class prop211(Scene):
    """
    This seemed to be incomplete, but at the moment all this proposition says on the nLab is
    that the class of CW spectra is closed under finite wedge sums (of spectra)
    """
    def construct(self):
        t = make_title("Proposition", 2.11)
        self.title(t)

        p1 = TextMobject(r"""
            The class of CW-spectra is closed under finite wedge sums.
        """, alignment="").scale(.75)

        self.cycle(
            [p1],
            out=False
        )
        self.clear()

class prop212(Scene):
    """
    So we now finally arrive at our cofibrancy condition. A sequential spectrum X is cofibrant
    precisely if X0 is cofibrant, and each structure map is a cofibration. In particular, cell
    spectra and CW spectra are cofibrant.
    So let's prove this. The initial object in SeqSpec is the spectrum constant on a point.
    So when is a map from this to another spectrum X a cofibration? Well, we defined this
    to be the case precisely if the morphism from the initial object in topcg to X0 is a classical
    cofibration, i.e. X0 is cofibrant, and also if this was a classical cofibration. So it
    really remains only to show the second point. Well, S1 smash a point is a point, so this is
    equivalently the condition that this map is a classical cofibration. But this is precisely
    the condition we just stated.
    """
    def construct(self):
        t = make_title("Proposition", 2.12)
        self.title(t)

        p1 = TextMobject(r"""
            A sequential spectrum $X\in SeqSpec(Top_{cg})$ is cofibrant in 
            $SeqSpec(Top_{cg})_{strict}$ precisely if
            \begin{enumerate}
                \item $X_0$ is cofibrant
                \item each structure map $\sigma_n:S^1\wedge X_n\to X_{n+1}$ is a cofibration
            \end{enumerate}
            In particular, cell spectra and specifically CW-spectra are cofibrant.
        """, alignment="").scale(.75)

        self.cycle(
            [p1]
        )

        p2 = TextMobject(r"""
            \begin{enumerate}
                \item the morphism $\ast\to X_0$ is a classical cofibration, hence if the 
                    object $X_0$ is a classical cofibrant object, hence a retract of a cell complex
                \item the morphisms
                    $$
                    \ast_{n+1}\underset{S^1\wedge\ast_n}{\sqcup}S^1\wedge X_n
                    \longrightarrow X_{n+1}
                    $$
                    are classical cofibration. But since $S^1\wedge\ast\simeq\ast
                    \overset{\simeq}{\to}\ast$ is an isomorphism in this case the pushout 
                    reduces to just its second summand, and so this is now equivalent to
                    $$S^1\wedge X_n\longrightarrow X_{n+1}.$$
            \end{enumerate}
        """, alignment="").scale(.75)

        self.cycle(
            [p2],
            out=False
        )
        self.clear()

class prop213(Scene):
    """
    Now lets check that the cylinder spectrum we defined a few videos back is
    indeed a cylinder object in the abstract sense. We do require that X is a CW
    spectrum, which may hint as to why our current strict model structure is not
    sufficient.
    So we need to show that it factors
    the codiagonal in a suitable way, i.e. that this map here is a cofibration.
    So by definition we need to check that this is a classical cofibration, hence a 
    retract of a relative cell complex. We can rewrite this as follows. Well by assumption
    X is a CW spectrum, so each Xn is a CW complex, so Xn smash I plus is a relative cell 
    complex in pointed Top. Well then the map above is a relative cell cell complex, since
    the thing we ended up with was a relative cell complex.
    """
    def construct(self):
        t = make_title("Proposition", 2.13)
        self.title(t)

        p1 = TextMobject(r"""
            For $X\in SeqSpec(Top)_{stable}$ a CW-spectrum then its standard cylinder spectrum 
            $X\wedge (I_+)$ satisfies the conditions on an abstract cylinder inclusion: the 
            inclusion
            $$ X\vee X\longrightarrow X\wedge (I_+)$$
            is a cofibration in $SeqSpec(Top)_{stable}$.
        """, alignment="").scale(.75)

        self.cycle(
            [p1]
        )

        p2 = TexMobject(r"""
            (X\vee X)_{n+1}
                \underset{S^1\wedge (X\vee X)_n}{\sqcup}
            S^1\wedge (X\wedge (I_+))_n
                \longrightarrow
            (X\wedge (I_+))_{n+1}
        """).scale(.75)

        p3 = TexMobject(r"""
            (X_{n+1}\wedge X_{n+1})
                \underset{(S^1\wedge X_n)\vee (S^1\wedge X_n)}{\sqcup}
            S^1\wedge X_n\wedge (I_+)
                \longrightarrow
            X_{n+1}\wedge (I_+)
        """).scale(.75)

        p_2_to_3 = VGroup(
            p2, p3
        ).arrange_submobjects(
            DOWN,
            buff=1
        )

        self.cycle(
            [p2, p3],
            out=False
        )
        self.clear()

class lemma214(Scene):
    """
    We'd like to now turn to CW approximation of sequential spectra. We begin by reviewing
    what that meant for topological spaces. So some defintiions first, given a continuous function
    f between topological spaces, it is n connected if on the level of homotopy groups it is
    an isomorphism in degree less than n, and an epimorphism in degree n.
    A weak homotopy equivalence is thus a quote on quote infinity connected map.
    So here's a lemma from which the full statement of CW approximation for topological
    spaces follows. We have a continuous function between topological spaces, then there
    exists a relative CW complex and an extension such that the extension is n connected.
    Iif f was k connected, then the relative CW complex can have cells only of dimension
    k+1 to n inclusive, and if A was already a CW complex, then f hat can be a subcomplex
    inclusion.
    """
    def construct(self):
        l1 = TextMobject(r"""
            A continuous function $f:X\to Y$ between topological spaces is an
        """, " $n$-connected map ", r"""
            if the induced morphism on homotopy groups $\pi_\bullet(f):\pi_\bullet
            (X,x)\to\pi_\bullet(Y,f(x))$ is
            \begin{enumerate}
                \item an isomorphism in degree $<n$
                \item an epimorphism in degree $n$
            \end{enumerate}
        """, alignment="").scale(.75)
        l1[1].set_color(BLUE)

        self.cycle(
            [l1]
        )

        t = make_title("Lemma", 2.14)
        self.title(t)

        l1 = TextMobject(r"""
            Let $f:A\to X$ be a continuous function between topological spaces. Then 
            there exists for each $n\in\mathbb{N}$ a relative CW-complex $\hat{f}:A
            \hookrightarrow\hat{Y}$ together with an extension $\phi:Y\to X$ such that
            \begin{itemize}
                \item $\phi$ is $n$-connected
                \item if $f$ is $k$-connected, then $\hat{f}$ may be chosen to have cells 
                    only of dimension $k+1\leq dim\leq n$
                \item if $A$ is a CW-complex, then $\hat{f}:A\to X$ may be chosen to be a 
                    subcomplex inclusion.
            \end{itemize}
        """, alignment="").scale(.65).to_title(t)

        l2 = tikz("lemma214_l2", r"""
            \begin{tikzcd}
                A
                    \arrow{r}[above]{f}\arrow{d}[left]{\hat{f}}
                    & X \\
                \hat{X}
                    \arrow{ur}[right,yshift=-.5em]{\phi}
            \end{tikzcd}
        """, fn).next_to(l1, direction=DOWN, buff=.25).shift(1*(RIGHT))

        self.cycle(
            [l1, l2],
            out=False,
            successive=False
        )
        self.clear()

class prop215(Scene):
    """
    The real punchline is this- for every continuous function out of a CW complex, there
    is a relative CW complex that factors f followed by a weak homotopy equivalence.
    The idea is that we iteratively apply the previous lemma to get a cocone of this form.
    So we first apply it to f to get X0 and phi 0, then apply iit to X0 to get X1 and
    phi1, etc. Each phin is n connected by the previous lemma, and also each fn is
    a relative CW complex. In the 0th case we just attach 0 cells, in the 1st case
    the previous lemma says we can take f1 to be a subcomplex inclusion, so we only
    need to attach 1 cells, so in short each fn adds cells exactly of dimension n.
    Ok, now let X hat be the colimit over this, and f hat from A to X the induced
    component map, i.e. since the colimit is itself a cocone over the sequence.
    So we have somehting like this. It remains to show that phi is a weak homotopy equivalence.
    Again we use that n spheres are compact, so there image appears at a finite stage i
    for Xi. If we need to, we can keep including into higher stages until we have its image in a
    finite stage i greater than n. Well commutativity says that mapping along phi
    is the same as mapping along the original phi i. By construction this is i greater than n
    connected, so an isomoprhism on the homotopy class and we are done.
    """
    def construct(self):
        t = make_title("Proposition", 2.15)
        self.title(t)

        p1 = TextMobject(r"""
            For every continuous function $f:A\to X$ out of a CW-complex $A$, there exists 
            a relative CW-complex $\hat{f}:A\to\hat{X}$ that factors $f$ followed by a weak 
            homotopy equivalence
        """, alignment="").scale(.75).shift(1*UP)

        p2 = tikz("prop215_p2", r"""
            \begin{tikzcd}
                A
                    \arrow{rr}[above]{f}\arrow{dr}[left,yshift=-.5em]{\hat{f}}
                    & & X \\
                & \hat{X}
                    \arrow{ur}[right,yshift=-.5em]{\phi\in W_{cl}}
            \end{tikzcd}
        """, fn).next_to(p1, direction=DOWN, buff=.5)

        self.cycle(
            [p1, p2],
            successive=False
        )

        p3 = tikz("prop215_p3", r"""
            \begin{tikzcd}
                A
                    \arrow{r}[above]{f_0}\arrow{dr}[left,yshift=-.5em]{f}
                    & X_0
                    \arrow{r}[above]{f_1}\arrow{d}[right]{\phi_0}
                    & X_1
                    \arrow{r}\arrow{dl}[right,yshift=-.5em]{\phi_1}
                    & \cdots \\
                & X
            \end{tikzcd}
        """, fn)

        self.cycle(
            [p3],
            out=False
        )

        p4 = tikz("prop215_p4", r"""
            \begin{tikzcd}
                A
                    \arrow{r}[above]{f_0}\arrow{dr}
                    & X_0
                    \arrow{r}[above]{f_1}\arrow{d}
                    & X_1
                    \arrow{r}\arrow{dl}
                    & \cdots \\
                & \hat{X} 
                    \arrow{d}[right]{\phi}
                    & & \\
                & X
            \end{tikzcd}
        """, fn).scale(1.5)

        self.fade_replace(
            p3, p4
        )
        self.clear()

class prop216(Scene):
    """
    Now lets upgrade to spectra. So for X any sequential spectrum there exists a 
    CW spectrum and a homomorphism which is a degreewise weak homotopy equivalence. This is
    equivalently a weak equivalence in the strict model structure.
    So we will prove by induction. Let X0 hat to X0 be a CW approximation of the degree 0
    component space. Now suppose we found it up to n such that all structure maps
    in degree less than n are respected. 
    Ok, now consider this composite. Well the left is assumed by induction to be a 
    relative CW complex, and topological CW approximation says we can factor this composite as
    a relative cell inclusion followed by a weak homotopy equiavlence.
    So we have constructed the n+1 component space and made it weak homotopy equivalent to
    Xn+1. We just need to show that structure maps are respected. But indeed, we have the
    following square.
    """
    def construct(self):
        t = make_title("Proposition", 2.16)
        self.title(t)

        p1 = TextMobject(r"""
            For $X$ any topological sequential spectrum, then there exists a CW-spectrum 
            $\hat{X}$ and a homomorphism
            $$ \phi:\hat{X}\overset{\in W_{strict}}{\longrightarrow} X $$
            which is degreewise a weak homotopy equivalence, hence a weak equivalence in the 
            strict model structure.
        """, alignment="").scale(.75)

        self.cycle(
            [p1]
        )

        p2 = TexMobject(r"""
            S^1\wedge\hat{X}_n
                \overset{S^1\wedge\phi_n}{\longrightarrow}
                S^1\wedge X_n
                \overset{\sigma_n}{\longrightarrow}
                X_{n+1}
        """).scale(.75)

        p3 = TexMobject(r"""
            S^1\wedge\hat{X}_n\hookrightarrow\hat{X}_{n+1}
            \overset{\phi_{n+1}}{\longrightarrow}X_{n+1}
        """).scale(.75)

        p_2_to_3 = VGroup(
            p2, p3
        ).arrange_submobjects(
            DOWN, buff=1
        )

        self.cycle(
            [p2, p3],
            out=False
        )

        p4 = tikz("prop216_p4", r"""
            \begin{tikzcd}
                S^1\wedge\hat{X}_n
                    \arrow{r}[above]{S^1\wedge\phi_n}\arrow{d}[left]{incl}
                    & S^1\wedge X_n
                    \arrow{d}[right]{\sigma_n} \\
                \hat{X}_{n+1}
                    \arrow{r}[below]{\phi_{n+1}}
                    & X_{n+1}
            \end{tikzcd}
        """, fn)

        self.fade_replace(
            p_2_to_3, p4
        )
        self.clear()

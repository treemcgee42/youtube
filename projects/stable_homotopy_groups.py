from manimlib.imports import *
fn = "stable_homotopy_groups"


"""
INTRODUCTION:
We've been of course building up to stable homotopy groups.
We've constructed spectra in such a way that we hope
to have its homotopy groups correspond to stable homotopy
groups, so analagous to how homotopy groups are fundamental
invariants in classical homotopy theory, the fundamental
invariants of stable homotopy theory are stable homotopy groups.
"""


class def111(Scene):
    """
    So let's define them. The stable homotopy groups of a sequential
    prespectrum X is given by the colimit of the homotopy groups of
    the component spaces. The way we've defined it makes sure we
    stay on the diagonal in a sense, which our intuition from
    the stable homotopy groups of spheres gives us.
    Of course, we need to specify what diagram this colimit is actually
    taken over, and it is just the one given by the sequential
    diagram, that you might expect. So this would lead us to at least
    intuitively believe that we would get the same colimit no matter
    if we used the sequential spectrum with the standard structure maps
    or the adjunct structure maps. This will be our next proposition.
    But first, let's consider where we actually start taking this colimit.
    So let's say we are trying to compute the qth stable homotopy
    group. We can define that if q is greater than 0, then we just start at
    0, or the beginning, of the sequential spectrum. However, if q is less
    than 0, then we start at the absolute value of q. This makes sense,
    because we can't have negative standard homotopy groups.
    But this gives us a neat property that you might at first glaze over:
    our stable homotopy groups are Z graded, whereas standard homotopy 
    groups are N graded.
    """
    def construct(self):
        title = make_title("Definition", 1.11)

        self.play(
            Write(title)
        )
        self.wait(2)

        thedef1 = TextMobject("The ", "stable homotopy groups", " of a sequential \
                prespectrum $X$ is given by the \\\\ colimit of homotopy groups of the \
                component spaces over the sequential \\\\ diagram:"\
                , alignment="").scale(.75)
        thedef1[1].set_color(BLUE)
        thedef2 = TexMobject("\\pi_\\bullet(X):=\\underset{\\to k}{\\lim}\\pi_{\\bullet+k}\
                (X_k)").scale(.75)
        thedef = VGroup(
            thedef1,
            thedef2
        ).arrange_submobjects(
            DOWN,
            buff=.5
        )

        self.play(
            ShowCreation(thedef)
        )
        self.wait(2)

        self.play(
            FadeOut(thedef1),
            Transform(thedef2,thedef2.copy().shift(3*UP))
        )

        stablespheres = ImageMobject("stable_homotopy_groups/stablespheres.png")\
            .scale(2).shift(1*DOWN)

        self.play(
            FadeIn(stablespheres)
        )
        self.wait(2)
        self.play(
            FadeOut(thedef2),
            FadeOut(stablespheres)
        )

        originalspectrum = tikz("originalspectrum", r"""
            \begin{tikzcd}
                \cdots\arrow{d} & X_{n-1}\arrow{d} & X_n\arrow{d} & X_{n+1}\arrow{d} 
                    & \cdots\arrow{d} \\
                \cdots\arrow{ur} & \Sigma X_{n-1}\arrow{ur}[rotate=30,xshift=1em]{} 
                    & \Sigma X_n\arrow{ur}[rotate=30,xshift=1em]{} 
                    & \Sigma X_{n+1}\arrow{ur} & \cdots
            \end{tikzcd}
        """, fn)

        self.play(
            FadeIn(originalspectrum)
        )
        self.wait(2)
        self.play(
            FadeOut(originalspectrum)
        )

        homotopyspectrum = tikz("homotopyspectrum", r"""
            \begin{tikzcd}
                \cdots\arrow{d} & \pi_{\bullet + (n-1)}(X_{n-1})\arrow{d} & 
                    \pi_{\bullet +n}(X_n)\arrow{d} & 
                    \pi_{\bullet+(n+1)}(X_{n+1})\arrow{d} & \cdots\arrow{d} \\
                \cdots\arrow{ur} & \pi_{\bullet+n}(\Sigma X_{n-1})
                    \arrow{ur}[rotate=30,xshift=1em]{} 
                    & \pi_{\bullet+(n+1)}(\Sigma X_n)
                    \arrow{ur}[rotate=30,xshift=1em]{} 
                    & \pi_{\bullet+(n+2)}(\Sigma X_{n+1})\arrow{ur} & \cdots
            \end{tikzcd}
        """, fn)

        comp_morphs = tikz("comp_morphs", r"""
            \begin{tikzcd}
                \pi_{q+k}(X_k)\simeq \left[S^{q+k},X_k\right]_{\ast}
                    \arrow{r}[above]{(S^1\wedge(-))} &
                    \left[S^{q+k+1},S^1\wedge X_k\right]_{\ast}
                    \arrow{r}[above]{\left[S^{q+k+1},\sigma_k\right]} &
                    \left[S^{q+k+q},X_{k+1}\right]_{\ast}\simeq
                    \pi_{q+k+1}(X_{k+1})
            \end{tikzcd}
        """, fn).to_edge(DOWN,buff=1).scale(.35)

        self.play(
            FadeIn(homotopyspectrum)
        )
        self.wait(2)
        self.play(
            FadeIn(comp_morphs)
        )
        self.wait(2)
        self.play(
            FadeOut(homotopyspectrum),
            FadeOut(comp_morphs)
        )

        adj_homotopyspectrum = tikz("adj_homotopyspectrum", r"""
            \begin{tikzcd}
                \cdots\arrow{dr} & \pi_{n-1}(X_{n-1})
                    \arrow{dr}[rotate=-30,xshift=-1em]{} & 
                    \pi_n(X_n)\arrow{dr}[rotate=-30,xshift=-1em]{} & 
                    \pi_{n+1}(X_{n+1})\arrow{dr} & \cdots \\
                \cdots\arrow{u} & \Omega \pi_{n-1}(X_{n-1})
                    \arrow{u} & \pi_n(\Omega X_n)\arrow{u} & 
                    \pi_{n+1}(\Omega X_{n+1})\arrow{u} & \cdots\arrow{u}
            \end{tikzcd}
        """, fn)

        adj_comp_morphs = tikz("adj_comp_morphs", r"""
            \begin{tikzcd}
                \pi_{q+k}(X_k)\arrow{r}[above]{\simeq} & \left[S^{q+k},X_k\right]_\ast
                    \arrow{r}[above]{\left[S^{q+k},\tilde{\sigma}_k\right]}
                    & \left[S^{q+k},\cat{Maps}(S^1,X_{k+1})_\ast\right]_\ast \simeq
                    \left[S^1\wedge S^{q+k},X_{k+1}\right]_\ast \simeq
                    \pi_{q+k+1}(X_{k+1})
            \end{tikzcd}
        """, fn).to_edge(DOWN,buff=1).scale(.35)

        self.play(
            FadeIn(adj_homotopyspectrum)
        )
        self.play(
            FadeIn(adj_comp_morphs)
        )
        self.wait(2)
        self.play(
            FadeOut(adj_homotopyspectrum), 
            FadeOut(adj_comp_morphs)
        )

        colimit_starts = TexMobject(r"""
            k = \begin{cases}
                0 & \text{if }q\geq 0 \\
                |q| & \text{if }q<0
            \end{cases}
        """).scale(.75)

        self.play(
            FadeIn(colimit_starts)
        )
        self.wait(2)

        ext_to_functor = TexMobject(r"""
            \pi_\bullet:\text{SeqSpec}(\text{Top}_{\text{cg}})\to
            \text{Ab}^\mathbb{Z}
        """).scale(.75)

        self.play(
            Transform(colimit_starts, ext_to_functor)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class prop112(Scene):
    """
    So as promised, let's see that the colimits over the standard and
    adjunct structure maps indeed agree. So here are how the two
    structure maps are defined on the level of homotopy groups.
    We then consider the following commutative diagram. This is
    given by the standars suspension looping smash hom adjunction.
    The horizontal maps are isomorphisms. We can then think about
    the identity in the top left. This is the identity map from S1 smash Xk
    to S1 smash Xk. If we move down to the bottom left, then we
    get a map from S1 smash Sq+k to X k+1. This is the first structure map.
    If we instead take the identity map to the left and then down to the
    bottom right, we get the adjunct structure map. It then follows that
    these are isomorphic by that bottom isomorphism.
    So I'll be the first to admit that this proof confused me a little.
    In particular, I'm not entirely sure what the alpha in the vertical maps
    is. I believe it is the function that sends the object X_k to the object
    S q+k, but I'm not entirely sure. If anyone has any insights into this
    proof, please leave it down in the comments.
    """
    def construct(self):
        title = make_title("Proposition", 1.12)

        self.play(
            Write(title)
        )
        self.wait(2)

        theprop = TextMobject("The two component morphisms agree.").scale(.75)\
            .next_to(title,direction=DOWN,buff=1).to_edge(LEFT,buff=.5)
        pftitle = TextMobject("Pf:").scale(.75)\
            .next_to(title,direction=DOWN,buff=1).to_edge(LEFT,buff=.5)

        self.play(
            FadeIn(theprop)
        )
        self.wait(2)
        self.play(
            ReplacementTransform(theprop,pftitle)
        )

        comp_morphs = tikz("comp_morphs_prop112", r"""
            \begin{tikzcd}
                \pi_{q+k}(X_k)\simeq \left[S^{q+k},X_k\right]_{\ast}
                    \arrow{r}[above]{(S^1\wedge(-))} &
                    \left[S^{q+k+1},S^1\wedge X_k\right]_{\ast}
                    \arrow{r}[above]{\left[S^{q+k+1},\sigma_k\right]} &
                    \left[S^{q+k+q},X_{k+1}\right]_{\ast}\simeq
                    \pi_{q+k+1}(X_{k+1})
            \end{tikzcd}
        """, fn).to_edge(DOWN,buff=1).scale(.35)

        adj_comp_morphs = tikz("adj_comp_morphs_prop112", r"""
            \begin{tikzcd}
                \pi_{q+k}(X_k)\arrow{r}[above]{\simeq} & \left[S^{q+k},X_k\right]_\ast
                    \arrow{r}[above]{\left[S^{q+k},\tilde{\sigma}_k\right]}
                    & \left[S^{q+k},\cat{Maps}(S^1,X_{k+1})_\ast\right]_\ast \simeq
                    \left[S^1\wedge S^{q+k},X_{k+1}\right]_\ast \simeq
                    \pi_{q+k+1}(X_{k+1})
            \end{tikzcd}
        """, fn).to_edge(DOWN,buff=.25).scale(.35)

        self.play(
            FadeIn(comp_morphs)
        )
        self.play(
            FadeIn(adj_comp_morphs)
        )
        self.wait(2)

        pfdiag1 = tikz("prop112pf", r"""
            \begin{tikzcd}
                \left[S^1\wedge X_k,S^1\wedge X_k\right]_\ast \arrow{r}[above]{\simeq}
                    \arrow{d}[right]{\left[S^1\wedge\alpha,\sigma_k\right]}
                    & \left[X_k,\cat{Maps}(S^1,S^1\wedge X_k)_\ast\right]_\ast
                    \arrow{d}[right]{\left[\alpha,\cat{Maps}(S^1,\sigma_k)_\ast\right]_\ast} \\
                \left[S^1\wedge S^{q+k},X_{k+1}\right]_\ast \arrow{r}[above]{\simeq} &
                    \left[S^{q+k},\cat{Maps}(S^1,X_{k+1})_\ast\right]_\ast
            \end{tikzcd}
        """, fn).shift(.5*UP)

        self.play(
            FadeIn(pfdiag1)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class ex113(Scene):
    """
    A really nice example to think about is the stable homotopy groups
    of a topological spaces suspension spectrum. In particular, we have this
    nice way of writing them, due to the fact that the component spaces are
    the nfold suspensions of the starting space.
    We can again apply this idea to the standard sphere spectrum. We have
    an even easier way of writing the colimit, as the kth component space is the
    standard k sphere. If we recall the Freundenthal suspension theorem, we
    in fact can do one better. The qth stable homotopy group of X under
    some assumptions, so not just for the sphere spectrum, is attained at stage
    q+2 in the colimit.
    """
    def construct(self):
        title = make_title("Example", 1.13)

        self.play(
            Write(title)
        )
        self.wait(2)

        ex1 = TextMobject(r"""
            Given $X\in\text{Top}_{\text{cg}}^{\ast /}$, the stable homotopy 
            groups of its suspension spectrum are given by
            \begin{align*}
                \pi_q^S(X):=& \pi_q(\Sigma^\infty X) \\
                =& \underset{\to k}{\lim}\pi_{q+k}(S^k\wedge X)\\
                    \simeq & \underset{\to k}{\lim}\pi_q(\Omega^k(\Sigma^k X)).
            \end{align*}
        """, alignment="").scale(.75).next_to(title,direction=DOWN,buff=1).to_edge(LEFT,buff=.5)

        self.play(
            FadeIn(ex1)
        )
        self.wait(2)
        self.play(
            FadeOut(ex1)
        )

        ex2 = TextMobject(r"""
            \begin{align*}
                \pi_q^S(S^0) :=& \pi_q(\mathbb{S}) \\
                =& \underset{\to k}{\lim}\pi_{q+k}(S^k)
            \end{align*}
        """).scale(.75)

        self.play(
            FadeIn(ex2)
        )
        self.wait(2)

        ex3 = TexMobject(r"""
            \pi_q^S(X)\simeq\pi_{q+(q+2)}(\Sigma^{q+2}X)
        """).scale(.75)

        self.play(
            ReplacementTransform(ex2, ex3)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class def114(Scene):
    """
    As a last quick definition, we say that there is a stable weak homotopy
    equivalence f between sequential spectra X and Y if it induces isomorphisms
    on all stable homotopy groups. So just extended the idea of a weak
    homotopy equivalence to this new setting.
    """
    def construct(self):
        title = make_title("Definition", 1.14)

        self.play(
            Write(title)
        )
        self.wait(2)

        thedef = TextMobject("A morphism $f:X\\to Y$ of sequential spectra is a ",\
                    "stable weak homotopy \\\\equivalence", " if $$\\pi_{\\bullet}(f)\
                    :\\pi_{\\bullet}(X)\\overset{\\simeq}{\\longrightarrow}\
                    \\pi_{\\bullet}(Y).$$", alignment="").scale(.75)
        thedef[1].set_color(BLUE)

        self.play(
            FadeIn(thedef)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )


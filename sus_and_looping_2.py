# Date: 2/28/21
# Purpose: suspension and looping section in strict model in nLab 1.1
# Notes:

from manimlib.imports import *
fn = "sus_and_looping_2"


class prop24(Scene):
    """
    With this model structure in hand, let's revisit suspensions and loopings in this
    context of sequential spectra. The first observation is that the sigma infinite and
    omega infity functors we showed wwere in adjunction present themselves as 
    Quillen adjunctions. So to see this it suffices to show for example that the right
    adjoint functor omega infity preserves fibrations and acyclic fibrations, but this is
    almost immediate from the definition of strict fibrations. Recall the omega infity
    functor picks out the first component space, and strict fibrations are component
    wise classical fibrations, so in particular between first component spaces.
    """
    def construct(self):
        t = make_title("Proposition", 2.4)
        self.title(t)

        p1 = TextMobject(r"""
            The $(\Sigma^\infty \dashv \Omega^\infty)$-adjunction is a Quillen adjunction
            $$
                SeqSpec(Top_{cg})_{strict}
                \underoverset
                {\underset{\Omega^{\infty}}{\longrightarrow}}
                {\overset{\Sigma^\infty}{\longleftarrow}}
                {\bot}
                (Top_{cg}^{\ast/})_{Quillen}
            $$
        """, alignment="").scale(.75).to_edge(LEFT)

        self.cycle(
            [p1],
            out=False
        )
        self.clear()

class prop25(Scene):
    """
    We also had these alternative suspension and alternative looping functors.
    We showed these formed an adjunction, and this proposition says that we can upgrade
    these to a Quillen adjunction. Well the right adjoint omega takes a space and sends
    it to the pointed mapping space from s1 to that space. This is a quillen functor from 
    our work in pointed top cg, and hence preserves fibrations and acyclic fibrations.
    Well, fibrations in SeqSpec are degree wise fibrations in pointed top cg, so we
    are done.
    """
    def construct(self):
        t = make_title("Proposition", 2.5)
        self.title(t)

        p1 = TextMobject(r"""
            The $(\Sigma\dashv \Omega)$-adjunction is a Quillen adjunction
            $$
            SeqSpec(Top_{cg})_{strict}
            \underoverset
            {\underset{\Omega}{\longrightarrow}}
            {\overset{\Sigma}{\longleftarrow}}
            {\bot}
            SeqSpec(Top_{cg})_{strict}
            $$
        """, alignment="").scale(.75).to_edge(LEFT)

        self.cycle(
            [p1],
            out=False
        )
        self.clear()

class cor26(Scene):
    """
    These two upgrade this previous square to the level of homotopy- the commuting square
    is not only of adjunction, but of quillen adjunctions.
    Philosophically, one of the ideas of stable homotopy theory is to force the suspension
    looping adjunction to exhibit an equivalence of categories. Hence, what we have now isn't
    really good enough. And this goes back to the drawbacks of this strict model structure-
    we aren't really capturing the stable phenomenon yet. When we do pass to the stable homotopy
    category, this bottom adjunction will become a quillen equivalence, and hence exhibit the
    property that we are after.
    The stable model structure ends up having the same cofibrations as the strict model structure,
    but more weak equivalences.
    """
    def construct(self):
        t = make_title("Corollary", 2.6)
        self.title(t)

        c1 = tikz("cor26_c1", r"""
            \begin{tikzcd}
                (Top_{cg}^{\ast /})_{Quillen}
                    \arrow[yshift=-.5em]{r}[below]{\Omega}[above]{\bot}
                    \arrow[xshift=-.5em]{d}[left]{\Sigma^\infty}[right]{\dashv}
                    & (Top_{cg}^{\ast /})_{Quillen}
                    \arrow[yshift=.5em]{l}[above]{\Sigma}
                    \arrow[xshift=-.5em]{d}[left]{\Sigma^\infty}[right]{\dashv} \\
                SeqSpec(Top_{cg})_{strict}
                    \arrow[yshift=-.5em]{r}[below]{\Omega}[above]{\bot}
                    \arrow[xshift=.5em]{u}[right]{\Omega^\infty}
                    & SeqSpec(Top_{cg})_{strict}
                    \arrow[yshift=.5em]{l}[above]{\Sigma}
                    \arrow[xshift=.5em]{u}[right]{\Omega^\infty}
            \end{tikzcd}
        """, fn).scale(1.5)

        self.cycle(
            [c1],
            out=False
        )
        self.clear()

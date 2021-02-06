# Date: 2/5/21
# Purpose: Omega-spectra section in nLab
# Notes: 1/2 part of the section, focused on motivating


from manimlib.imports import *


fn = "omega_spectra"


class ex115(Scene):
    """
    So we now arrive at a pretty important concept, that of
    Omega-spectra. Despite the reverence with which the nLab talks
    about them, I found it really difficult to see why these were so
    important. Hopefully I can do that to some extent here.
    In terms of motivations, I'd like to start with intrinsic motivations,
    as sort of an initial motivation for constructing these things.
    We first recall a peculiar result from last time. The stable homotopy
    groups of a sequential spectrum are Z graded, whereas regular homotopy
    groups are N graded.
    We then observe that a Z graded abelian group is equivalently a
    N sequence of N graded abelian groups, together with isomorphisms
    that correspond to "shifting down 1". So look at this example here.
    And maybe just suppose tha a i are just the natural numbers,
    so a0 is 0, a1 is 1, etc. Then shifting down by one is an isomorphism.
    In that scenario, a_{-1} is obviously not a natural number, but we
    recover the notion of a negative number with the isomorphism that
    says the second element of A1 is the first of A0, or that for the sequence A2
    whose elements are shifted down two, the first element of A1 is the
    same as the second element of A2. In other words, we want isomorphisms
    along the diagonals.
    So if we want to deconstruct and analyze the Z graded stable homotopy
    groups in this manner, we'd like the A_i to correspond to the standard
    pi_i. Like I've drawn here. In this case, shifting the sequence down or
    moving to the right corresponds to forming the loopspace.
    But remember, this only recovers the Z
    graded structre if the diagonals are isomorphisms.
    """
    def construct(self):
        title = make_title("Example", 1.15)

        self.play(
            Write(title)
        )
        self.wait(2)

        z_and_n_graded = TexMobject(r"""
            \begin{cases}
                \pi_n(X_{\text{Top}}) & n\in\mathbb{N} \\
                \pi_n^S(X_{\text{SeqSpec}}) & n\in\mathbb{Z}
            \end{cases}
        """).scale(.75)

        self.play(
            FadeIn(z_and_n_graded)
        )
        self.wait(2)
        self.play(
            FadeOut(z_and_n_graded)
        )

        seq_n_graded = TexMobject(r"""
            \begin{array}{cccc}
                \vdots & \vdots & \vdots & \\
                a_3 & a_2 & a_1 & \cdots \\
                a_2 & a_1 & a_0 & \cdots \\
                a_1 & a_0 & a_{-1} & \cdots \\
                \underset{A_0}{\underbrace{a_0}} & \underset{A_1}{\underbrace{a_{-1}}}
                    & \underset{A_2}{\underbrace{a_{-2}}} & \cdots
            \end{array}
        """).scale(.75)

        self.play(
            FadeIn(seq_n_graded)
        )
        self.wait(2)
        self.play(
            FadeOut(seq_n_graded)
        )

        stable_version = TexMobject(r"""
            \begin{array}{cccc}
                \vdots & \vdots & \vdots & \\
                \pi_0(X_3) & \pi_1(X_3) & \pi_2(X_3) & \cdots \\
                \pi_0(X_2) & \pi_1(X_2) & \pi_2(X_2) & \cdots \\
                \pi_0(X_1) & \pi_1(X_1) & \pi_2(X_1) & \cdots \\
                \underset{\pi_0}{\underbrace{\pi_0(X_0)}} & \underset{\pi_1}{\underbrace{\pi_{1}(X_0)}}
                    & \underset{\pi_2}{\underbrace{\pi_{2}(X_0)}} & \cdots
            \end{array}
        """).scale(.75)

        self.play(
            FadeIn(stable_version)
        )
        self.wait(2)

        loop_space_ex = TexMobject(r"""
            \pi_n(\Omega^k X)=\pi_{n+k}(X)
        """).scale(.75).next_to(stable_version, direction=DOWN, buff=1)

        self.play(
            FadeIn(loop_space_ex)
        )
        self.wait(2)

        loop_arrow = TexMobject(r"""
            \underset{\Omega}{\longrightarrow}
        """).scale(1.25).move_to(loop_space_ex).set_color(BLUE)

        self.play(
            ReplacementTransform(loop_space_ex, loop_arrow)
        )
        self.wait(2)

        stable_vgroup = VGroup(
            stable_version,
            loop_arrow
        )

        self.play(
            Transform(stable_vgroup, stable_vgroup.copy().to_edge(RIGHT, buff=1))
        )
        self.play(
            FadeIn(seq_n_graded.to_edge(LEFT, buff=1))
        )
        self.wait(2)
        self.play(
            FadeOut(seq_n_graded)
        )
        self.play(
            Transform(stable_vgroup, stable_vgroup.move_to((0,0,0)).shift(1*DOWN))
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class ex118(Scene):
    """
    This is the property that we are looking for, and we will call sequential
    spectra which hold this property Omega spectra. But rather than
    explicitly requiring it, we'd instead like to impose a restriction instrinsic
    to the definition of sequential spectra themselves. In particular,
    since the act of shifting down corresponded to forming loopspaces,
    we are led to consider restrictions on the adjunct structure maps,
    which map a component space to the loopspace of the next component space,
    i.e. these are precisely the maps which in our previous diagram
    go along the upwards diagonal.
    Recall
    the structure maps on the level of homotopy groups, and we see that
    the added requirement we'd like to impose is to make the adjunct
    structure maps weak homotopy equivalences.
    """
    def construct(self):
        title = make_title("Example", 1.18)

        self.play(
            Write(title)
        )
        self.wait(2)

        theex = TexMobject(r"""
            X\text{ is Omega-spectrum}\quad\Rightarrow\quad \pi_k(X)\simeq
            \begin{cases}
                \pi_{k+n}(X_n) & k+n\geq 0 \\
                \pi_k(X_0) & k\geq 0 \\
                \pi_0X_{|k|} & k<0
            \end{cases}.
        """).scale(.75)

        self.play(
            FadeIn(theex)
        )
        self.wait(2)

        adj_comp_morphs = ImageMobject("omega_spectra/adj_comp_morphs_prop112.png")\
            .to_edge(DOWN, buff=.5).scale(.35)

        self.play(
            FadeIn(adj_comp_morphs)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class def116(Scene):
    """
    So just to make this explicit, here's the definition for 
    Omega-spectra. Again, we require that the adjunct structure maps
    are weak homotopy equivalences.
    """
    def construct(self):
        title = make_title("Definition", 1.16)

        self.play(
            Write(title)
        )
        self.wait(2)

        thedef = TextMobject("An ", "Omega-spectrum", " is a sequential spectrum \
            $X$ of topological spaces such that the adjunct structure maps \
            $\\tilde{\\sigma}_n:X_n\\to\\Omega X_{n+1}$ are weak homotopy equivalences.",\
            alignment="")\
            .scale(.75).next_to(title, direction=DOWN, buff=1).to_edge(LEFT, buff=.5)
        thedef[1].set_color(BLUE)

        adj_spectra = ImageMobject("omega_spectra/2.png").shift(1*DOWN)

        self.play(
            FadeIn(thedef)
        )
        self.play(
            FadeIn(adj_spectra)
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class ex117(Scene):
    """
    One instance where these mysterious Omega-spectra pop up is
    in what is probably one of the most underrated theorems in 
    mathematics, the Brown representability theorem. I hope to get
    to this theorem eventually, but for now, it suffices to say that
    that an implication of this theorem is that every, again, every
    generalized Eilenberg-Steenrod axiomatized cohomology theory
    is represented by an Omega-spectrum. So even though we don't 
    really know yet what it means to be represented, we can sense a
    deep relationship between Omega-spectra and generalized cohomology
    theories.
    For one example, if we an ordinary cohomology with coefficients in some
    abelian group A, then the Omega spectrum that the Brown Representability
    Theorem spits out has component spaces that are Eilenberg-MacLane spaces.
    An example of this in non-ordinary cohomology, i.e. extraordinary
    cohomology, is with topological K theory. The Omega spectrum that the
    Brown Representability theorem spits out now is called the K-theory
    spectrum and is denoted KU.
    But as it stands, we only have that Omega-spectra are a special subclass
    of sequential spectra. What will will explore next time is a way
    of associating an Omega spectrum to another other sequential spectrum.
    We will ultimately Omega spectra to be ideal candidates for objects
    of the elusive stable model category.
    """
    def construct(self):
        title = make_title("Example", 1.17)

        self.play(
            Write(title)
        )
        self.wait(2)

        theex = TextMobject("The Brown representability theorem implies that \
            every generalized (Eilenberg-Steenrod) cohomology theory is represented \
            by an Omega-spectrum.", alignment="")\
            .scale(.75).next_to(title, direction=DOWN, buff=1).to_edge(LEFT, buff=.5)

        self.play(
            FadeIn(theex)
        )
        self.wait(2)

        ex1 = TextMobject("- For an ordinary cohomology with coefficients some abelian \
            group $A$, this representation is the \\textit{Eilenberg-Maclane spectra} \
            $HA$, whose $n$th component space is an Eilenberg-Maclane space\
            $$(HA)_n\simeq K(A,n).$$", alignment="")\
            .scale(.75).next_to(theex, direction=DOWN, buff=1)

        ex2 = TextMobject("- An example of an extra-ordinary cohomology theory is \
            topological K-theory $K^\\bullet(-)$. Its Omega-spectrum representative is the \
            K-theory spectrum KU.", alignment="")\
            .scale(.75).next_to(ex1, direction=DOWN, buff=.5)

        self.play(
            FadeIn(ex1)
        )
        self.wait(2)
        self.play(
            FadeIn(ex2)
        )
        self.wait(2)

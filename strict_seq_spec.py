# Date: 2/21/21
# Purpose: prelude section 2 seq spec nLab
# Notes:

from manimlib.imports import *
fn = "strict_seq_spec"


class def21(Scene):
    """
    Before we talk about the true stable model structure with which stable homotopy theory 
    is concerned with, its useful to have a strict model structure in our toolbelt. As 
    we alluded to earlier, we eventually find that the real objects of interests are
    Omega-spectra. But with this strict model structure in hand, we will be able to 
    construct the stable model strucutre. But we will get there soon.
    As far as candidates for the model structure on sequential prespectra, this is
    perhaps the most natural:
    set our weak equivalences to those sequential spectra homomorphisms which are
    weak equivalences on the component spaces, set our fibrations to those that are fibrations
    on the component spaces, and cofibrations the maps on the component spaces are retracts
    of relative cell complexes. We call these strict weak equivalences, strict fibrations, 
    and strict cofibrations respectively.
    So keep in mind the projective model structure on topologically enriched functors. We showed
    that sequential spectra are equivalent as categoreis to a category of topologically 
    enriched functors. So the strict weak equivalences and strict fibrations are defined as they
    are in the projective model structure. The only difference is in the cofibrations, which
    we will talk about later.
    """
    def construct(self):
        t = make_title("Definition", 2.1)
        self.title(t)

        d1 = TextMobject(r"""
            Say that a homomorphism $f_\bullet:X_\bullet \to Y_\bullet$ in the category 
            $SeqSpec(Top)$ is
            \begin{itemize}
                \item a \textbf{strict weak equivalence} if each component 
                    $f_n:X_n\to Y_n$ is a weak equivalence in $Top_{Quillen}$
                \item a \textbf{strict fibration} if each component 
                    $f_n:X_n\to Y_n$ is a (Serre) fibration in $Top_{Quillen}$
                \item a \textbf{strict cofibration} if the maps $f_0:X_0\to Y_0$ as well as 
                    for all $n\in\mathbb{N}$ the maps
                    $$
                    (f_{n+1},\sigma_n^Y):X_{n+1}\underset{S^1\wedge X_n}{\sqcup}
                    S^1\wedge Y_n\longrightarrow Y_{n+1}
                    $$
                    are cofibrations in $Top_{Quillen}$.
            \end{itemize}
        """, alignment="").scale(.75)

        self.cycle(
            [d1],
            out=False
        )
        self.clear()

class def22(Scene):
    """
    Just like we did with the category of topologically enriched functors more generally,
    we have the pointed generating cofibrations and acyclic generating cofibrations. So 
    then we define these to what will be generating cofibrations and acyclic cofibrations.
    Again, this is just from our work with topologically enriched functors, which you can
    see in the introduction to homotopy theory section of the nLab and which I will release
    a video on soon. So if any of this confuses you, I'd recommend going to review that.
    """
    def construct(self):
        t = make_title("Definition", 2.2)
        self.title(t)

        d1 = TexMobject(r"""
            I_{Top^{\ast /}}:=\{S^{n-1}_+\overset{(\iota_n)_+}{\longrightarrow}D^n_+\}_
            {n\in\mathbb{N}} \\
            J_{Top^{\ast /}}:=\{D^n\overset{(j_n)_+}{\longrightarrow}D^n\times I\}_
            {n\in\mathbb{N}}
        """).scale(.75)

        self.cycle(
            [d1],
            out=False
        )

        d2 = TexMobject(r"""
            I_{seq}^{strict}
                :=
                \left\{
                y(S^n) \cdot i_+
                \right\}_{{S^n \in StdSpheres,} \atop {i_+ \in I_{Top^{\ast/}}}}
                \ \ 
                \in [StdSpheres, Top^{\ast/}] \simeq SeqSpec(Top) \\
            J_{seq}^{strict}
                :=
                \left\{
                y(S^n) \cdot j_+
                \right\}_{{ S^n \in StdSpheres} \atop {j_+ \in J_{Top^{\ast/}}}}
                \ \ 
                \in [StdSpheres, Top^{\ast/}] \simeq SeqSpec(Top)
        """).scale(.75)

        self.fade_replace(
            d1, d2
        )
        self.clear()

class thm23(Scene):
    """
    So now let's actually talk about the strict model structure on topological sequential
    spectra. This is also called the level model structure. We claim that the classes we
    defined earlier exhibit a model structure. Furthermore, the generating cofibrations
    and acyclic cofibrations we defined previously exhibit this structure as a cofibrantly
    generated model category.
    So like I alluded to in the first definition, the weak equivalences and fiibrations 
    agree with the already established projective model structure on the category of 
    topologically enriched functors. So the only thing we need to show that the cofibrations
    as we defined are indeed cofibrations.
    Our goal is liftings, so let's get this commuting square of sequential spectra.
    So this is an N collection of commuting diagrams in Top cg, not just on the component
    spaces, but we also need the structure maps to be respected. So there needs to be an nlift
    and an n+1 lift that makes all these diagrams commute. Ok, let's proceed by induction. In
    the n=0 case. Well if you recall our definition for striction cofibrations, the map
    X0 to Y0 is a cofibration by assumption. Ok, now assume we have a lift in degree n.
    So it remains to show that the degree n+1 lifting makes those structure maps commute,
    which we can compact into the following single diagram. But this looks a lot like a cocone
    under a pushout product, so lets do that, and we see an n+1 lift from yn+1 to An+1 is
    equivalently a lift in this diagram. The left vertical map is what we defined in our 
    definition of strict cofibrations, i.e. it is a cofibration in the classical sense.
    So indeed, if the right vertical morphism had the right lifting property, then it would
    have to be a form of fibration for each n, which would imply a strict fibration on
    the level sequential spectra, and we are done.
    """
    def construct(self):
        t = make_title("Theorem", 2.3)
        self.title(t)

        t1 = TextMobject(r"""
            These classes of morphisms give the structure of a model category, 
            $SeqSpec(Top)_{strict}$, called the
        """, " strict model structure on topological sequential spectra ",\
        " or ", " level model structure", r"""
            . \vskip .5em
            Moreover, this is cofibrantly generated via $I^{strict}_{seq}$ and 
            $J^{strict}_{seq}$.
        """, alignment="").scale(.75)
        t1[1].set_color(BLUE)
        t1[3].set_color(BLUE)

        self.cycle(
            [t1]
        )

        t2 = tikz("thm23_t2", r"""
            \begin{tikzcd}
                X
                    \arrow{r}[above]{h}\arrow{d}[right]{f}
                    & A
                    \arrow{d} \\
                Y
                    \arrow{r}
                    & B
            \end{tikzcd}
        """, fn)

        self.cycle(
            [t2],
            out=False
        )
        
        t3 = tikz("thm23_t3", r"""
            \begin{tikzcd}
                X_n
                    \arrow{r}[above]{h_n}\arrow{d}[right]{f_n}
                    & A_n
                    \arrow{d} \\
                Y_n
                    \arrow{r}
                    & B_n
            \end{tikzcd}
        """, fn).shift(2*UP)

        t4 = tikz("thm23_t4", r"""
            $
            \begin{tikzcd}
                S^1\wedge X_n
                    \arrow{r}[above]{\sigma_n^X}\arrow{d}[right]{S^1\wedge f_n}
                    & X_{n+1}
                    \arrow{d}[right]{f_{n+1}}
                    & \\
                S^1\wedge Y_n
                    \arrow{r}[above]{\sigma_n^Y}\arrow{dr}
                    & Y_{n+1}
                    \arrow{dr}
                    & \\
                & S^1\wedge B_n
                    \arrow{r}[above]{\sigma_n^B}
                    & B_{n+1}
            \end{tikzcd}
            =
            \begin{tikzcd}
                S^1\wedge X_n
                    \arrow{r}[above]{\sigma_n^X}\arrow{dr}[left,yshift=-.5em]{S^1\wedge h_n}
                    & X_{n+1}
                    \arrow{dr}[right,yshift=.5em]{h_{n+1}} \\
                & S^1\wedge A_n
                    \arrow{d}\arrow{r}[above]{\sigma_n^A}
                    & A_{n+1}
                    \arrow{d} \\
                & S^1\wedge B_n
                    \arrow{r}[above]{\sigma_n} 
                    & B_{n+1}
            \end{tikzcd}
            $
        """, fn).scale(1.5).next_to(t3, direction=DOWN, buff=1)

        self.play(
            FadeOut(t2),
            *[FadeIn(mob) for mob in [t3, t4]]
        )
        self.wait(2)
        self.play(
            *[FadeOut(mob) for mob in [t3, t4]]
        )

        t5 = tikz("thm23_t5", r"""
            \begin{tikzcd}
                X_n
                    \arrow{r}[above]{h_n}\arrow{d}[right]{f_n}
                    & A_n
                    \arrow{d} \\
                Y_n
                    \arrow{r}\arrow{ur}[right,yshift=-.5em]{l_n}
                    & B_n
            \end{tikzcd}
        """, fn).shift(3*LEFT)

        t6 = tikz("thm23_t6", r"""
            \begin{tikzcd}
                S^1\wedge X_n
                    \arrow{r}[above]{\sigma_n^X}\arrow{d}[right]{S^1\wedge f_n}
                    & X_{n+1}
                    \arrow{d}[right]{f_{n+1}}\arrow[bend left=30]{ddr}
                    & \\
                S^1\wedge Y_n
                    \arrow{r}[above]{\sigma_n^Y}\arrow{dr}[left,yshift=-.5em]{S^1\wedge l_n}
                    & Y_{n+1}
                    \arrow{dr}[right,yshift=.5em]{l_{n+1}} 
                    & \\
                & S^1\wedge A_n
                    \arrow{r}[above]{\sigma_n^A}
                    & A_{n+1}
            \end{tikzcd}
        """, fn).scale(1.5).shift(3*RIGHT)

        self.cycle(
            [t5, t6]
        )

        t7 = tikz("thm23_t7", r"""
            \begin{tikzcd}[column sep = huge, row sep = huge]
                S^1\wedge Y_n \underset{S^1\wedge X_n}{\sqcup} X_{n+1}
                    \arrow{r}[above]{(\sigma_n^A\circ S^1\wedge l_n,h_{n+1})}
                        \arrow{d}[left]{f_n\Box\sigma_n^X}
                    & A_{n+1}
                    \arrow{d} \\
                Y_n
                    \arrow{r}\arrow{ur}[left,yshift=.5em]{l_{n+1}}
                    & B_{n+1}
            \end{tikzcd}
        """, fn).scale(1.5)

        self.cycle(
            [t7],
            out=False
        )
        self.clear()

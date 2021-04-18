# Date: 4/16
# Purpose: relationship between Kan extensions and adjunctions

from manimlib.imports import *
fn = "kan_adjunction"


class the_thm(Scene):
    """
    There is a strong connection between Kan extensions and adjunctions.
    This further demonstrates that Kan extensions are everywhere.
    Here's the idea. In particular, every adjunction is special type of
    Kan extension. What is perhaps more surprising is that there is a partial
    converse. I mean, we could only hope for a partial converse considering the
    generality of Kan extensions. But anyways, assume L and R are not a priori
    determined to be adjoint functors. If L is a right Kan extension of the
    identity on C along R, AND if R preserves it, then L and R form an 
    adjunction. To me, the second condition is the notable one. The way I
    see the condition that R preserves L is sort of encompassing the properties
    of the counit, something like doing R and then L is an identity.
    By the way, the preserving Kan extension property is implicit in the first
    case too. So we have an if and only if for the second statement at least.
    Also dually we can show the case for R, so if R is a left Kan extension
    preserved by L etc etc.
    """
    def construct(self):
        t = make_title("Theorem", "")
        self.title(t)

        the_adjunction = TextMobject(r"""
            For $C\to D$, let $L\dashv R$ be an adjunction, with unit \\
            $\eta:1_D\to R L$ and counit $\epsilon:L R\to 1_C$.
        """, alignment="").scale(.75).to_title(t)

        self.play(
            FadeIn(the_adjunction)
        )
        self.wait(2)

        bullet_1 = TextMobject(r"""
            \begin{itemize}
                \item Every adjunction is a Kan extension.
            \end{itemize}
        """).scale(.75)

        bullet_2 = TextMobject(r"""
            \begin{itemize}
                \item Conversely, if $(L, \epsilon)$ is a right Kan extension of 
                $1_C$ along $R$, and if $R$ preserves $L$, then $L\dashv R$ 
                with counit $\epsilon$. Dually for $R$.
            \end{itemize}
        """).scale(.75)

        bullets = VGroup(
            bullet_1,
            bullet_2
        ).arrange_submobjects(
            DOWN,
            buff=.5,
            aligned_edge=LEFT
        ).shift(.5*DOWN)

        self.cycle(
            [bullet_1, bullet_2],
            out=False
        )

        self.clear()

class forward_pf(Scene):
    """
    For before proving, let's just recall the traingle identites for an adjunction.
    These will give us the ability to collapse diagrams in our diagram chases.
    Ok, so let's prove the forward direction first. We need to show that L comma
    epsilon is a right Kan extension. It suffices to show that it is universal,
    as it certainly commutes appropriately. To that end, let H gamma be any other
    pair, i.e. any other extension of this form. But by the triangle identites
    this is equivalent to this diagram, right, because we can collapse the 
    left to triangles to the identity on R, so we're kind of multiplying by 1
    in a sense. But this already shows that gamma factors through epsilon. In
    particular its equal to epsilon followed by eta and gamma.
    All we need now is to show that this factorization is unique to conclude
    that L epsilon is indeed a right Kan extension.
    So ok, take any arbitrary factorization, and we want to show that this is the 
    same as the factorization from before. i.e, that this arbitrary factorization
    is just eta followed by gamma.
    Call this arbitrary factorization
    alpha, and it fits like this into the diagram.
    But this is just an equality, so lets add eta to the diagram. 
    If we do it to both sides, equality will be preserved.
    But now the right side by the triangle properties is just alpha,
    so we have successfully showed that alpha, this arbitrary factorization 
    through L epsilon, is just eta gamma as before, and we are done with
    uniqueness. This shows the forward direction.
    """
    def construct(self):
        t = make_title("$(\Rightarrow)$", "")
        self.title(t)

        triangle_identity_1 = tikz("triangle_identity_1", r"""
        $$
            \begin{tikzcd}
                C
                    \arrow{rr}[above]{1_C}[below,yshift=-.5em,color=red]{\Uparrow\epsilon}
                    \arrow{dr}[left,yshift=-.5em]{R}
                    & & C \arrow{dr}[right,yshift=.5em]{R}
                    & \\
                & D \arrow{rr}[below]{1_D}[above,yshift=.75em,color=red]{\Uparrow\eta} 
                    \arrow{ur}[right,yshift=-.5em]{L}
                    & & D
            \end{tikzcd}
            \quad = \quad
            \begin{tikzcd}
                C
                    \arrow{rr}[above]{1_C}[below,yshift=-1em,xshift=2em,color=red]{\Rightarrow 1_R}
                    \arrow{dr}[left,yshift=-.5em]{R}
                    & & C \arrow{dr}[right,yshift=.5em]{R}
                    & \\
                & D \arrow{rr}[below]{1_D}
                    & & D
            \end{tikzcd}
        $$
        """, fn).shift(1*UP)

        triangle_identity_2 = tikz("triangle_identity_2", r"""
        $$
            \begin{tikzcd}
                & C \arrow{rr}[above]{1_C} \arrow{dr}[right,yshift=.5em]{R}
                    & & C\\
                D \arrow{ur}[left,yshift=.5em]{L} 
                \arrow{rr}[below]{1_D}[above,yshift=1em,color=red]{\Uparrow\eta}
                    & 
                    & D \arrow{ur}[right,yshift=-.5em]{L}
                    [left,xshift=-1.25em,yshift=.5em,color=red]{\Uparrow\epsilon}
                    &
            \end{tikzcd}
            \quad = \quad
            \begin{tikzcd}
                & C \arrow{rr}[above]{1_C}
                    & & C\\
                D \arrow{ur}[left,yshift=.5em]{L} \arrow{rr}[below]{1_D}
                [above,yshift=1.25em,xshift=2em,color=red]{\Leftarrow 1_L}
                    & 
                    & D 
                    \arrow{ur}[right,yshift=-.5em]{L}
                    &
            \end{tikzcd}
        $$
        """, fn).next_to(triangle_identity_1, direction=DOWN)

        self.cycle(
            [triangle_identity_1, triangle_identity_2],
            successive=False
        )
        
        h_gamma_extension = tikz("h_gamma_extension", r"""
            \begin{tikzcd}
                C \arrow{rr}[above]{1_C}
                    [below,yshift=-.5em,color=red]{\Uparrow\gamma}
                    \arrow{dr}[left,yshift=-.5em]{R}
                    & & C \\
                & D \arrow{ur}[right,yshift=-.5em]{H} &
            \end{tikzcd}
        """, fn).shift(1*UP)

        h_gamma_aug = tikz("h_gamma_aug", r"""
            \begin{tikzcd}
                C
                    \arrow{rr}[above]{1_C}[below,yshift=-.5em,color=red]{\Uparrow\epsilon}
                    \arrow{dr}[left,yshift=-.5em]{R}
                    & & C \arrow{dr}[right,yshift=.5em]{R}
                    \arrow{rr}[above]{1_C}
                    [below,yshift=-.5em,color=red]{\Uparrow\gamma}
                    & & C \\
                & D \arrow{rr}[below]{1_D}[above,yshift=.75em,color=red]{\Uparrow\eta} 
                    \arrow{ur}[right,yshift=-.5em]{L}
                    & & D \arrow{ur}[right,yshift=-.5em]{H}
            \end{tikzcd}
        """, fn).next_to(h_gamma_extension, direction=DOWN)

        self.cycle(
            [h_gamma_extension, h_gamma_aug]
        )

        arbitary_factor_1 = tikz("arbitary_factor_1", r"""
        $$
            \begin{tikzcd}
                C \arrow{rr}[above]{1_C}
                    [below,yshift=-.5em,color=red]{\Uparrow\gamma}
                    \arrow{dr}[left,yshift=-.5em]{R}
                    & & C \\
                & D \arrow{ur}[right,yshift=-.5em]{H} &
            \end{tikzcd}
            \quad = \quad
            \begin{tikzcd}
                C \arrow{rr}[above]{1_C}
                    [below,yshift=-.5em,color=red]{\Uparrow\epsilon}
                    \arrow{dr}[left,yshift=-.5em]{R}
                    & & C \\
                & D \arrow{ur}[left,yshift=.5em]{L}
                [right,yshift=-.5em,xshift=-.25em,color=red]{\Leftarrow\alpha}
                \arrow[bend right=45]{ur}[left,yshift=.5em,xshift=1.75em]{H} &
            \end{tikzcd}
        $$
        """, fn).shift(1*UP)

        arbitary_factor_2 = tikz("arbitrary_factor_2", r"""
        $$
            \begin{tikzcd}
                & C \arrow{rr}[above]{1_C}
                    [below,yshift=-.5em,color=red]{\Uparrow\gamma}
                    \arrow{dr}[left,yshift=-.5em]{R}
                    & & C \\
                D \arrow{rr}[above,yshift=.5em,color=red]{\Uparrow\eta}
                [below]{1_D}
                    \arrow{ur}[left,yshift=.5em]{L}
                    & & D \arrow{ur}[right,yshift=-.5em]{H} &
            \end{tikzcd}
            \quad = \quad
            \begin{tikzcd}
                & C \arrow{rr}[above]{1_C}
                    [below,yshift=-.5em,color=red]{\Uparrow\epsilon}
                    \arrow{dr}[left,yshift=-.5em]{R}
                    & & C \\
                D \arrow{rr}[above,yshift=.5em,color=red]{\Uparrow\eta}
                [below]{1_D} \arrow{ur}[left,yshift=.5em]{L}
                & & D \arrow{ur}[left,yshift=.5em]{L}
                [right,yshift=-.5em,xshift=-.25em,color=red]{\Leftarrow\alpha}
                \arrow[bend right=45]{ur}[left,yshift=.5em,xshift=1.75em]{H} &
            \end{tikzcd}
        $$
        """, fn).next_to(arbitary_factor_1, direction=DOWN)

        self.cycle(
            [arbitary_factor_1, arbitary_factor_2],
            out=False
        )

        self.clear()

class reverse_pf(Scene):
    """
    Ok, now let's prove the reverse direction. So we are supposing that
    L epsilon is a right Kan extension of the identity along C along 
    another functor R. We are also assuming it is preserved by R.
    So let's take that last condition.
    Define eta as the unqiue (by assumption of right
    Kan extension) factorization in the following sense. So what just happened?
    Well, R preserves L as a right Kan extension, so there is a right Kan
    extension RL that is hidden here. Then 1D comma 1R is another pair that
    commutes, so by properties of the right Kan extension there must exist
    a unique map eta from 1D to L R. So that's what we are defining eta as.
    We will want to show of course that LR is is an adjunction with unit eta
    and co unit epsilon. To do that it suffices to show the triangle properties
    hold. But observe already that
    since the right map is the identity on D, this entire diagram is just
    this one on the right, with natural transformation the identity on R.
    This is first triangle property. So it remains to show the other one.

    But ok, take what we had, and take on an L map to both sides of the equality.
    With a little bit of rearranged, we get that this is equivalently this
    equality. Well, even though this is obvious, I want to point out that we
    can in fact fact a right kan extension through itself via the identity on L.
    I do this so that I can write our overall equality a bit more suggistively:

    And you can probably see where this is going, removing epsilon from both
    sides yields the other triangle identity and we are done.
    """
    def construct(self):
        t = make_title("$(\Leftarrow)$", "")
        self.title(t)

        def_of_eta = tikz("def_of_eta", r"""
        $$
            \begin{tikzcd}
                C \arrow{rr}[above]{1_C}
                [below,yshift=-.5em,color=red]{\Uparrow\epsilon}
                \arrow{dr}[left,yshift=-.5em]{R}
                    & & C
                    \arrow{rr}[above]{R}
                    & & D \\
                & D
                \arrow{ur}[left,yshift=.5em]{L} 
                \arrow[bend right=30]{urrr}[right,yshift=-.5em]{1_D}
                [left,xshift=-1em,yshift=1.5em,color=red]{\Uparrow\eta}
                & & &
            \end{tikzcd}
            \quad = \quad
            \begin{tikzcd}
                C \arrow{rr}[above]{R}
                [below,yshift=-.5em,color=red]{\Uparrow 1_R}
                \arrow{dr}[left,yshift=-.5em]{R}
                    & & D \\
                & D
                \arrow{ur}[right,yshift=-.5em]{1_D} 
                & & & &
            \end{tikzcd}
        $$
        """, fn).shift(1*RIGHT)

        self.cycle(def_of_eta, out=False)

        aug_eta = tikz("aug_eta", r"""
        $$
            \begin{tikzcd}
                C \arrow{rr}[above]{1_C}
                [below,yshift=-.5em,color=red]{\Uparrow\epsilon}
                \arrow{dr}[left,yshift=-.5em]{R}
                    & & C
                    \arrow{rr}[above]{R}
                    & & D \arrow{r}[above]{L} & C \\
                & D
                \arrow{ur}[left,yshift=.5em]{L} 
                \arrow[bend right=30]{urrr}[right,yshift=-.5em]{1_D}
                [left,xshift=-1em,yshift=1.5em,color=red]{\Uparrow\eta}
                & & &
            \end{tikzcd}
            \quad = \quad
            \begin{tikzcd}
                C \arrow{rr}[above]{R}
                [below,yshift=-.5em,color=red]{\Uparrow 1_R}
                \arrow{dr}[left,yshift=-.5em]{R}
                    & & D \arrow{r}[above]{L} & C \\
                & D
                \arrow{ur}[right,yshift=-.5em]{1_D} 
                & & & &
            \end{tikzcd}
        $$
        """, fn).shift(.75*RIGHT).shift(1*UP)

        self.fade_replace(def_of_eta, aug_eta)

        rearrange_aug_eta = tikz("rearrange_aug_eta", r"""
        $$
            \begin{tikzcd}
                C \arrow{rr}[above]{1_C}
                [below,yshift=-.5em,color=red]{\Uparrow\epsilon}
                \arrow{dr}[left,yshift=-.5em]{R}
                    & & C
                    \arrow{rr}[above]{1_C}
                    [below,yshift=-.5em,color=red]{\Uparrow\epsilon}
                    \arrow{dr}[left,yshift=-.5em]{R}
                    & & C \\
                & D \arrow{rr}[below]{1_D}
                [above,yshift=.5em,color=red]{\Uparrow\eta}
                \arrow{ur}[left,yshift=.5em]{L}
                    & & D
                    \arrow{ur}[left,yshift=.5em]{L}
                    &
            \end{tikzcd}
            \quad = \quad
            \begin{tikzcd}
                C \arrow{rr}[above]{1_C}
                [below,yshift=-.5em,color=red]{\Uparrow\epsilon}
                \arrow{dr}[left,yshift=-.5em]{R}
                    & & C \\
                & D \arrow{ur}[left,yshift=.5em]{L}
                    &
            \end{tikzcd}
        $$
        """, fn).next_to(aug_eta,direction=DOWN)

        self.cycle(rearrange_aug_eta, out=False)

        rearranged_copy = rearrange_aug_eta.copy().move_to(aug_eta)\
            .shift(1*LEFT)

        aug_factor = tikz("aug_factor", r"""
        $$
            =\quad
            \begin{tikzcd}
                C \arrow{rr}[above]{1_C}
                    [below,yshift=-.5em,color=red]{\Uparrow\epsilon}
                    \arrow{dr}[left,yshift=-.5em]{R}
                    & & C \\
                & D \arrow{ur}[left,yshift=.5em]{L}
                [right,yshift=-.5em,xshift=-.25em,color=red]{\Leftarrow 1_L}
                \arrow[bend right=45]{ur}[left,yshift=.5em,xshift=1.75em]{L} &
            \end{tikzcd}
        $$
        """, fn).next_to(rearranged_copy, direction=DOWN)

        self.play(
            FadeOut(aug_eta),
            FadeOut(rearrange_aug_eta),
            FadeIn(rearranged_copy),
            FadeIn(aug_factor)
        )
        self.wait(2)

        self.play(
            FadeOut(rearranged_copy),
            FadeOut(aug_factor)
        )

        new_equality = tikz("new_equality", r"""
        $$
            \begin{tikzcd}
                C \arrow{rr}[above]{1_C}
                [below,yshift=-.5em,color=red]{\Uparrow\epsilon}
                \arrow{dr}[left,yshift=-.5em]{R}
                    & & C
                    \arrow{rr}[above]{1_C}
                    [below,yshift=-.5em,color=red]{\Uparrow\epsilon}
                    \arrow{dr}[left,yshift=-.5em]{R}
                    & & C \\
                & D \arrow{rr}[below]{1_D}
                [above,yshift=.5em,color=red]{\Uparrow\eta}
                \arrow{ur}[left,yshift=.5em]{L}
                    & & D
                    \arrow{ur}[left,yshift=.5em]{L}
                    &
            \end{tikzcd}
            \quad = \quad
            \begin{tikzcd}
                C \arrow{rr}[above]{1_C}
                [below,yshift=-.5em,color=red]{\Uparrow\epsilon}
                \arrow{dr}[left,yshift=-.5em]{R}
                    & & C
                    \arrow{rr}[above]{1_C}
                    & & C \\
                & D \arrow{rr}[below]{1_D}
                [above,yshift=1em,xshift=1.5em,color=red]{\Leftarrow 1_L}
                \arrow{ur}[left,yshift=.5em]{L}
                    & & D
                    \arrow{ur}[left,yshift=.5em]{L}
                    &
            \end{tikzcd}
        $$
        """, fn).scale(.9).shift(1*UP)

        wo_epsilon = tikz("wo_epsilon", r"""
        $$
            \begin{tikzcd}
                & C
                    \arrow{rr}[above]{1_C}
                    [below,yshift=-.5em,color=red]{\Uparrow\epsilon}
                    \arrow{dr}[left,yshift=-.5em]{R}
                    & & C \\
                D \arrow{rr}[below]{1_D}
                [above,yshift=.5em,color=red]{\Uparrow\eta}
                \arrow{ur}[left,yshift=.5em]{L}
                    & & D
                    \arrow{ur}[left,yshift=.5em]{L}
                    &
            \end{tikzcd}
            \quad = \quad
            \begin{tikzcd}
                & C
                    \arrow{rr}[above]{1_C}
                    & & C \\
                D \arrow{rr}[below]{1_D}
                [above,yshift=1em,xshift=1.5em,color=red]{\Leftarrow 1_L}
                \arrow{ur}[left,yshift=.5em]{L}
                    & & D
                    \arrow{ur}[left,yshift=.5em]{L}
                    &
            \end{tikzcd}
        $$
        """, fn).next_to(new_equality,direction=DOWN)

        self.cycle(
            [new_equality, wo_epsilon],
            out=False
        )

        self.clear()

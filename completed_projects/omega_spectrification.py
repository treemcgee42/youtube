# Date: 2/10/21
# Purpose: second part of Omega-spectra section nLab
# Notes:


from manimlib.imports import *
fn = "omega_spectrification"


class prop120(Scene):
    """
    So last time we saw that Omega spectra are really the types of
    sequential spectra we'd like to study with regards to the stable
    phenomenon. But of course, not every sequential spectrum is an 
    Omega spectrum. But this proposition states that for any sequential
    spectrum X, we can construct a corresponding omega spectrum QX
    such that there is a stable weak homotopy equivalence between X and
    QX (which already justifies using it to study the stable phenomenon). 
    This map become an actual, strick, or level weak equivalence precisely
    if X was already an Omega-spectrum. Furthermore, two sequential spectra
    are stable weak homotopy equivalence precisely if their corresponding
    Omega spectra are level or strick weak equivalences.
    But now we need to actually construct QX, and after that we'll return 
    to this proposition and prove it.
    """
    def construct(self):
        title = make_title("Proposition", "1.20")

        self.play(
            Write(title)
        )
        self.wait(2)

        p1 = TextMobject(r"""
            Let $X\in\text{SeqSpec}(\text{Top}_\text{cg})$ be a sequential 
            prespectrum. There exists $j_X:X\to QX$ such that
            \begin{enumerate}
                \item $QX$ is an Omega-spectrum
                \item $\eta_X:X\to QX$ is a stable weak homotopy equivalence
                \item $\eta_X$ is a level weak equivalence previsely if $X$ is 
                    an Omega-spectrum
                \item a morphism $f:X\to Y$ is a stable weak homotopy equivalence
                     precisely if $Qf:QX\to QY$ is a level weak equivalence.
            \end{enumerate} 
        """, alignment="").scale(.65)

        self.cycle(
            [p1],
            out=False
        )
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class def119(Scene):
    """
    This process is called spectrification, because what we're gonna
    do is take our sequential spectrum and continuously break it into
    other spectra, and once we have this massive collection of spectra
    we're going to combine them.
    So we start with a sequential spectra, and we're going to want to
    consider them equipped with their adjunct structure maps, because
    an Omega spectrum is concerned with that.
    So let's consider just one piece of this. We recall that since
    the original component spaces are compactly generated topological
    spaces which has a model category structure on it, we can factor
    the original adjunct structure map as a projective morphism followed
    by an injective morphism. In particular, as a generating cofibration
    or an Itop relative cell complex, followed by an acyclic fibration,
    which is in particular a classical weak equivalence. This will be
    important in proving our earlier proposition.
    So this intermediary space is Z 1 comma k, and for notation we rewrite
    the original component spaces in this way.
    Well as you can imagine, we want to make a new spectra with component
    spaces these Z 1 comma k. If we apply the loop space functor to that
    top arrow, we can construct the bottom arrow to the loopspace of Z
    1 comma k. Then we define the new adjunct structure maps as the diagonal
    map followed by the bottom horizontal map. We can do this for all k, i.e.
    all the original component spaces to get a whole new spectrum with
    component spaces Z 1 comma k right next to the original one. But now we
    could just apply this same process to the new spectra! and so on and so 
    forth.
    Ultimately, we end up with some huge collection of spectra, and just to see
    what we've done I've drawn it like this, with the blue reprsenting the
    original spectrum. I think its pretty amazing.
    Ok, and now we want to package all of the relevant information from that
    into a single sequential spectra. So it is what you might expect, the component
    spaces for this new spectrum QX are the colimits over i of the Z i comma k, i.e.
    over each row in the diagrams from before. And the adjunct structure maps are also
    defined as the colimit.
    The only ambiguity is whether the colimit of the loop spaces of all these intermediary
    Z i comma k is the loop space of the colimit, but since each component space is
    compactly generated, stemming from our original definition of Omega spectra,
    and since S1 is compact, we do have cartesian closure, and so the internal hom
    here preserves colimits.
    """
    def construct(self):
        title = make_title("Definition", 1.19)

        self.play(
            Write(title)
        )
        self.wait(2)

        d1 = ImageMobject("omega_spectrification/2.png")

        self.cycle(
            [d1]
        )

        d2 = tikz("def119_d2", r"""
            \begin{tikzcd}
                \vdots \\
                X_k \arrow{d}[left]{\tilde{\sigma}_k} \\
                \Omega X_{k+1} & \\
                \vdots
            \end{tikzcd}
        """, fn).scale(2.5).shift(4*LEFT)

        self.cycle(
            [d2]
        )

        d3 = tikz("def119_d3", r"""
            \begin{tikzcd}
                \vdots \\
                X_k \arrow{d}[left]{\tilde{\sigma}_k} = Z_{0,k} 
                    \arrow{r}[above]{\in I_\text{Top}\text{Cell}} & 
                    Z_{1,k} \arrow{dl}[right,yshift=-.5em]{\in W_\text{cl}} \\
                \Omega X_{k+1} = \Omega Z_{0,k+1} \\
                \vdots
            \end{tikzcd}
        """, fn).scale(2.5).shift(3*LEFT)

        self.cycle(
            [d3]
        )

        d4 = tikz("def119_d4", r"""
            \begin{tikzcd}
                \vdots \\
                X_k \arrow{d}[left]{\tilde{\sigma}_k} = Z_{0,k} 
                    \arrow{r}[above]{\iota_{0,k}} & 
                    Z_{1,k} \arrow{dl}[right,yshift=-.5em]{\phi_{0,k}} 
                    \arrow{d}[right]{\tilde{\sigma}_{1,k}=\phi_{0,k}\circ\Omega(\iota_{0,k+1})}\\
                \Omega X_{k+1} = \Omega Z_{0,k+1} \arrow{r}[below]{\Omega(\iota_{0,k+1})}
                    & \Omega Z_{1,k+1} \\
                \vdots
            \end{tikzcd}
        """, fn).scale(2.5).shift(3*LEFT)

        self.cycle(
            [d4]
        )

        d5 = tikz("def119_d5", r"""
            \begin{tikzcd}
                \vdots & \vdots & \vdots & \vdots \\
                X_k = Z_{0,k} \arrow{d} \arrow{r} & Z_{1,k} \arrow{d} \arrow{r}
                    & Z_{2,k} \arrow{d} \arrow{r} & \cdots \\
                \Omega X_{k+1} = \Omega Z_{0,k+1} \arrow{r} & \Omega Z_{1,k+1}
                    \arrow{r} & \Omega Z_{2,k+1} \arrow{r} & \cdots \\
                \vdots & \vdots & \vdots & \vdots
            \end{tikzcd}
        """, fn).scale(2.5).shift(1*LEFT)

        self.cycle(
            [d5]
        )

        d6 = tikz("def119_d6", r"""
            \begin{tikzcd}[ampersand replacement=\&]
            \& \& \& \& \& \vdots \\
            \& \& X_{k+2}=Z_{0,k+2}\arrow[blue]{d}\arrow{rr} \& \& Z_{1,k+2}\arrow{rr}\arrow{dll}\arrow{d}\& \& \cdots\\
            \& \& \Omega X_{k+3}=Z_{0,k+3}\arrow{rr} \& \& \Omega Z_{1,k+3} \arrow{rr} \& \& \cdots\\
            \& X_{k+1}=Z_{0,k+1}\arrow{rr}\arrow[blue]{d} \& \& Z_{1,k+1}\arrow{rr}\arrow{d}\arrow{dll} \& \& Z_{2,k+1}\arrow{d}\arrow{dll}\arrow{r}\& \cdots \\
            \& \Omega X_{k+2}=\Omega Z_{0,k+2}\arrow{rr}\arrow[blue,dashed]{uuur} \& \& \Omega_{1,k+2}\arrow{rr} \& \& \Omega Z_{2,k+2}\arrow{r} \& \cdots\\
            X_k=Z_{0,k}\arrow[blue]{d}\arrow{rr} \& \& Z_{1,k}\arrow{dll}\arrow{rr}\arrow{d} \& \& Z_{2,k}\arrow{d}\arrow{rr}\arrow{dll} \& \& \cdots \\
        \Omega X_{k+1}=\Omega Z_{0,k+1}\arrow{rr}\arrow[blue,dashed]{uuur}  \& \& \Omega Z_{1,k+1}\arrow{rr}\& \& \Omega Z_{2,k+1}\arrow{rr} \& \& \cdots \\
        \& \vdots
        \end{tikzcd}
        """, fn).scale(3)

        self.cycle(
            [d6]
        )

        d7 = TextMobject(r"""
            $$ \eta_X:X\to QX $$
            \begin{itemize}
                \item component spaces:
                    $$ (QX)_k := \underset{\longrightarrow i}{\lim} Z_{i,k} $$
                \item (adjunct) structure maps:
                    $$ \tilde{\sigma}_k^{QX} := \underset{\longrightarrow i}{\lim}
                        \tilde{\sigma}_{i,k}: (QX)_k\longrightarrow\Omega(QX)_{k+1} $$
            \end{itemize}
        """).scale(.75).shift(1.5*LEFT)

        self.cycle(
            [d7]
        )

        d8 = TextMobject(r"""
            \begin{align*}
                \underset{\longrightarrow i}{\lim} \Omega Z_{i,k} =&
                    \underset{\longrightarrow i}{\lim} \text{Maps}(S^1, Z_{i,k})_\ast \\
                \simeq & \text{Maps}(S^1, \underset{\longrightarrow i}{\lim} Z_{i,k})_\ast \\
                =& \Omega \underset{\longrightarrow i}{\lim} Z_{i,k} \\
                \simeq & \Omega (QX)_k
            \end{align*}
        """).scale(.75)

        self.cycle(
            [d8],
            out=False
        )
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class prop120_pf_1(Scene):
    """
    So now to return and prove the proposition. One general observation we will
    be using is the following. By our factorization, as in particular a relative
    cell complex on those top maps, we see that the colimit is the transfinite
    composition of relative cell compelexes. We then recall that the compact image
    intersects a finite number of cells, and since in particular spheres are compact,
    the image of an element in any homotopy group is actually achieved completely at some
    finite stage.
    So for the first statement, we use this fact. the diagonal maps here
    in our factorization are weak classical equivalences, this is preserved when
    we pass to colimits. The only ambiguity our image of something in the homotopy group
    is actually achieved at a finite stage, which our previous remarks just confirmed.
    So a cycle up top is weakly equivalent to a cycle at the bottom when we pass
    to colimits, and thus the adjunct structure maps, which are the colimits of the
    dashed lines here, are weak homotopy equivalence and so QX is indeed an Omega
    spectrum.
    """
    def construct(self):
        title = make_title("Proposition", "1.20")

        self.play(
            Write(title)
        )
        self.wait(2)

        p1 = TextMobject(r"""
            \begin{itemize}
                \item $X_k\to(QX)_k$ is a relative cell complex
                \item $\pi_\bullet((QX)_k)$ is in the image of a finite stage 
                    $\pi_\bullet(Z_{i,k})$
            \end{itemize}
        """).scale(.75)

        self.cycle(
            [p1]
        )

        p2 = tikz("prop120_pf_1_p2", r"""
            \begin{tikzcd}
                & Z_{i,k} \arrow{dl}[above,yshift=.5em]{\simeq} \arrow{r} \arrow[dashed]{d}
                    & Z_{i+1, k} \arrow{dl}[above,yshift=.5em]{\simeq} \arrow{r} \arrow[dashed]{d}
                    & Z_{i+2, k} \arrow{dl}[above,yshift=.5em]{\simeq} \arrow{r} & \cdots \\
                \Omega Z_{i-1, k} \arrow{r} & \Omega Z_{i, k} \arrow{r} & \Omega Z_{i+1, k}
                    \arrow{r} & \cdots
            \end{tikzcd}
        """, fn).shift(.5*DOWN)

        p3 = TextMobject(r"""
            $QX$ is an Omega-spectrum.
        """).scale(.75).next_to(title, direction=DOWN, buff=1).to_edge(LEFT, buff=.5)

        self.cycle(
            [p3, p2]
        )

class prop120_pf_2(Scene):
    """
    Regarding the second statement, observe that this sort of backtracking
    maneuver in the spectrification. We move along the diagonals which are
    weak equivalences by construction in order to get an element that is
    related to an original component space.
    So to see that we have a stable weak equivalence. So on the left
    we have the definition of the qth stable homotopy group of a general
    sequential prespectrum, and on the right is how we saw stable homotopy
    groups in Omega spectra.
    We want to show that this map is an isomorphism, and we use the backtracking
    method. The idea is that the qth homotopy group of the k fold loopspace of
    Xk is the q plus kth homotopy group of Xk.
    """
    def construct(self):
        title = make_title("Proposition", "1.20")

        self.add(title)

        p1 = TextMobject(r"""
            $\eta_X:X\to QX$ is a stable weak homotopy equivalence.
        """).scale(.75).next_to(title, direction=DOWN, buff=1).to_edge(LEFT, buff=.5)

        self.cycle(
            [p1],
            out=False
        )

        p2 = tikz("prop120_pf_2_p2", r"""
            \begin{tikzcd}
                & & & Z_{k,0} \arrow{dl} \\
                & & \Omega Z_{k-1, 1} \arrow{dl} & \\
                & \cdots \arrow{dl} & & \\
                \Omega^k X_k = \Omega^k Z_{0, k}
            \end{tikzcd}
        """, fn).scale(2).shift(1*DOWN)

        self.cycle(
            [p2]
        )

        p3 = TexMobject(r"""
            \underset{\longrightarrow k\in\mathbb{N}}{\lim}\pi_{q+k}(X_k)
                \longrightarrow \pi_q((QX)_0)
        """).scale(.75).shift(1*UP)

        p4 = TextMobject(r"""
            \begin{align*}
                \pi_q((QX)_0) =& \pi_q(\underset{\longrightarrow k}{\lim} Z_{k,0}) \\
                \simeq & \underset{\longrightarrow k}{\lim} \pi_q(Z_{k,0}) \\
                \simeq & \underset{\longrightarrow k}{\lim} \pi_q(\Omega^k X_k)
            \end{align*}
        """).scale(.75).next_to(p3, direction=DOWN, buff=1)

        self.cycle(
            [p3, p4]
        )
        self.play(
            *[FadeOut(mob) for mob in self.mobjects[1:]]
        )

class prop120_pf_3(Scene):
    """
    For the third statment, let eta x again be the map from X to QX. First we will
    prove the reverse direction. Well, if X is an Omega spectrum, then these
    vertical maps are weak equivalences. Well, by the model structure on compactly
    generated topological spaces we know that classical weak equivalences are
    closed under two-out-of-three, so the top map is a classical weak equivalence
    as well. So again, a cycle in X passes through a sequence of ayclic maps
    and is achieved in a finite stage, so we have a weak equivalence.
    To see the other direction, consider the homomoprhism between X and QX.
    Then the top map is a weak equivalence by assumption, and we already showed
    that the right one is, which also implies the bottom one is. Then by commutativity
    the left one has to as well, which shows that X is an Omega spectrum.
    """
    def construct(self):
        title = make_title("Proposition", "1.20")
        
        self.add(title)

        p1 = TextMobject(r"""
            $\eta_X$ is a level weak equivalence precisely if $X$ is an Omega-spectrum.
        """).scale(.75).next_to(title, direction=DOWN, buff=1).to_edge(LEFT, buff=.5)

        self.cycle(
            [p1],
            out=False
        )

        p2 = tikz("prop120_pf_3_p2", r"""
            \begin{tikzcd}
                X_k \arrow{r} \arrow{d}[left]{\simeq} & Z_{1,k} \arrow{dl}[right,yshift=-.5em]{\simeq} \\
                \Omega X_{k+1}
            \end{tikzcd}
        """, fn)

        self.cycle(
            [p2]
        )

        p3 = tikz("prop120_pf_3_p3", r"""
            \begin{tikzcd}[column sep=huge, row sep=huge]
                X_n \arrow{r}[above]{(j_X)_n}[below]{\in W_{\text{cl}}}
                    \arrow{d}[left]{\tilde{\sigma}_n^X} & (QX)_n
                    \arrow{d}[left]{\in W_{\text{cl}}}[right]{\tilde{\sigma}_n^{QX}} \\
                \cat{Maps}(S^1, X_{n+1}) \arrow{r}[above]{\in W_{\text{cl}}}[below]
                    {\cat{Maps}(S^1,(j_X)_{n+1})} & \cat{Maps}(S^1, (QX)_{n+1})
            \end{tikzcd}
        """, fn).scale(1.5).shift(1*DOWN)

        self.cycle(
            [p3],
            out=False
        )
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

class rmk121(Scene):
    """
    The other statements follow analagously, so lets move to the final remark.
    So while we did all that work in finding resolutions to construct QX,
    it turns out that this is unnecessary in the case of CW complexes. The nLab
    contains references to this fact, which we don't prove here. But this is a
    very nice simpilification.
    """
    def construct(self):
        title = make_title("Remark", 1.21)
        
        self.play(
            Write(title)
        )
        self.wait(2)

        r1 = TextMobject("If $X$ is a $CW$-spectrum,")\
            .scale(.75).next_to(title, direction=DOWN, buff=1).to_edge(LEFT, buff=.5)
        
        r2 = TexMobject(r"""
            (Q_{\text{CW}}X)_n:=\underset{\longrightarrow k}{\lim}\Omega^k X_{n+k}
        """).scale(.75)

        r_1_and_2 = VGroup(
            r1, 
            r2
        )

        self.cycle(
            [r_1_and_2],
            out=False
        )
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

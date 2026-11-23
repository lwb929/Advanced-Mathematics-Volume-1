---
tags: [高数, 附录]
---

# 附录I 初等数学几个内容简介

## 附录Ⅰ

初等数学几个内容简介

## （一）三角函数公式

1. 两角和差公式

$$
\sin (\alpha + \beta) = \sin \alpha \cos \beta + \cos \alpha \sin \beta
$$

$$
\sin (\alpha - \beta) = \sin \alpha \cos \beta - \cos \alpha \sin \beta
$$

$$
\cos (\alpha + \beta) = \cos \alpha \cos \beta - \sin \alpha \sin \beta
$$

$$
\cos (\alpha - \beta) = \cos \alpha \cos \beta + \sin \alpha \sin \beta
$$

$$
\tan (\alpha + \beta) = \frac {\tan \alpha + \tan \beta}{1 - \tan \alpha \tan \beta}
$$

$$
\tan (\alpha - \beta) = \frac {\tan \alpha - \tan \beta}{1 + \tan \alpha \tan \beta}
$$

2. 和差化积公式

$$
\sin \alpha + \sin \beta = 2 \sin {\frac {\alpha + \beta}{2}} \cos {\frac {\alpha - \beta}{2}}
$$

$$
\sin \alpha - \sin \beta = 2 \cos {\frac {\alpha + \beta}{2}} \sin {\frac {\alpha - \beta}{2}}
$$

$$
\cos \alpha + \cos \beta = 2 \cos {\frac {\alpha + \beta}{2}} \cos {\frac {\alpha - \beta}{2}}
$$

$$
\cos \alpha - \cos \beta = - 2 \sin {\frac {\alpha + \beta}{2}} \sin {\frac {\alpha - \beta}{2}}
$$

3. 积化和差公式

$$
\sin \alpha \cos \beta = \frac {1}{2} [ \sin (\alpha + \beta) + \sin (\alpha - \beta) ]
$$

$$
\cos \alpha \sin \beta = \frac {1}{2} [ \sin (\alpha + \beta) - \sin (\alpha - \beta) ]
$$

$$
\cos \alpha \cos \beta = \frac {1}{2} [ \cos (\alpha + \beta) + \cos (\alpha - \beta) ]
$$

附录Ⅰ初等数学几个内容简介

$$
\sin \alpha \sin \beta = - \frac {1}{2} [ \cos (\alpha + \beta) - \cos (\alpha - \beta) ]
$$

4. 倍角公式

$$
\sin 2 \alpha = 2 \sin \alpha \cos \alpha = \frac {2 \tan \alpha}{1 + \tan^ {2} \alpha}
$$

$$
\cos 2 \alpha = \cos^ {2} \alpha - \sin^ {2} \alpha = 2 \cos^ {2} \alpha - 1 = 1 - 2 \sin^ {2} \alpha = \frac {1 - \tan^ {2} \alpha}{1 + \tan^ {2} \alpha}
$$

$$
\tan 2 \alpha = \frac {2 \tan \alpha}{1 - \tan^ {2} \alpha}
$$

5. 半角公式

$$
\sin \frac {\alpha}{2} = \pm \sqrt {\frac {1 - \cos \alpha}{2}}
$$

$$
\cos \frac {\alpha}{2} = \pm \sqrt {\frac {1 + \cos \alpha}{2}}
$$

$$
\tan \frac {\alpha}{2} = \frac {\sin \alpha}{1 + \cos \alpha} = \frac {1 - \cos \alpha}{\sin \alpha} = \pm \sqrt {\frac {1 - \cos \alpha}{1 + \cos \alpha}}
$$

（正、负号由$\frac{\alpha}{2}$所在的象限决定.）

（二）反三角函数

三角函数作为一种从它们各自的定义域到值域的映射，都不是单射。然而，如果对其定义域作某种限制，也可以使每一个三角函数都成为单射，从而就存在反函数，这样得到的反函数就是通常所说的反三角函数，它们的定义以及性质如下：

正弦函数 $y = \sin x, x \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ 的反函数称为反正弦函数，记作 $y = \arcsin x$，即 $x = \sin y$，这里 $x$ 是自变量，$y$ 是因变量。

因为 $\frac{1}{2} = \sin \frac{\pi}{6}$，所以 $\arcsin \frac{1}{2} = \frac{\pi}{6}$；类似地，有

$$
\frac {\sqrt {2}}{2} = \sin \frac {\pi}{4} \Rightarrow \arcsin \frac {\sqrt {2}}{2} = \frac {\pi}{4};
$$

$$
\frac {\sqrt {3}}{2} = \sin \frac {\pi}{3} \Rightarrow \arcsin \frac {\sqrt {3}}{2} = \frac {\pi}{3};
$$

$$
- 1 = \sin \left(- \frac {\pi}{2}\right) \Rightarrow \arcsin (- 1) = - \frac {\pi}{2},
$$

等等.反正弦函数 $y = \arcsin x$ 的定义域为 $[-1, 1]$，值域为 $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$，它在闭区间

[ -1, 1 ] 上是有界的、单调增加的，且为奇函数，函数的图形如图 1(a) 所示.

余弦函数 $y=\cos x, x \in [0, \pi]$ 的反函数称为反余弦函数，记作 $y=\arccos x$，即 $x=\cos y$。反余弦函数 $y=\arccos x$ 的定义域为 $[-1, 1]$，值域为 $[0, \pi]$，它在闭区间 $[-1, 1]$ 上是有界的、单调减少的，函数的图形如图 1(b) 所示.

正切函数 $y=\tan x, x \in \left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ 的反函数称为反正切函数，记作 $y=\arctan x$，即 $x=\tan y$。反正切函数 $y=\arctan x$ 的定义域为 $(-\infty, +\infty)$，值域为 $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$，它在 $(-\infty, +\infty)$ 内是有界的、单调增加的，且为奇函数，函数的图形如图 1(c) 所示.

余切函数 $y=\cot x = \frac{\cos x}{\sin x}, x \in (0, \pi)$ 的反函数称为反余切函数，记作 $y=\operatorname{arccot} x$，即 $x=\cot y$。反余切函数 $y=\operatorname{arccot} x$ 的定义域为 $(-\infty, +\infty)$，值域为 $(0, \pi)$，它在 $(-\infty, +\infty)$ 内是有界的、单调减少的，函数的图形如图 1(d) 所示.

图1

## （三）极坐标

在平面上取定一点 $O$，从点 $O$ 引一条射线 $OA$，再选定一个长度单位和角的正方向（通常取逆时针方向），这样，平面上任意一点 $M$ 的位置就可用两个数 $\rho$ 和 $\theta$ 来确定，确定的方法是（图 2）：$\rho = |OM|$，因此 $\rho \geqslant 0; \theta = \angle AOM, 0 \leqslant \theta < 2\pi$。这样规定的数 $\rho$ 和 $\theta$ 叫做点 $M$ 的极坐标，且以有序实数对 $(\rho, \theta)$ 表示，$\rho$ 称为点 $M$ 的极径，$\theta$ 称为点 $M$ 的极角，$O$ 称为极点，$OA$ 称

为极轴.这样建立的坐标系称为极坐标系.

当点 $M$ 在极点时,极径 $\rho=0$,极角 $\theta$ 可取任意值.在极坐标系中,除了极点 $O$ 以外,平面上任一点 $M$ 与有序实数对 $(\rho,\theta)$ 之间建立了一一对应关系.但在实际应用中,有时为了方便起见,在极坐标中,允许 $\rho$ 和 $\theta$ 可取一切实数.这时,设有两个任意实数 $\rho$ 和 $\theta$,先作射线 $OP$,使 $\angle AOP=\theta$,如果 $\rho>0$,在 $OP$ 上作一点 $M$,使 $|OM|=\rho$;如果 $\rho<0$,在 $P$ 向 $O$ 的延长线上,作一点 $M$,使 $|OM|=|\rho|$(图3).这样,对于任意一对实数 $\rho$ 和 $\theta$,总可以在平面上确定唯一的一点 $M$,$(\rho,\theta)$ 仍称为点 $M$ 的极坐标.由此可知,有序实数对 $(\rho,\theta)$ 与 $(\rho,\theta+2k\pi)$ 或 $(- \rho,\theta+(2k+1)\pi)$ 表示同一个点,这里 $k$ 取任意整数.

与直角坐标系一样,在极坐标系中,把曲线看作适合某种条件的点的集合,用曲线上的点的极坐标 $\rho,\theta$ 的关系式 $\varphi(\rho,\theta)=0$ 表示的方程,就是曲线的极坐标方程.

当极坐标系中的极点与直角坐标系中的原点重合,极轴与 $x$ 轴正半轴重合,两种坐标系的长度单位一致时(图4),极坐标与直角坐标可以互换.

由直角坐标到极坐标的变换公式为

$$
x=\rho\cos\theta,\quad y=\rho\sin\theta.
$$

由极坐标到直角坐标的变换公式为

$$
\rho^ {2} = x ^ {2} + y ^ {2}, \quad \tan \theta = \frac {y}{x} \quad (x \neq 0).
$$

下面给出常用曲线的极坐标方程：

图4

1. 圆心在极点，半径为 $r$ 的圆的方程为 $\rho = r$.

2. 圆心为 $(a,0)$，半径为 $a$ 的圆的方程为 $\rho = 2a\cos \theta$.

3. 圆心为 $\left(a, \frac{\pi}{2}\right)$，半径为 $a$ 的圆的方程为 $\rho = 2a\sin \theta$.

4. 过极点，倾角为 $\alpha$ 的直线方程为 $\theta = \alpha (\rho \in \mathbb{R})$.

5. 过点 $(a,0)$ 且垂直于极轴的直线方程为 $\rho \cos \theta = a$.

6. 过点 $\left(a, \frac{\pi}{2}\right)$ 且平行于极轴的直线方程为 $\rho \sin \theta = a$.

## （四）参数方程

在平面直角坐标系中，如果曲线上任意一点的坐标 $x, y$ 都是某个变量 $t$ 的函数

$\begin{cases} x = \varphi (t), \\ y = \psi (t), \end{cases}$ 并且对于 $t$ 的每一个允许的取值，由方程组确定的点 $(x, y)$ 都在这条曲线上，那么这个方程就叫做曲线的参数方程，变量 $t$ 叫做参数.

下面给出常用曲线的参数方程：

1. 以 $(a, b)$ 为圆心，$r$ 为半径的圆的参数方程为

$$
\begin{cases}
x = a + r \cos \theta, \\
y = b + r \sin \theta,
\end{cases}
$$

其中 $\theta$ 为参数.

2. 椭圆 $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ ($a > b > 0$) 的参数方程为

$$
\begin{cases}
x = a \cos \theta, \\
y = b \sin \theta.
\end{cases}
$$

3. 双曲线 $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$ ($a > b > 0$) 的参数方程为

$$
\begin{cases}
x = a \sec \theta, \\
y = b \tan \theta.
\end{cases}
$$

4. 抛物线 $y^2 = 2px$ 的参数方程为

$$
\begin{cases}
x = 2pt^2, \\
y = 2pt.
\end{cases}
$$

## （五）二阶和三阶行列式

给出二元线性方程组

$$
\begin{cases}
a_{11}x_1 + a_{12}x_2 = b_1, \\
a_{21}x_1 + a_{22}x_2 = b_2,
\end{cases}
$$

 (1)

求这方程组的解.

用大家熟知的消元法，分别消去方程组(1)中的 $x_2$ 及 $x_1$，得

$$
\begin{cases}
(a_{11}a_{22} - a_{12}a_{21})x_1 = b_1 a_{22} - a_{12} b_2, \\
(a_{11}a_{22} - a_{12}a_{21})x_2 = a_{11}b_2 - b_1 a_{21}.
\end{cases}
$$

 (2)

下面引入二阶行列式，然后利用二阶行列式来进一步讨论上述问题.

设已知四个数排成正方形表

$$
\begin{pmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{pmatrix},
$$

则数 $a_{11}a_{22} - a_{12}a_{21}$ 称为对应于这个表的二阶行列式，用记号

附录Ⅰ 初等数学几个内容简介

$$
\begin{vmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{vmatrix} \tag{3}
$$

表示，因此

$$
\begin{vmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{vmatrix} = a_{11}a_{22} - a_{12}a_{21}.
$$

数 $a_{11}, a_{12}, a_{21}, a_{22}$ 叫做行列式(3)的**元素**，横排叫做**行**，竖排叫做**列**。元素 $a_{ij}$ 中的第一个指标 i 和第二个指标 j 依次表示该元素所在的行数和列数。例如，元素 $a_{21}$ 在行列式(3)中位于第二行和第一列。

现在，方程组(2)可利用行列式来表示。设

$$
\begin{array}{l} D = \left| \begin{array}{c c} a _ {1 1} & a _ {1 2} \\ a _ {2 1} & a _ {2 2} \end{array} \right| = a _ {1 1} a _ {2 2} - a _ {1 2} a _ {2 1}, \\ D _ {1} = \left| \begin{array}{c c} b _ {1} & a _ {1 2} \\ b _ {2} & a _ {2 2} \end{array} \right| = b _ {1} a _ {2 2} - a _ {1 2} b _ {2}, \\ D _ {2} = \left| \begin{array}{c c} a _ {1 1} & b _ {1} \\ a _ {2 1} & b _ {2} \end{array} \right| = a _ {1 1} b _ {2} - b _ {1} a _ {2 1}, \end{array}
$$

则方程组(2)可写成

$$
\left\{ \begin{array}{l} D x _ {1} = D _ {1}, \\ D x _ {2} = D _ {2}. \end{array} \right. \tag{2'}
$$

我们注意到，D 就是方程组(1)中  $x_{1}$  及  $x_{2}$  的系数构成的行列式，因此称为系数行列式，而  $D_{1}$  和  $D_{2}$  分别是用方程组(1)右端的常数项代替 D 的第一列和第二列而形成的。

若 $D \neq 0$，则方程组(2)的解为

$$
x _ {1} = \frac {D _ {1}}{D}, \quad x _ {2} = \frac {D _ {2}}{D}. \tag{4}
$$

把(4)中 $x_{1}$ 及 $x_{2}$ 的值代入方程组(1)，便可证实 $x_{1}$ 及 $x_{2}$ 的这对值也是方程组(1)的解。另一方面，(2)是由(1)导出的，因此(1)的解一定是(2)的解。现在(2)只有一组解(4)，所以(4)是方程组(1)的唯一解。由此得出结论：

在 $D \neq 0$ 的条件下，方程组(1)有唯一的解

$$
x _ {1} = \frac {D _ {1}}{D}, \quad x _ {2} = \frac {D _ {2}}{D}.
$$

例1 解方程组

$$
\left\{ \begin{array}{l} 2 x + 3 y = 8, \\ x - 2 y = - 3. \end{array} \right.
$$

解 $D=\begin{vmatrix}2 & 3 \\ 1 & -2\end{vmatrix}=2\times(-2)-3 \times 1=-7$，

$D_{1}=\begin{vmatrix}8 & 3 \\ -3 & -2\end{vmatrix}=8 \times(-2)-3 \times(-3)=-7$，

$D_{2}=\begin{vmatrix}2 & 8 \\ 1 & -3\end{vmatrix}=2 \times(-3)-8 \times 1=-14$。

因 $D=-7 \neq 0$，故所给方程组有唯一解

$$
x=\frac{D_{1}}{D}=\frac{-7}{-7}=1, \quad y=\frac{D_{2}}{D}=\frac{-14}{-7}=2.
$$

下面介绍三阶行列式概念。

设已知9个数排成正方形表

$$
\begin{pmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{pmatrix},
$$

则数 $a_{11}a_{22}a_{33}+a_{12}a_{23}a_{31}+a_{13}a_{21}a_{32}-a_{13}a_{22}a_{31}-a_{12}a_{21}a_{33}-a_{11}a_{23}a_{32}$ 称为对应于这个表的三阶行列式，用记号

$$
\begin{array}{l}
\left| \begin{array}{ccc}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{array} \right| \\
= a_{11}a_{22}a_{33} + a_{12}a_{23}a_{31} + a_{13}a_{21}a_{32} - a_{13}a_{22}a_{31} - a_{12}a_{21}a_{33} - a_{11}a_{23}a_{32}.
\end{array} \tag{5}
$$

关于三阶行列式的元素、行、列等概念，与二阶行列式的相应概念类似，不再重复。

(5) 式右端相当复杂，我们可以借助图5得出它的计算法则（通常称为对角线法则）：

行列式中从左上角到右下角的直线称为**主对角线**，从右上角到左下角的直线称为**次对角线**。主对角线上元素的乘积以及位于主对角线的平行线上的元素与对角上的元素的乘积，前面都取正号。次对角线上元素的乘积以及位于次对角线

的平行线上的元素与对角上的元素的乘积，前面都取负号.

例2

$$
\begin{array}{l}
= 2 \times 3 \times 5 + 1 \times 1 \times 2 + 2 \times (-4) \times 3 - 2 \times 3 \times 2 - 1 \times (-4) \times 5 - 2 \times 1 \times 3 \\
= 30 + 2 - 24 - 12 + 20 - 6 = 10.
\end{array}
$$

利用交换律及结合律，可把（5）式改写如下：

$$
\left| \begin{array}{c c c} a _ {1 1} & a _ {1 2} & a _ {1 3} \\ a _ {2 1} & a _ {2 2} & a _ {2 3} \\ a _ {3 1} & a _ {3 2} & a _ {3 3} \end{array} \right| = a _ {1 1} (a _ {2 2} a _ {3 3} - a _ {2 3} a _ {3 2}) - a _ {1 2} (a _ {2 1} a _ {3 3} - a _ {2 3} a _ {3 1}) + a _ {1 3} (a _ {2 1} a _ {3 2} - a _ {2 2} a _ {3 1}).
$$

把上式右端三个括号中的式子表示为二阶行列式，则有

$$
\left| \begin{array}{c c c} a _ {1 1} & a _ {1 2} & a _ {1 3} \\ a _ {2 1} & a _ {2 2} & a _ {2 3} \\ a _ {3 1} & a _ {3 2} & a _ {3 3} \end{array} \right| = a _ {1 1} \left| \begin{array}{c c} a _ {2 2} & a _ {2 3} \\ a _ {3 2} & a _ {3 3} \end{array} \right| - a _ {1 2} \left| \begin{array}{c c} a _ {2 1} & a _ {2 3} \\ a _ {3 1} & a _ {3 3} \end{array} \right| + a _ {1 3} \left| \begin{array}{c c} a _ {2 1} & a _ {2 2} \\ a _ {3 1} & a _ {3 2} \end{array} \right|.
$$

上式称为三阶行列式按第一行的展开式.

例3 将例2中的行列式按第一行展开并计算它的值.

解

$$
\begin{array}{l} \left| \begin{array}{c c c} 2 & 1 & 2 \\ - 4 & 3 & 1 \\ 2 & 3 & 5 \end{array} \right| = 2 \left| \begin{array}{c c} 3 & 1 \\ 3 & 5 \end{array} \right| - \left| \begin{array}{c c} - 4 & 1 \\ 2 & 5 \end{array} \right| + 2 \left| \begin{array}{c c} - 4 & 3 \\ 2 & 3 \end{array} \right| \\ = 2 \times 1 2 - (- 2 2) + 2 \times (- 1 8) = 2 4 + 2 2 - 3 6 = 1 0. \\ \end{array}
$$

## 习题

1. 利用二阶行列式解下列方程组：

(1) 

$$
\left\{ \begin{array}{l} 5 x - y = 2, \\ 3 x + 2 y = 9; \end{array} \right.
$$

(2) 

$$
\left\{ \begin{array}{l} 3 x + 4 y = 2, \\ 2 x + 3 y = 7. \end{array} \right.
$$

2. 利用对角线法则，计算下列各行列式：

(1) 

$$
\left| \begin{array}{c c c} 2 & 0 & 1 \\ 1 & - 4 & - 1 \\ - 1 & 8 & 3 \end{array} \right|;
$$

(2) 

$$
\left| \begin{array}{c c c} 4 & - 2 & 4 \\ 1 0 & 2 & 1 2 \\ 1 & 2 & 2 \end{array} \right|;
$$

(3) 

$$
\left| \begin{array}{c c c} 3 & 4 & 2 \\ 7 & 5 & 1 \\ 3 & 2 & 4 \end{array} \right|;
$$

(4) 

$$
\left| \begin{array}{c c c} 1 & 1 + a & 1 \\ 1 & 1 & 1 + b \end{array} \right|.
$$

3. 将下列行列式按第一行展开并计算它们的值：

(1) 

$$
\begin{vmatrix}
1 & 2 & 3 \\
3 & 1 & 2 \\
2 & 3 & 1
\end{vmatrix};
$$

(2) 

$$
\begin{vmatrix}
-1 & 2 & 2 \\
2 & -1 & 2 \\
2 & 2 & -1
\end{vmatrix}.
$$

4. 证明下列等式：

(1) 

$$
\left| \begin{array}{l l l} a _ {1 1} & a _ {1 2} & a _ {1 3} \\ a _ {2 1} & a _ {2 2} & a _ {2 3} \\ a _ {3 1} & a _ {3 2} & a _ {3 3} \end{array} \right| = - a _ {2 1} \left| \begin{array}{l l} a _ {1 2} & a _ {1 3} \\ a _ {3 2} & a _ {3 3} \end{array} \right| + a _ {2 2} \left| \begin{array}{l l} a _ {1 1} & a _ {1 3} \\ a _ {3 1} & a _ {3 3} \end{array} \right| - a _ {2 3} \left| \begin{array}{l l} a _ {1 1} & a _ {1 2} \\ a _ {3 1} & a _ {3 2} \end{array} \right|;
$$

(2) 

$$
\left| \begin{array}{l l l} a _ {1 1} & a _ {1 2} & a _ {1 3} \\ a _ {2 1} & a _ {2 2} & a _ {2 3} \\ a _ {3 1} & a _ {3 2} & a _ {3 3} \end{array} \right| = a _ {3 1} \left| \begin{array}{l l} a _ {1 2} & a _ {1 3} \\ a _ {2 2} & a _ {2 3} \end{array} \right| - a _ {3 2} \left| \begin{array}{l l} a _ {1 1} & a _ {1 3} \\ a _ {2 1} & a _ {2 3} \end{array} \right| + a _ {3 3} \left| \begin{array}{l l} a _ {1 1} & a _ {1 2} \\ a _ {2 1} & a _ {2 2} \end{array} \right|.
$$

注：上面这两个等式分别称为三阶行列式按第二行和按第三行的展开式。

## 答案

1. (1) $x=1, y=3$; (2) $x=-22, y=17$.

2. (1) -4; (2) 8; (3) -48; (4) ab.

3. (1) 18; (2) 27.

4. 略.
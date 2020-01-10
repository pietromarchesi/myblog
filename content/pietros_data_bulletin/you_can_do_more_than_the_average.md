Title: You can do more than the average
Category: Pietro's Data Bulletin
Date: 2017-6-20
Slug: robust-graphical-methods
Summary: **TL;DR**: With little effort, you can get a lot more from your data than by just comparing means and plotting bar plots: a recent paper elaborates on graphical methods that could be an good addition to your data analysis toolbox.

**TL;DR**: With little effort, you can get a lot more from your data than by just comparing means and plotting bar plots: a recent paper elaborates on graphical methods that could be an good addition to your data analysis toolbox.
___

When analyzing data it is very common to focus on differences in mean between groups of interest, and to represent the results with bar plots. However, the mean is just one of several summary statistics to describe a distribution (and perhaps not always the best one), and bar plots conceal a lot of potentially interesting information.

While the classic t-test on the means might not be significant, you may find that your distributions of interest are actually extremely different, perhaps leading to new insights. Most importantly, you could get much more out of your data with relatively little effort. Doing something as simple as using dot plots, box plots, or violin plots for visualization may reveal interesting features.

A recent paper by Guillaume Rousselet and colleagues [[1](#ref)] reviews the benefits of robust graphical methods, clarifies the meaning of some commong statistical approaches (which might be obvious to some and a useful reminder to others) and present two useful tools to compare two distributions, namely the **shift function** and the **difference asymmetry function**. A particularly relevant recommendation is made in the conclusions, namely the splitting of a data set into a discovery and a testing sample: this is a safeguard against the inevitable increase in false positive rate that occurs when performing multiple similar tests on the same data. 

A last note: although using the standard error of the mean (SEM) for your error bars gives you shorter bars and thus seemingly stronger results (at least to the eyes of the naive observer), be reminded that actually SEM is often less straightforward to interpret (and thus less useful in the end) than a confidence interval of your estimate.

### References {#ref}

[1] Rousselet, Guillaume A., Cyril R. Pernet, and Rand R. Wilcox. "[Beyond differences in means: robust graphical methods to compare two groups in neuroscience.](https://www.biorxiv.org/content/early/2017/03/27/121079)" European Journal of Neuroscience (2017).

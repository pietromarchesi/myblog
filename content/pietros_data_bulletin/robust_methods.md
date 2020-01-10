Title: A note on robust statistical methods
Date: 2017-10-23
Category: Pietro's Data Bulletin
Slug: robust-statistical-methods
Authors: Pietro Marchesi
Summary: __TL;DR__: Conventional statistical methods like the t-test or the ANOVA F test can perform very poorly if the data does not meet the assumptions of normality and homoscedasticity. So-called robust statistical methods have been developed which perform well even when these assumptions are violated (and we should use them).

__TL;DR__: Conventional statistical methods like the t-test or the ANOVA F test can perform very poorly if the data does not meet the assumptions of normality and homoscedasticity. So-called robust statistical methods have been developed which perform well even when these assumptions are violated (and we should use them).
___

In neuroscience, common statistical methods to compare groups or test associations include the omnipresent t-test, the ANOVA F test, Pearson correlation, and least squares regression. And while most people are aware that these methods rely on certain assumptions, most prominently normality and homoscedasticity (equal variances), much less widespread is the awareness that __violating these assumptions can strongly impact the Type I error rate (the probability of a false positive) and statistical power__. 

In the last few decades, __a range of statistical techniques known as robust methods have been developed to deal with skewness, outliers, heteroscedasticity, and curvature__ in the regression line, which represent the main violations of the common assumptions.  In general, these methods will perform well if the distributions are well-behaved, and will continue to control Type I error rates and provide higher power as we depart from the standard assumptions. 

While that is certainly good news, robust methods are generally not part of the standard statistical training of a neuroscientist, and finding the right method for your problem can be a daunting task. We _could_ read the 608 pages [Introduction to Robust Estimation and Hypothesis Testing](https://www.elsevier.com/books/introduction-to-robust-estimation-and-hypothesis-testing/wilcox/978-0-12-386983-8) by Rand Wilcox (which, from the parts I have read, seems like a great read, by the way), but we won’t. And Wilcox knows that. So, earlier this year, he joined forces with Guillaume Rousselet to write an introduction to robust methods which can reasonably fit into our schedules: _‘A Guide to Robust Statistical Methods in Neuroscience’_ [[1](#ref)]. 

A good chunk of the guide is dedicated to showing how and why conventional methods fail when dealing with skewed distributions, outliers, heteroscedasticity, and curvature. A few simulations are provided which show how skewness can dramatically increase false positives and destroy power, and how this can be avoided by employing robust methods which test the _median_ or the _trimmed mean_. 

__While conventional statistics does provide you with ways to deal with violations of the classical assumptions, these strategies often turn out to be unsatisfactory__. Testing the assumptions is perhaps the most obvious, but it never comes with the guarantee that the test will have enough power to detect deviations that can have sizeable consequences. Other approaches like discarding outliers before comparing means or transforming data are also flawed, and even rank-based and permutation methods do not always perform well. 

While _no single methods dominates in all circumstances_, a few general guidelines are presented in the last section of the article. Notably, __always use a method which allows for heteroscedasticity, plot your data in an informative way (i.e. never a bar plot), and consider comparing multiple quantiles instead of only the central tendency__. 

To leave us no excuses to not adopt more robust methods, there is R code available for all functions. The functions written by Wilcox and described throughout his books are available on [his webpage](https://dornsife.usc.edu/labs/rwilcox/software/) as a [single text file](https://dornsife.usc.edu/assets/sites/239/docs/Rallfun-v34.txt) or on Github [here](https://github.com/nicebread/WRS). A subset of these functions, which contains a number of robust statistical methods (and has the advantage of being more thoroughly documented) is maintained by Patrick Mair and available as the CRAN package [WRS2](https://cran.r-project.org/web/packages/WRS2/index.html), and is described [here](https://dornsife.usc.edu/assets/sites/239/docs/WRS2.pdf). And if you’re thinking ‘wait, but this code is written in R, I don’t use R’, neither do I, I just installed [rpy2](http://rpy2.readthedocs.io/en/version_2.8.x/introduction.html) and I call the functions from Python, it's very easy to set up. 

### References {#ref}
[1] Wilcox, Rand R., and Guillaume A. Rousselet. "[A guide to robust statistical methods in neuroscience.](https://www.biorxiv.org/content/early/2017/06/20/151811)" bioRxiv (2017): 151811.



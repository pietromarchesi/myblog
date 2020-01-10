Title: (Effect) size matters
Date: 2017-09-4
Category: Pietro's Data Bulletin
Slug: effect-size
Authors: Pietro Marchesi
Summary: __TL;DR__: Looking at statistical significance alone can be misleading. There are a lot of good reasons to make use, on a regular basis, of measures of effect size together with their confidence intervals, as opposed to only looking at p-values. 

__TL;DR__: looking at statistical significance alone can be misleading. There are a lot of good reasons to make use, on a regular basis, of measures of effect size together with their confidence intervals, as opposed to only looking at p-values. 
___

Although null-hypothesis significance testing (i.e. p-values) continues to dominate statistical inference in (but not only) neuroscience, statisticians have been complaining about the widespread use of this methodology for quite some time, and __advocating a shift towards measures of effect size together with their confidence interval__. 

It turns out that the p-value dogma has statistical weaknesses, but, perhaps more prominently, it is also accompanied by many misconceptions regarding the use and meaning of p-values. __One of the most common misunderstandings is that a smaller p-value corresponds to a larger effect__. However, the p-value is influenced by a number of factors, including the statistical test used, the type of data, and the sample size, and even if these factors are kept constant, its relation to the effect size is markedly nonlinear. 

For example, it can easily be the case that, although the strength of the effect is so small as to be completely irrelevant, a minuscule p-value is found, simply due to a very large sample size. Measures of effect size, which estimate the magnitude of the observed effect, would in this case allow us to quantitatively verify that, although statistically significant, the difference that we observe is unlikely to be scientifically meaningful. __While looking at significance might be very useful, looking at significance alone might be misleading__.

A concise yet very insightful overview of this issue, with specific reference to neuroscience, is provided by Hentschke and Stuttgen in [[1](#ref)]. The paper first summarizes the shortcomings of standard null-hypothesis testing, and some common misconceptions related to its practice (one of which I described above). It then introduces the notion of effect size, and provides three examples of analysis of neuroscientific datasets in which measures of effect size come to the rescue, and avoid the misleading and meaningless conclusions that would be drawn based on p-values alone. Lastly, the authors introduce a well-documented [Matlab toolbox](https://github.com/hhentschke/measures-of-effect-size-toolbox) for calculating a variety of measures of effect size, together with analytical and bootstrap confidence intervals. If you are not familiar with measures of effect size, I would highly recommend taking a look at this article: these measures can have tremendous advantages, and with this toolbox they can be adopted with very little effort.  

### References {#ref}
[1] Hentschke, Harald, and Maik C. Stüttgen. "[Computation of measures of effect size for neuroscience data sets.](http://onlinelibrary.wiley.com/doi/10.1111/j.1460-9568.2011.07902.x/full)" European Journal of Neuroscience 34.12 (2011): 1887-1894.



Title: Don't let your analysis run in circles
Date: 2017-06-26
Category: Pietro's Data Bulletin
Slug: circular-analysis-in-neuroscience
Authors: Pietro Marchesi
Summary: __TL;DR__: If you use a certain criteria to first select a part of your data (e.g. a certain set of neurons) and then test another related measure on this subset, you might be heavily biasing your results. An easy way to prevent this is to use half of your data for selection, and the other half for testing.

__TL;DR__: If you use a certain criteria to first select a part of your data (e.g. a certain set of neurons) and then test another related measure on this subset, you might be heavily biasing your results. An easy way to prevent this is to use half of your data for selection, and the other half for testing.
___

Given the complexity and heterogeneity of neural responses, it is often challenging to extract a clear, easily communicable, and easily interpretable pattern from the intricacies of the data. A common strategy to aid our understanding is to restrict the analysis to a subset of neurons (for instance ones that show a certain response or selectivity), and characterize their response in detail. If done naively, however, this practice (also known as ‘double dipping’) is statistically flawed, and will lead to biased and spurious results. 

The problem arises because selection is never only based on the ‘true’ neural responses, but is always affected by noise: this creates unwanted dependencies which violate the assumption of random sampling. If the selection criterion is identical or related to the target statistic of the following analysis, the selection will distort the results in a way that makes them more consistent with the desired outcome (and thus scientifically and editorially more appealing). 

There are two main ways in which this can be avoided. The first way is to make sure that the selection criterion is orthogonal (i.e. independent) to the hypothesis tested in the following analysis (but this is not always easy to achieve nor is it always enough). The second (and the easiest) way is to split your data: for instance, use the odd trials to select a subset of your population, and the even trials to test your hypothesis (you can go a step further and use cross-validation).

This issue is presented in more detail, and with several examples in [[1](#ref)]. The extensive supplementary [‘A policy for noncircular analysis’](https://images.nature.com/full/nature-assets/neuro/journal/v12/n5/extref/nn.2303-S1.pdf) gives a detailed guideline on how to avoid double dipping in practice. 

### References {#ref}

[1] Kriegeskorte, Nikolaus, et al. "[Circular analysis in systems neuroscience: the dangers of double dipping.](http://www.nature.com/neuro/journal/v12/n5/abs/nn.2303.html)" Nature neuroscience 12.5 (2009): 535-540.

Title: When less (dimensions) is more
Date: 2017-07-5
Category: Pietro's Data Bulletin
Slug: dimensionality-reduction
Authors: Pietro Marchesi
Summary: __TL;DR__: Dimensionality reduction methods are an interesting tool to visualize, interrogate, and summarize your high-dimensional neural data.

__TL;DR__: Dimensionality reduction methods are an interesting tool to visualize, interrogate, and summarize your high-dimensional neural data.  
___

Extracting structure from high-dimensional data is notoriously very challenging. In a typical electrophysiological experiment, we often resort to averaging spike trains from multiple trials to yield a more interpretable view of the neural responses. Sometimes, however, trial-averaged responses can still be difficult to interpret, and the averaging procedure might obfuscate features of the response. How can we then summarize population activity within a single trial? And how can we gain insight from high-dimensional recordings? A range of techniques under the umbrella term of __dimensionality reduction methods__ can come to the rescue. 

In short, dimensionality reduction methods seek to find a __mapping from the high-dimensional data space to a lower dimensional space__ where the projected data can be visualized and explored. Patterns in the population response structure and other interesting features of the data, which remained hidden in high-dimensional neural space, can be revealed in low dimensional space, leading to new insights and allowing the formulation of new hypotheses. 

You have probably come across dimensionality reduction in the form of one of its simplest and most widely used members: principal component analysis (PCA). But there is much more to it: in [[1](#ref)], John Cunningham and Byron Yu review a wide range of these methods and their applications in neuroscience. 

P.S. While performing dimensionality reduction is a great way to summarize, explore, and visualize the data, there is more to it. The intrinsic dimensionality of population activity is in fact of great theoretical interest, where we would like to understand the dimensionality and structure of the neural manifolds, and how these relate to the cognitive processes [[2](#ref)].

### References {#ref}
[1] Cunningham, John P., and M. Yu Byron. "[Dimensionality reduction for large-scale neural recordings.](http://www.nature.com/neuro/journal/v17/n11/abs/nn.3776.html)" Nature neuroscience 17.11 (2014): 1500-1509.

[2] Gao, Peiran, and Surya Ganguli. "[On simplicity and complexity in the brave new world of large-scale neuroscience.](https://arxiv.org/abs/1503.08779)" Current opinion in neurobiology 32 (2015): 148-155.

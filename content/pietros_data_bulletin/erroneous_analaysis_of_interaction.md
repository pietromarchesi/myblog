Title: Is the difference between significant and not significant... significant?
Date: 2017-09-15
Category: Pietro's Data Bulletin
Slug: erroneous-interaction
Authors: Pietro Marchesi

Admittely, the question in the title might seem convoluted and perhaps even nonsensical at first, yet it exposes an important misconception in statistical analysis, which often goes unnoticed. 

Suppose you are interested in showing that a certain experimental effect is larger in a certain group or under certain conditions. You might be tempted to say something along the lines of “in condition A, we found a statistically significant increase in the effect of interest as compared to baseline (p&lt;0.05), whereas in condition B no statistically significant effect was found (p=0.4)”.
Since there’s a difference in the significance under condition A and under condition B, you would then conclude that the condition plays a role in modulating your effect. However, and here’s the catch, __the difference between significant and not significant need not be itself statistically significant__. That is, the fact that you found a significant effect in one condition and not in the other could be purely due to random fluctuations, and is thus not enough to conclude that the conditions are different with respect to the effect of interest. 

I won’t elaborate this issue further here, because the article by Nieuwenhuis and colleagues [[1](#ref)] (Dutch statisticians to the rescue) is very clear and very short, so I encourage you to take a look at it if you were not already aware of this pitfall. 

### References {#ref}
[1] Nieuwenhuis, Sander, Birte U. Forstmann, and Eric-Jan Wagenmakers. "Erroneous analyses of interactions in neuroscience: a problem of significance." Nature neuroscience 14.9 (2011): 1105-1107.

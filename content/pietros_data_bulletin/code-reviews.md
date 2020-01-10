Title: Show me your code and I’ll tell you who you are
Date: 2017-010-5
Category: Pietro's Data Bulletin
Slug: code-reviews
Authors: Pietro Marchesi
Summary: __TL;DR__: We should do code reviews in science. That's it. It's that simple. 

__TL;DR__: We should do code reviews in science. That's it. It's that simple.
___

_“My code is always one hundred percent correct, completely bug-free, it always does exactly what I say it does, and I know the code and the language so well that I know precisely what is going on at every line. __Trust me__.”_ 

I am sure none of you would be confident enough to say this sentence out loud to a colleague or use it as an introductory statement to your talk or paper (I most certainly wouldn’t be!). Yet this is effectively what we as scientists say when we publish a paper that uses homemade code to analyze data or perform a simulation and we don’t make the code and/or the data accessible. And that’s a lot of trust to ask for! 

In fact, we all know how easy it is to make mistakes when writing software. Some people learn it the hard way, like [this scientist](http://science.sciencemag.org/content/314/5807/1856.full?_ga=2.255010120.172139448.1507538586-895231392.1507538586) who had to retract three Science papers because two columns in his data were unintentionally flipped. Sharing code with your publication is definitely a step in the right direction, because it allows other scientists to check that your code does what you say it does, yet it is not ideal to find out about bugs in your analysis _after_ your paper is published. Strangely enough, while __it is common practice to have your manuscript reviewed by colleagues__, so that it can pushed to the highest attainable standard, __a lot of the content of that manuscript rests on code that no one other than the author has ever looked at. So why don’t we review code?__

Some may argue: “what if I wrote unit tests for all my code? Then I know for sure that it is doing what it should do”. For one, although good practice, unit testing will never cover the space of all possible bugs. Secondly, __computations can not only be wrong, but can often be misrepresented__ by the authors, so that their explanation may not exactly match what actually happens in the scripts. Making sure that two people understand code in the same way can help to prevent this.

Code review can also incentivize the production of __more readable code__ (which will also be easier to read for your future self), and foster __knowledge exchange__ between more experienced and less experienced coders on general practices, tips, and tricks. 

In the scientific community, there’s a __growing awareness of the importance of code reviews__, and a growing interest in developing effective strategies to carry it out in practice. You can take a look at this [blog post](https://uwescience.github.io/neuroinformatics/2017/10/08/code-review.html), or [this](https://software-carpentry.org/blog/2015/10/code-review-habit.html), or [this article](https://mozillascience.github.io/codeReview/intro.html), or [this arXiv paper](https://arxiv.org/pdf/1407.5648v2.pdf). Code review can happen asynchronously (where for example you would send the code of a soon-to-be-submitted publication to one or two colleagues and they will submit their review in their own time) but it can also become an opportunity for discussion within a larger group. Let's start reviewing!




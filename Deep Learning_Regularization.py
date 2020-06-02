
Important Assumptions to be considered:
1. Training and dev set belong to the same distribution
2. Human error, or the bayes error is 0. This value should be considered as the base error when looking at training error.

Let training set error = e
Let dev set error = E

Bias and Variance -

1. How to check if model has high bias or high variance?

Ans: When a model overfits training data, it has low bias/high variance. 
4 cases -
1. When e = 15% - Model has underfit - high bias.
	In this case, if the E = 30%, it also means high variance -> high bias/high variance
	If E is just 16%, then it is just  high bias model -> high bias

2. If e = 1%, means model has overfit the data, hence low bias/high variance
	if E = 11%, means the model has low bias, -> low bias 
	if E = 0.5%, means the model has low variance too -> low bias/lowe variance model 	
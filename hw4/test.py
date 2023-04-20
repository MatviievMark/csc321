import scipy.stats

# Parameters for the binomial distribution
n = 188
p = 0.68

# Calculate the cumulative probability of 131 successes (less than or equal to 131)
probability_less_than_or_equal_131 = scipy.stats.binom.cdf(131, n, p)

# Calculate the probability of more than 131 successes
probability_more_than_131 = 1 - probability_less_than_or_equal_131

print("The probability of more than 131 successes is:", probability_more_than_131)

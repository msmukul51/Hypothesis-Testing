#Example 2: An online medicine shop claims that the mean delivery time for medicines is less than 120 minutes with a standard deviation of 30 minutes.
# Is there enough evidence to support this claim at a 0.05 significance level if 49 orders were examined with a mean of 100 minutes?

#H0=120
#Ha<120
import math
from scipy import stats

def one_sample_z_test(sample_mean, population_mean, sample_std_dev, sample_size, alternative='less'):
    # Calculate the standard error
    std_error = sample_std_dev / math.sqrt(sample_size)

    # Calculate the z-score
    z_score = (sample_mean - population_mean) / std_error

    # Calculate the p-value
    if alternative == 'two-sided':
        p_value = 2 * (1 - stats.norm.cdf(abs(z_score)))
    elif alternative == 'greater':
        p_value = 1 - stats.norm.cdf(z_score)
    elif alternative == 'less':
        p_value = stats.norm.cdf(z_score)
    else:
        raise ValueError("Invalid alternative argument. Must be 'two-sided', 'greater', or 'less'.")

    return z_score, p_value



# Example usage
sample_mean = eval(input("Enter the sample Mean-:"))
population_mean = eval(input("Enter the population Mean-:"))
sample_std_dev = eval(input("Enter the sample std deviation-:"))
sample_size = eval(input("Enter the sample size-:"))
significance_value=eval(input("Enter the significance value-:"))
alternative = 'less'

z_score, p_value = one_sample_z_test(sample_mean, population_mean, sample_std_dev, sample_size, alternative)


print("Z-score:", z_score)
print("P-value:", p_value)



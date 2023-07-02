#HERE 1-5 THE EXAMPLE OF TWO TAILED ONE SAMPLE Z TEST BECAUSE = SIGN IS HERA

#Problem 1:A company claims that the average weight of their product is 10 ounces. You take a random sample of
#50 products and find that the average weight is 9.5 ounces with
#a standard deviation of 0.8 ounces. Test whether there is sufficient
#evidence to reject the company's claim at a significance level of 0.05.

#Problem 2:
#A university claims that the average IQ score of their students is 110.
#A random sample of 36 students is taken, and their average IQ score is found to be 108 with
#a standard deviation of 5.Test whether there is enough evidence to support the university's claim at a significance level of 0.01.

#Problem3
#A car manufacturer claims that their cars have an average fuel efficiency of 30 miles per gallon.
# You randomly select 25 cars and find that their average fuel efficiency is 28 miles per gallon with a standard deviation of 2 miles per gallon.
# Test whether there is sufficient evidence to reject the manufacturer's claim at a significance level of 0.05.

#Problem4
#A researcher claims that the average reaction time for a specific task is 3 seconds.
# A random sample of 20 participants is tested, and their average reaction time is found to be 2.8 seconds with a standard deviation of 0.4 seconds.
# Test whether there is enough evidence to support the researcher's claim at a significance level of 0.01.

#Problem5
#A coffee shop claims that their average serving temperature for coffee is 160 degrees Fahrenheit.
# You collect a random sample of 30 cups of coffee and find that the average serving temperature is 158 degrees Fahrenheit with a standard deviation of 2 degrees Fahrenheit.
# Test whether there is sufficient evidence to reject the coffee shop's claim at a significance level of 0.05.

#one tailed problems

#Problem 1:
#A company claims that the average waiting time for their customer service hotline is less than 5 minutes.
# A random sample of 40 callers is taken, and their average waiting time is found to be 4.6 minutes with a standard deviation of 0.7 minutes.
# Test whether there is enough evidence to support the company's claim at a significance level of 0.05 (left-tailed test).

#Problem 2:
#A school district claims that the average score of their students on a standardized test is higher than 85.
# A random sample of 50 students is taken, and their average score is found to be 87 with a standard deviation of 4.
# Test whether there is sufficient evidence to support the school district's claim at a significance level of 0.01 (right-tailed test).

#Problem 3:
#A pharmaceutical company claims that their new drug reduces cholesterol levels by more than 10%.
# You conduct a study with 30 participants and find that the average reduction in cholesterol levels is 12% with a standard deviation of 2%.
# Test whether there is enough evidence to support the pharmaceutical company's claim at a significance level of 0.05 (right-tailed test).

#Problem 4:
#A retailer claims that their online delivery service takes, on average, no more than 3 days to deliver products.
# A random sample of 25 deliveries is taken, and the average delivery time is found to be 2.8 days with a standard deviation of 0.6 days.
# Test whether there is sufficient evidence to support the retailer's claim at a significance level of 0.01 (left-tailed test).

#Problem 5:
#A fitness instructor claims that their exercise program results in an average weight loss of at least 5 pounds.
# A random sample of 20 participants is taken, and the average weight loss is found to be 4 pounds with a standard deviation of 1.2 pounds.
# Test whether there is enough evidence to support the fitness instructor's claim at a significance level of 0.05 (left-tailed test).

#These problems involve testing a claim about a population mean using a one-sample, one-tailed z-test.
# Depending on the direction of the claim, you will perform a left-tailed or right-tailed test.
# Remember to set up the null and alternative hypotheses accordingly and choose the appropriate critical value or calculate the p-value for making a decision.

import math as m
from scipy.stats import norm
import numpy as np
class Hypothesis_zest:
    def __int__(self,sample_size,population_mean,sample_mean,standard_deviation,significance_level):
        self.sample_size=sample_size
        self.population_mean=population_mean
        self.sample_mean=sample_mean
        self.standard_deviation=standard_deviation
        self.signifcance_level=significance_level

    def two_tailed_z_test(self,sample_size,population_mean,sample_mean,standard_deviation,significance_level):#call this function when there is "=" sign in null hypothesis
        z_score=(population_mean-sample_mean)/(standard_deviation/m.sqrt(sample_size))
        p_value=p_value = 2*(1 - norm.cdf(abs(z_score)))
        if p_value<significance_level:
            print("The P-Value is-:",p_value)
            print("Null hypothesis is rejected",p_value,"is Less than significance level-:",significance_level)
        else:
            print("Null hypothesis is accepted")

    def one_tailed_right_side(self,sample_size,population_mean,sample_mean,standard_deviation,significance_level):#call this function when there is ">" sign in null hypothesis
        z_score=(population_mean-sample_mean)/(standard_deviation/m.sqrt(sample_size))
        p_value=1-norm.cdf(z_score)
        if p_value<significance_level:
            print("The P-Value is-:",p_value)
            print("Null hypothesis is rejected",p_value,"is Less than significance level-:",significance_level)
        else:
            print("Null hypothesis is accepted")

    def one_tailed_left_side(self, sample_size, population_mean, sample_mean, standard_deviation,significance_level): # call this function when there is "<" sign in null hypothesis
        z_score = (population_mean - sample_mean) / (standard_deviation / m.sqrt(sample_size))
        p_value = norm.cdf(z_score)
        if p_value < significance_level:
            print("The P-Value is-:", p_value)
            print("Null hypothesis is rejected", p_value, "is Less than significance level-:",significance_level)
        else:
            print("Null hypothesis is accepted")


h=Hypothesis_zest()
problem1=h.two_tailed_z_test(50,9.5,10,0.8,0.05)
print(problem1)
problem2=h.two_tailed_z_test(36,108,110,5,0.01)
print(problem2)
problem3=h.two_tailed_z_test(25,28,30,2,0.05)
print(problem3)
problem4=h.two_tailed_z_test(20,2.8,3,0.4,0.01)
print(problem4)


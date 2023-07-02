import math as m
from scipy.stats import norm
import numpy as np
class Hypothesis_zest:
    def _int_(self,sample_size,population_mean,sample_mean,standard_deviation,significance_level):
        self.sample_size=sample_size
        self.population_mean=population_mean
        self.sample_mean=sample_mean
        self.standard_deviation=standard_deviation
        self.signifcance_level=significance_level

    def two_tailed_z_test(self,sample_size,population_mean,sample_mean,standard_deviation,significance_level):#call this function when there is "=" sign in null hypothesis
        z_score=(population_mean-sample_mean)/(standard_deviation/m.sqrt(sample_size))
        p_value=p_value = 2 * (1 - norm.cdf(abs(z_score)))
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
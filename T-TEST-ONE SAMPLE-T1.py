import math
from scipy import stats
import statistics as st
class T_test:


    def __int__(self,sample_mean,population_mean,stdv,sample_size,significance_level,degree_of_freedom):
        self.sample_mean=sample_mean
        self.population_mean=population_mean
        self.stdv=stdv
        self.sample_size=sample_size
        self.significance_level=significance_level
        self.degree_of_freedom=degree_of_freedom


    def one_sample_t_test_two_tailed(self,sample_mean,population_mean,stdv,sample_size,significance_level):
        t_score=(population_mean-sample_mean)/(stdv/(math.sqrt(sample_size)))
        degree_of_freedom=sample_size-1
        p_value=2*stats.t.sf(abs(t_score),degree_of_freedom)#we can also use here cdf function which is "1-sf"
        if p_value<significance_level:
            print("Null Hypothesis is rejected")
            print("Because",p_value,"Is less than",significance_level,)
        else:
            print("Null hypothesis is accepted")


    def one_sample_t_test_left_tailed(self,sample_mean,population_mean,stdv,sample_size,significance_level):
        t_score=(population_mean-sample_mean)/(stdv/(math.sqrt(sample_size)))
        degree_of_freedom=sample_size-1
        p_value=stats.t.cdf(t_score,degree_of_freedom)
        if p_value<significance_level:
            print("Null Hypothesis is rejected")
            print("Because",p_value,"Is less than",significance_level,)
        else:
            print("Null hypothesis is accepted")


    def one_sample_t_test_right_tailed(self,sample_mean,population_mean,stdv,sample_size,significance_level):
        t_score=(population_mean-sample_mean)/(stdv/(math.sqrt(sample_size)))
        degree_of_freedom=sample_size-1
        p_value=1-stats.t.cdf(t_score,degree_of_freedom)
        if p_value<significance_level:
            print("Null Hypothesis is rejected")
            print("Because",p_value,"Is less than",significance_level,)
        else:
            print("Null hypothesis is accepted")

t=T_test()
result=t.one_sample_t_test_two_tailed(25,21,3,25,0.05)
print(result)

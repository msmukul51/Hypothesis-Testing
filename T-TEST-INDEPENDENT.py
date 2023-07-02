import math as m
from scipy.stats import norm as nm
from scipy import stats as st
class Independence_T_test:
    def _int_(self,sample1_mean,sample2_mean,stdv1,stdv2,sample1_size,sample2_size,significance_level):
        self.sample1_mean=sample1_mean
        self.sample2_mean=sample2_mean
        self.stdv1=stdv1
        self.stdv2=stdv2
        self.sample1_size=sample1_size
        self.sample2_size=sample2_size
        self.significance_level=significance_level

    def two_tailed_two_sample(self,sample1_mean,sample2_mean,stdv1,stdv2,sample1_size,sample2_size,significance_level):#call this function when there is condition of "=" sign
        degree_of_freedom=((sample1_size+sample2_size)-2)
        t_score=(sample1_mean-sample2_mean)/(m.sqrt(((stdv1*2)/sample1_size)+((stdv2*2)/sample2_size)))
        p_value=2*(1-(st.t.cdf(t_score,degree_of_freedom)))
        if p_value<significance_level:
            print("Null hypothesis is rejected")
            print(p_value,"Is less than",significance_level)
        else:
            print("Null hypothesis is accepted")
            print(p_value,"Is Greater than",significance_level)

    def right_tail_two_sample(self,sample1_mean,sample2_mean,stdv1,stdv2,sample1_size,sample2_size,significance_level):#call this function when there is condition of ">" sign
        degree_of_freedom = ((sample1_size + sample2_size) - 2)
        t_score=(sample1_mean-sample2_mean)/(m.sqrt(((stdv1*2)/sample1_size)+((stdv2*2)/sample2_size)))
        p_value=1-st.t.cdf(t_score,degree_of_freedom)
        if p_value<significance_level:
            print("Null hypothesis is rejected")
            print(p_value,"Is less than",significance_level)
        else:
            print("Null hypothesis is accepted")
            print(p_value,"Is Greater than",significance_level)

    def left_tail_two_sample(self,sample1_mean,sample2_mean,stdv1,stdv2,sample1_size,sample2_size,significance_level):#call this function when there is condition of "<" sign
        degree_of_freedom = ((sample1_size + sample2_size) - 2)
        t_score=(sample1_mean-sample2_mean)/(m.sqrt(((stdv1*2)/sample1_size)+((stdv2*2)/sample2_size)))
        p_value=st.t.cdf(t_score,degree_of_freedom)
        if p_value<significance_level:
            print("Null hypothesis is rejected")
            print(p_value,"Is less than",significance_level)
        else:
            print("Null hypothesis is accepted")
            print(p_value,"Is Greater than",significance_level)

ts=Independence_T_test()
result1=ts.two_tailed_two_sample(5,4.8,1,0.8,35,35,0.05)
print(result1)
result2=ts.two_tailed_two_sample(85,80,10,8,30,35,0.01)
print(result2)
result3=ts.two_tailed_two_sample(0.6,0.5,0.1,0.09,48,45,0.05)
print(result3)
result4=ts.two_tailed_two_sample(5000,4800,500,600,50,60,.01)
print(result4)
result5=ts.two_tailed_two_sample(6,5.5,1.5,1.2,40,35,.01)
print(result5)
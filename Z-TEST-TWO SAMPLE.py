import math as m
from scipy.stats import norm as nm
class Two_sample_z_test:
    def _int_(self,sample1_mean,sample2_mean,stdv1,stdv2,sample1_size,sample2_size,significance_level):
        self.sample1_mean=sample1_mean
        self.sample2_mean=sample2_mean
        self.stdv1=stdv1
        self.stdv2=stdv2
        self.sample1_size=sample1_size
        self.sample2_size=sample2_size
        self.significance_level=significance_level

    def two_tailed_two_sample(self,sample1_mean,sample2_mean,stdv1,stdv2,sample1_size,sample2_size,significance_level):#call this function when there is condition of "=" sign
        z_score=(sample1_mean-sample2_mean)/(m.sqrt(((stdv1*2)/sample1_size)+((stdv2*2)/sample2_size)))
        p_value=2*(1-(nm.cdf(z_score)))
        if p_value<significance_level:
            print("Null hypothesis is rejected")
            print(p_value,"Is less than",significance_level)
        else:
            print("Null hypothesis is accepted")
            print(p_value,"Is Greater than",significance_level)

    def right_tail_two_sample(self,sample1_mean,sample2_mean,stdv1,stdv2,sample1_size,sample2_size,significance_level):#call this function when there is condition of ">" sign
        z_score=(sample1_mean-sample2_mean)/(m.sqrt(((stdv1*2)/sample1_size)+((stdv2*2)/sample2_size)))
        p_value=1-nm.cdf(z_score)
        if p_value<significance_level:
            print("Null hypothesis is rejected")
            print(p_value,"Is less than",significance_level)
        else:
            print("Null hypothesis is accepted")
            print(p_value,"Is Greater than",significance_level)

    def left_tail_two_sample(self,sample1_mean,sample2_mean,stdv1,stdv2,sample1_size,sample2_size,significance_level):#call this function when there is condition of "<" sign
        z_score=(sample1_mean-sample2_mean)/(m.sqrt(((stdv1*2)/sample1_size)+((stdv2*2)/sample2_size)))
        p_value=nm.cdf(z_score)
        if p_value<significance_level:
            print("Null hypothesis is rejected")
            print(p_value,"Is less than",significance_level)
        else:
            print("Null hypothesis is accepted")
            print(p_value,"Is Greater than",significance_level)

z=Two_sample_z_test()
result1=z.two_tailed_two_sample(5,4.8,1,0.8,35,35,0.05)
print(result1)
result2=z.two_tailed_two_sample(85,80,10,8,30,35,0.01)
print(result2)
result3=z.two_tailed_two_sample(0.6,0.5,0.1,0.09,48,45,0.05)
print(result3)
result4=z.two_tailed_two_sample(5000,4800,500,600,50,60,.01)
print(result4)
result5=z.two_tailed_two_sample(6,5.5,1.5,1.2,40,35,.01)
print(result5)

#1-10 two tailed two sample
#Problem 1:
#A company claims that there is no difference in the average response time between their two customer service teams.
# To test this claim, you randomly select two samples of customer service calls.
# Team A has an average response time of 5 minutes, with a standard deviation of 1 minute, while Team B has an average response time of 4.8 minutes,
# with a standard deviation of 0.8 minutes. Test whether there is enough evidence to support the claim of no difference in average response
# time at a significance level of 0.05 (two-tailed test).

#Problem 2:
#A school district wants to determine if there is a difference in average test scores between two schools, School A and School B.
# To test this, you randomly select two samples of students from each school and compare their average test scores. In School A, the average test score is 85,
# with a standard deviation of 10, while in School B, the average test score is 80, with a standard deviation of 8. Test whether there is sufficient evidence to
# support the claim of a difference in average test scores at a significance level of 0.01 (two-tailed test).

#Problem 3:
#A researcher investigates whether there is a difference in average reaction times between two groups, Group A and Group B.
# Participants from each group perform a reaction time task, and their average reaction times are recorded.
# In Group A, the average reaction time is 0.6 seconds, with a standard deviation of 0.1 seconds,
# while in Group B, the average reaction time is 0.5 seconds, with a standard deviation of 0.09 seconds.
# Test whether there is enough evidence to support the claim of a difference in average reaction times at a significance level of 0.05 (two-tailed test).

#Problem 4:
#A retailer wants to determine if there is a difference in average sales between two store locations, Store A and Store B.
# To test this, you randomly select two samples of sales data from each store and compare their average sales.
# In Store A, the average sales are $5,000, with a standard deviation of $500, while in Store B, the average sales are $4,800, with a standard deviation of $600.
# Test whether there is sufficient evidence to support the claim of a difference in average sales at a significance level of 0.01 (two-tailed test).

#Problem 5:
#A researcher investigates whether there is a difference in average cholesterol levels between two groups, Group A and Group B.
# Participants from each group have their cholesterol levels measured, and the average levels are recorded. In Group A, the average cholesterol level is 180 mg/dL,
# with a standard deviation of 20 mg/dL, while in Group B, the average cholesterol level is 175 mg/dL, with a standard deviation of 18 mg/dL.
# Test whether there is enough evidence to support the claim of a difference in average cholesterol levels at a significance level of 0.05 (two-tailed test).

#Problem 6:
#A company claims that the average response time for their customer service hotline is the same for both weekdays and weekends.
# To test this claim, you randomly select two samples of callers. Group A consists of 40 callers from weekdays, and Group B consists of 35 callers from weekends.
# The average response time for Group A is 6 minutes, with a standard deviation of 1.5 minutes, while the average response time for Group B is 5.5 minutes,
# with a standard deviation of 1.2 minutes. Test whether there is enough evidence to support the claim that the average response
# time is the same for weekdays and weekends at a significance level of 0.05 (two-tailed test).

#Problem 7:
#A company claims that there is no difference in the average satisfaction ratings between their two products, A and B.
# To test this claim, you randomly select two samples of customers.
# Group A consists of 50 customers who purchased product A, and Group B consists of 55 customers who purchased product B.
# The average satisfaction rating for Group A is 8.2, with a standard deviation of 1.5,
# while the average satisfaction rating for Group B is 7.8, with a standard deviation of 1.3.
# Test whether there is sufficient evidence to support the claim that there is no difference in average satisfaction ratings between the two products at a significance
# level of 0.01 (two-tailed test).

#Problem 8:
#A school district introduces a new curriculum and claims that it has no impact on student test scores compared to the old curriculum.
# To test this claim, you randomly select two groups of students. Group A consists of 60 students taught with the new curriculum,
# and Group B consists of 65 students taught with the old curriculum. The average test score for Group A is 85, with a standard deviation of 10,
# while the average test score for Group B is 87, with a standard deviation of 9. Test whether there is enough evidence to support the claim that there is no difference
# in average test scores between the two curricula at a significance level of 0.05 (two-tailed test).

#Problem 9:
#A researcher investigates the effect of two different study methods on exam performance.
# Two groups of students are randomly assigned. Group A uses study method X, while Group B uses study method Y. After the exam,
# you compare the average exam scores of both groups. Group A has an average score of 75, with a standard deviation of 5, while Group B has an average score of 78,
# with a standard deviation of 4. Test whether there is sufficient evidence to support the claim that there is no difference in average exam scores between the two
# study methods at a significance level of 0.01 (two-tailed test).

#Problem 10:
#A company claims that there is no significant difference in the mean heights between their two production lines.
# To test this claim, you randomly select two samples of products. Group A consists of 30 products from Line 1, and Group B consists of 35 products from Line 2.
# The average height for Group A is 40 cm, with a standard deviation of 2 cm, while the average height for Group B is 38 cm, with a standard deviation of 3 cm.
# Test whether there is enough evidence to support the claim that there is no significant difference in mean heights between the two production lines at a significance
# level of 0.05 (two-tailed test).

#Problem 1:
#A company claims that the average response time for their customer service hotline is lower on weekdays compared to weekends.
# To test this claim, you randomly select two samples of callers. Group A consists of 40 callers from weekdays, and Group B consists of 35 callers from weekends.
# The average response time for Group A is 5.5 minutes, with a standard deviation of 1.2 minutes, while the average response time for Group B is 6 minutes,
# with a standard deviation of 1.5 minutes. Test whether there is enough evidence to support the claim that the average response time is lower on weekdays compared
# to weekends at a significance level of 0.05 (left-tailed test).

#Problem 2:
#A company claims that the new version of their software has a lower error rate compared to the old version.
# To test this claim, you randomly select two samples of users. Group A consists of 50 users of the new version, and Group B consists of 55 users of the old version.
# The average error rate for Group A is 1.8%, with a standard deviation of 0.6%, while the average error rate for Group B is 2.2%, with a standard deviation of 0.8%.
# Test whether there is sufficient evidence to support the claim that the new version has a lower error rate at a significance level of 0.01 (left-tailed test).

#Problem 3:
#A school district introduces a new teaching method and claims that it results in a lower
# student dropout rate compared to the previous method. To test this claim, you randomly select two groups of students.
# Group A consists of 60 students taught with the new method, and Group B consists of 65 students taught with the old method.
# The dropout rate for Group A is 10%, while the dropout rate for Group B is 15%. Test whether there is enough evidence to support the claim that the new
# teaching method leads to a lower dropout rate at a significance level of 0.05 (left-tailed test).

#Problem 4:
#A researcher investigates the effect of two different diets on weight loss.
# Two groups of participants are randomly assigned. Group A follows diet X, while Group B follows diet Y.
# After a specified period, you compare the average weight loss of both groups. Group A has an average weight loss of 8 pounds,
# with a standard deviation of 2 pounds, while Group B has an average weight loss of 7 pounds, with a standard deviation of 1.5 pounds.
# Test whether there is sufficient evidence to support the claim that diet X leads to greater weight loss at a significance level of 0.01 (left-tailed test).

#Problem 5:
#A company claims that there is a lower defect rate in products produced by Machine A compared to Machine B.
# To test this claim, you randomly select two samples of products. Group A consists of 30 products from Machine A,
# and Group B consists of 35 products from Machine B. The defect rate for Group A is 2%, while the defect rate for Group B is 4%.
# Test whether there is enough evidence to support the claim that Machine A has a lower defect rate at a significance level of 0.05 (left-tailed test).

#Problem 1:
#A company claims that the average response time for their customer service hotline is higher on weekdays compared to weekends.
# To test this claim, you randomly select two samples of callers. Group A consists of 40 callers from weekdays, and Group B consists of 35 callers from weekends.
# The average response time for Group A is 6 minutes, with a standard deviation of 1.5 minutes, while the average response time for Group B is 5.5 minutes,
# with a standard deviation of 1.2 minutes. Test whether there is enough evidence to support the claim that the average response time is higher on weekdays
# compared to weekends at a significance level of 0.05 (right-tailed test).

#Problem 2:
#A company claims that the new version of their software has a higher user satisfaction rating compared to the old version.
# To test this claim, you randomly select two samples of users. Group A consists of 50 users of the new version,
# and Group B consists of 55 users of the old version. The average satisfaction rating for Group A is 8.2, with a standard deviation of 1.5,
# while the average satisfaction rating for Group B is 7.8, with a standard deviation of 1.3.
# Test whether there is sufficient evidence to support the claim that the new version has a higher user satisfaction rating at a significance level of 0.01 (right-tailed test).

#Problem 3:
#A school district introduces a new teaching method and claims that it results in a higher average test score compared to the previous method.
# To test this claim, you randomly select two groups of students. Group A consists of 60 students taught with the new method, and Group B consists of 65 students taught with the old method. The average test score for Group A is 85, with a standard deviation of 10, while the average test score for Group B is 87, with a standard deviation of 9. Test whether there is enough evidence to support the claim that the new teaching method leads to a higher average test score at a significance level of 0.05 (right-tailed test).

#Problem 4:
#A researcher investigates the effect of two different diets on weight loss. Two groups of participants are randomly assigned.
# Group A follows diet X, while Group B follows diet Y. After a specified period, you compare the average weight loss of both groups.
# Group A has an average weight loss of 8 pounds, with a standard deviation of 2 pounds, while Group B has an average weight loss of 7 pounds,
# with a standard deviation of 1.5 pounds. Test whether there is sufficient evidence to support the claim that diet X leads to greater weight
# loss at a significance level of 0.01 (right-tailed test).

#Problem 5:
#A company claims that there is a higher success rate in products produced by Machine A compared to Machine B.
# To test this claim, you randomly select two samples of products. Group A consists of 30 products from Machine A,
# and Group B consists of 35 products from Machine B. The success rate for Group A is 95%, while the success rate for Group B is
# 90%. Test whether there is enough evidence to support the claim that Machine A has a higher success rate at a significance level of 0.05 (right-tailed test).
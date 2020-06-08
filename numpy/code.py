# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
census=np.concatenate([data,new_record])
print(census)

age=census[:,0]
print(age)

max_age=max(age)
min_age=min(age)
print(max_age)
print(min_age)
age_mean=age.mean()
print(age_mean.round(2))
age_std=age.std()
print(age_std.round(2))

race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]

length=np.array([len(race_0),len(race_1),len(race_2),len(race_3),len(race_4)])

minority_race=np.where(length==min(length))
print("Minority race is ",minority_race[0])

senior_citizens=census[census[:,0]>60]
working_hours_sum=senior_citizens.sum(axis=0)[6]
print(working_hours_sum)

avg_working_hours=working_hours_sum/len(senior_citizens)
print("the average workinh hours {}".format(avg_working_hours.round(2)))

high,low=census[census[:,1]>10],census[census[:,1]<=10]
avg_pay_high=high.mean(axis=0)[7]
avg_pay_low=low.mean(axis=0)[7]
print(avg_pay_high.round(2))
print(avg_pay_low.round(2))














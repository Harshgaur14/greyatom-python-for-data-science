# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)


#Code starts here

# Step 1 
#Reading the file


#Creating a new variable to store the value counts
loan_status=data['Loan_Status'].value_counts()
print(loan_status)
loan_status.plot(kind='bar')
plt.show()


#Plotting bar plot



# Step 2
#Plotting an unstacked bar plot
property_and_loan=data.groupby(['Property_Area','Loan_Status']).size().unstack()

print(property_and_loan)
property_and_loan.plot(kind='bar',stacked=False,figsize=(10,10))
plt.xlabel('Property Area')
plt.ylabel('Loan Status')

#Changing the x-axis label


#Changing the y-axis label


#Rotating the ticks of X-axis
plt.xticks(rotation=45)
plt.show()
# Step 3
#Plotting a stacked bar plot
education_and_loan=data.groupby(['Education','Loan_Status']).size().unstack()
education_and_loan.plot(kind='bar',stacked=True,figsize=(10,10))
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.yticks(rotation=45)
plt.show()





#Changing the x-axis label


#Changing the y-axis label


#Rotating the ticks of X-axis


# Step 4 
#Subsetting the dataframe based on 'Education' column
graduate=pd.DataFrame(data[data['Education']=='Graduate']['LoanAmount'])
print(graduate.head(4))

#Subsetting the dataframe based on 'Education' column
not_graduate=pd.DataFrame(data[data['Education']=='Not Graduate']['LoanAmount'])
print(not_graduate.head(4))
#Plotting density plot for 'Graduate'
graduate.plot(kind='density',label='Graduate')


#Plotting density plot for 'Graduate'
not_graduate.plot(kind='density',label='not_graduate')


#For automatic legend display


# Step 5
#Setting up the subplots
fig,(ax_1, ax_2,ax_3) = plt.subplots(3,1, figsize=(18,8))
ax_1.set_title('Applicant Income')
ax_1.scatter(x=data['ApplicantIncome'],y=data['LoanAmount'])
ax_2.scatter(x=data['CoapplicantIncome'],y=data['LoanAmount'])
ax_2.set_title('CoapplicantIncome')
data['TotalIncome']=data['ApplicantIncome']+data['CoapplicantIncome']

ax_3.scatter(x=data['TotalIncome'],y=data['LoanAmount'])
ax_3.set_title('Total Income')
print(data['TotalIncome'].head(4))



#Plotting scatter plot


#Setting the subplot axis title


#Plotting scatter plot


#Setting the subplot axis title


#Creating a new column 'TotalIncome'


#Plotting scatter plot



#Setting the subplot axis title




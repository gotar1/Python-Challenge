# Python-Challenge 


## PyBank

* In this challenge, the tasked is to create a Python script for analyzing the financial records of a company.
* We will analyse the budget data [here](PyBank/Resources/budget_data.csv). 
* The dataset is composed of two columns: `Date` and `Profit/Losses`.

* We created a Python script that analyzes the entire budget period and calculate the following:

  * The total number of months included in the budget.

  * The net total amount of "Profit/Losses".

  * The average of the changes in "Profit/Losses".

  * The greatest increase in profits (date and amount).

  * The greatest decrease in losses (date and amount).

```text
Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average Change:  $-2315.12
Greatest Increase in Profits:  Feb-2012 ($1926159)
Greatest Decrease in Profits:  Sep-2013 ($-2196167)
```  
  
## PyPoll

* In this challenge, the tasked is to help a small, rural town modernize its voting counting process.

* We will analyse a set of poll data called [here](PyPoll/Resources/election_data.csv). 
* The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`.
 
* The task is to create a Python script that analyzes the votes and calculates the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

```text
Election Results
-------------------------
Total Votes:  3521001
-------------------------
Khan: 63.0% (2218231)
Correy: 20.0% (704200)
Li: 14.0% (492940)
O'Tooley: 3.0% (105630)
-------------------------
Winner: Khan
```

## PyBoss

![Boss](/PyBoss/Images/boss.jpg)

* In this challenge, we get to be a boss that oversee hundreds of employees across the country. 
* Our company recently decided to purchase a new HR system, unfortunately, the new system requires 
employee records be stored completely differently.

* The task is to create a Python script to convert employee records to the required format.
* The script will need to do the following conversions:

  * The `Name` column should be split into separate `First Name` and `Last Name` columns.

  * The `DOB` data should be re-written into `MM/DD/YYYY` format.

  * The `SSN` data should be re-written such that the first five numbers are hidden from view.

  * The `State` data should be re-written as simple two-letter abbreviations.

* Old employee data format file [here](PyBoss/Resources/employee_data.csv):

```csv
Emp ID,Name,DOB,SSN,State
214,Sarah Simpson,1985-12-04,282-01-8166,Florida
15,Samantha Lara,1993-09-08,848-80-7526,Colorado
411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania
```

* New data format file [here](PyBoss/output/new_employee_data.csv):

```csv
Emp ID,First Name,Last Name,DOB,SSN,State
214,Sarah,Simpson,12/04/1985,***-**-8166,FL
15,Samantha,Lara,09/08/1993,***-**-7526,CO
411,Stacy,Charles,12/20/1957,***-**-8526,PA 

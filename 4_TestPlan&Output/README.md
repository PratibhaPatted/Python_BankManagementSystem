# TestPlan

| Test Id | HLT id | Description | Expected Output | Actual Output | PASS\ FAIL |
| --------|--------|-------------|-----------------|---------------|------------|
| T_1     | H_01   | Enter positive value for balance input| input > 0 | input > 0| PASS |
| T_2     | H_02   | Enter positive value for deposit amount | deposit>=0 | deposit>=0 | PASS |
| T_3     | H_03   | Enter withdraw amount greater than current balance | Valid | Valid| PASS|
| T_4     | H_04   | No amount/balance <=0 | Invalid | Invalid | PASS|
| T_5     | H_01   | Enter negative or zero value for deposit amount |Invalid | Invalid | PASS |






## Output Screenshots
## Main Menu

![4main](https://user-images.githubusercontent.com/98818228/163027370-6011f670-5a05-45b5-bddc-bedbe0cf6bd3.PNG)


## Create Account 1 (Shows no amount <= 0 valid)


![1](https://user-images.githubusercontent.com/98818228/163027384-bb1ca16a-0bf3-4e9c-b119-ac30111cb5a4.PNG)


## Deposit Amount operation

![2](https://user-images.githubusercontent.com/98818228/163027357-7459737a-01ad-4acf-ae91-17719860bf0e.PNG)
![7invaild](https://user-images.githubusercontent.com/98818228/163028034-05fceb8b-fb67-41d3-8046-538165ce3fb8.PNG)

## Withdraw Amount operation (Shows withdraw amount should be less than or equal to current balance )

![3](https://user-images.githubusercontent.com/98818228/163027367-9e1d1348-ed0b-44a4-bccf-a9f7e5e8e72e.PNG)
![8invaild](https://user-images.githubusercontent.com/98818228/163028042-bd71e458-73f9-45ec-acf2-25fc7ee030b2.PNG)


## Display all accounts

![5](https://user-images.githubusercontent.com/98818228/163027375-917971bc-c4b0-428b-b63e-606c3c7ef709.PNG)
![6](https://user-images.githubusercontent.com/98818228/163027378-84ea2c09-9bad-4e25-96d6-61e81dbc2e6f.PNG)


# Introduction

This system is primarily intended for the storage of banking information. The C programming language was used to create the entire system. It establishes a basic notion of how clients' bank details, such as their name, address, phone number, and other information, are preserved. The user interface is straightforward, with a standard screen design, so staff may quickly become accustomed to it.

# Requirements

## High level requirements
1. Manage Customers Information
2. Manage Bank Records
3. Withdraw money
4. Deposit money
5. create different types of accounts (Savings,current)
6. Search accounts

## Low level requirements
1. Add the customer id, name, amount.
2. Search the customer details by using their user id.
3. Deposit and withdraw amount by user id.


# Benefits

1. Required very little manpower.
2. Simplify the problem of editing.
3. Maintain the clearance level by the hierarchy.
4. Maintain data integrity Validate the manual calculations avoid calculation error.
5. Safeguard the data accuracy.
6. User Friendly


# SWOT ANALYSIS
![swot](https://user-images.githubusercontent.com/98818228/154980738-04154de1-887f-449a-9271-ec452c6d0dd9.PNG)


## 4W's and 1'H

## Who
Banks
## What
This bank management system is based on bank requirements. The system can encode customer information. Banking admin can have access to the customer status and information of different accounts. Users can create account, deposit and withdraw amount.

## When
When we want to Safeguard the data accuracy.
When we want to reduce calculation error and manual work.
When user wants to carry out the tasks quickly.


## Where
In the banks 

## How

We can implement this to do the basic banking activities and the admin can keep the track of all the records and about customer details. And customers can deposit , withdraw and create different types of accounts.


# Design 
# High Level Design

## Architecture Design

![design](https://user-images.githubusercontent.com/98818228/152687123-10db9ae7-3db2-42cd-859a-c5742ac9933e.PNG)


# Usecase Diagram
![uml](https://user-images.githubusercontent.com/98818228/152687161-9e8c8aec-0ee0-498b-9ba7-daf259c0824a.jpg)


# Low Level Design
## Level0
![0level](https://user-images.githubusercontent.com/98818228/152687175-0d825cfe-bf38-41f0-b027-7eb704b3f920.jpg)



## Level1

![level1 (1)](https://user-images.githubusercontent.com/98818228/152687185-71dcb9fc-1e8c-45b5-9ad8-80fe5c36c7db.jpg)


# Output Screenshots
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

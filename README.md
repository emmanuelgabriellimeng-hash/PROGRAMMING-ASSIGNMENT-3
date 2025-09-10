# PA 3 – PANDAS  

## Overview  
This assignment covers the use of **Pandas** in Python for handling tabular data. The program demonstrates loading a CSV file into a DataFrame, displaying rows, and performing subsetting, slicing, and indexing.  

---

## Directory  
### Problem 1:
* https://github.com/emmanuelgabriellimeng-hash/PROGRAMMING-ASSIGNMENT-3/blob/main/Lim_Pandas-P1%20(1).py

### Problem 2:
* https://github.com/emmanuelgabriellimeng-hash/PROGRAMMING-ASSIGNMENT-3/blob/main/Lim_Pandas-P2%20(1).py

### Program Link:
* https://github.com/emmanuelgabriellimeng-hash/PROGRAMMING-ASSIGNMENT-3/blob/main/Lim_Pandas.ipynb  

### Download csv file:
* https://github.com/emmanuelgabriellimeng-hash/PROGRAMMING-ASSIGNMENT-3/blob/main/cars.csv

---

## Problem 1  

**Description:**  
Load the `cars.csv` file into a DataFrame named `cars`. Display the first five and last five rows of the dataset.  

**Explanation:**  
1. Import Pandas.  
```python
import pandas as pd
```  

2. Load the dataset into a DataFrame named `cars`. Using `read_csv()`, the program reads the cars.csv file and creates a DataFrame named cars.
```python
cars = pd.read_csv("cars.csv")
```  
3. Display the first five rows. To do this, the function `head()` was applied to automatically display the first five rows
```python
cars.head()
```  
**Example Output:**  

<img width="696" height="233" alt="image" src="https://github.com/user-attachments/assets/89666520-9969-4419-a84d-8351f43944e4" />

4. Display the last five rows. To do this, the function `tail()` was applied to automatically display the last five rows
```python
cars.tail()
```  
**Example Output:**  

<img width="678" height="231" alt="image" src="https://github.com/user-attachments/assets/c5807d84-2368-469a-9b4a-9f11feddb744" />

---

## Problem 2  

**Description:**  
Using the `cars` DataFrame, perform subsetting, slicing, and indexing to answer specific queries.  

**Explanation:**  
1. Display the first five rows with odd-numbered columns. With `iloc` as integer-based indexing, the slice 0:5 selects the first five rows, while ::2 selects every second column. 
```python
cars.iloc[0:5, ::2]
```  
**Example Output**

<img width="366" height="208" alt="image" src="https://github.com/user-attachments/assets/07bf43c6-0dc4-4786-92b1-e2690f368900" />

2. Display the row where `Model` is `"Mazda RX4"`. By indexing, the DataFrame checks where the Model column equals Mazda RX4.
```python
cars[cars['Model'] == 'Mazda RX4']
```  
**Example Output**

<img width="578" height="67" alt="image" src="https://github.com/user-attachments/assets/76983a39-8d04-4427-a2ee-a8e1f6206f23" />

3. Find the number of cylinders for `"Camaro Z28"`. Using `loc[]`, the program selects data by labels. Row index 23 corresponds to "Camaro Z28". Consequently, calling `['Model', 'cyl']`  would display the desired car name with its cylinder count.
```python
cars.loc[[23], ['Model', 'cyl']]
```
**Example Output:**  

<img width="159" height="66" alt="image" src="https://github.com/user-attachments/assets/eb8f0a23-0cfc-4cef-a9c5-fa1bb422c4ce" />

4. Display the cylinders and gear type for `"Mazda RX4 Wag"`, `"Ford Pantera L"`, and `"Honda Civic"`. `isin` checks if each row’s Model value is in the selected_models list. Additionally, `loc` filters those rows and shows only the Model, cyl, and gear columns. 
```python
selected_models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
cars.loc[cars['Model'].isin(selected_models), ['Model', 'cyl', 'gear']]
```
**Example Output:**  

<img width="229" height="137" alt="image" src="https://github.com/user-attachments/assets/b31deb48-4ce4-4458-a376-0bfdaa4ce277" />

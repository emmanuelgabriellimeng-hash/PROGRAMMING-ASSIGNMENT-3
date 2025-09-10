{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "a822ebed-70ba-441b-91b4-5b4e1e1e859e",
   "metadata": {},
   "source": [
    "# Experiment 3 - PANDAS\n",
    "### Name: Emmanuel Gabriel M. Lim\n",
    "### Section: 2ECE-B\n",
    "### Date: September 10, 2025\n",
    "### Subject Code: ECE2112"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e0c23c33-f15e-4e56-a66a-e83249908fe2",
   "metadata": {},
   "source": [
    "## Problem 2\n",
    "\n",
    "Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and\n",
    "indexing operations.\n",
    "\n",
    "    a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "8c960713-0d5f-4121-bc90-52af8b0605dc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Model</th>\n",
       "      <th>cyl</th>\n",
       "      <th>hp</th>\n",
       "      <th>wt</th>\n",
       "      <th>vs</th>\n",
       "      <th>gear</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Mazda RX4</td>\n",
       "      <td>6</td>\n",
       "      <td>110</td>\n",
       "      <td>2.620</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mazda RX4 Wag</td>\n",
       "      <td>6</td>\n",
       "      <td>110</td>\n",
       "      <td>2.875</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Datsun 710</td>\n",
       "      <td>4</td>\n",
       "      <td>93</td>\n",
       "      <td>2.320</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Hornet 4 Drive</td>\n",
       "      <td>6</td>\n",
       "      <td>110</td>\n",
       "      <td>3.215</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Hornet Sportabout</td>\n",
       "      <td>8</td>\n",
       "      <td>175</td>\n",
       "      <td>3.440</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               Model  cyl   hp     wt  vs  gear\n",
       "0          Mazda RX4    6  110  2.620   0     4\n",
       "1      Mazda RX4 Wag    6  110  2.875   0     4\n",
       "2         Datsun 710    4   93  2.320   1     4\n",
       "3     Hornet 4 Drive    6  110  3.215   1     3\n",
       "4  Hornet Sportabout    8  175  3.440   0     3"
      ]
     },
     "execution_count": 87,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "cars = pd.read_csv(\"cars.csv\")  \n",
    "cars.iloc[0:5, ::2]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "199aa625-b68f-472d-a634-6522e4e2d8c9",
   "metadata": {},
   "source": [
    "    b. Display the row that contains the ‘Model’ of ‘Mazda RX4’."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "c197aff8-fbaf-468c-a766-eff15f21e6c8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Model</th>\n",
       "      <th>mpg</th>\n",
       "      <th>cyl</th>\n",
       "      <th>disp</th>\n",
       "      <th>hp</th>\n",
       "      <th>drat</th>\n",
       "      <th>wt</th>\n",
       "      <th>qsec</th>\n",
       "      <th>vs</th>\n",
       "      <th>am</th>\n",
       "      <th>gear</th>\n",
       "      <th>carb</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Mazda RX4</td>\n",
       "      <td>21.0</td>\n",
       "      <td>6</td>\n",
       "      <td>160.0</td>\n",
       "      <td>110</td>\n",
       "      <td>3.9</td>\n",
       "      <td>2.62</td>\n",
       "      <td>16.46</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Model   mpg  cyl   disp   hp  drat    wt   qsec  vs  am  gear  carb\n",
       "0  Mazda RX4  21.0    6  160.0  110   3.9  2.62  16.46   0   1     4     4"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mazda_rx4_row = cars[cars['Model'] == 'Mazda RX4']\n",
    "mazda_rx4_row"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fcf35414-dc2c-44e7-be39-72f17ed11907",
   "metadata": {},
   "source": [
    "    c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "c59f8d52-8a24-428f-a7c5-2f341ed282ab",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Model</th>\n",
       "      <th>cyl</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>Camaro Z28</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Model  cyl\n",
       "23  Camaro Z28    8"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cars.loc[[23], ['Model', 'cyl']]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "399f8d52-93f5-411a-878c-7a1cad19935d",
   "metadata": {},
   "source": [
    "\n",
    "    d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "4cc1229b-7392-468e-9033-f367bae8af0c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Model</th>\n",
       "      <th>cyl</th>\n",
       "      <th>gear</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mazda RX4 Wag</td>\n",
       "      <td>6</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>Honda Civic</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>Ford Pantera L</td>\n",
       "      <td>8</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             Model  cyl  gear\n",
       "1    Mazda RX4 Wag    6     4\n",
       "18     Honda Civic    4     4\n",
       "28  Ford Pantera L    8     5"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "selected_models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']\n",
    "cars.loc[cars['Model'].isin(selected_models), ['Model', 'cyl', 'gear']]"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

# Report

## Dataset
I chose "college-salaries" data to be the dataset.
This dataset contains **three** part.
The "salary" attrs are seperated into different parts. Each corresponds to a typical time period of career.  
1. degrees-that-pay-back
stores the average salaries of all colleges for each **major**.
2. salaries-by-college-type
stores certain colleges' names and types and the average salaries.
3. salaries-by-region
stores certain colleges' names and region and the average salaries.

## Analysis
1. degrees-that-pay-back
This dataset aims to show the differences among those majors.
So, the majors should be shown in form of single scattered points, in which way, we could see the distribution of those majors.
To compare the majors of career's different time periods, we need to pick 2 specified periods. One as "x" axis, the other as "y".
In the image, we can find which major's salary changes the most, and the amounts of salary are easy to be compared with.
2. salaries-by-colleges-type
This dataset aims to show the dofferences among those different school types.
This contains certain schools, each of them is shown as a point on it.
Except the time periods comparision mentioned above, this dataset features in the "school type". We need to analyse the special situation 
of each "school type".
3. salaries-by-region
This dataset is similar to the one above. To make a difference, this dataset is shown in the way of 'bar graph'.
I want to see the comparision among certain schools in the specific region. And also, in each region, I want to check the situations of different time periods.

## layout
![UI](\imgs\1.png)
![UI](\imgs\2.png)
Three graphs in total. There is no such associations among the three, so I just put them parallelly.
Each graph has two or three drop down list, used to interact with users. User can tap the option, to change the data and analyse them.

## patterns revealed
1. Salaries of majors belong to liberal arts are lower in most circumstances. But they increase faster then the science majors' salaries.
2. The salary of each instructor always increases as the he or she gets older.
3. Famous colleges provide higher salaries.
4. Salaries of schools in Ivy League are higher and change more quickly.
5. Salaries of schools which share the "liberal arts" type are lower and stabler.
6. Salaries of states's schools are similar to each other, and also stable.
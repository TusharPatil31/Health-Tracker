# Health-Tracker

DESCRIPTION

Lyka, the sporting shoe company, approaches you to create a simple python app that helps in tracking workouts, energy (or calories) burnt, BMI, weekly rewards, monthly rewards, fastest week, slowest month, etc. Some of the features are shown below. 

 

The application will accept the following initial inputs from any user: 

Name, Age, Sex, Weight, Height 

 

You should be able to use either the FPS or Metric system with regards to weight and height. 

 

The app should accept the next set of inputs, which are: 

Day 
Number of steps 
Time taken (hours:minutes: seconds) 
 

You can provide a number of inputs based on the following: Assumptions: Day = 1 for Monday, Day = 2 for Tuesday, etc. 

 

Sample Input and Output 

A typical 1-week sample input of 7 days will have the following input: 

1, 7500, 1:02:05 

2, 8500, 1:06:12 

3, 3500, 0:52:25 

4, 4250, 0:59:35 

5, 7800, 1:01:55 

6, 8500, 1:12:15 

7, 9500, 1:15:25 

 

The sample output for this data should be: 

Weekly Average: 4.64 Km/hr (or 2.95 mi/hr) 

 

A typical 1-month sample input of 5 days will have the following input: 

1, 7500, 1:02:05 

2, 8500, 1:06:12 

3, 3500, 0:52:25 

4, 4250, 0:59:35 

5, 7800, 1:01:55 

6, 8500, 1:12:15 

7, 9500, 1:15:25

1, 7500, 1:02:05 

2, 8500, 1:06:12 

3, 3500, 0:52:25 

4, 4250, 0:59:35 

5, 7800, 1:01:55 

6, 8500, 1:12:15 

7, 9500, 1:15:25 

1, 7500, 1:02:05 

2, 8500, 1:06:12 

3, 3500, 0:52:25 

4, 4250, 0:59:35 

5, 7800, 1:01:55 

6, 8500, 1:12:15 

7, 9500, 1:15:25 

1, 7500, 1:02:05 

2, 8500, 1:06:12 

3, 3500, 0:52:25 

4, 4250, 0:59:35 

5, 7800, 1:01:55 

6, 8500, 1:12:15 

7, 9500, 1:15:25 

 

Any breaks in the schedule can be provided as follows. Again, a sample of 1-week data is given: 

1, 7500, 1:02:05 

2, 0, 0:00:0 

3, 3500, 0:52:25 

4, 4250, 0:59:35 

5, 0, 0:00:00 

6, 8500, 1:12:15 

7, 9500, 1:15:25 

 

Sample calculation for missing dates (days) and computation of speed and distance 

Weekly Average: 4.44 Km/hr (or 2.77 mi/hr) 

No Awards this week, as there are breaks in the schedule 

 

This can be done across the monthly data as well, as shown previously. Naturally, there are some weeks of achievement in terms of speed and total distance. 

 

For 1-month data, say, the output should include the number of weeks of achievement. Note that, if there are missing workout days, that week cannot be considered for the computation of the monthly award. 

Congrats! You have got a 3 7/7 award for this month, if there are 3 consecutive weeks of workouts, with a break of one/two days of workout in one particular week.

 

Similarly, for 4-month data, the output should include the number of months of achievement. Again, note that if the days have missing workout days, they cannot be considered for monthly achievement. 

Congrats! You have got a 2 M/M award for this month, if there are 3 consecutive months of workout, and there is a week in a month, where there is a one or two days break with no workouts. 

 

For a complete input/output cycle for a week, typically, the app should provide the following: 

Input - - - - - - 

Name: Ramana 

Sex: Male 

Age (years): 45 

Weight (Kg): 70 

Height (cms): 196 

 

Workout Input- - - - - - - 

1, 7500, 1:02:05 

2, 8500, 1:06:12 

3, 3500, 0:52:25 

4, 4250, 0:59:35 

5, 7800, 1:01:55 

6, 8500, 1:12:15 

7, 9500, 1:15:25 

 

Output- - - - - - - 

Hi Mr. Ramana 

Your BMI is: 18.3. Try to put on some weight!! 

Your Weekly achievement is as follows: 

No breakout in Sessions: You get a 7/7 award 

Your Fastest Speed is: 5.52 Km/hr 

Your Longest Distance is: 6.7 km 

Your Slowest Speed is: 3.06 Km/hr 

Your Shortest Distance is: 2.5 Km 

Your Weekly Average Speed is: 4.64 Km/hr 

Your Weekly Average Distance is: 35.39 Km 

 

For an incomplete input/output cycle for a week, typically, the app should provide the following: 

Input - - - - - - 

Name: Ramana 

Sex: Male 

Age (years): 45 

Weight (Kg): 70 

Height (cms): 196 

 

Workout Input- - - - - - - 

1, 7500, 1:02:05 

2, 0, 0:00:0

3, 3500, 0:52:25 

4, 4250, 0:59:35 

5, 0, 0:00:00 

6, 8500, 1:12:15 

7, 9500, 1:15:25 

 

Output- - - - - - - 

Your BMI is: 18.3. Try to put on some weight!! Your Weekly achievement is as follows: Your Fastest Speed is: 5.52 Km/hr 

Your Longest Distance is: 6.7 km 

Your Slowest Speed is: 3.06 Km/hr 

Your Shortest Distance is: 2.5 Km 

Your Weekly Average Speed is: 4.44 Km/hr Your Weekly Average Distance is: 23.75 Km 

This is extendable across monthly data as well. 

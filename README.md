# chart-denoiser
We know that the least squares answer of the equation Ax=y is a vector that minimizes the value of the objective function ||Ax -y||^2. <br>
First, we opened the price_btc.py file with the load function and used the plot function in the matplotlib library to draw the loaded array in a graph format. The chart shows the price of Bitcoin every 2 hours from the end of 2020 to the 20th of May. As you can see, this chart has many fluctuations and it can be difficult to work with it. Here we want to denoise this graph using least-squares.
![image](https://user-images.githubusercontent.com/117355603/222463964-61b45eca-1311-4eca-b215-8ce7adf84f0e.png)
## Least-squared
Suppose that the vector 𝒚 is the vector of bitcoin price values, the unknown vector 𝒙 is the noise-free vector of the price we are looking for, and the vector 𝒗 is the uncertain noise vector. Thus, we have: <br>
y = x + v <br>
or <br>
y = Ix + v
<br>
If we solve the square-least answer of the y = Ix + v equation for the above equation, we have actually minimized the following function. <br>
![image](https://user-images.githubusercontent.com/117355603/222464591-455e54e3-e26f-41a6-a8e6-9e450e3f47df.png)
<br>
Minimizing this function makes the values of the vector 𝒙 close to 𝒚. But this condition alone does not cause the vector to be denoised. Another necessary condition is the smallness of the difference between two adjacent regions of the vector 𝒙. So, we write the above objective function by adding the second condition as below (𝝀 is the parameter of the problem that adjusts the ratio of the effect of the two conditions mentioned in the answer of the problem). <br>
![image](https://user-images.githubusercontent.com/117355603/222465067-fca77b92-bc46-4009-9dd6-442d35e035de.png)
<br>
The second expression can also be written in the form below, where 𝑫 is equal to the matrix 𝒏 × (𝒏 − 𝟏): <br>
![image](https://user-images.githubusercontent.com/117355603/222465508-80c41c1b-69f1-48d2-a403-06d379c3f8c8.png)
<br>
So finally our goal is to minimize the function <br>
![image](https://user-images.githubusercontent.com/117355603/222465623-9b138eb8-29a9-435e-bd47-7c7f9eb6f251.png)
<br>
The above function can also be written in the form of the following block matrices: <br>
![image](https://user-images.githubusercontent.com/117355603/222465732-7aad52f5-08f2-4bfe-9234-7abfc31d7b6a.png)
<br>
So, we were able to make our objective function in the form of the objective function of the least squares problem.
In this project, by minimizing the above function with the help of the solution of the least squares problem, we denoized the given array and drew it, and we tried this work for different values of the parameter 𝝀.











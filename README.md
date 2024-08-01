# IIT_KGP_Assignments
IIT Kharagpur AI4ICPS Certificate Programme

# How to check Command Line Argument :
Save and Close the Script:
Ensure your script is saved and closed before running it from the terminal.

Open a Terminal in VS Code:
Open the terminal in VS Code. You can do this by selecting Terminal > New Terminal from the top menu.

Navigate to the Directory (Optional):
If your script is not in the current directory, navigate to the directory containing your script. For example:

cd "D:\"
Run the Python Script with Command-Line Arguments:
Execute your Python script and pass any command-line arguments you want. For example:

python "D:\Programming_Assignment_1.py" arg1 arg2 arg3
Replace arg1 arg2 arg3 with your actual arguments.

Check the Output:
Your script should print the command-line arguments passed to it. For example, if you ran the command above, the output would be:

plaintext
Copy code
Command-line arguments passed:
Argument 0: D:\Programming_Assignment_1.py
Argument 1: arg1
Argument 2: arg2
Argument 3: arg3
This method allows you to check and use command-line arguments in your Python script when running it from the terminal.

# Numpy Insiders

1. What is NumPy ? 

NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays. 

2. Why use NumPy ?

 In Python we have lists that serve the purpose of arrays, but they are slow to process. NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy. 
Arrays are very frequently used in data science, where speed and resources are very important. 

3. Why is NumPy Faster Than Lists? 

NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently. 
This behavior is called locality of reference in computer science. 
This is the main reason why NumPy is faster than lists. Also it is optimized to work with latest CPU architectures.





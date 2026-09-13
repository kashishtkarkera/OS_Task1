# OS_Task1
Operating Systems thread-based implementations of the Producer-Consumer problem and Matrix Multiplication with animation.
🧵 Operating Systems — Thread-Based Implementation
📌 Overview

This repository contains implementations of two thread-based problems from the Operating Systems assignment:

Producer–Consumer Problem using Python Threads
Matrix Multiplication using Python Threads with Animation

The programs demonstrate fundamental concepts of multithreading, synchronization, shared resources, circular buffers, concurrent execution, and thread-based computation.

📂 Files in this Repository
File	Description
1) producer_consumer.py	Implementation of the Producer–Consumer problem using Python threads
2)matrix_multiplication.py	Thread-based multiplication of two 105 × 105 matrices
matrix_multiplication.gif	Animation demonstrating the matrix multiplication process
1️⃣ Producer–Consumer Problem
📖 Description

The Producer–Consumer problem is a classic synchronization problem in Operating Systems where a Producer thread generates data and places it into a shared buffer, while a Consumer thread removes and processes that data.

The implementation uses a fixed-size circular buffer shared between the two threads.

⚙️ How It Works
The Producer adds items to the shared buffer.
The Consumer removes items from the buffer.
in_pos keeps track of the next position where an item will be inserted.
out_pos keeps track of the next position from which an item will be removed.
The buffer positions wrap around using the modulo operation.
Synchronization is handled using Python's threading.Condition.
The Producer waits when the buffer is full.
The Consumer waits when the buffer is empty.

This prevents incorrect access to the shared resource while allowing both threads to execute concurrently.

Concepts Demonstrated
Python Threads
Producer–Consumer synchronization
Shared resources
Circular buffer
Locks
Condition variables
wait() and notify()
Concurrent execution
2️⃣ Matrix Multiplication Using Threads
📖 Description

The second program performs multiplication of two 105 × 105 matrices using Python threads.

For every position (row, column) in the result matrix, a separate thread is created to calculate that result cell.

The multiplication follows the standard matrix multiplication operation:

C[i][j] = Σ A[i][k] × B[k][j]

Since the result matrix contains:

105 × 105 = 11,025 cells

the program creates 11,025 threads, with each thread responsible for calculating one result cell.

⚙️ How It Works
Two 105 × 105 matrices are generated.
A result matrix is initialized.
A thread is created for every result-cell position.
Each thread calculates the corresponding dot product.
The completed result is stored in the result matrix.
Thread completion is tracked using a lock.
The program waits for all threads to finish.
The resulting matrix is verified after computation.

The terminal displays information such as:

Matrix multiplication completed successfully.
Threaded result verified successfully.
Matrix size: 105 x 105
Total result cells: 11025
Threads used: 11025
🎬 Matrix Multiplication Animation

The program also generates a GIF animation showing the progress of the threaded matrix multiplication.

The animation visually represents:

Matrix A
Matrix B
The result matrix being calculated
The progress of individual result cells
The movement of the computation across the matrices

The animation is based on the actual progress of the threaded computation.

Animation Output

🛠️ Technologies Used
Python
Python threading module
NumPy
Matplotlib
Matplotlib Animation
▶️ How to Run
1. Install the required libraries
pip install numpy matplotlib
2. Run the Producer–Consumer program
python "1) producer_consumer.py"
3. Run the Matrix Multiplication program
python "2)matrix_multiplication.py"

The second program performs the threaded computation and generates the matrix multiplication animation.

🎯 Learning Outcomes

This assignment demonstrates how threads can be used to perform concurrent operations and how synchronization mechanisms are required when multiple threads share resources.

The implementations provide practical understanding of:

Thread creation and execution
Synchronization
Shared-memory access
Producer–Consumer coordination
Circular buffers
Parallel cell computation
Thread completion
Visualization of concurrent computation

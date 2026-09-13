# 💻 OS_Task1

## 🧵 Operating Systems — Thread-Based Implementations

This repository contains the implementations for the Operating Systems thread-based programming assignment.

The assignment demonstrates two fundamental synchronization and multithreading problems using Python:

1. **Producer–Consumer Problem using Threads**
2. **Matrix Multiplication using Threads with Animation**

---

## 📌 Overview

The programs demonstrate important Operating Systems concepts including:

- Thread creation and execution
- Concurrent execution
- Synchronization
- Shared resources
- Circular buffers
- Thread coordination
- Parallel computation
- Thread completion
- Visualization of threaded computation

---

## 📂 Files in This Repository

| File | Description |
|------|-------------|
| `1) producer_consumer.py` | Implementation of the Producer–Consumer problem using Python threads |
| `2)matrix_multiplication.py` | Thread-based multiplication of two 105 × 105 matrices |
| `matrix_multiplication.gif` | Animation demonstrating the matrix multiplication process |

---

# 1️⃣ Producer–Consumer Problem

## 📖 Description

The Producer–Consumer Problem is a classic synchronization problem in Operating Systems.

A **Producer thread** generates items and places them into a shared buffer, while a **Consumer thread** removes and processes those items.

The implementation uses a fixed-size circular buffer shared between the Producer and Consumer.

## ⚙️ How It Works

- `in_pos` keeps track of the next position where an item will be inserted.
- `out_pos` keeps track of the next position from which an item will be removed.
- The buffer operates as a circular buffer using the modulo operation.
- `threading.Condition` is used for synchronization.
- The Producer waits when the buffer is full.
- The Consumer waits when the buffer is empty.
- `notify()` is used to wake the waiting thread when the buffer state changes.

This prevents incorrect access to the shared resource while allowing both threads to execute concurrently.

## 🧠 Concepts Demonstrated

- Python Threads
- Producer–Consumer synchronization
- Shared resources
- Circular buffer
- Locks
- Condition variables
- `wait()` and `notify()`
- Concurrent execution

---

# 2️⃣ Matrix Multiplication Using Threads

## 📖 Description

The second program performs multiplication of two **105 × 105 matrices** using Python threads.

Each result cell is computed through an independent threaded computation.

The program records the completion of the threaded computations and uses the recorded execution order to generate an animation.

## ⚙️ How It Works

For matrix multiplication:

```text
Matrix A (105 × 105) × Matrix B (105 × 105)
                    ↓
              Matrix C (105 × 105)

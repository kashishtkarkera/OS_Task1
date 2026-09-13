import threading
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter


Size = 105
Total_Cells = Size * Size

matrix_a = np.random.randint(1, 10, size=(Size, Size))
matrix_b = np.random.randint(1, 10, size=(Size, Size))

result = np.zeros((Size, Size), dtype=int)

completion_order = []
completion_lock = threading.Lock()
threads = []


def calculate_cell(row, column):
    value = 0

    for index in range(Size):
        value += matrix_a[row][index] * matrix_b[index][column]

    result[row][column] = value

    with completion_lock:
        completion_order.append((row, column))


for row in range(Size):
    for column in range(Size):
        worker = threading.Thread(
            target=calculate_cell,
            args=(row, column)
        )
        threads.append(worker)
        worker.start()


for worker in threads:
    worker.join()


expected_result = matrix_a @ matrix_b

if np.array_equal(result, expected_result):
    print("\nMatrix multiplication completed successfully.")
    print("Threaded result verified successfully.")
else:
    print("\nError: threaded result does not match expected result.")

print(f"Matrix size: {Size} x {Size}")
print(f"Total result cells: {Total_Cells}")
print(f"Threads used: {len(threads)}")


fig, axes = plt.subplots(1, 3, figsize=(16, 6))

fig.patch.set_facecolor("#111111")

for axis in axes:
    axis.set_facecolor("#111111")
    axis.tick_params(colors="white")
    axis.xaxis.label.set_color("white")
    axis.yaxis.label.set_color("white")


axes[0].imshow(
    matrix_a,
    cmap="magma",
    interpolation="nearest"
)

axes[0].set_title(
    "Matrix A",
    color="white",
    fontsize=14,
    fontweight="bold"
)

axes[0].set_xlabel("Columns")
axes[0].set_ylabel("Rows")


axes[1].imshow(
    matrix_b,
    cmap="cividis",
    interpolation="nearest"
)

axes[1].set_title(
    "Matrix B",
    color="white",
    fontsize=14,
    fontweight="bold"
)

axes[1].set_xlabel("Columns")
axes[1].set_ylabel("Rows")


visible_result = np.full(
    (Size, Size),
    np.nan
)

result_image = axes[2].imshow(
    visible_result,
    cmap="plasma",
    interpolation="nearest",
    vmin=0,
    vmax=result.max()
)

axes[2].set_title(
    "Result Matrix C",
    color="white",
    fontsize=14,
    fontweight="bold"
)

axes[2].set_xlabel("Columns")
axes[2].set_ylabel("Rows")


line_a = axes[0].axhline(
    0,
    linewidth=2
)

line_b = axes[1].axvline(
    0,
    linewidth=2
)

current_cell = axes[2].plot(
    [0],
    [0],
    marker="s",
    markersize=8,
    markerfacecolor="none",
    markeredgewidth=2
)[0]


fig.suptitle(
    "Threaded Matrix Multiplication",
    color="white",
    fontsize=18,
    fontweight="bold"
)

status = fig.text(
    0.5,
    0.025,
    f"Computing: 0 / {Total_Cells}",
    ha="center",
    color="white",
    fontsize=11
)

plt.tight_layout(rect=(0, 0.06, 1, 0.94))


frame_step = 40

animation_order = [
    completion_order[index]
    for index in range(0, Total_Cells, frame_step)
]

if completion_order[-1] not in animation_order:
    animation_order.append(completion_order[-1])


def update(frame):

    row, column = animation_order[frame]

    completed_count = min(
        (frame + 1) * frame_step,
        Total_Cells
    )

    for finished_row, finished_column in completion_order[
        :completed_count
    ]:
        visible_result[finished_row][finished_column] = (
            result[finished_row][finished_column]
        )

    result_image.set_data(visible_result)

    line_a.set_ydata([row, row])

    line_b.set_xdata([column, column])

    current_cell.set_data(
        [column],
        [row]
    )

    status.set_text(
        f"Computing C[{row}][{column}]    |    "
        f"Completed: {completed_count} / {Total_Cells}"
    )

    return (
        result_image,
        line_a,
        line_b,
        current_cell,
        status
    )


animation = FuncAnimation(
    fig,
    update,
    frames=len(animation_order),
    interval=70,
    repeat=False,
    blit=False,
    cache_frame_data=False
)


# GIF ANIMATION
animation.save(
    "matrix_multiplication.gif",
    writer=PillowWriter(fps=12)
)

print("\nAnimation saved as: matrix_multiplication.gif")

plt.show()
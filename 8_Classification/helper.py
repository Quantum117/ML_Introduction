import numpy as np

def resize(matrix_2D):
    # split to 28x28 blocks and get mean value from each block
    block_size = matrix_2D.shape[0] // 28
    img_resized = matrix_2D[0:block_size * 28, 0:block_size * 28]

    # Convert to NumPy
    img_array = np.array(img_resized)


    # Create the downsampled 28x28 matrix using max pooling
    downsampled = np.zeros((28, 28))

    for i in range(28):
        for j in range(28):
            block = img_array[i*block_size:(i+1)*block_size, j*block_size:(j+1)*block_size]
            downsampled[i, j] = np.mean(block)

    return downsampled

def softmax(x):
    return np.exp(x) / np.exp(x).sum(axis=1, keepdims=True)
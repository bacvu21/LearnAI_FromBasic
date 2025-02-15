### Learn Python from Basics

#### Create a Virtual Environment

1. **Install virtualenv:**

    ```bash
    pip install virtualenv
    ```

2. **Create a virtual environment:**

    ```bash
    virtualenv env
    ```

3. **Activate the virtual environment:**
    - On Windows:

      ```bash
      .\env\Scripts\activate
      ```

    - On macOS and Linux:

      ```bash
      source env/bin/activate
      ```

#### Install numpy

```bash
pip install numpy

- Example for initilize matrix

```import numpy as np
    matrixdefault = [[1, 2], [3, 4]]
    matrx = np.array(matrixdefault)
```

- Example for tranpose matrix

```matrxTran = matrx.T

- Example for normalize matrix 

``` def min_max_normalize(matrix):
    min_val = np.min(matrix)
    max_val = np.max(matrix)
    normalized_matrix = (matrix - min_val) / (max_val - min_val)
    return normalized_matrix

normalized_matrix = min_max_normalize(matrx)
print(normalized_matrix)
```

Feel free to copy this to your README file. If you have any more requests or need further assistance, just let me know!

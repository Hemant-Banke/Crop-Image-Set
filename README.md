# Crop Image Set

Allows you to crop all images in a directory easily.

### Usage

- To Run :
    ```
    python crop.py
    ```

- Specify source directory while executing program
    ```
    Enter image set source : path/
    ```

### Variables

- Change CROP_AREA variable to adjust crop area.
    ```python
    CROP_AREA = ( topleft_x, topleft_y, bottomright_x, bottomright_y )
    ```

- Change destination directory
    ```python
    DEST_DIR = SOURCE_DIR + "crops/"
    ```

# Capturing full Screen Screen shot 

## Importing Modules

```python
import time
import pyscreenshot
```

- The `time` module provides time-related functions.
- The `pyscreenshot` module is used for capturing screenshots.

## Delay Execution

```python
time.sleep(10)
```

- The `time.sleep()` function pauses the script for 10 seconds.

## Capture Screenshot

```python
image = pyscreenshot.grab()
```

- The `pyscreenshot.grab()` function captures the entire screen and stores it in the `image` variable.

## Display Screenshot

```python
image.show()
```

- The `show()` method displays the captured screenshot in the default image viewer.

## Save Screenshot to File

```python
image.save('Screenshot.png')
```

- The `save()` method saves the screenshot to a file named "Screenshot.png".

In summary, this Python script captures a screenshot, displays it, and saves it to a file for various purposes.

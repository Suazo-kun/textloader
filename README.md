# Textloader
Small Python module to display loading animations in the console/terminal.

## Use
```Python
from time import sleep
from textloader import CirculatePointsLoader


if __name__ == "__main__":
    temp = CirculatePointsLoader()
    temp.PrintAsyncAnimation()
    sleep(temp.number_of_characters * temp.animation_delay * 5)
    temp.StopAsyncAnimation()
```

## Documentation
### Class properties and methods
* **number_of_characters** (int) (read). Returns the number of characters in the animation.
* **current_animation** (int) (read). Returns the number of the current character.
* **current_character** (str) (read). Returns the current character.
* **animation_delay** (float) (read/write). Property to specify the time to wait before printing the next character.
* **NextAnimation()** (return str). Returns the next character that corresponds to the animation.
* **PrintAsyncAnimation()**. Print the animation using a thread. NOTE: The thread is set to demonic.
* **StopAsyncAnimation()**. Stops the asynchronous printing of the animation.

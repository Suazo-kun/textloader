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
### class BaseTextLoader()
It is the base class from which all other classes in the code inherit. This class contains all the fundamental methods and properties, the classes that inherit to this super class only modify the property **_animation**, which is a list that contains all the characters that will be printed. Its **_animation** property is empty, so using this class directly will not show any noticeable result, unlike the following classes:

### class CirculatePointsLoader()
Its animation consists of dots that simulate an external rotation.
```Python
_animation = ['⠾', '⠽', '⠻', '⠟', '⠯', '⠷']
```

### class DownPointsLoader()
Its animation consists of dots that simulate falling to complete a 2x3 rectangle.
```Python
_animation = [
    '⠁', '⠂', '⠄', '⡀', '⡈', '⡐', '⡠', '⣀', '⣁', '⣂', '⣄', '⣌', '⣔', '⣤',
    '⣥', '⣦', '⣮', '⣶', '⣷', '⣿', '⣿', '⣿']
```

### class SetPointsLoader()
Its animation consists of setting several points every so often until a 2x3 rectangle is completed.
```Python
_animation = ['⡀', '⡠', '⡢', '⡪', '⡫', '⡻', '⡿', '⣿', '⣿', '⣿']
```

### class RotatePointsLoader()
Its animation consists of dots that simulate an internal rotation.
```Python
_animation = ['⣀', '⡄', '⠆', '⠃', '⠉', '⠘', '⠰', '⢠']
```

### property BaseTextLoader.number_of_characters
An integer that returns the number of characters in the animation.
```Python
from textloader import *
rtl = RotatePointsLoader()
print(rtl.number_of_characters)

# Output: 8
```

### property BaseTextLoader.current_animation
An integer that returns the position of the last returned or printed character.
```Python
from textloader import *

rtl = RotatePointsLoader()
print(rtl.current_animation)
print(rtl.NextAnimation())
print(rtl.NextAnimation())
print(rtl.current_animation)

# Output:
# 0
# ⣀
# ⡄
# 1
```

### property BaseTextLoader.current_character
A string that returns the last returned or printed character.
```Python
from textloader import *

rtl = RotatePointsLoader()
print(rtl.current_character)
rtl.NextAnimation()
rtl.NextAnimation()
print(rtl.current_character)

# Output:
# ⣀
# ⡄
```

### property BaseTextLoader.animation_delay
A float that determines the time to wait before proceeding to the next character. Internally, it is used when **PrintAsyncAnimation** is active. The default value is 0.1.
```Python
from textloader import *

rtl = RotatePointsLoader()
print(rtl.animation_delay)
rtl.animation_delay = 0.5
print(rtl.animation_delay)

# Output:
# 0.1
# 0.5
```

### method BaseTextLoader.NextAnimation()
Return the following character. In case the last character has already been returned, this method will consequently restart the count and return the first character.
```Python
from textloader import *

rtl = RotatePointsLoader()
print(rtl.NextAnimation())
print(rtl.NextAnimation())

# Output:
# ⣀
# ⡄
```

### method BaseTextLoader.PrintAsyncAnimation()
Starts a thread in which the animation will be printed until the **StopAsyncAnimation** method is called or until the program terminates. **NOTE:** The method is executed in a daemon thread to avoid deadlocks when terminating the program without having previously called **StopAsyncAnimation**.
```Python
from textloader import *
from time import sleep

rtl = RotatePointsLoader()
rtl.PrintAsyncAnimation()

sum_result = 0

for i in range(1, 6):
    sleep(0.5)
    sum_result += i

rtl.StopAsyncAnimation()
print(sum_result)

# Output:
# (animation)
# 15
```

### method BaseTextLoader.StopAsyncAnimation()
Stops the call made to **PrintAsyncAnimation**.
```Python
from textloader import *
from time import sleep

rtl = RotatePointsLoader()
rtl.PrintAsyncAnimation()

sum_result = 0

for i in range(1, 6):
    sleep(0.5)
    sum_result += i

rtl.StopAsyncAnimation()
print(sum_result)

# Output:
# (animation)
# 15
```

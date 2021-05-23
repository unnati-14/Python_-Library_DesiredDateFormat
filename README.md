# DesiredDateFormat
This module will convert any format of date into the desired date format 
User need to pass 2 arguments, the first argument will be the date and the second one is the desired date format which the user wants to receive output. 
### for example:
> convert("2021/05/14","dd/mm/yy")
> 
>\>> output would be : 14/05/2021

OR
> convert("2021-05-14","dd-mm-yy")
> 
>\>> output would be : 14-05-2021

OR
#### user doesnt need to pass the date as a string ,user can also pass python inbuilt datetime
### for example: 
> import datetime
> 
> convert(datetime.datetime.now(), "dd-mm-yy")
> 
> and the output would be same as above 
> 
>\>> output: 23-05-2021 (current date : 2021-05-23)

## Installation
  Run the following command to install:
  ```pip install DesiredDateFormat```


## Usage
```
from DesiredDateFormat import convert
import datetime
convert(datetime.datetime.now(), "dd-mm-yy")
>> output: 23-05-2021 (current date : 2021-05-23) 
```

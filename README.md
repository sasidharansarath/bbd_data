# bbd_data
1. Weather Data collection for the project BuiltByData

Weather data using the API from DarkSky.Net https://darksky.net/dev/docs

Dependencies: 

    datetime https://docs.python.org/2/library/datetime.html

    requests http://docs.python-requests.org/en/master/user/quickstart/

    pandas

Steps:

    Get the API key from DarkSky.Net (free for upto 1000 calls per day) https://darksky.net/dev/account

    Get the coordinates for the location where we need the weather data for. https://www.gps-coordinates.net/

    Construct the url using the DarkSky.Net base url, API key, latitude and longitude, as well as time in UNIX format (https://www.tutorialspoint.com/How-to-convert-Python-date-to-Unix-timestamp)

    Get the weather data using requests.get(url) passing in the parameters required https://darksky.net/dev/docs

    Use the pandas json module to convert the data read from the previous step to json format.

    Convert the required data (hourly) to a pandas dataframe

    Format the timestamp into standard format using datetime.datetime.utcfromtimestamp() function

    Select and rearrange the dataframe to have the required data only.

    Write the required data into a CSV file.

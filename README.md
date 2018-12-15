# html_screenshotter
Renders html and screenshots it.

Remember to `pip install pyppeteer`in your py-env.

```
>>> from screen import get_screen
>>> print(get_screen("<h1>It works!</h1>", "./screenshots/test.png"))
./screenshots/test.png
```

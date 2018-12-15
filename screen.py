import asyncio
from datetime import datetime
from glob import glob
import os
from pyppeteer import launch
import random

DEFAULT_EXPORT_DIR = "./screenshots/"
SAMPLE_FILES = glob(os.path.join("sample_pages", "*.htm*"))
SAMPLE_FILE = random.choice(SAMPLE_FILES)
with open(SAMPLE_FILE, "r") as f:
    SAMPLE_HTML = f.read()

async def screen(html, export_filepath=None):
    if export_filepath is None:
        filename = f"{datetime.now()}.png"
        export_filepath = os.path.join(DEFAULT_EXPORT_DIR, filename)
    os.makedirs(os.path.dirname(export_filepath), exist_ok=True)
    browser = await launch()
    page = await browser.newPage()
    await page.setContent(html)
    await page.screenshot({"path": export_filepath})
    return export_filepath

def get_screen(html, export_filepath=None):
    return asyncio.get_event_loop().run_until_complete(screen(html, export_filepath))

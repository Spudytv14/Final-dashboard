import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': 1280, 'height': 800})
        await page.goto(f"file://{os.path.abspath('index.html')}")

        # Give JS a moment to initialize
        await page.wait_for_timeout(1000)

        os.makedirs('/home/jules/verification', exist_ok=True)

        # Take screenshot of overview
        await page.screenshot(path="/home/jules/verification/01_overview.png", full_page=True)

        # Click on AI Tools
        await page.evaluate("switchPage('ai')")
        await page.wait_for_timeout(500)
        await page.screenshot(path="/home/jules/verification/02_tools.png", full_page=True)

        # Click on Library
        await page.evaluate("switchPage('library')")
        await page.wait_for_timeout(500)
        await page.screenshot(path="/home/jules/verification/03_library.png", full_page=True)

        # Click on Games
        await page.evaluate("switchPage('games')")
        await page.wait_for_timeout(500)
        await page.screenshot(path="/home/jules/verification/04_games.png", full_page=True)

        # Click on Users
        await page.evaluate("switchPage('users')")
        await page.wait_for_timeout(500)
        await page.screenshot(path="/home/jules/verification/05_users.png", full_page=True)

        # Click on Revenue
        await page.evaluate("switchPage('revenue')")
        await page.wait_for_timeout(500)
        await page.screenshot(path="/home/jules/verification/06_revenue.png", full_page=True)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())

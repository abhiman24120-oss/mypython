"""
Playwright Sample Script
This script demonstrates basic Playwright usage in Python
"""

import asyncio
from playwright.async_api import async_playwright, Page, Browser, BrowserContext


async def run_example():
    """
    Basic example of using Playwright to automate browser interactions
    """
    async with async_playwright() as p:
        # Launch a browser instance
        browser: Browser = await p.chromium.launch(headless=False)
        
        # Create a new browser context
        context: BrowserContext = await browser.new_context()
        
        # Create a new page
        page: Page = await context.new_page()
        
        # Navigate to a website
        await page.goto("https://example.com")
        
        # Get page title
        title = await page.title()
        print(f"Page title: {title}")
        
        # Take a screenshot
        await page.screenshot(path="example.png")
        
        # Get all text content
        content = await page.content()
        print(f"Page loaded successfully")
        
        # Close resources
        await context.close()
        await browser.close()


async def example_with_interactions():
    """
    Example with user interactions like clicking and typing
    """
    async with async_playwright() as p:
        browser: Browser = await p.chromium.launch()
        page: Page = await browser.new_page()
        
        # Navigate to the website
        await page.goto("https://example.com")
        
        # Example: Find and interact with elements
        # await page.click('button.submit')  # Click a button
        # await page.fill('input[name="search"]', 'Playwright')  # Fill input
        # await page.press('input', 'Enter')  # Press a key
        # await page.wait_for_load_state('networkidle')  # Wait for page to load
        
        # Get specific element text
        # text = await page.text_content('h1')
        # print(f"Heading: {text}")
        
        await browser.close()


async def example_with_assertions():
    """
    Example with assertions for testing
    """
    async with async_playwright() as p:
        browser: Browser = await p.chromium.launch()
        page: Page = await browser.new_page()
        
        # Navigate to the website
        await page.goto("https://example.com")
        
        # Assertion examples
        title = await page.title()
        assert "Example" in title, f"Expected 'Example' in title, got: {title}"
        
        # Check if element exists
        is_visible = await page.is_visible('h1')
        assert is_visible, "H1 element should be visible"
        
        print("All assertions passed!")
        
        await browser.close()


async def example_with_multiple_pages():
    """
    Example with handling multiple pages/tabs
    """
    async with async_playwright() as p:
        browser: Browser = await p.chromium.launch()
        page1: Page = await browser.new_page()
        page2: Page = await browser.new_page()
        
        # Navigate on both pages
        await page1.goto("https://example.com")
        await page2.goto("https://example.com")
        
        title1 = await page1.title()
        title2 = await page2.title()
        
        print(f"Page 1 title: {title1}")
        print(f"Page 2 title: {title2}")
        
        await page1.close()
        await page2.close()
        await browser.close()


async def example_with_error_handling():
    """
    Example with error handling
    """
    async with async_playwright() as p:
        browser: Browser = await p.chromium.launch()
        page: Page = await browser.new_page()
        
        try:
            # Navigate with timeout
            await page.goto("https://example.com", timeout=10000)
            
            # Try to click an element with error handling
            try:
                await page.click('button.nonexistent', timeout=1000)
            except Exception as e:
                print(f"Element not found: {e}")
            
            await browser.close()
        except Exception as e:
            print(f"Error during navigation: {e}")
            await browser.close()


if __name__ == "__main__":
    # Run the basic example
    asyncio.run(run_example())
    
    # Uncomment to run other examples:
    # asyncio.run(example_with_interactions())
    # asyncio.run(example_with_assertions())
    # asyncio.run(example_with_multiple_pages())
    # asyncio.run(example_with_error_handling())

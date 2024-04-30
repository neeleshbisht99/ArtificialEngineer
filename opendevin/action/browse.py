import os
import base64
from dataclasses import dataclass
from opendevin.observation import BrowserOutputObservation
from opendevin.schema import ActionType
from typing import TYPE_CHECKING
from playwright.async_api import async_playwright

from .base import ExecutableAction

if TYPE_CHECKING:
    from opendevin.controller import AgentController


@dataclass
class BrowseURLAction(ExecutableAction):
    url: str
    action: str = ActionType.BROWSE

    async def run(self, controller:'AgentController') -> BrowserOutputObservation:
        asked_url = self.url
        if not asked_url.startswith('http'):
            asked_url = os.path.abspath(os.curdir) + self.url
        
        try:
            async with async_playwright() as p:
                browser = await p.chromium.launch()
                page = browser.new_page()
                response = await page.goto(asked_url)

                inner_text = await page.evaluate('() => document.body.innerText')
                screenshot_bytes = await page.screenshot(full_page=True)
                await browser.close()
                
                screenshot_base64 = base64.b64encode(screenshot_bytes).decode('utf-8')
                return BrowserOutputObservation(
                    content=inner_text,
                    screenshot=screenshot_base64,
                    url=asked_url,
                    status_code=response.status if response else 0
                )

        except Exception as e:
            return BrowserOutputObservation(
                content=str(e),
                screenshot='',
                error=True,
                url=asked_url
            )


    @property
    def message(self) -> str:
        return f'Browsing URL: {self.url}'
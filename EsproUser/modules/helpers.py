import httpx
import asyncio
import json
import random
import time

class RequestCore:
    def __init__(self, timeout: int = 10, retries: int = 3, proxy=None):
        self.timeout = timeout
        self.retries = retries
        self.proxy = proxy  # Proxy ka support hata diya gaya hai

    async def asyncPostRequest(self, url: str, data: dict, headers: dict = {}):
        """POST request using httpx.AsyncClient without 'proxies' parameter"""
        async with httpx.AsyncClient() as client:  # << PROXY ARGUMENT HATA DIYA
            for attempt in range(self.retries):
                try:
                    response = await client.post(url, json=data, headers=headers, timeout=self.timeout)
                    if response.status_code == 200:
                        return response.json()
                except httpx.HTTPStatusError as e:
                    print(f"HTTP error on attempt {attempt+1}: {e}")
                except Exception as e:
                    print(f"Request failed: {e}")
                await asyncio.sleep(random.uniform(1, 3))
        return None

    async def asyncGetRequest(self, url: str, headers: dict = {}):
        """GET request using httpx.AsyncClient without 'proxies' parameter"""
        async with httpx.AsyncClient() as client:  # << PROXY ARGUMENT HATA DIYA
            for attempt in range(self.retries):
                try:
                    response = await client.get(url, headers=headers, timeout=self.timeout)
                    if response.status_code == 200:
                        return response.json()
                except httpx.HTTPStatusError as e:
                    print(f"HTTP error on attempt {attempt+1}: {e}")
                except Exception as e:
                    print(f"Request failed: {e}")
                await asyncio.sleep(random.uniform(1, 3))
        return None

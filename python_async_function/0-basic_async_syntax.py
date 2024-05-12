#!/usr/bin/env python3
"""Async"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Waits random time and returns that random number"""
    a = random.uniform(0, max_delay)
    await asyncio.sleep(a)
    return a
import asyncio
import logging

import flet as ft

from app.config import APP_NAME
from app.logging_config import report_async_error
from app.ui.home import home_view

logger = logging.getLogger(__name__)


def report_page_error(event: ft.Event[ft.Page]) -> None:
    logger.error("Unhandled Flet error: %s", event.data)


async def main(page: ft.Page) -> None:
    asyncio.get_running_loop().set_exception_handler(report_async_error)
    page.on_error = report_page_error
    page.title = APP_NAME
    page.padding = 24
    page.scroll = ft.ScrollMode.AUTO
    page.add(home_view())
    logger.info("Application ready")
    logger.debug("Page initialization complete")

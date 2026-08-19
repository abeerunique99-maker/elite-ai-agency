import logging
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
import httpx

logger = logging.getLogger(__name__)

api_retry = retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=10),
    retry=retry_if_exception_type((
        httpx.TimeoutException,
        httpx.HTTPStatusError,
        ConnectionError,
    )),
    before_sleep=lambda retry_state: logger.warning(f"إعادة المحاولة بسبب خطأ في الشبكة. المحاولة رقم: {retry_state.attempt_number}")
)
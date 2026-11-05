"""COMMUNICATE accepts numbers written in Indic (and other) native digits."""

import pytest

from tau2.data_model.message import AssistantMessage
from tau2.evaluator.evaluator_communicate import CommunicateEvaluator, normalize_digits


@pytest.mark.parametrize(
    "content",
    [
        "total is 1,628",          # ASCII, unchanged behaviour
        "आपका कुल ₹१६२८ है",        # Devanagari
        "মোট ১,৬২৮ ডলার",           # Bengali
        "کل ۱۶۲۸ ڈالر",             # Extended Arabic-Indic (Urdu)
        "ਕੁੱਲ ੧੬੨੮",                # Gurmukhi
        "மொத்தம் ௧௬௨௮",            # Tamil
    ],
)
def test_native_digits_match(content):
    checks = CommunicateEvaluator.evaluate_communicate_info(
        [AssistantMessage(role="assistant", content=content)], ["1628"]
    )
    assert checks[0].met


def test_wrong_number_still_fails():
    checks = CommunicateEvaluator.evaluate_communicate_info(
        [AssistantMessage(role="assistant", content="total १२६८")], ["1628"]
    )
    assert not checks[0].met


def test_ascii_text_unchanged():
    assert normalize_digits("Order #W2378156, $1,000") == "Order #W2378156, $1,000"

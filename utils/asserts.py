from typing import Any

import allure
from jsonschema import validate
from jsonschema.validators import Draft202012Validator

from utils.logger import get_logger

logger = get_logger("ASSERT")


@allure.step("Проверка статус код равен {expected}")
def assert_status_code(expected: int, actual: int) -> None:
    """"
    Проверяет, что фактический статус-код ответа соответствует ожидаемому.

    :param expected: Ожидаемый статус-код.
    :param actual: Фактический статус-код ответа.
    :raises AssertionError: Если статус-коды не совпадают.
    """
    logger.info(f"Check that response status code equals to {expected}")
    assert actual == expected, f"Не верный статус код. exp:{expected}, act:{actual}"


@allure.step("Проверка соответствия JSON-схеме")
def validate_json_schema(instance: Any, schema: dict) -> None:
    """
    Проверяет, соответствует ли JSON-объект (instance) заданной JSON-схеме (schema).

    :param instance: JSON-данные, которые нужно проверить.
    :param schema: Ожидаемая JSON-schema.
    :raises jsonschema.exceptions.ValidationError: Если instance не соответствует schema.
    """
    logger.info("Check that response response JSON-schema is valid ")
    validate(
        schema=schema,
        instance=instance,
        format_checker=Draft202012Validator
    )

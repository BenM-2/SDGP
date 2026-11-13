"""
@Author:        Ben Marples
@Date:          13/11/2026
@Name:          test_algorithm_errors.py
@Description:   Tests for all errors to check they work
"""


import pytest 
from delivery.errors.errors import (
    AlgorithmError,
    AlgorithmErrorCode,
)

class Test_algorithm_erros:

    @pytest.mark.parametrize("code", list(AlgorithmErrorCode))
    def test_all_codes(self, code):
        with pytest.raises(AlgorithmError) as exc_info:
            raise AlgorithmError(code)

        assert exc_info.value.error is code
        assert exc_info.value.message == code.name


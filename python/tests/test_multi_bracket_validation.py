import pytest
from challenges.multi_bracket_validation.multi_bracket_validation import multi_bracket_validation as mbv


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ('{}', True),
        ('{}(){}', True),
        ('()[[Extra Characters]]', True),
        ('(){}[[]]', True),
        ('{}{Code}[Fellows](())', True),
        ('[({}]', False),
        ('(](', False),
        ('{(})', False),
        ('{', False),
        (')', False),
        ('[}', False)
    ]
)
def test_multi_bracket_validation_all(test_input, expected):
  actual = mbv(test_input)
  assert actual == expected
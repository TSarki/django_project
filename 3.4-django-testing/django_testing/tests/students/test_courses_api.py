import pytest

from rest_framework.test import APIClient


@pytest.mark.django_db
def test_example():
    assert 2==2

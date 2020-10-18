import pytest

from random import randint
from faker import Faker
from splinter import Browser


@pytest.fixture(scope='session', autouse=True)
def faker_seed():
    return randint(1,50000)


def test_login_non_existing_user(faker):
    with Browser('firefox') as browser:
        first = faker.first_name()
        last = faker.last_name()

        browser.visit('http://127.0.0.1:5000')
        browser.find_by_id('email').type('{}@{}.com'.format(first, last))
        browser.find_by_id('password').type('{}{}'.format(last, first))
        browser.find_by_id('loginbutton').click()
        assert browser.is_text_present('New around here?')


def test_register_user():
    with Browser('firefox') as browser:
        browser.visit('http://127.0.0.1:5000')
        browser.find_by_id('registerbutton').click()

        browser.find_by_id('email').type('qwe@qwe.com')
        browser.find_by_id('password').type('sup3rs3cr3t')
        browser.find_by_id('registerbutton').click()
        assert browser.is_text_present('New around here?')


def test_login_registered_user():
    with Browser('firefox') as browser:
        browser.visit('http://127.0.0.1:5000')
        browser.find_by_id('email').type('qwe@qwe.com')
        browser.find_by_id('password').type('sup3rs3cr3t')
        browser.find_by_id('loginbutton').click()
        assert browser.is_text_present('You\'ve been logged in!')


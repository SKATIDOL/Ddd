from http import HTTPStatus

from django.test import Client, TestCase

import parameterized


class StaticURLTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, HTTPStatus.OK)


class StaticURL(TestCase):
    @parameterized.parameterized.expand([
        ('0', HTTPStatus.OK),
        ('1', HTTPStatus.OK),
        ('01', HTTPStatus.OK),
        ('010', HTTPStatus.OK),
        ('10', HTTPStatus.OK),
        ('100', HTTPStatus.OK),
        ('abcd', HTTPStatus.NOT_FOUND),
        ('aa4a', HTTPStatus.NOT_FOUND),
        ('232%', HTTPStatus.NOT_FOUND),
        ('-0', HTTPStatus.NOT_FOUND),
        ('-1', HTTPStatus.NOT_FOUND),
        ('0193920100101jsjdhdbs$$$', HTTPStatus.NOT_FOUND),
    ])
    def test_catalog_fff(self, fff, expected_status):
        status_code = Client().get(f'/catalog/{fff}/').status_code
        self.assertEqual(
            status_code,
            expected_status,
            msg=f'/catalog/{fff}/ get not {expected_status}',
        )


class StaticURLTest(TestCase):
    @parameterized.parameterized.expand([
        ('0', HTTPStatus.NOT_FOUND),
        ('1', HTTPStatus.OK),
        ('01', HTTPStatus.NOT_FOUND),
        ('010', HTTPStatus.NOT_FOUND),
        ('10', HTTPStatus.OK),
        ('100', HTTPStatus.OK),
        ('abcd', HTTPStatus.NOT_FOUND),
        ('aa4a', HTTPStatus.NOT_FOUND),
        ('232%', HTTPStatus.NOT_FOUND),
        ('-0', HTTPStatus.NOT_FOUND),
        ('-1', HTTPStatus.NOT_FOUND),
    ])
    def test_catalog_rrr(self, rrr, expected_status):
        status_code = Client().get(f'/catalog/re/{rrr}/').status_code
        self.assertEqual(
            status_code,
            expected_status,
            msg=f'/catalog/re/{rrr}/ get not {expected_status}',
        )


class StaticUrlTest(TestCase):
    @parameterized.parameterized.expand([
        ('0', HTTPStatus.NOT_FOUND),
        ('1', HTTPStatus.OK),
        ('01', HTTPStatus.NOT_FOUND),
        ('010', HTTPStatus.NOT_FOUND),
        ('10', HTTPStatus.OK),
        ('100', HTTPStatus.OK),
        ('abcd', HTTPStatus.NOT_FOUND),
        ('aa4a', HTTPStatus.NOT_FOUND),
        ('232%', HTTPStatus.NOT_FOUND),
        ('-0', HTTPStatus.NOT_FOUND),
        ('-1', HTTPStatus.NOT_FOUND),
        ('0193920100101jsjdhdbs$$$', HTTPStatus.NOT_FOUND),
    ])
    def test_catalog_re(self, re, expected_status):
        status_code = Client().get(f'/catalog/converter/{re}/').status_code
        self.assertEqual(
            status_code,
            expected_status,
            msg=f'/catalog/converter/{re}/ get not {expected_status}',
        )

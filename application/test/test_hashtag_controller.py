# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from application.models.request import Request  # noqa: E501
from application.models.result import Result  # noqa: E501
from application.test import BaseTestCase


class TestHashtagController(BaseTestCase):
    """HashtagController integration test stubs"""

    def test_compute_popularity(self):
        """Test case for detect_requirement

        Retrieve a list with values for given set of requirements indicating their confidence for the crowd on twitter.
        """
        body = [Request()]
        response = self.client.open(
            '/v1/confidence',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

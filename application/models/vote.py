# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401
from typing import List, Dict  # noqa: F401
from application.models.base_model_ import Model
from application.util import util


class Vote(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, stakeholder_id: int, rating: int, weight: float, confidence: float):  # noqa: E501
        """Requirement - a model defined in Swagger
        """
        self.swagger_types = {
            'stakeholder_id': int,
            'rating': int,
            'weight': float,
            'confidence': float
        }

        self.attribute_map = {
            'stakeholder_id': 'stakeholder_id',
            'rating': 'rating',
            'weight': 'weight',
            'confidence': 'confidence'
        }

        self._stakeholder_id = stakeholder_id
        self._rating = rating
        self._weight = weight
        self._confidence = confidence

    @classmethod
    def from_dict(cls, dikt) -> 'Vote':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Request of this Request.  # noqa: E501
        :rtype: Request
        """
        return Vote(dikt["stakeholder_id"], dikt["rating"], dikt["weight"], dikt["confidence"])

    @property
    def stakeholder_id(self) -> int:
        """Gets the id of the stakeholder.


        :return: The id of the stakeholder.
        :rtype: int
        """
        return self._stakeholder_id

    @stakeholder_id.setter
    def stakeholder_id(self, stakeholder_id: int):
        """Sets the id of the stakeholder.


        :param stakeholder_id: The id of the stakeholder.
        :type stakeholder_id: int
        """

        self._stakeholder_id = stakeholder_id

    @property
    def rating(self) -> int:
        """Gets the rating of this vote.


        :return: The rating of this vote.
        :rtype: int
        """
        return self._rating

    @rating.setter
    def rating(self, rating: int):
        """Sets the rating of this vote.


        :param rating: The rating of this vote.
        :type rating: int
        """

        self._rating = rating

    @property
    def weight(self) -> float:
        """Gets the weight of the voter.


        :return: The weight of the voter.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight: float):
        """Sets the weight of the voter.


        :param weight: The weight of the voter.
        :type weight: int
        """

        self._weight = weight

    @property
    def confidence(self) -> float:
        """Gets the confidence of the vote.


        :return: The confidence of this vote.
        :rtype: int
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence: float):
        """Sets the confidence of this vote.


        :param confidence: The confidence of the voter.
        :type confidence: int
        """

        self._confidence = confidence

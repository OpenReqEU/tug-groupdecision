# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401
from typing import List, Dict  # noqa: F401
from application.models.base_model_ import Model
from application.util import util
from application.models.conflict import Conflict


class Result(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, utility: float, conflicts: List[Conflict]):  # noqa: E501
        """Result - a model defined in Swagger

        :param utility: The utility value.  # noqa: E501
        :type utility: float
        :param conflicts: The list of conflicts.  # noqa: E501
        :type conflicts: List[Conflict]
        """
        self.swagger_types = {
            'utility': float,
            'conflicts': List[Conflict]
        }

        self.attribute_map = {
            'utility': 'utility',
            'conflicts': 'conflicts'
        }

        self._utility = utility
        self._conflicts = conflicts

    @classmethod
    def from_dict(cls, dikt) -> 'Result':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Result of this Result.  # noqa: E501
        :rtype: Result
        """
        return util.deserialize_model(dikt, cls)

    @property
    def utility(self) -> float:
        """Gets the utility.


        :return: The utility.
        :rtype: float
        """
        return self._utility

    @utility.setter
    def utility(self, utility: utility):
        """Sets the utility.


        :param utility: The utility.
        :type utility: float
        """

        self._utility = utility

    @property
    def conflicts(self) -> List[Conflict]:
        """Gets the list of conflicts


        :return: The list of conflicts.
        :rtype: List[Conflict]
        """
        return self._conflicts

    @conflicts.setter
    def conflicts(self, conflicts: List[Conflict]):
        """Sets the confidence value


        :param conflicts: The conflicts value.
        :type conflicts: List[Conflict]
        """

        self._conflicts = conflicts
import connexion
import six
from application.models.request import Request  # noqa: E501
from application.models.result import Result  # noqa: E501
from application.models.conflict import Conflict  # noqa: E501
from application.preprocessing import preprocessing


def detect_requirement(body):  # noqa: E501
    """
     # noqa: E501

    :param body: Text segments
    :type body: list

    :rtype: List[Result]
    """
    response = None
    if connexion.request.is_json:
        content = connexion.request.get_json()
        request = Request.from_dict(content)  # noqa: E501

        # compute utility value
        if request.aggregation_function.upper() == "WEIGHTED_AVG":
            numerator = 0.0
            denominator = 0.0
            for v in request.votes:
                numerator += v.rating * v.weight * v.confidence
                denominator += v.weight * v.confidence
            utility_value = numerator / denominator if denominator > 0.0 else 0.0
        elif request.aggregation_function.upper() == "LEAST_MISERY":
            utility_value = min(map(lambda v: v.rating, request.votes))
        else:
            utility_value = 0.0

        # determine conflicts
        RANGE_WIDTH = 5.0
        conflicts = []
        for v1 in request.votes:
            for v2 in request.votes:
                distance = float(abs(v1.rating - v2.rating))
                if distance >= (RANGE_WIDTH / 2.0):
                    conflicts += [Conflict(from_id=v1.stakeholder_id, to_id=v2.stakeholder_id, distance=distance)]

        response = Result(utility=float("{0:.2f}".format(utility_value)), conflicts=conflicts)

    return response


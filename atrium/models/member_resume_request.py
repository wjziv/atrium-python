# coding: utf-8

"""
    MX API

    The MX Atrium API supports over 48,000 data connections to thousands of financial institutions. It provides secure access to your users' accounts and transactions with industry-leading cleansing, categorization, and classification.  Atrium is designed according to resource-oriented REST architecture and responds with JSON bodies and HTTP response codes.  Use Atrium's development environment, vestibule.mx.com, to quickly get up and running. The development environment limits are 100 users, 25 members per user, and access to the top 15 institutions. Contact MX to purchase production access.   # noqa: E501
"""


import pprint
import re  # noqa: F401

import six

from atrium.models.credential_request import CredentialRequest  # noqa: F401,E501


class MemberResumeRequest(object):


    """
    Attributes:
      mx_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    mx_types = {
        'challenges': 'list[CredentialRequest]'
    }

    attribute_map = {
        'challenges': 'challenges'
    }

    def __init__(self, challenges=None):  # noqa: E501

        self._challenges = None
        self.discriminator = None

        if challenges is not None:
            self.challenges = challenges

    @property
    def challenges(self):
        """Gets the challenges of this MemberResumeRequest.  # noqa: E501


        :return: The challenges of this MemberResumeRequest.  # noqa: E501
        :rtype: list[CredentialRequest]
        """
        return self._challenges

    @challenges.setter
    def challenges(self, challenges):
        """Sets the challenges of this MemberResumeRequest.


        :param challenges: The challenges of this MemberResumeRequest.  # noqa: E501
        :type: list[CredentialRequest]
        """

        self._challenges = challenges

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.mx_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(MemberResumeRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MemberResumeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

"""
    MX API

    The MX Atrium API supports over 48,000 data connections to thousands of financial institutions. It provides secure access to your users' accounts and transactions with industry-leading cleansing, categorization, and classification.  Atrium is designed according to resource-oriented REST architecture and responds with JSON bodies and HTTP response codes.  Use Atrium's development environment, vestibule.mx.com, to quickly get up and running. The development environment limits are 100 users, 25 members per user, and access to the top 15 institutions. Contact MX to purchase production access.   # noqa: E501
"""


from __future__ import absolute_import

import unittest

import atrium-python
from atrium-python.api.members_api import MembersApi  # noqa: E501
from atrium-python.rest import ApiException


class TestMembersApi(unittest.TestCase):
    """MembersApi unit test stubs"""

    def setUp(self):
        self.api = atrium-python.api.members_api.MembersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_aggregate_member(self):
        """Test case for aggregate_member

        Aggregate member  # noqa: E501
        """
        pass

    def test_create_member(self):
        """Test case for create_member

        Create member  # noqa: E501
        """
        pass

    def test_delete_member(self):
        """Test case for delete_member

        Delete member  # noqa: E501
        """
        pass

    def test_list_member_accounts(self):
        """Test case for list_member_accounts

        List member accounts  # noqa: E501
        """
        pass

    def test_list_member_credentials(self):
        """Test case for list_member_credentials

        List member credentials  # noqa: E501
        """
        pass

    def test_list_member_mfa_challenges(self):
        """Test case for list_member_mfa_challenges

        List member MFA challenges  # noqa: E501
        """
        pass

    def test_list_member_transactions(self):
        """Test case for list_member_transactions

        List member transactions  # noqa: E501
        """
        pass

    def test_list_members(self):
        """Test case for list_members

        List members  # noqa: E501
        """
        pass

    def test_read_member(self):
        """Test case for read_member

        Read member  # noqa: E501
        """
        pass

    def test_read_member_status(self):
        """Test case for read_member_status

        Read member connection status  # noqa: E501
        """
        pass

    def test_resume_member(self):
        """Test case for resume_member

        Resume aggregation from MFA  # noqa: E501
        """
        pass

    def test_update_member(self):
        """Test case for update_member

        Update member  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
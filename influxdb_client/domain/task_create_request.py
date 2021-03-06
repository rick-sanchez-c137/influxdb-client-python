# coding: utf-8

"""
    Influx API Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class TaskCreateRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'type': 'str',
        'org_id': 'str',
        'org': 'str',
        'status': 'TaskStatusType',
        'flux': 'str',
        'description': 'str'
    }

    attribute_map = {
        'type': 'type',
        'org_id': 'orgID',
        'org': 'org',
        'status': 'status',
        'flux': 'flux',
        'description': 'description'
    }

    def __init__(self, type=None, org_id=None, org=None, status=None, flux=None, description=None):  # noqa: E501
        """TaskCreateRequest - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._org_id = None
        self._org = None
        self._status = None
        self._flux = None
        self._description = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if org_id is not None:
            self.org_id = org_id
        if org is not None:
            self.org = org
        if status is not None:
            self.status = status
        self.flux = flux
        if description is not None:
            self.description = description

    @property
    def type(self):
        """Gets the type of this TaskCreateRequest.  # noqa: E501

        The type of task, this can be used for filtering tasks on list actions.  # noqa: E501

        :return: The type of this TaskCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TaskCreateRequest.

        The type of task, this can be used for filtering tasks on list actions.  # noqa: E501

        :param type: The type of this TaskCreateRequest.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def org_id(self):
        """Gets the org_id of this TaskCreateRequest.  # noqa: E501

        The ID of the organization that owns this Task.  # noqa: E501

        :return: The org_id of this TaskCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this TaskCreateRequest.

        The ID of the organization that owns this Task.  # noqa: E501

        :param org_id: The org_id of this TaskCreateRequest.  # noqa: E501
        :type: str
        """

        self._org_id = org_id

    @property
    def org(self):
        """Gets the org of this TaskCreateRequest.  # noqa: E501

        The name of the organization that owns this Task.  # noqa: E501

        :return: The org of this TaskCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._org

    @org.setter
    def org(self, org):
        """Sets the org of this TaskCreateRequest.

        The name of the organization that owns this Task.  # noqa: E501

        :param org: The org of this TaskCreateRequest.  # noqa: E501
        :type: str
        """

        self._org = org

    @property
    def status(self):
        """Gets the status of this TaskCreateRequest.  # noqa: E501


        :return: The status of this TaskCreateRequest.  # noqa: E501
        :rtype: TaskStatusType
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TaskCreateRequest.


        :param status: The status of this TaskCreateRequest.  # noqa: E501
        :type: TaskStatusType
        """

        self._status = status

    @property
    def flux(self):
        """Gets the flux of this TaskCreateRequest.  # noqa: E501

        The Flux script to run for this task.  # noqa: E501

        :return: The flux of this TaskCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._flux

    @flux.setter
    def flux(self, flux):
        """Sets the flux of this TaskCreateRequest.

        The Flux script to run for this task.  # noqa: E501

        :param flux: The flux of this TaskCreateRequest.  # noqa: E501
        :type: str
        """
        if flux is None:
            raise ValueError("Invalid value for `flux`, must not be `None`")  # noqa: E501

        self._flux = flux

    @property
    def description(self):
        """Gets the description of this TaskCreateRequest.  # noqa: E501

        An optional description of the task.  # noqa: E501

        :return: The description of this TaskCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TaskCreateRequest.

        An optional description of the task.  # noqa: E501

        :param description: The description of this TaskCreateRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TaskCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

from typing import cast

import pytest
from django.utils import timezone
from rest_framework import status

from posthog.test.base import APIBaseTest

# Testing enterprise properties of feature flags here.


@pytest.mark.ee
class TestFeatureFlagApi(APIBaseTest):
    def test_create_action_update_delete_tags(self):
        from ee.models.license import License, LicenseManager

        super(LicenseManager, cast(LicenseManager, License.objects)).create(
            key="key_123", plan="enterprise", valid_until=timezone.datetime(2038, 1, 19, 3, 14, 7), max_users=3,
        )

        response = self.client.post(
            f"/api/projects/{self.team.id}/feature_flags/", {"name": "Feature", "key": "nice-feature"}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()["tags"], [])

        response = self.client.patch(
            f"/api/projects/{self.team.id}/feature_flags/{response.json()['id']}",
            {"key": "nice-feature", "tags": ["hello", "random"]},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["tags"], ["hello", "random"])

        response = self.client.patch(
            f"/api/projects/{self.team.id}/feature_flags/{response.json()['id']}", {"key": "nice-feature", "tags": []}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["tags"], [])

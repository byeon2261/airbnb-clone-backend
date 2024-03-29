from rest_framework.test import APITestCase
from . import models
from users.models import User


class TestAmenities(APITestCase):

    NAME = "Amenity test"
    DESC = "Amenity Des"

    AMENITIES_URL = "/api/v2/rooms/amenities/"

    def setUp(self):
        models.Amenity.objects.create(
            name=self.NAME,
            description=self.DESC,
        )

    def test_all_amenities(self):
        response = self.client.get(self.AMENITIES_URL)

        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
            "Response status code isn't 200.",
        )
        self.assertIsInstance(
            data,
            list,
            "data isn't list instance.",
        )
        self.assertEqual(
            len(data),
            1,
            "data is not once.",
        )
        self.assertEqual(
            data[0]["name"],
            self.NAME,
            "Name isn't coincide",
        )
        self.assertEqual(
            data[0]["description"],
            self.DESC,
            "Description isn't coincide",
        )

    def test_create_amenity(self):

        new_amenity_name = "New Amenity"
        new_amenity_description = "New Amenity desc."

        response = self.client.post(
            self.AMENITIES_URL,
            data={
                "name": new_amenity_name,
                "description": new_amenity_description,
            },
        )
        self.assertEqual(
            response.status_code,
            200,
            "Create Failed.",
        )

        data = response.json()
        self.assertEqual(
            len(data),
            2,
            "data isn't twice.",
        )
        self.assertEqual(
            data["name"],
            new_amenity_name,
            "name isn't coincide.",
        )
        self.assertEqual(
            data["description"],
            new_amenity_description,
            "description isn't coincide.",
        )

        response = self.client.post(self.AMENITIES_URL)
        data = response.json()

        self.assertEqual(
            response.status_code,
            400,
            "Post name is 필수",
        )
        self.assertIn(
            "name",
            data,
        )


class TestAmenity(APITestCase):

    NAME = "amenity test"
    DESC = "test Amenity dsc."

    AMENITY_URL = "/api/v2/rooms/amenities/"

    def setUp(self):
        models.Amenity.objects.create(
            name=self.NAME,
            description=self.DESC,
        )

    def test_amenity_not_found(self):
        response = self.client.get(f"{self.AMENITY_URL}2/")

        self.assertEqual(response.status_code, 404)

    def test_get_amenity(self):
        response = self.client.get(f"{self.AMENITY_URL}1/")

        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(data["name"], self.NAME)
        self.assertEqual(data["description"], self.DESC)

    def test_put_amenity(self):

        PUT_NAME = "put name"

        response = self.client.put(
            f"{self.AMENITY_URL}1/",
            data={"name": PUT_NAME},
        )

        self.assertEqual(
            response.status_code,
            200,
            "Put amenity is Failed.",
        )

        data = response.json()

        self.assertEqual(
            data["name"],
            PUT_NAME,
            "put name is PUT_NAME",
        )

    def test_delete_amenity(self):
        response = self.client.delete(f"{self.AMENITY_URL}1/")

        self.assertEqual(response.status_code, 204)


class TestRooms(APITestCase):

    URL = "/api/v2/rooms/"

    def test_create_room_not_login(self):
        response = self.client.post(self.URL)

        self.assertEqual(response.status_code, 401)

    def test_create_room(self):
        user = User.objects.create(
            username="test",
        )
        # user.set_password("123")
        # user.save()

        self.client.force_login(
            user,
        )

        response = self.client.post(self.URL)

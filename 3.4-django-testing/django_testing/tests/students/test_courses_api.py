import pytest
from model_bakery import baker
import json
import os

from rest_framework.test import APIClient
from students.models import Student, Course


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def course( *args, **kwargs):
    return baker.make(Course,  *args, **kwargs)


@pytest.fixture
def courses( *args, **kwargs):
    return baker.make(Course,  _quantity = 10)


@pytest.fixture
def student( *args, **kwargs):
    return baker.make(Student, *args, **kwargs)


@pytest.mark.django_db
def test_courses_urls(course, client):
    response = client.get(f'/api/v1/courses/{course.id}/')
    assert response.status_code == 200
    assert response.data['id'] == course.id
    
    
@pytest.mark.django_db
def test_courses_list(courses, client):
    response = client.get(f'/api/v1/courses/')
    assert response.status_code == 200
    assert len(response.data) == len(courses)
    
    
@pytest.mark.django_db
def test_courses_filter_id(courses, client):
    cour = courses[0]
    response = client.get(f'/api/v1/courses/?id={cour.id}')
    assert response.status_code == 200
    assert response.data[0]['id'] == cour.id
    
    
@pytest.mark.django_db
def test_courses_filter_name(courses, client):
    cour = courses[0]
    response = client.get(f'/api/v1/courses/?name={cour.name}')
    assert response.status_code == 200
    assert response.data[0]['name'] == cour.name


@pytest.mark.django_db
def test_course_create(student, api_client):
    course_data = {
        "name": "Test Course",
        "students": [student.id],
    }
    response = api_client.post("/api/v1/courses/", data=course_data)
    assert response.status_code == 201
    assert Course.objects.filter(name="Test Course").exists()
    

@pytest.mark.django_db
def test_course_update(course, api_client, student):
    course_data = {
        "name": "Updated Test Course",
        "students": [student.id],
    }
    response = api_client.put(f"/api/v1/courses/{course.id}/", data=course_data)
    assert response.status_code == 200
    assert response.data['name'] == "Updated Test Course"
    
    
@pytest.mark.django_db
def test_course_delete(course, api_client):
    response = api_client.delete(f"/api/v1/courses/{course.id}/")
    assert response.status_code == 204
    assert not Course.objects.filter(id=course.id).exists()

import requests
from django.http import JsonResponse
from django.conf import settings


def get_data(request):
    try:
        headers = {
            "Authorization": f"Bearer {settings.GLAM_API_KEY}",  # ✅ Must include Bearer token
            "Content-Type": "application/json",  # Required for POST/PUT
            "Accept": "application/json",  # Ensures JSON response
        }

        response = requests.get(
            "https://api.glam.ai/api/v1/filters",
            headers=headers,
            timeout=10,
        )
        response.raise_for_status()  # Raises HTTPError for bad responses (4XX, 5XX)
        return JsonResponse(response.json())

    except requests.exceptions.RequestException as e:
        return JsonResponse(
            {"error": f"API request failed: {str(e)}"},
            status=500,
        )
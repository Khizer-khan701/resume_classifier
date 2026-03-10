import logging
import traceback
from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings

logger = logging.getLogger(__name__)

class GlobalErrorHandlingMiddleware:
    """
    Middleware to catch unhandled exceptions across the project,
    log them with full tracebacks, and return user-friendly responses.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
            return response
        except Exception as e:
            return self.process_exception(request, e)

    def process_exception(self, request, exception):
        # Log the full error for the developer
        error_msg = f"Unhandled Exception: {str(exception)}"
        logger.error(f"{error_msg}\n{traceback.format_exc()}")

        # Check if the request was an AJAX/JSON request
        if request.headers.get('x-requested-with') == 'XMLHttpRequest' or \
           request.content_type == 'application/json':
            return JsonResponse({
                'status': 'error',
                'message': 'An internal server error occurred. Please try again later.',
                'error_detail': str(exception) if settings.DEBUG else None
            }, status=500)

        # For standard browser requests, render a friendly error page
        context = {
            'error_message': str(exception),
            'debug': settings.DEBUG
        }
        return render(request, 'common/error_500.html', context, status=500)

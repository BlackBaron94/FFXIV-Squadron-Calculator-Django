from datetime import datetime


def footer_info(request):
    return {
        'current_year': datetime.now().year
    }
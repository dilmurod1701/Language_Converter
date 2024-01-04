from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

from .models import File
from .serializers import FileSerializer


latin_letter = {
            'А': 'A', 'Б': 'B', 'Ц': 'C', 'Д': 'D', 'Е': 'E', 'Ф': 'F', 'Г': 'G', 'Х': 'H', 'И': 'I', 'Й': 'Y',
            'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'К': 'Q', 'Р': 'R', 'С': 'S', 'Т': 'T',
            'У': 'U', 'В': 'V', 'Ш': 'Sh', 'Х': 'X', 'Ј': 'Y', 'З': 'Z',
            'а': 'a', 'б': 'b', 'ц': 'c', 'д': 'd', 'е': 'e', 'ф': 'f', 'г': 'g', 'х': 'h', 'и': 'i', 'й': 'y',
            'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'к': 'k', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'в': 'v', 'ш': 'sh', 'x': 'x', 'ј': 'y', 'з': 'z', 'ё': 'yo', 'ў': "o'", 'ь': ''
        }

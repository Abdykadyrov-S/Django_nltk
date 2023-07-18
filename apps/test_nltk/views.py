from rest_framework.views import APIView
from rest_framework.response import Response
from nltk.corpus import wordnet
import nltk
from .serializers import SynonymSerializer, AntonymSerializer

class SynonymView(APIView):
    serializer_class = SynonymSerializer

    def post(self, request, format=None):
        word = request.data.get('word', '')
        synonyms = []
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                synonyms.append(lemma.name())
                if len(synonyms) >= 4:
                    break
            if len(synonyms) >= 4:
                break
        serializer = SynonymSerializer(data={'word': word, 'synonyms': synonyms[:4]})
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class AntonymView(APIView):
    serializer_class = AntonymSerializer

    def post(self, request, format=None):
        word = request.data.get('word', '')
        antonyms = []
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                if lemma.antonyms():
                    antonyms.append(lemma.antonyms()[0].name())
                    if len(antonyms) >= 4:
                        break
            if len(antonyms) >= 4:
                break
        serializer = AntonymSerializer(data={'word': word, 'antonyms': antonyms[:4]})
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

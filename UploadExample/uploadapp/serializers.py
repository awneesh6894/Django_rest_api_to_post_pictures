from rest_framework import serializers
from .models import File


# serializers do the packing and unpacking of data. they package data when going to the server and unpackage it while
# going from the server serializers take the data from the server and serializes it into the format like json that
# can be read by any technologies

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"

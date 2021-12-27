from rest_framework import serializers
from users.models import NewUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    email = serializers.EmailField(required=True)
    user_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = NewUser
        fields = ('email', 'user_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self,args):
        email = args.get('email',None)
        username = args.get('user_name',None)
        if NewUser.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email':('Email already exists!')})
        if NewUser.objects.filter(user_name=username).exists():
            raise serializers.ValidationError({'user_name':('Username already exists!')})
        
        return super().validate(args)
        
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['is_staff'] = user.is_staff
        return token
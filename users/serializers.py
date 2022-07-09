from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer, UserSerializer


class UserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = '__all__'


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('url', 'id', 'email', 'name', 'last_name', 'account_address', 'password')

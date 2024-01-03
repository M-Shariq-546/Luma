from django.contrib.auth.models import User
from profiles.models import Profile
from rest_framework import serializers

class UserCreationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input':'password'},write_only=True)
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'email',
            'password',
            'password2',
        ]

        extra_kwargs = {'password':{'write_only':True}}
    def get_message(self, obj):
        return "Thank You for Registering."
    
    
    def validate(self , data):
        pw = data.get('password')
        pw2 = data.get('password2')
        if pw != pw2:
            raise serializers.ValidationError("password Doesn't Match At All")
        return data
    
    def create(self , validate_data):
        print(validate_data)
        
        user = User.objects.create_user(
            username=validate_data.get('username'),
            email=validate_data.get('email'),
            first_name=validate_data.get('first_name'),
        )    
        user.set_password(validate_data.get('password'))        
        user.save()
        return user


class ProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField(read_only=True)
    username = serializers.SerializerMethodField(read_only=True)
    email = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Profile
        fields = ['first_name', 'profile' , 'username' , 'email','image']
    
    def get_username(self, obj):
        return obj.user.username
    
    def get_first_name(self, obj):
        return obj.user.first_name
        
    def get_email(self, obj):
        return obj.user.email
        
    
class ProfileUpdateSerializer(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField(read_only=True)
    username = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Profile
        fields = ['username','first_name', 'group_name','image']
                
    def get_first_name(self, obj):
        return obj.user.first_name
    
    def get_username(self, obj):
        return obj.user.username

class CreateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'user'
        ]
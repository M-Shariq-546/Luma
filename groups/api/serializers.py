from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework import serializers
from groups.models import Group , Members
from profiles.models import Profile

class GroupCreationSerailizer(serializers.ModelSerializer):
   class Meta:
        model = Group
        fields= [
            'admin',
            'group_name',
        ]   

class GroupListSerailizer(serializers.ModelSerializer):
    admin = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Group
        fields= [
            'admin',
            'group_name',
        ]
          
    def get_admin(self , obj):
        return obj.admin.username

    
class GroupDetailSerailizer(serializers.ModelSerializer):
    admin = serializers.SerializerMethodField(read_only=True)
    members = serializers.SerializerMethodField(read_only=True)
    members_invited_list = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Group
        fields= [
            'admin',
            'group_name',
            'group_id',
            'members',
            'members_invited_list',
        ]
          
    def get_admin(self , obj):
        return obj.admin.user.username     
            
    def get_members(self, obj):
        is_admin_user = Group.objects.get(group_id=obj.group_id)
        users = Members.objects.filter(Q(is_member=True)&Q(is_active=True))
        return str(list(users))
    
    def get_members_invited_list(self, obj):
        users = Group.objects.get(group_id=obj.group_id)
        members_invited_list = Members.objects.all().filter(Q(is_invited=True) & Q(is_active=True))
        return str(list(members_invited_list))
    
class GroupInviteSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Members
        fields = [
            'email',
            'group_name',
        ]
        
    def validate_invite(self, obj):
        email = Profile.objects.filter(email=obj.email).exists()
        if email:
            return email
        else:
            raise ValueError("So Such email Found")
        

class GroupDetailUpdateSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields= [
            'group_name',
        ]

class RemoveMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = [
            'member',
        ]
        
    def get_member(self , obj):
        members_invited_list = Members.objects.filter(Q(is_invited=True) & Q(is_active=True) & Q(member=obj.member))
        members = Members.objects.filter(Q(is_member=True) & Q(is_active=True) & Q(member=obj.member))
        if not members_invited_list and not members:
            return Response({'Alert':"Member not found"}, status=status.HTTP_204_NO_CONTENT)
        else:
            if members_invited_list:
                return list(members_invited_list)
            return list(members)
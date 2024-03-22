from rest_framework import serializers
from django.utils.dateformat import format
from .models import Event
from attending.models import Attend

class EventSerializer(serializers.ModelSerializer):
    """
    Serializer for the event model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.image.url'
    )
    attend_id = serializers.SerializerMethodField()
    comments_count = serializers.ReadOnlyField()
    attending_count = serializers.ReadOnlyField()
    reviews_count = serializers.ReadOnlyField()
    average_rating = serializers.ReadOnlyField()
    review_id = serializers.SerializerMethodField()
    
    def validate_image(self, value):
        if value.size > 1024 * 1024 *2:
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
        )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px'
        )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px'
        )
        return value
 
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    def get_attend_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            attend = Attend.objects.filter(
                owner=user, event=obj
            ).first()
            return attend.id if attend else None
        return None
    
    def get_review_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            review = Review.objects.filter(
                owner=user, event=obj
            ).first()
            return review.id if review else None
        return None
    
    class Meta:
        model = Event
        fields = [
            'id', 'owner', 'is_owner', 'profile_id','title',
            'description', 'category', 'created_at','updated_at', 
            'event_date', 'profile_image', 'image', 'event_date',
            'category','image_filter', 'attend_id', 'comments_count',
            'attending_count', 'reviews_count', 'average_rating',
            'review_id,'
        ]
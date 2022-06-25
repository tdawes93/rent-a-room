from django.shortcuts import get_object_or_404, render
from django.views import generic, View
from django.db.models import Avg
from .models import Property


class AddProperty(generic.ListView):
    """
    A list view class rendering the add property page
    """
    model = Property
    queryset = Property.objects.filter(status=1).order_by(
        '-created_on',
        'title',
    )
    template_name = 'add-property.html'


class PropertyDetail(View):
    """
    A standard view class rendering the individual
    page for each property
    """

    def get(self, request, slug, *args, **kwargs):
        """
        This method gets the individual property information
        needed for each property page from the model dataset
        """
        queryset = Property.objects.filter(status=1)
        property = get_object_or_404(queryset, slug=slug)
        reviews = property.reviews.order_by('date_reviewed')
        review_count = reviews.all().count()
        # property_rating = 0
        # for review in reviews:
        #     property_rating += int(review.overall_rating)
        #     return property_rating
        # overall_property_rating = int((property_rating)/(review_count))
        average_property_rating = reviews.aggregate(Avg('overall_rating'))
        print(average_property_rating)


        return render(
            request,
            'property.html',
            {
                'property': property,
                'reviews': reviews,
                'review_count': review_count,
                'average_property_rating': average_property_rating,
            },
        )

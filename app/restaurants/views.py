from rest_framework import generics
from .models import Restaurant, Menu, Dish
from .serializers import RestaurantSerializer, MenuSerializer, DishSerializer

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from authentication.views import AuthBaseClass


class RestaurantListAPIView(AuthBaseClass, generics.ListAPIView):
    """
    List all Restaurants in DB
    """
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        queryset = Restaurant.objects.all()
        _id = self.request.query_params.get('id')
        delivery = self.request.query_params.get('delivery')

        if _id:
            queryset = queryset.filter(id=_id)

        if delivery:
            queryset = queryset.filter(delivery=delivery)

        return queryset


class MenuListAPIView(AuthBaseClass, generics.ListAPIView):
    """
    List all Menus in DB

    Restaurant represents as ID

    Days of the week represents as integer
    0 - menu available every day
    1 - 7 --> Monday - Sunday

    To get all menus by providing specific day there is get_queryset() method
    """
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()

    def get_queryset(self):
        queryset = Menu.objects.all()
        day = self.request.query_params.get('day')
        restaurant_id = self.request.query_params.get('restaurant_id')
        _id = self.request.query_params.get('id')
    

        if day:
            queryset = queryset.filter(day=day)

        if restaurant_id:
            queryset = queryset.filter(restaurant_id=restaurant_id)

        if _id:
            queryset = queryset.filter(id=id)

        return queryset


class DishListAPIView(AuthBaseClass, generics.ListAPIView):
    """
    List all Dishes in DB
    """
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    

class RestaurantCreateAPIView(AuthBaseClass, generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def perform_create(self, serializer):
        serializer.save(address=self.request.data.get('address', None),
                        phone_number=self.request.data.get('phone_number', None))


class MenuCreateAPIView(AuthBaseClass, generics.CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class DishCreateAPIView(AuthBaseClass, generics.CreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class RestaurantUpdateAPIView(AuthBaseClass, generics.UpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class MenuUpdateAPIView(AuthBaseClass, generics.UpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer



class DishUpdateAPIView(generics.UpdateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser]


class RestaurantDeleteAPIView(generics.DestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser]


class MenuDeleteAPIView(generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser]


class DishDeleteAPIView(generics.DestroyAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser]

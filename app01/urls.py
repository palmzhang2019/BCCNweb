from django.conf.urls import url, include
from app01.views import institute,activity,utils, account, product


urlpatterns = [
    url(r'^institute/$', institute.InstituteView.as_view({'get': 'list'})),
    url(r'^institute/(?P<pk>\d+)/$', institute.InstituteView.as_view({'get': 'retrieve'})),
    url(r'^activity/$', activity.ActivityView.as_view({'get': 'list', "post": "create"})),
    url(r'^activity/(?P<pk>\d+)/$', activity.ActivityView.as_view({'get': 'retrieve'})),
    url(r'^product/$', product.ProductView.as_view({'get': 'list'})),
    url(r'^product/(?P<pk>\d+)/$', product.ProductView.as_view({'get': 'retrieve'})),
    url(r'^subject/$', utils.SubjectView.as_view({'get': 'list'})),
    url(r'^subject/(?P<pk>\d+)/$', utils.SubjectView.as_view({'get': 'retrieve'})),
    url(r'^instituterec/$', institute.InstituteRecView.as_view({'get': 'list'})),
    url(r'^account/$', account.AccountView.as_view({'get': 'list'})),
    url(r'^account/(?P<pk>\d+)/$', account.AccountView.as_view({'get': 'retrieve'})),
    #
    # url(r'^course/$', course.CourseView.as_view({'get': 'list'})),
    # url(r'^course/(?P<pk>\d+)/$', course.CourseView.as_view({'get': 'retrieve'})),
    #
    # url(r'^shoppingcar/$', shoppingcar.ShoppingCarViewSet.as_view()),
    # url(r'^payment/$', payment.PaymentViewSet.as_view()),
    # url(r'^order/$', order.OrderViewSet.as_view()),

]
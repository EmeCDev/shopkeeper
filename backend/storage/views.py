from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def Iniciar_Sesion(request):
    
    data = request.data
    
    if request.user.is_authenticated:
        message = "User is authenticated."
    else:
        message = "User is not authenticated."
        
    return Response({'message': message})
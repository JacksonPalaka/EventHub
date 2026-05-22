from rest_framework import viewsets  
from rest_framework.decorators import action  
from rest_framework.response import Response 
from rest_framework import status  

from events.models import Event, Reservation 
from events.serializers import EventSerializer, ReservationSerializer  


# ViewSet for Event model
class EventViewSet(viewsets.ModelViewSet):
    
    serializer_class = EventSerializer  

    def get_queryset(self):
        queryset = Event.objects.all()  # get all events
        
        status_param = self.request.query_params.get('status')    # type: ignore
        venue_param  = self.request.query_params.get('venue')     # type: ignore

        if status_param:
            queryset = queryset.filter(status=status_param)  

        if venue_param:
            queryset = queryset.filter(venue__icontains=venue_param)  

        return queryset  



# ViewSet for Reservation model
class ReservationViewSet(viewsets.ModelViewSet):

    serializer_class = ReservationSerializer  

    def get_queryset(self):
        queryset = Reservation.objects.all()  # get all reservations
        event_id = self.request.query_params.get('event_id')   # type: ignore

        if event_id:
            queryset = queryset.filter(event_id=event_id) 

        return queryset 

    
    # Custom action for cancelling reservation
    # URL => /reservations/{id}/cancel/
    @action(detail=True, methods=['post'])

    def cancel(self, request, pk=None):
        reservation = self.get_object()  

        if reservation.status == 'cancelled':  
            return Response(
                {'error': 'Already cancelled.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        reservation.event.available_seats += reservation.seats_reserved  
        reservation.event.save()  
        reservation.status = 'cancelled'  
        reservation.save()  

        return Response(self.get_serializer(reservation).data)
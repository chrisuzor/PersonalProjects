# api/views.py
from artifacts.models import Artifact
from people.models import Person
from people.serializers import PersonSerializer
from rest_framework import mixins, viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from vehicles.models import Vehicle
from vehicles.serializers.vehicles import VehicleSerializer


@api_view(["GET"])
def listing(request):
    doctors = Person.objects.filter(title="Dr.")
    vehicles = Vehicle.objects.all()

    context = {
        "request": request,
    }
    vehicle_serializer = VehicleSerializer(vehicles, many=True, context=context)

    results = {
        "doctors": PersonSerializer(doctors, many=True).data,
        "vehicles": vehicle_serializer.data,
    }

    return Response(results)


class DoctorsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    def list(self, request):
        doctors = Person.objects.filter(title="Dr.")
        results = {
            "doctors": PersonSerializer(doctors, many=True).data,
        }

        return Response(results)


class MassDeleteArtifactsViewSet(mixins.DestroyModelMixin, viewsets.GenericViewSet):
    @action(detail=False, methods=["delete"])
    def mass_delete(self, request, pk=None):
        for artifact_id in request.POST["ids"].split(","):
            Artifact.objects.get(id=artifact_id).delete()

        return Response()

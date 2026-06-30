from rest_framework.views import APIView, Request, Response
from features.locations.serializers import (
    LocationSearchSerializer,
    LocationSerializer,
    LocationUpdateSerializer,
)
from features.locations.models import Location
from features.shared.helpers.helper import toApiResponse, log_action
from features.locations.helpers import setLocationFilters
from features.shared.helpers.helper import generateId


# <!--==============================
#   LOCATIONS VIEWS
# ================================-->
class LocationView(APIView):

    def post(self, request: Request) -> Response:
        print("route entered")
        serializer = LocationSerializer(data=request.data)
        serializer.initial_data["location_id"] = generateId(
            Location, "location_id", "LOC"
        )
        print("this is document data ", serializer.initial_data)

        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            print("this is error e: ", e)
            raise (e)

        location = serializer.save()

        if location:
            log_action(
                user=request.user,
                action="CREATE",
                model_name="locations",
                object_id=location.id,
                description=f"Upload {location.location_name}",
            )

        return toApiResponse(
            data=LocationSerializer(location).data,
            message=f"{location.location_name} has been created!",
        )

    def get(self, request: Request) -> Response:

        locations = Location.objects.all()
        res = LocationSerializer(locations, many=True)

        return Response({"locations": res.data})

    def put(self, request: Request, id: int) -> Response:
        print("route entered!")
        location = Location.objects.get(id=id)
        serializer = LocationUpdateSerializer(instance=location, data=request.data)
        serializer.is_valid(raise_exception=True)

        location = serializer.save()

        if location:
            log_action(
                user=request.user,
                action="UPDATE",
                model_name="locations",
                object_id=location.id,
                description=f"Updated {location.location_name}",
            )

        return Response(
            {
                "location": LocationSerializer(location).data,
                "message": f"{location.location_name} has been updated!",
            }
        )

    def delete(self, request: Request, id: int) -> Response:

        location = Location.objects.get(id=id)

        num, _ = location.delete()

        if num < 0:
            return Response({"message": f"Failed to delete {location.location_name}"})

        log_action(
            user=request.user,
            action="DELETE",
            model_name="locations",
            object_id=location.id,
            description=f"Deleted {location.location_name}",
        )

        return Response({"message": f"{location.location_name} has been deleted!"})


class GetLocationByIdView(APIView):

    def get(self, request: Request, id: int) -> Response:

        location = Location.objects.get(id=id)

        return Response({"location": LocationSerializer(location).data})


class GetLocationByColumnView(APIView):

    def get(self, request: Request) -> Response:

        serializer = LocationSearchSerializer(data=request.query_params)

        serializer.is_valid(raise_exception=True)

        filters = setLocationFilters(serializer.validated_data)

        locations = Location.objects.filter(filters)

        return Response({"locations": LocationSerializer(locations, many=True).data})


class GetLocationOptionsView(APIView):
    def get(self, request: Request) -> Response:
        return Response(
            {
                "location_types": list(
                    Location.objects.exclude(location_type__isnull=True)
                    .exclude(location_type="")
                    .values_list("location_type", flat=True)
                    .distinct()
                ),
                "location_names": list(
                    Location.objects.exclude(location_name__isnull=True)
                    .exclude(location_name="")
                    .values_list("location_name", flat=True)
                    .distinct()
                ),
                "cities": list(
                    Location.objects.exclude(city__isnull=True)
                    .exclude(city="")
                    .values_list("city", flat=True)
                    .distinct()
                ),
                "longitudes": list(
                    Location.objects.exclude(longitude__isnull=True)
                    .values_list("longitude", flat=True)
                    .distinct()
                ),
                "latitudes": list(
                    Location.objects.exclude(latitude__isnull=True)
                    .values_list("latitude", flat=True)
                    .distinct()
                ),
                "coordinates": list(
                    Location.objects.exclude(latitude__isnull=True)
                    .exclude(longitude__isnull=True)
                    .values("latitude", "longitude")
                    .distinct()
                ),
            }
        )

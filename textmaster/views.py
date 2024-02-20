from rest_framework import viewsets
from .models import (
    AudiometerThresholdDecimats, BloodTest, Urine_Examination, Complaints,
    Hematology, LungFunctionTest, MicroscopicExamination, OtherTests,
    PhysiologicalTest, SystematicExamination, VisualTest
)
from .serializers import (
    AudiometerThresholdDecimatsSerializer, BloodTestSerializer,
    Urine_ExaminationSerializer, ComplaintsSerializer,
    HematologySerializer, LungFunctionTestSerializer,
    MicroscopicExaminationSerializer, OtherTestsSerializer,
    PhysiologicalTestSerializer, SystematicExaminationSerializer,
    VisualTestSerializer
)
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class AudiometerThresholdDecimatsViewSet(viewsets.ModelViewSet):
    queryset = AudiometerThresholdDecimats.objects.all()
    serializer_class = AudiometerThresholdDecimatsSerializer
    authentication_classes = [JWTAuthentication]  # Use JWT authentication
    permission_classes = [IsAuthenticated] 

class BloodTestViewSet(viewsets.ModelViewSet):
    queryset = BloodTest.objects.all()
    serializer_class = BloodTestSerializer
    authentication_classes = [JWTAuthentication]  # Use JWT authentication
    permission_classes = [IsAuthenticated]

class Urine_ExaminationViewSet(viewsets.ModelViewSet):
    queryset = Urine_Examination.objects.all()
    serializer_class = Urine_ExaminationSerializer
    authentication_classes = [JWTAuthentication]  # Use JWT authentication
    permission_classes = [IsAuthenticated]

class ComplaintsViewSet(viewsets.ModelViewSet):
    queryset = Complaints.objects.all()
    serializer_class = ComplaintsSerializer
    authentication_classes = [JWTAuthentication]  # Use JWT authentication
    permission_classes = [IsAuthenticated]

class HematologyViewSet(viewsets.ModelViewSet):
    queryset = Hematology.objects.all()
    serializer_class = HematologySerializer
    authentication_classes = [JWTAuthentication]  # Use JWT authentication
    permission_classes = [IsAuthenticated]

class LungFunctionTestViewSet(viewsets.ModelViewSet):
    queryset = LungFunctionTest.objects.all()
    serializer_class = LungFunctionTestSerializer
    authentication_classes = [JWTAuthentication]  # Use JWT authentication
    permission_classes = [IsAuthenticated]

class MicroscopicExaminationViewSet(viewsets.ModelViewSet):
    queryset = MicroscopicExamination.objects.all()
    serializer_class = MicroscopicExaminationSerializer

class OtherTestsViewSet(viewsets.ModelViewSet):
    queryset = OtherTests.objects.all()
    serializer_class = OtherTestsSerializer
    authentication_classes = [JWTAuthentication]  # Use JWT authentication
    permission_classes = [IsAuthenticated]

class PhysiologicalTestViewSet(viewsets.ModelViewSet):
    queryset = PhysiologicalTest.objects.all()
    serializer_class = PhysiologicalTestSerializer
    authentication_classes = [JWTAuthentication]  # Use JWT authentication
    permission_classes = [IsAuthenticated]

class SystematicExaminationViewSet(viewsets.ModelViewSet):
    queryset = SystematicExamination.objects.all()
    serializer_class = SystematicExaminationSerializer
    authentication_classes = [JWTAuthentication]  # Use JWT authentication
    permission_classes = [IsAuthenticated]

class VisualTestViewSet(viewsets.ModelViewSet):
    queryset = VisualTest.objects.all()
    serializer_class = VisualTestSerializer
    authentication_classes = [JWTAuthentication]  # Use JWT authentication
    permission_classes = [IsAuthenticated]

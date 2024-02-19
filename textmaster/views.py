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

class AudiometerThresholdDecimatsViewSet(viewsets.ModelViewSet):
    queryset = AudiometerThresholdDecimats.objects.all()
    serializer_class = AudiometerThresholdDecimatsSerializer

class BloodTestViewSet(viewsets.ModelViewSet):
    queryset = BloodTest.objects.all()
    serializer_class = BloodTestSerializer

class Urine_ExaminationViewSet(viewsets.ModelViewSet):
    queryset = Urine_Examination.objects.all()
    serializer_class = Urine_ExaminationSerializer

class ComplaintsViewSet(viewsets.ModelViewSet):
    queryset = Complaints.objects.all()
    serializer_class = ComplaintsSerializer

class HematologyViewSet(viewsets.ModelViewSet):
    queryset = Hematology.objects.all()
    serializer_class = HematologySerializer

class LungFunctionTestViewSet(viewsets.ModelViewSet):
    queryset = LungFunctionTest.objects.all()
    serializer_class = LungFunctionTestSerializer

class MicroscopicExaminationViewSet(viewsets.ModelViewSet):
    queryset = MicroscopicExamination.objects.all()
    serializer_class = MicroscopicExaminationSerializer

class OtherTestsViewSet(viewsets.ModelViewSet):
    queryset = OtherTests.objects.all()
    serializer_class = OtherTestsSerializer

class PhysiologicalTestViewSet(viewsets.ModelViewSet):
    queryset = PhysiologicalTest.objects.all()
    serializer_class = PhysiologicalTestSerializer

class SystematicExaminationViewSet(viewsets.ModelViewSet):
    queryset = SystematicExamination.objects.all()
    serializer_class = SystematicExaminationSerializer

class VisualTestViewSet(viewsets.ModelViewSet):
    queryset = VisualTest.objects.all()
    serializer_class = VisualTestSerializer

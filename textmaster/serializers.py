from rest_framework import serializers
from rest_framework.response import Response

from .models import AudiometerThresholdDecimats, BloodTest, Urine_Examination, Complaints, Hematology, LungFunctionTest, MicroscopicExamination, OtherTests, PhysiologicalTest, SystematicExamination, VisualTest
class AudiometerThresholdDecimatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudiometerThresholdDecimats
        fields = '__all__'

class BloodTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodTest
        fields = '__all__'
    # def update(self, request, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     # instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #     return Response(serializer.data)

        
class Urine_ExaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Urine_Examination
        fields = '__all__'
        
class ComplaintsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaints
        fields = '__all__'
class HematologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hematology
        fields = '__all__'
        
class LungFunctionTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LungFunctionTest
        fields = '__all__'

class MicroscopicExaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MicroscopicExamination
        fields = '__all__'
class OtherTestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherTests
        fields = '__all__'
class PhysiologicalTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysiologicalTest
        fields = '__all__'
class SystematicExaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystematicExamination
        fields = '__all__'
class VisualTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisualTest
        fields = '__all__'


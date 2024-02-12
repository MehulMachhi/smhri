from rest_framework import serializers
from .models import *


class AudiometerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudiometerThresholdDecimats
        fields = '__all__'


class Add_Test_Serializer(serializers.ModelSerializer):
    class Meta:
        model = AudiometerThresholdDecimats
        fields = '__all__'


class BloodTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodTest
        fields = '__all__'

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

class MicroscopicExaminationSerializers(serializers.ModelSerializer):
    class Meta:
        model = MicroscopicExamination
        fields = '__all__'

class OtherTestsSerializers(serializers.ModelSerializer):
    class Meta:
        model = OtherTests
        fields = '__all__'

class PhysiologicalTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysiologicalTest
        fields = '__all__'


class SystematicExaminationSerializers(serializers.ModelSerializer):
    class Meta:
        model = SystematicExamination
        fields = '__all__'



class TestMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestMaster
        fields = '__all__'



class VisualTestSerializers(serializers.ModelSerializer):
    class Meta:
        model = VisualTest
        fields = '__all__'




        



    
from django.urls import path
from . import views

urlpatterns = [

    path('get_test', views.get_test, name='get_test'),
    # path('view_test_audiometerthresholddecimats', views.view_test_audiometerthresholddecimats,name='view_test_audiometerthresholddecimats'),
    # path('update_test_audiometerthresholddecimats/<int:id>', views.update_test_audiometerthresholddecimats,name='update_test_audiometerthresholddecimats'),
    # path('delete_test_audiometerthresholddecimats/<int:id>', views.delete_test_audiometerthresholddecimats,name='delete_test_audiometerthresholddecimats'),
    
    path('add_test_audiometerthresholddecimats/<int:id>', views.add_test_audiometerthresholddecimats, name='add_test_audiometerthresholddecimats'),
    
    path('post_patch_audioAPIView', views.post_patch_audioAPIView.as_view(), name='post_patch_audioAPIView.as_view()'),
    path('post_patch_audioAPIView/<int:pk>', views.post_patch_audioAPIView.as_view(), name='post_patch_audioAPIView.as_view()'),
    
    path('AudioAddView', views.AudioAddView.as_view(), name='AudioAddView.as_view()'),
    path('AudioRetUPdDestGetView/<int:pk>', views.AudioRetUPdDestGetView.as_view(), name='AudioRetUPdDestGetView.as_view()'),
    # path('view_test_audiometerthresholddecimats', views.view_test_audiometerthresholddecimats, name='view_test_audiometerthresholddecimats'),
    # path('update_test_audiometerthresholddecimats/<int:id>', views.update_test_audiometerthresholddecimats, name='update_test_audiometerthresholddecimats'),
    # path('delete_test_audiometerthresholddecimats/<int:id>', views.delete_test_audiometerthresholddecimats, name='delete_test_audiometerthresholddecimats'),

    path('add_test_bloodtest/<int:id>', views.add_test_bloodtest, name='add_test_bloodtest'),
    path('BloodTestAddView', views.BloodTestAddView.as_view(), name='BloodTestAddView.as_view()'),
    path('BloodTestRetUpdDesView/<int:pk>', views.BloodTestRetUpdDesView.as_view(), name='BloodTestRetUpdDesView.as_view()'),
    # path('view_test_bloodtest', views.view_test_bloodtest,name='view_test_bloodtest'),
    # path('update_test_bloodtest/<int:id>', views.update_test_bloodtest,name='update_test_bloodtest'),
    # path('delete_test_bloodtest/<int:id>', views.delete_test_bloodtest,name='delete_test_bloodtest'),
    
    path('add_test_complaints/<int:id>', views.add_test_complaints, name='add_test_complaints'),
    path('CompainstAddView', views.CompainstAddView.as_view(), name='CompainstAddView.as_view()'),
    path('ComplainstRetUpdDesView/<int:pk>', views.ComplainstRetUpdDesView.as_view(), name='ComplainstRetUpdDesView.as_view()'),
    # path('view_test_complaints', views.view_test_complaints, name='view_test_complaints'),
    # path('update_test_complaints/<int:id>', views.update_test_complaints, name='update_test_complaints'),
    # path('delete_test_complaints/<int:id>', views.delete_test_complaints, name='delete_test_complaints'),

    path('add_urine_examination/<int:id>', views.add_urine_examination, name='add_urine_examination'),
    path('UrineTestAddView', views.UrineTestAddView.as_view(), name='UrineTestAddView.as_view()'),
    path('UrineTestRetUpdDesView/<int:pk>', views.UrineTestRetUpdDesView.as_view(), name='UrineTestRetUpdDesView.as_view()'),
    # path('view_test_complaints', views.view_test_complaints, name='view_test_complaints'),
    # path('update_test_complaints/<int:id>', views.update_test_complaints, name='update_test_complaints'),
    # path('delete_test_complaints/<int:id>', views.delete_test_complaints, name='delete_test_complaints'),
    
    path('add_test_hematology/<int:id>', views.add_test_hematology, name='add_test_hematology'),
    path('HematologyAddView', views.HematologyAddView.as_view(), name='HematologyAddView.as_view()'),
    path('HematologyRetUpdDesView/<int:pk>', views.HematologyRetUpdDesView.as_view(), name='HematologyRetUpdDesView.as_view()'),
    # path('view_test_hematology', views.view_test_hematology, name='view_test_hematology'),
    # path('update_test_hematology/<int:id>', views.update_test_hematology, name='update_test_hematology'),
    # path('delete_test_hematology/<int:id>', views.delete_test_hematology, name='delete_test_hematology'),
    
    path('add_test_lungfunctiontest/<int:id>', views.add_test_lungfunctiontest, name='add_test_lungfunctiontest'),
    path('LungFunctionAddView', views.LungFunctionAddView.as_view, name='LungFunctionAddView.as_view()'),
    path('LungFunctionTestRetUpdDesView/<int:pk>', views.LungFunctionTestRetUpdDesView.as_view(), name='LungFunctionTestRetUpdDesView.as_view()'),
    # path('view_test_lungfunctiontest', views.view_test_lungfunctiontest, name='view_test_lungfunctiontest'),
    # path('update_test_lungfunctiontest/<int:id>', views.update_test_lungfunctiontest, name='update_test_lungfunctiontest'),
    # path('delete_test_lungfunctiontest/<int:id>', views.delete_test_lungfunctiontest, name='delete_test_lungfunctiontest'),
    
    path('add_test_microscopicexamination/<int:id>', views.add_test_microscopicexamination, name='add_test_microscopicexamination'),
    path('MicroAddview', views.MicroAddview.as_view(), name='MicroAddview.as_view()'),
    path('MicroRetUpaDesView/<int:pk>', views.MicroRetUpaDesView.as_view(), name='MicroRetUpaDesView.as_view()'),
    # path('view_test_microscopicexamination', views.view_test_microscopicexamination, name='view_test_microscopicexamination'),
    # path('update_test_microscopicexamination/<int:id>', views.update_test_microscopicexamination,name='update_test_microscopicexamination'),
    # path('delete_test_microscopicexamination/<int:id>', views.delete_test_microscopicexamination,name='delete_test_microscopicexamination'),
    
    path('add_test_othertests/<int:id>', views.add_test_othertests,name='add_test_othertests'),
    path('OthertestsAddView', views.OthertestsAddView.as_view(), name='OthertestsAddView.as_view()'),
    path('OthertestsRetUpdDesView/<int:pk>', views.OthertestsRetUpdDesView.as_view(), name= 'OthertestsRetUpdDesView.as_view()'),
    # path('view_test_othertests', views.view_test_othertests,name='view_test_othertests'),
    # path('update_test_othertests/<int:id>', views.update_test_othertests,name='update_test_othertests'),
    # path('delete_test_othertests/<int:id>', views.delete_test_othertests,name='delete_test_othertests'),
    
    
    
    path('add_test_physiologicaltest/<int:id>', views.add_test_physiologicaltest, name='add_test_physiologicaltest'),
    path('PhysiologicalTestAddView', views.PhysiologicalTestAddView.as_view(), name='PhysiologicalTestAddView.as_view()'),
    path('PhysiologicalTestRetUpdDesView/<int:pk>', views.PhysiologicalTestRetUpdDesView.as_view(), name='PhysiologicalTestRetUpdDesView.as_view()'),
    # path('view_test_physiologicaltest', views.view_test_physiologicaltest, name='view_test_physiologicaltest'),
    # path('update_test_physiologicaltest/<int:id>', views.update_test_physiologicaltest, name='update_test_physiologicaltest'),
    # path('delete_test_physiologicaltest/<int:id>', views.delete_test_physiologicaltest, name='delete_test_physiologicaltest'),
    
    path('add_test_systematicexamination/<int:id>', views.add_test_systematicexamination, name='add_test_systematicexamination'),
    path('SystematicExaminationAddView', views.SystematicExaminationAddView.as_view(), name='SystematicExaminationAddView.as_view()'),
    path('SystematicExaminationRetUpdDesView/<int:pk>', views.SystematicExaminationRetUpdDesView.as_view(), name='SystematicExaminationRetUpdDesView.as_view()'),
    # path('view_test_systematicexamination', views.view_test_systematicexamination, name='view_test_systematicexamination'),
    # path('update_test_systematicexamination/<int:id>', views.update_test_systematicexamination,name='update_test_systematicexamination'),
    # path('delete_test_systematicexamination/<int:id>', views.delete_test_systematicexamination,name='delete_test_systematicexamination'),
    
    
    path('add_test_visualtest/<int:id>', views.add_test_visualtest, name='add_test_visualtest'),
    path('VisualTestAddView', views.VisualTestAddView.as_view(), name='VisualTestAddView.as_view()'),
    path('VisualTestRetUpdDel/<int:pk>', views.VisualTestRetUpdDel.as_view(), name='VisualTestRetUpdDel.as_view()'),
    # path('view_test_visualtest', views.view_test_visualtest, name='view_test_visualtest'),
    # path('update_test_visualtest/<int:id>', views.update_test_visualtest,name='update_test_visualtest'),
    # path('delete_test_visualtest/<int:id>', views.delete_test_visualtest,name='delete_test_visualtest'),
    
    # path('add_test_testmaster', views.add_test_testmaster, name='add_test_testmaster'),
    # path('view_test_testmaster', views.view_test_testmaster, name='view_test_testmaster'),
    # path('update_test_testmaster/<int:id>', views.update_test_testmaster, name='update_test_testmaster'),
    # path('delete_test_testmaster/<int:id>', views.delete_test_testmaster, name='delete_test_testmaster'),

]


















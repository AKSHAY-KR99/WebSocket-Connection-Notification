path('notifications/', views.index, name='notification'),
    path('notifications/<str:room_name>/', views.room, name='room')

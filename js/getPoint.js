
    // 创建一个QWebChannel对象
    var channel = new QWebChannel(qt.webChannelTransport, function(channel) {
        // 获取Python注册的槽函数对象
        var onMapClicked = channel.objects.onMapClicked;
        // 添加一个鼠标点击事件监听器
        map.on('click', function(e) {
            // 获取点击的经纬度坐标
            var lat = e.latlng.lat;
            var lng = e.latlng.lng;
            // 调用Python的槽函数，将经纬度坐标作为参数传递
            onMapClicked(lat, lng);
        });
    });

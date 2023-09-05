
//import { getBottomLeft, getBottomRight, getTopLeft, getTopRight } from '../ol7/extent';
//创建源及图层
var source = new ol.source.Vector();
var v_layer = new ol.layer.Vector({
    source: source
})
v_layer.set('name', 'vLayer');
map.addLayer(v_layer);

//画点功能
// var draw = new ol.interaction.Draw({
//     type: 'Point',
//     source: source,
//     free: false
// })
//矩形
drawRect = new ol.interaction.Draw({
    source: source,
    type: 'Circle',
    freehand: false,
    geometryFunction: ol.interaction.Draw.createBox()
});
//map.addInteraction(draw);

drawRect.on('drawend', function (e) {
    source.clear();
    var geom = e.feature.getGeometry();//拿到绘制图形的geometry
    //map.removeInteraction(draw);//移除绘制状态，一次只绘制一个图形						
    //let featureGeoJson = JSON.parse(new GeoJSON().writeFeature(e.feature));//将绘制图层转为geojson
    var coordinates = geom.getCoordinates();
    console.log(geom.getCoordinates());
    // sendMes(coordinates)
    sendMes(geom.getExtent())
    
});

//多边形
drawPolygon = new ol.interaction.Draw({
    source: source,
    type: 'Polygon',
    freehand: false,
    // geometryFunction: ol.interaction.Draw.createRegularPolygon(4)
});
drawPolygon.on('drawend', function (e) {
    source.clear();
    var geom = e.feature.getGeometry();//拿到绘制图层的geometry
    //map.removeInteraction(draw);//移除绘制状态，一次可同时绘制多一图层						
    //let featureGeoJson = JSON.parse(new GeoJSON().writeFeature(e.feature));//将绘制图层进行解汇
    var coordinates = geom.getCoordinates();
    console.log(geom.getCoordinates());
    // console.log(geom.getExtent());
    // console.log(geom.getExtent()[0]);
    
    // sendMes(coordinates)
    sendMes(geom.getExtent())
    
});


function sendMes(points) {
    // 调用python端的功能类的方法执行操作
    window.printer.setExtent(JSON.stringify(points));
  }



